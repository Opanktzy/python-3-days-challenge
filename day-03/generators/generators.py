import time as t

def generator(angka_mulai):
    print("---- Generator Dimulai ----")
    while angka_mulai > 0:
        yield angka_mulai
        angka_mulai -= 1
    print("---- Generator Selesai ----")


hitung_mundur = generator(20)

for angka in hitung_mundur:
    print(angka)
    t.sleep(1)
