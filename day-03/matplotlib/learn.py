import matplotlib.pyplot as plt

# 1. Menyiapkan Data
bahasa = ['Python', 'Java', 'C', 'JavaScript', 'Go']
nilai = [85, 75, 80, 90, 70]

# =========================================================================
# GRAPH 1: BAR CHART (Grafik Batang) - Cocok untuk perbandingan nilai
# =========================================================================
plt.figure(figsize=(8, 5))
# Membuat grafik batang dengan warna kustom
plt.bar(bahasa, nilai, color=['#3776AB', '#007396', '#A8B9CC', '#F7DF1E', '#00ADD8'])

# Menambahkan judul dan label informasi
plt.title('Perbandingan Nilai Siswa per Bahasa Pemrograman', fontsize=14, fontweight='bold')
plt.xlabel('Bahasa Pemrograman', fontsize=12)
plt.ylabel('Nilai', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) # Menambahkan garis bantu horizontal

# Menampilkan grafik
plt.show()


# =========================================================================
# GRAPH 2: LINE CHART (Grafik Garis) - Cocok untuk melihat tren/urutan
# =========================================================================
plt.figure(figsize=(8, 5))
# Membuat grafik garis dengan penanda (marker) bulat di setiap titik data
plt.plot(bahasa, nilai, marker='o', color='purple', linewidth=2, markersize=8)

# Menambahkan judul dan label informasi
plt.title('Tren Nilai Siswa per Bahasa Pemrograman', fontsize=14, fontweight='bold')
plt.xlabel('Bahasa Pemrograman', fontsize=12)
plt.ylabel('Nilai', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6) # Menambahkan grid penuh (kotak-kotak)

# Menampilkan grafik
plt.show()


# =========================================================================
# GRAPH 3: PIE CHART (Grafik Lingkaran) - Cocok untuk melihat kontribusi/proporsi
# =========================================================================
plt.figure(figsize=(6, 6))
# Membuat grafik lingkaran dengan persentase otomatis (autopct)
# explode digunakan untuk memberikan efek sedikit menonjol pada nilai tertinggi (JavaScript)
efek_tonjol = [0, 0, 0, 0.1, 0]

plt.pie(nilai, labels=bahasa, autopct='%1.1f%%', startangle=140,
        explode=efek_tonjol, colors=['#4f81bd', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6'])

# Menambahkan judul
plt.title('Proporsi Kontribusi Nilai Bahasa Pemrograman', fontsize=14, fontweight='bold')

# Menampilkan grafik
plt.show()
