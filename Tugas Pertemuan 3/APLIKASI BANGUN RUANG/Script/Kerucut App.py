import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas_selimut():
    phi = 3.14
    r = float(txtjarijari.get())
    s = float(txtgarispelukis.get())
    t = float(txttinggi.get())
    LS = round(phi * r * s,2)

    txtluasselimut.delete(0, END)
    txtluasselimut.insert(END, LS)

def hitung_luas_permukaan():
    phi = 3.14
    r = float(txtjarijari.get())
    s = float(txtgarispelukis.get())
    t = float(txttinggi.get())
    LP = round((phi * r * s) + (phi * r**2),2)

    txtluaspermukaan.delete(0, END)
    txtluaspermukaan.insert(END, LP)

def hitung_volume():
    phi = 3.14
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    V = round(1/3 * phi * r**2 * t,2)

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Kerucut")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label Jari-Jari
jarijari = Label(frame, text="Jari-Jari:")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Jari-Jari
txtjarijari = Entry(frame)
txtjarijari.grid(row=0, column=1)

# Label Garis Pelukis
garispelukis = Label(frame, text="Garis Pelukis:")
garispelukis.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Garis Pelukis
txtgarispelukis = Entry(frame)
txtgarispelukis.grid(row=1, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)


# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut= Label(frame, text="Luas Selimut:" )
luas_selimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Selimut
txtluasselimut = Entry(frame)
txtluasselimut.grid(row=4, column=1)

# Output Label Luas Permukaan
luas_permukaan= Label(frame, text="Luas Permukaan:" )
luas_permukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Permukaan
txtluaspermukaan = Entry(frame)
txtluaspermukaan.grid(row=5, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1)

app.mainloop()