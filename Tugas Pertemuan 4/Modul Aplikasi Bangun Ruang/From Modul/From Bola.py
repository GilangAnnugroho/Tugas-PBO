import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi
from fungsi import luas_bola,volume_bola
def hitung_luas():
    j = float(txtjari_jari.get())
    
    L = luas_bola(j)
    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    j = float(txtjari_jari.get())

    V = volume_bola(j)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Keliling Bola")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Gilang Annugroho") 
nama.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5,)

# Label Jari-jari
Jari_jari = Label(frame, text="Jari-jari:") 
Jari_jari.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Textbox
txtjari_jari= Entry(frame)
txtjari_jari.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#label volume
Volume= Label(frame, text="Volume:")
Volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

#label Luas
Luas= Label(frame, text="Luas:")
Luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()