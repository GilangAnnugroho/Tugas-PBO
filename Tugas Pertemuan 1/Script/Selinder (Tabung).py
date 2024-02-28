print("Aplikasi Menghitung Luas dan Volume Selinder (Tabung)")

"""
Nama  : Gilang Annugroho
NIM   : 220511135
Kelas : TI22B
PBO   : Tugas Pertemuan 1

Keterangan:
L = Luas permukaan tabung
r = Jari - jari lingkaran tabung
T = Tinggi
phi = 3.14
"""

# Atur Nilai
phi = 3.14
r = 19
T = 45

# Rumus
luas_selimut = 2 * phi * r * T
luas_permukaan = (2 * phi * r * T) + (2 * phi * r**2)
volume = phi * r**2 * T

# output
print("Phi:", phi)
print("Jari - Jari Lingkaran Tabung:", r)
print("Tinggi:", T)
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)