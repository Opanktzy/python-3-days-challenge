import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(numbers[1:3])
print(numbers[:3])
print(arr_2d[0, 2])
print(arr_2d[1, 1])

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + 2)    # Hasil: [3, 4, 5] (ditambah ke semua elemen)
print(a * b)    # Hasil: [4, 10, 18] (perkalian posisi yang sama)
print(b ** 2)   # Hasil: [16, 25, 36] (pangkat dua)

data = np.array([1, 2, 3, 4, 5])
print(np.sum(data))   # Hasil: 15 (total penjumlahan)
print(np.mean(data))  # Hasil: 3.0 (rata-rata)
print(np.max(data))   # Hasil: 5 (nilai tertinggi)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Hasil: (2, 3) -> Artinya 2 baris dan 3 kolom


# Membuat array 1D dengan 6 elemen
awal = np.array([1, 2, 3, 4, 5, 6])

# Mengubah menjadi 2 baris dan 3 kolom (2D)
baru_2d = awal.reshape(2, 3)
print(baru_2d)
# Hasil:
# [[1, 2, 3],
#]

# Mengubah menjadi 3 baris dan 2 kolom (2D)
baru_3d = awal.reshape(3, 2)
print(baru_3d)
# Hasil:
# [[1, 2],
#,
#]
