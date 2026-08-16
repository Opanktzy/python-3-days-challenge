
import statistics as st

class Student:
    # List class untuk menampung semua data siswa
    list_student = []

    # Memberikan default value None agar bisa membuat objek kosong untuk menu
    def __init__(self, nama=None, nilai=None):
        if nama is not None and nilai is not None:
            self.nama = nama
            self.nilai = nilai
            self.list_student.append(self)

    def add(self):
        nama = input("Nama: ")
        nilai = int(input("Nilai: "))
        # Membuat objek baru dan otomatis masuk ke list_student
        Student(nama, nilai)
        print(f"Siswa {nama} berhasil ditambahkan.")

    def look(self):
        if not self.list_student:
            print("Belum ada data siswa.")
            return
        print("\n--- Daftar Siswa ---")
        for student in self.list_student:
            print(f"Nama: {student.nama} | Nilai: {student.nilai}")

    def search(self):
        nama = input("Masukkan nama siswa yang dicari: ")
        for student in self.list_student:
            if student.nama.lower() == nama.lower():
                print(f"Ditemukan! Nama: {student.nama}, Nilai: {student.nilai}")
                return
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

    def count(self):
        if not self.list_student:
            print("Belum ada data untuk dihitung.")
            return
        # Mengambil angka nilai saja dari daftar objek siswa
        daftar_nilai = [s.nilai for s in self.list_student]
        total = sum(daftar_nilai)
        jumlah = len(self.list_student)
        avarag = st.mean(daftar_nilai)  # Memasukkan list angka, bukan list objek
        print(f"Total Nilai: {total}, Jumlah Siswa: {jumlah}, Rata-rata: {avarag:.2f}")

    def siswa_terbaik(self):
        if not self.list_student:
            print("Belum ada data siswa.")
            return
        siswa_terbaik = max(self.list_student, key=lambda x: x.nilai)
        print(f"Siswa terbaik: {siswa_terbaik.nama} dengan nilai {siswa_terbaik.nilai}")

    def delete(self):
        nama = input("Masukkan nama siswa yang ingin dihapus: ")
        for student in self.list_student:
            if student.nama.lower() == nama.lower():
                self.list_student.remove(student)
                print(f"Siswa {nama} telah dihapus.")
                return
        print(f"Siswa {nama} tidak ditemukan.")

    def main(self):
        while True:
            print("\n===== Student Management =====")
            print("1. Tambah siswa")
            print("2. Lihat siswa")
            print("3. Cari siswa")
            print("4. Hitung Rata-rata Nilai")
            print("5. Tentukan Siswa terbaik")
            print("6. Hapus siswa")
            print("7. Keluar")

            try:
                pilihan = int(input("Pilihan: "))
                if pilihan == 1:
                    self.add()
                elif pilihan == 2:
                    self.look()
                elif pilihan == 3:
                    self.search()
                elif pilihan == 4:
                    self.count()
                elif pilihan == 5:
                    self.siswa_terbaik()
                elif pilihan == 6:
                    self.delete()
                elif pilihan == 7:
                    print("Terima kasih telah menggunakan program ini.")
                    break
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan input berupa angka!")

# Menjalankan aplikasi
if __name__ == "__main__":
    app = Student()
    app.main()
