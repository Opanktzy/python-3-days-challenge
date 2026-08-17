# database.py
import json
import csv
import os
from typing import List, Dict, Optional
from models import Student

class Database:
    """Class untuk handle operasi database"""

    def __init__(self, file_path='data/students.json'):
        self.file_path = file_path
        self.data = []
        self._load_data()

    def _load_data(self):
        """Load data dari file dengan exception handling"""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data_list = json.load(f)
                    self.data = [Student.from_dict(item) for item in data_list]
            else:
                self.data = []
                self._save_data()
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"⚠️ Error loading data: {e}")
            self.data = []

    def _save_data(self):
        """Save data ke file dengan exception handling"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([student.to_dict() for student in self.data], f, indent=2, ensure_ascii=False)
        except (IOError, PermissionError) as e:
            print(f"⚠️ Error saving data: {e}")

    def add_student(self, student: Student) -> bool:
        """Tambah student baru"""
        try:
            if any(s.student_id == student.student_id for s in self.data):
                raise ValueError("Student ID sudah terdaftar!")
            self.data.append(student)
            self._save_data()
            return True
        except ValueError as e:
            print(f"⚠️ {e}")
            return False

    def get_all_students(self) -> List[Student]:
        """Dapatkan semua student"""
        return self.data

    def find_student(self, student_id: str) -> Optional[Student]:
        """Cari student berdasarkan ID dengan searching"""
        try:
            for student in self.data:
                if student.student_id == student_id:
                    return student
            return None
        except Exception as e:
            print(f"⚠️ Error searching: {e}")
            return None

    def find_students_by_name(self, name: str) -> List[Student]:
        """Cari student berdasarkan nama dengan searching"""
        try:
            result = []
            for student in self.data:
                if name.lower() in student.name.lower():
                    result.append(student)
            return result
        except Exception as e:
            print(f"⚠️ Error searching: {e}")
            return []

    def update_student(self, student_id: str, **kwargs) -> bool:
        """Update data student"""
        try:
            student = self.find_student(student_id)
            if not student:
                raise ValueError("Student tidak ditemukan!")

            for key, value in kwargs.items():
                if hasattr(student, key) and key != 'student_id':
                    setattr(student, key, value)

            self._save_data()
            return True
        except (ValueError, AttributeError) as e:
            print(f"⚠️ Error updating: {e}")
            return False

    def delete_student(self, student_id: str) -> bool:
        """Hapus student"""
        try:
            student = self.find_student(student_id)
            if not student:
                raise ValueError("Student tidak ditemukan!")

            self.data.remove(student)
            self._save_data()
            return True
        except ValueError as e:
            print(f"⚠️ {e}")
            return False

    def get_statistics(self) -> Dict:
        """Dapatkan statistik data"""
        if not self.data:
            return {}

        ages = [s.age for s in self.data]
        grades = [s.grade for s in self.data]

        return {
            'total_students': len(self.data),
            'average_age': sum(ages) / len(ages),
            'min_age': min(ages),
            'max_age': max(ages),
            'grade_distribution': self._get_grade_distribution(),
            'gender_distribution': self._get_gender_distribution(),
            'major_distribution': self._get_major_distribution()
        }

    def _get_grade_distribution(self) -> Dict:
        """Hitung distribusi grade dengan dictionary"""
        distribution = {}
        for student in self.data:
            distribution[student.grade] = distribution.get(student.grade, 0) + 1
        return distribution

    def _get_gender_distribution(self) -> Dict:
        """Hitung distribusi gender"""
        distribution = {}
        for student in self.data:
            distribution[student.gender] = distribution.get(student.gender, 0) + 1
        return distribution

    def _get_major_distribution(self) -> Dict:
        """Hitung distribusi major"""
        distribution = {}
        for student in self.data:
            distribution[student.major] = distribution.get(student.major, 0) + 1
        return distribution

    def sort_students(self, key: str, reverse: bool = False) -> List[Student]:
        """Sorting data student"""
        valid_keys = ['student_id', 'name', 'age', 'grade', 'major']
        if key not in valid_keys:
            raise ValueError(f"Key harus salah satu dari: {valid_keys}")

        return sorted(self.data, key=lambda s: getattr(s, key), reverse=reverse)

    def export_to_csv(self, filename='data/students_export.csv') -> bool:
        """Export data ke CSV"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['student_id', 'name', 'age', 'gender', 'grade', 'major', 'subjects']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for student in self.data:
                    row = student.to_dict()
                    row['subjects'] = ', '.join(row['subjects'])
                    writer.writerow(row)

            return True
        except Exception as e:
            print(f"⚠️ Error exporting: {e}")
            return False
