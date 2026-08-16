numbers = [12, 5, 8, 20, 3, 15, 7]
nilai = numbers[0]
jumlah = numbers[0]
for n in numbers:
    if n > nilai:
        nilai = n
print(f"Nilai terbesar: {nilai}")

for n in numbers:
    if n < nilai:
        nilai = n
print(f"Nilai terkecil: {nilai}")

for n in numbers:
    jumlah += n
print(f"Jumlah: {jumlah}")

for n in numbers:
    jumlah += n
print(f"Rata-rata: {jumlah / len(numbers):.0f}")
