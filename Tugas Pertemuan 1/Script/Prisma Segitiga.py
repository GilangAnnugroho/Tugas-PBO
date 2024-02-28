print("Aplikasi Menghitung Luas dan Volume Prisma Segitiga")
"""
Nama  : Gilang Annugroho
Keterangan:
S = Sisi
T = Tinggi prisma
a = Alas
t = Tinggi
"""
# Atur Nilai
S_1 = 5
S_2 = 6
S_3 = 7
T = 8
a = 9 
t = 10
# Rumus
keliling_segitiga = S_1 + S_2 + S_3
luas_segitiga = keliling_segitiga * T
luas_prisma = keliling_segitiga * T + a * t
volume = 1/2 * a * t * T
# Output
print("Sisi 1:", S_1)
print("Sisi 2:", S_2)
print("Sisi 3:", S_3)
print("Tinggi Prisma:", T)
print("Alas:", a)
print("Tinggi:", t)
print("Keliling Segitiga: ", keliling_segitiga)
print("Luas Segitiga: ", luas_segitiga)
print("Luas Prisma: ", luas_prisma)
print("Volume: ", volume)