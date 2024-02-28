import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
import balok
def hitung_luas():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())
    
    Luas_balok = balok.luas_balok(p,l,t)

    txtLuas.delete(0,END)
    txtLuas.insert(END,Luas_balok)

def hitung_volume():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())
    
    Volume_balok = balok.volume_balok(p,l,t)

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume_balok)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Balok")

# Windows
frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label Nama
nama= Label (frame, text="Nama : Gilang Annugroho ")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Panjang
panjang= Label (frame, text="Panjang: ")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar = Label(frame, text="Lebar:")
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi 
tinggi = Label(frame, text="Tinggi")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry (frame)
txtpanjang.grid(row=1, column=1)

# Textbox Lebar
txtlebar = Entry (frame)
txtlebar.grid(row=2, column=1)

# Textbox Tinggi
txttinggi = Entry (frame)
txttinggi.grid(row=3, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ") 
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame) 
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()