# models.py
from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    """Base class dengan inheritance"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self._created_at = datetime.now()

    @abstractmethod
    def display_info(self):
        pass

    def get_age_category(self):
        if self.age < 18:
            return "Underage"
        elif self.age < 25:
            return "Young Adult"
        elif self.age < 60:
            return "Adult"
        else:
            return "Senior"

class Student(Person):
    """Child class dengan inheritance"""
    def __init__(self, student_id, name, age, gender, grade, major):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.grade = grade
        self.major = major
        self.subjects = set()  # Menggunakan Set
        self.history = []  # Menggunakan List

    def display_info(self):
        return f"ID: {self.student_id} | Nama: {self.name} | Usia: {self.age} | {self.gender} | {self.major}"

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'grade': self.grade,
            'major': self.major,
            'subjects': list(self.subjects),
            'created_at': self._created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            data['student_id'],
            data['name'],
            data['age'],
            data['gender'],
            data['grade'],
            data['major']
        )
        if 'subjects' in data:
            student.subjects = set(data['subjects'])
        return student
