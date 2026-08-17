import pandas as pd


data = {
    'nama': ['Andi', 'Budi', 'Citra', 'Dewi'],
    'usia': [25, 30, 28, 32],
    'nilai': [85, 90, 88, 92],
}
df = pd.DataFrame(data)
rata_rata = df['nilai'].mean()
nilai_tertinggi = df['nilai'].max()
nilai_terendah = df['nilai'].min()
siswa_pinter= df[df['nilai'] > 80]
print(df)
print("-----------------")
print(f"Nilai rata-rata: {rata_rata}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")
print(f"Siswa dengan nilai > 80:\n {siswa_pinter}")
df.to_csv('siswa_pinter.csv', index=False)
