import asyncio
import time

async def pekerjaan(task, duration):
    print(f"Task Mulai dikerjakan {task} ({duration} detik)")

    await asyncio.sleep(duration)

    print(f"[Selesai] Proses {task} Selesai")
    return f"Data {task}"


async def main():
    waktu_mulai = time.perf_counter()

    print("==========  MEMULAI PROSES DENGAN CONCURRENCY ==============\n")

    result = await asyncio.gather(
        pekerjaan(1, 2),
        pekerjaan(2, 2),
        pekerjaan(3, 2)
    )
    waktu_selesai = time.perf_counter()
    print(f"Hasil diterima : {result}")
    print(f"[Selesai] Proses selesai dalam {waktu_selesai - waktu_mulai:.2f} detik")

asyncio.run(main())
