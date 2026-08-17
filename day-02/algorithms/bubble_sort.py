def bubble_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


angka_acak = [5, 2, 8, 1, 9]
print("Sebelum diurutkan:", angka_acak)

angka_urut = bubble_sort(angka_acak)
print("Setelah diurutkan:", angka_urut)
