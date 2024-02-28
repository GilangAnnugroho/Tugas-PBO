import math

def luas_limpat(sisi_alas,tinggi_limas,tinggi_segitiga) :
    luas_limpat = round ((sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga))
    return luas_limpat
def volume_limpat (sisi_alas,tinggi_limas) :
    volume_limpat = round ((sisi_alas ** 2 * tinggi_limas) / 3)
    return volume_limpat

def luas_balok (p,l,t) :
    luas_balok = round (2*p*l) + (2*p*t) + (2*l*t)
    return luas_balok
def volume_balok (p,l,t) :
    volume_balok = round (p*l*t)
    return volume_balok

def luas_bola (j) :
    luas_bola = round (4 * math.pi * (j ** 2))
    return luas_bola
def volume_bola (j) :
    volume_bola = round ((4/3) * math.pi * (j ** 3))
    return volume_bola

def luas_k (j,g_pelukis) :
    luas_k = round (math.pi * j * (j + g_pelukis))
    return luas_k
def volume_k (j,t) :
    volume_k = round ((1/3) * math.pi * (j ** 2) * t)
    return volume_k

def luas_kubus (r) :
    luas_kubus = round (6 * (r ** 2))
    return luas_kubus
def volume_kubus (r) :
    volume_kubus = round ( r ** 3)
    return volume_kubus

def luas_limse (sisi_alas,tinggi_limas,tinggi_segitiga) :
    luas_limse = round ((sisi_alas * tinggi_limas) / 2 + 3 * (0.5 * sisi_alas * tinggi_segitiga))
    return luas_limse
def volume_limse (sisi_alas,tinggi_segitiga) :
    volume_limse = round ((sisi_alas ** 2 * tinggi_segitiga) / 6)
    return volume_limse

def luas_prisma_segitiga (alas_segitiga,tinggi_prisma,tinggi_segitiga) :
    luas_prisma_segitiga = round ((alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga))
    return luas_prisma_segitiga
def volume_prisma_segitiga (alas_segitiga,tinggi_segitiga,tinggi_prisma) :
    volume_prisma_segitiga = round (0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma)
    return volume_prisma_segitiga

def luas_tabung (j,t) :
    luas_tabung = round (2 * math.pi * j * (j + t))
    return luas_tabung
def volume_tabung (j,t) :
    volume_tabung = round (math.pi * (j ** 2) * t)
    return volume_tabung
