import time

def timer(fungsi_asli):
    def bugnkus(*args, **kwargs):
        print("Memulai........")
        waktu_mulai = time.perf_counter()
        hasil = fungsi_asli(*args, **kwargs)
        waktu_selesai = time.perf_counter()
        print("Selesai.")
        print(f"Durasi: {waktu_selesai - waktu_mulai} detik")
        return hasil
    return bugnkus

@timer
def kalkulasi():
    total = 0
    for i in range(1000000):
        total += i
    return total

kalkulasi()
