# main.py
import os
import sys
from typing import Optional
from models import Student
from database import Database
from statistics import StatisticsAnalyzer
from api import APIManager
from utils import UIManager, DataGenerator, parse_command, validate_student_data

class DataManagerApp:
    """Main application class"""

    def __init__(self):
        self.db = Database()
        self.api = APIManager()
        self.ui = UIManager()
        self.current_user = None

    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        """Run the application"""
        while True:
            self.clear_screen()
            self.ui.display_menu()

            choice = self.ui.get_menu_choice()

            if choice == 0:
                print("👋 Terima kasih telah menggunakan Python Data Manager!")
                break
            elif choice == 1:
                self.add_data()
            elif choice == 2:
                self.view_data()
            elif choice == 3:
                self.search_data()
            elif choice == 4:
                self.update_data()
            elif choice == 5:
                self.delete_data()
            elif choice == 6:
                self.show_statistics()
            elif choice == 7:
                self.sort_data()
            elif choice == 8:
                self.export_csv()
            elif choice == 9:
                self.visualize_data()
            elif choice == 10:
                self.import_from_api()
            else:
                print("⚠️ Pilihan tidak valid!")

            input("\nTekan Enter untuk melanjutkan...")

    def add_data(self):
        """Tambah data baru"""
        print("\n📝 TAMBAH DATA BARU")
        print("-" * 40)

        try:
            student_id = input("ID Student: ").strip()
            if not student_id:
                raise ValueError("ID Student tidak boleh kosong")

            name = input("Nama: ").strip()
            if not name:
                raise ValueError("Nama tidak boleh kosong")

            age = int(input("Usia: "))
            if age < 0:
                raise ValueError("Usia harus positif")

            gender = input("Gender (L/P): ").strip().upper()
            if gender not in ['L', 'P']:
                raise ValueError("Gender harus L atau P")
            gender = "Laki-laki" if gender == 'L' else "Perempuan"

            grade = float(input("Grade (0-100): "))
            if grade < 0 or grade > 100:
                raise ValueError("Grade harus 0-100")

            major = input("Major: ").strip()
            if not major:
                raise ValueError("Major tidak boleh kosong")

            # Tambah subjects dengan set
            subjects_input = input("Mata Kuliah (pisahkan dengan koma): ").strip()
            subjects = set()
            if subjects_input:
                subjects = set([s.strip() for s in subjects_input.split(',') if s.strip()])

            student = Student(student_id, name, age, gender, grade, major)
            student.subjects = subjects

            if self.db.add_student(student):
                print("✅ Data berhasil ditambahkan!")
            else:
                print("⚠️ Gagal menambahkan data!")

        except ValueError as e:
            print(f"⚠️ Error: {e}")
        except Exception as e:
            print(f"⚠️ Terjadi kesalahan: {e}")

    def view_data(self):
        """Lihat semua data"""
        students = self.db.get_all_students()

        if not students:
            print("📭 Belum ada data.")
            return

        print("\n📋 SEMUA DATA")
        print("="*80)
        print(f"{'ID':<10} {'Nama':<20} {'Usia':<6} {'Gender':<10} {'Grade':<8} {'Major':<15}")
        print("-"*80)

        for student in students:
            print(f"{student.student_id:<10} {student.name:<20} {student.age:<6} "
                  f"{student.gender:<10} {student.grade:<8.1f} {student.major:<15}")
        print("="*80)
        print(f"Total: {len(students)} siswa")

    def search_data(self):
        """Cari data"""
        print("\n🔍 CARI DATA")
        print("-" * 40)
        print("1. Cari berdasarkan ID")
        print("2. Cari berdasarkan Nama")

        choice = input("Pilih metode (1-2): ").strip()

        if choice == '1':
            student_id = input("Masukkan ID: ").strip()
            student = self.db.find_student(student_id)
            if student:
                print("\n✅ Data ditemukan:")
                print(f"ID: {student.student_id}")
                print(f"Nama: {student.name}")
                print(f"Usia: {student.age}")
                print(f"Gender: {student.gender}")
                print(f"Grade: {student.grade}")
                print(f"Major: {student.major}")
                print(f"Mata Kuliah: {', '.join(student.subjects) if student.subjects else 'Tidak ada'}")
            else:
                print("❌ Data tidak ditemukan!")

        elif choice == '2':
            name = input("Masukkan nama (atau sebagian): ").strip()
            students = self.db.find_students_by_name(name)
            if students:
                print(f"\n✅ Ditemukan {len(students)} data:")
                for student in students:
                    print(f"  • {student.student_id} - {student.name}")
            else:
                print("❌ Tidak ada data dengan nama tersebut!")
        else:
            print("⚠️ Pilihan tidak valid!")

    def update_data(self):
        """Update data"""
        print("\n📝 UPDATE DATA")
        print("-" * 40)

        student_id = input("Masukkan ID student yang akan diupdate: ").strip()
        student = self.db.find_student(student_id)

        if not student:
            print("❌ Student tidak ditemukan!")
            return

        print(f"\nData saat ini: {student.display_info()}")
        print("\nField yang bisa diupdate:")
        print("1. Nama")
        print("2. Usia")
        print("3. Gender")
        print("4. Grade")
        print("5. Major")
        print("6. Mata Kuliah")

        field_choice = input("Pilih field (1-6): ").strip()

        updates = {}
        try:
            if field_choice == '1':
                updates['name'] = input("Nama baru: ").strip()
            elif field_choice == '2':
                updates['age'] = int(input("Usia baru: "))
            elif field_choice == '3':
                gender = input("Gender baru (L/P): ").strip().upper()
                if gender == 'L':
                    updates['gender'] = "Laki-laki"
                elif gender == 'P':
                    updates['gender'] = "Perempuan"
                else:
                    raise ValueError("Gender harus L atau P")
            elif field_choice == '4':
                updates['grade'] = float(input("Grade baru (0-100): "))
            elif field_choice == '5':
                updates['major'] = input("Major baru: ").strip()
            elif field_choice == '6':
                subjects_input = input("Mata Kuliah baru (pisahkan dengan koma): ").strip()
                if subjects_input:
                    student.subjects = set([s.strip() for s in subjects_input.split(',') if s.strip()])
                else:
                    student.subjects = set()
                self.db._save_data()
                print("✅ Mata kuliah berhasil diupdate!")
                return
            else:
                print("⚠️ Pilihan tidak valid!")
                return

            if self.db.update_student(student_id, **updates):
                print("✅ Data berhasil diupdate!")
            else:
                print("⚠️ Gagal mengupdate data!")

        except ValueError as e:
            print(f"⚠️ Error: {e}")
        except Exception as e:
            print(f"⚠️ Terjadi kesalahan: {e}")

    def delete_data(self):
        """Hapus data"""
        print("\n🗑️ HAPUS DATA")
        print("-" * 40)

        student_id = input("Masukkan ID student yang akan dihapus: ").strip()
        student = self.db.find_student(student_id)

        if not student:
            print("❌ Student tidak ditemukan!")
            return

        print(f"\nData yang akan dihapus: {student.display_info()}")
        confirm = input("Yakin ingin menghapus? (y/n): ").strip().lower()

        if confirm == 'y':
            if self.db.delete_student(student_id):
                print("✅ Data berhasil dihapus!")
            else:
                print("⚠️ Gagal menghapus data!")
        else:
            print("❌ Penghapusan dibatalkan.")

    def show_statistics(self):
        """Tampilkan statistik"""
        students = self.db.get_all_students()

        if not students:
            print("📭 Belum ada data untuk dianalisis.")
            return

        analyzer = StatisticsAnalyzer(students)
        analyzer.show_basic_stats()

        # Analisis dengan NumPy
        numpy_stats = analyzer.analyze_with_numpy()
        if numpy_stats:
            print("\n📊 ANALISIS NUMPY:")
            print(f"Rata-rata usia: {numpy_stats['age_stats']['mean']:.2f}")
            print(f"Median usia: {numpy_stats['age_stats']['median']:.2f}")
            print(f"Standar deviasi usia: {numpy_stats['age_stats']['std']:.2f}")
            print(f"Rata-rata grade: {numpy_stats['grade_stats']['mean']:.2f}")

        # Advanced stats dengan Pandas
        advanced_stats = analyzer.get_advanced_stats()
        if not advanced_stats.empty:
            print("\n📊 STATISTIK PER MAJOR:")
            print(advanced_stats)

    def sort_data(self):
        """Sorting data"""
        print("\n📊 SORTING DATA")
        print("-" * 40)
        print("Sort berdasarkan:")
        print("1. ID")
        print("2. Nama")
        print("3. Usia")
        print("4. Grade")
        print("5. Major")

        choice = input("Pilih (1-5): ").strip()
        reverse = input("Urutan descending? (y/n): ").strip().lower() == 'y'

        key_map = {'1': 'student_id', '2': 'name', '3': 'age', '4': 'grade', '5': 'major'}
        key = key_map.get(choice)

        if not key:
            print("⚠️ Pilihan tidak valid!")
            return

        try:
            sorted_students = self.db.sort_students(key, reverse)
            print(f"\n📋 Data diurutkan berdasarkan {key} ({'Descending' if reverse else 'Ascending'})")
            print("="*80)
            print(f"{'ID':<10} {'Nama':<20} {'Usia':<6} {'Grade':<8} {'Major':<15}")
            print("-"*80)
            for student in sorted_students:
                print(f"{student.student_id:<10} {student.name:<20} {student.age:<6} "
                      f"{student.grade:<8.1f} {student.major:<15}")
        except Exception as e:
            print(f"⚠️ Error sorting: {e}")

    def export_csv(self):
        """Export ke CSV"""
        print("\n📤 EXPORT CSV")
        print("-" * 40)

        filename = input("Nama file (default: data/students_export.csv): ").strip()
        if not filename:
            filename = 'data/students_export.csv'

        if self.db.export_to_csv(filename):
            print(f"✅ Data berhasil diexport ke {filename}")
        else:
            print("⚠️ Gagal export data!")

    def visualize_data(self):
        """Visualisasi data"""
        students = self.db.get_all_students()

        if not students:
            print("📭 Belum ada data untuk divisualisasi.")
            return

        try:
            analyzer = StatisticsAnalyzer(students)
            analyzer.create_visualizations()
            print("✅ Visualisasi selesai!")
        except Exception as e:
            print(f"⚠️ Error visualisasi: {e}")

    def import_from_api(self):
        """Import data dari API"""
        print("\n🌐 IMPORT DARI API")
        print("-" * 40)
        print("Mengambil data dari API...")

        api_data = self.api.get_sample_data()
        if not api_data:
            print("⚠️ Gagal mengambil data dari API!")
            return

        print(f"✅ Berhasil mengambil {len(api_data)} data dari API")

        # Convert dan tambahkan ke database
        added = 0
        for user_data in api_data[:5]:  # Ambil 5 data pertama
            student = self.api.create_student_from_api(user_data)
            if student and self.db.add_student(student):
                added += 1
                print(f"✅ Menambahkan: {student.name}")

        print(f"\n✅ Berhasil menambahkan {added} data dari API ke database")

        # Demo POST ke API
        if self.db.data:
            sample_student = self.db.data[0]
            if self.api.post_data_to_api(sample_student):
                print("✅ Data berhasil dikirim ke API (simulasi)")
            else:
                print("⚠️ Gagal mengirim data ke API")

if __name__ == "__main__":
    try:
        app = DataManagerApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"\n⚠️ Error fatal: {e}")
        sys.exit(1)
