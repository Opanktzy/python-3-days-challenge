import threading
import time

def tugas(nama, durasi):
    print(f"[Awal] Tugas {nama} dimulai...")
    time.sleep(durasi)  # Simulasi proses yang memakan waktu (misal: download)
    print(f"[Selesai] Tugas {nama} selesai!")

# 1. Membuat objek Thread
thread1 = threading.Thread(target=tugas, args=("A", 3)) # Berjalan 3 detik
thread2 = threading.Thread(target=tugas, args=("B", 1)) # Berjalan 1 detik
waktu_mulai = time.perf_counter()

# 2. Memulai eksekusi Thread
thread1.start()
thread2.start()

# 3. Menunggu semua Thread selesai sebelum melanjutkan program utama
thread1.join()
thread2.join()

waktu_selesai = time.perf_counter()
print(f"Semua tugas selesai, program utama ditutup. Waktu yang dibutuhkan: {waktu_selesai - waktu_mulai:.2f} detik  .")
