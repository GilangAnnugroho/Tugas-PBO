import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import luas_limpat,volume_limpat

def hitung_luas():
    sisi_alas = float(txtsisi_alas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())

    L = luas_limpat(sisi_alas,tinggi_limas,tinggi_segitiga)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    sisi_alas = float(txtsisi_alas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())

    v = volume_limpat(sisi_alas,tinggi_segitiga)
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas Permukaan dan Volume Limas Segiempat")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Gilang Annugroho") 
nama.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5,)

# Label sisi alas
sisi_alas_label = Label(frame, text="sisi_alas :") 
sisi_alas_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label tinggi limas
tinggi_limas = Label(frame, text="tinggi_limas :") 
tinggi_limas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="tinggi_segitiga :") 
tinggi_segitiga.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Textbox
txtsisi_alas= Entry(frame)
txtsisi_alas.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#Textbox
txttinggi_limas= Entry(frame)
txttinggi_limas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#Textbox
txttinggi_segitiga= Entry(frame)
txttinggi_segitiga.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label(frame, text="Volume : ")
Volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()