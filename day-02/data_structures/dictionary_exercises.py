numbers = [1, 4, 7, 10, 13, 16, 20, 25, 30]

genap = []
ganjil = []

for n in numbers:
    if n % 2 == 0:
        genap.append(n)
    else:
        ganjil.append(n)

print(f"Bilangan Genap: {genap}")
print(f"Bilangan Ganjil: {ganjil}")
