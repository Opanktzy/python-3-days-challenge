class Student:
    def __init__(self, nama, umur, kelas, nilai, status):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas
        self.nilai = nilai
        self.status = "Lulus" if nilai >= 70 else "Tidak Lulus"
    def tampilkan_info(self):
        print("==== DATA STUDENT ====")
        self.nama = input("Nama: ")
        self.umur = int(input("Umur: "))
        self.kelas = input("Kelas: ")
        self.nilai = int(input("Nilai: "))
    def cek_kelulusan(self):
        print("=====================")
        print(f"Nama : {self.nama}")
        print(f"Umur : {self.umur}")
        print(f"Kelas : {self.kelas}")
        print(f"Nilai : {self.nilai}")
        print(f"Status : {self.status}")

def main():
    student = Student("", 0, "", 0, "")
    student.tampilkan_info()
    student.cek_kelulusan()


main()
