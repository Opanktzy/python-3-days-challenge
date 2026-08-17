# utils.py
import time
from functools import wraps
from typing import Generator, Tuple, Any

# Decorator untuk timing
def timer_decorator(func):
    """Decorator untuk mengukur waktu eksekusi fungsi"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ {func.__name__} selesai dalam {end_time - start_time:.2f} detik")
        return result
    return wrapper

# Decorator untuk logging
def log_decorator(func):
    """Decorator untuk logging aktivitas"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Menjalankan: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Selesai: {func.__name__}")
        return result
    return wrapper

def validate_input(func):
    """Decorator untuk validasi input"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"⚠️ Input tidak valid: {e}")
            return None
    return wrapper

class DataGenerator:
    """Class dengan generator untuk menghasilkan data"""

    @staticmethod
    def generate_student_ids(start: int, end: int) -> Generator[str, None, None]:
        """Generator untuk membuat student IDs"""
        for i in range(start, end + 1):
            yield f"STU{i:04d}"

    @staticmethod
    def generate_sample_names() -> Generator[str, None, None]:
        """Generator untuk menghasilkan nama sample"""
        names = [
            "Budi Santoso", "Siti Rahayu", "Agus Wijaya", "Dewi Putri",
            "Hendra Gunawan", "Rina Kartika", "Bayu Pratama", "Citra Lestari",
            "Eko Prasetyo", "Fitri Handayani", "Gusnadi", "Indah Permata"
        ]
        for name in names:
            yield name

    @staticmethod
    def chunk_data(data: list, chunk_size: int) -> Generator[list, None, None]:
        """Generator untuk memproses data dalam chunk"""
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]

# Fungsi dengan Tuple sebagai return value
def parse_command(command: str) -> Tuple[str, list]:
    """Parse command menjadi tuple (command, args)"""
    parts = command.strip().split()
    if not parts:
        return "", []

    cmd = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return cmd, args

def validate_student_data(data: dict) -> Tuple[bool, str]:
    """Validasi data student dengan tuple return"""
    required_fields = ['student_id', 'name', 'age', 'gender', 'grade', 'major']

    for field in required_fields:
        if field not in data:
            return False, f"Field '{field}' tidak ditemukan"

    if not isinstance(data['age'], (int, float)) or data['age'] < 0:
        return False, "Usia harus angka positif"

    if data['grade'] < 0 or data['grade'] > 100:
        return False, "Grade harus antara 0-100"

    return True, "Valid"

# Class dengan decorator
class UIManager:
    """Class untuk menangani UI dengan decorator"""

    @staticmethod
    @timer_decorator
    def display_menu():
        """Tampilkan menu utama"""
        print("\n╔════════════════════════════════════╗")
        print("║       PYTHON DATA MANAGER          ║")
        print("╠════════════════════════════════════╣")
        print("║ 1. Tambah Data                     ║")
        print("║ 2. Lihat Data                      ║")
        print("║ 3. Cari Data                       ║")
        print("║ 4. Update Data                     ║")
        print("║ 5. Hapus Data                      ║")
        print("║ 6. Statistik                       ║")
        print("║ 7. Sorting                         ║")
        print("║ 8. Export CSV                      ║")
        print("║ 9. Visualisasi                     ║")
        print("║ 10. Import dari API                ║")
        print("║ 0. Keluar                          ║")
        print("╚════════════════════════════════════╝")

    @staticmethod
    @log_decorator
    @validate_input
    def get_menu_choice():
        """Dapatkan pilihan menu dengan validasi"""
        try:
            choice = input("\nPilih menu (0-10): ").strip()
            if not choice.isdigit():
                raise ValueError("Input harus angka")
            return int(choice)
        except ValueError as e:
            print(f"⚠️ {e}")
            return -1
