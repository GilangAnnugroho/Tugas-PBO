def hitung_luas_selimut(r, s, phi=3.14):
    return round((phi * r * s), 2)

def hitung_luas_permukaan(r, s, phi=3.14):
    return round(((phi * r * s) + (phi * r**2)), 2)

def hitung_volume(r, phi=3.14):
    return round((4/3 * phi * r**3), 2)
