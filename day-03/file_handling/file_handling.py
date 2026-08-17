import os

def add_file():
    try:
        file_name = input("Enter the file name: ")
        file_path = input("Enter the file path: ")
        full_path = os.path.join(file_path, file_name)
        with open(full_path, 'w') as file:
            file.write(input("Enter the content: \n"))
        print(f"File saved at: {full_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def look_up():
    try:
        file_name = input("Enter the file name: ")
        file_path = input("Enter the file path: ")
        full_path = os.path.join(file_path, file_name)
        if os.path.exists(full_path):
            with open(full_path, 'r') as file:
                print(file.read())
        else:
            print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search():
    try:
        search_term = input("Enter the search term: ")
        for root, dirs, files in os.walk('.'):
            for file in files:
                if search_term in file:
                    print(os.path.join(root, file))
    except Exception as e:
        print(f"An error occurred: {e}")

def delete():
    try:
        file_name = input("Enter the file name: ")
        file_path = input("Enter the file path: ")
        full_path = os.path.join(file_path, file_name)
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"File deleted: {full_path}")
        else:
            print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        try:
            print("1. Create file\n2. Look up file\n3. Search\n4. Delete\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                create()
            elif choice == '2':
                look_up()
            elif choice == '3':
                search()
            elif choice == '4':
                delete()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
