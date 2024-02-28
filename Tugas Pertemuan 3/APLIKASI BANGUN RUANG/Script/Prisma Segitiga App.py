import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_LS():
    s1 = float((txtsisi1.get()))
    s2 = float((txtsisi2.get()))
    s3 = float((txtsisi3.get()))
    T = float((txttinggiprisma.get()))
    a = float((txtalas.get()))
    t = float((txttinggi.get()))
    LS = round((s1+ s2+ s3) * T,2)

    txtluasselimut.delete(0, END)
    txtluasselimut.insert(END, LS)

def hitung_LP():
    LS = float(txtluasselimut.get())
    a = float((txtalas.get()))
    t = float((txttinggi.get()))
    LP = round(LS + (a * t),2)

    txtluasprisma.delete(0, END)
    txtluasprisma.insert(END, LP)
    
def hitung_volume():
    s1 = float((txtsisi1.get()))
    s2 = float((txtsisi2.get()))
    s3 = float((txtsisi3.get()))
    T = float((txttinggiprisma.get()))
    a = float((txtalas.get()))
    t = float((txttinggi.get()))
    V = round(1/2 * a * t * T,2)

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_LS()
    hitung_LP()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label Sisi 1
sisi1= Label(frame, text="Sisi 1:")
sisi1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 1
txtsisi1 = Entry(frame)
txtsisi1.grid(row=0, column=1)

# Label Sisi 2
sisi2= Label(frame, text="Sisi 2:")
sisi2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 2
txtsisi2 = Entry(frame)
txtsisi2.grid(row=1, column=1)

# Label Sisi 3
sisi3 = Label(frame, text="Sisi 3:")
sisi3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 3
txtsisi3 = Entry(frame)
txtsisi3.grid(row=2, column=1)

# Label Tinggi Prisma
tinggiprisma = Label(frame, text="Tinggi Prisma:")
tinggiprisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi Prisma
txttinggiprisma = Entry(frame)
txttinggiprisma.grid(row=3, column=1)

# Label Alas
alas = Label(frame, text="Alas:")
alas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 5
txtalas = Entry(frame)
txtalas.grid(row=4, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=5, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Luas Selimut
luasselimut= Label(frame, text="Luas Selimut:" )
luasselimut.grid(row=7, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Selimut
txtluasselimut = Entry(frame)
txtluasselimut.grid(row=7, column=1)

# Output Luas Prisma
luasprisma= Label(frame, text="Luas Prisma:" )
luasprisma.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Prisma
txtluasprisma = Entry(frame)
txtluasprisma.grid(row=8, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=9, column=1)

app.mainloop()