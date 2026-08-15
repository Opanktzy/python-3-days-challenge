import os
from pathlib import Path

def look_folder():
    try:
        folder_path = input("Masukan path folder: ")
        isi_folder = input("Pilih opsi[. / ..] :")
        print("-"*30)
        print(f"Posisi sekarang: {os.getcwd()}")
        print("-"*30)
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"[Folder] {entry.name}")
                elif entry.is_file():
                    print(f"[File] {entry.name}")
                else:
                    print(f"[Unknown] {entry.name}")
    except Exception as e:
        print(f"Error: {e}")

def create_folder():
    try:
        print("="*30)
        lokasi_folder = input("Masukan Path Folder: ")
        folder_name = input("Masukan Nama Folder: ")
        os.mkdir(os.path.join(lokasi_folder, folder_name))
        print(f"Folder [{folder_name}] Berhasil dibuat di [{os.path.join(lokasi_folder, folder_name)}]")
    except Exception as e:
        print(f"Error: {e}")

def remove_folder():
    try:
        folder_path = input("Masukan path Folder :")
        print("1. Hapus Folder")
        print("2. Hapus File")
        print("3. Hapus Folder Berisi")
        print("4. Kembali")
        choice = input("Pilih opsi: ")
        if choice == "4":
            return
        if choice == "1":
            os.rmdir(folder_path)
            print(f"Folder [{folder_path}] Berhasil di hapus")
        elif choice == "2":
            os.remove(folder_path)
            print(f"File [{folder_path}] Berhasil di hapus")
        elif choice == "3":
            shutil.rmtree(folder_path)
            print(f"Folder [{folder_path}] Berhasil di hapus")
    except Exception as e:
        print(f"Error: {e}")

def search_folder():
    try:
        folder_path = input("Masukan Path Folder: ")
        if folder_path.exists():
            print(f"Folder [{folder_path}] ditemukan")
        else:
            print("Folder tidak ditemukan")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        while True:
            print("="*30)
            print("1. Lihat Isi Folder")
            print("2. Buat Folder")
            print("3. Hapus Folder")
            print("4. Cek apakah file/folder ada")
            print("5. Keluar")
            choice = input("Pilih opsi: ")
            if choice == "5":
                break
            elif choice == "1":
                look_folder()
            elif choice == "2":
                create_folder()
            elif choice == "3":
                remove_folder()
            else:
                print("Opsi tidak valid")

    except Exception as e:
        print(f"Error: {e}")

main()
