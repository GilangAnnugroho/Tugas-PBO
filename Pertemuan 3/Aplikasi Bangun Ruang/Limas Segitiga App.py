import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    ls1 = float((txtluassisi1.get()))
    ls2 = float((txtluassisi2.get()))
    ls3 = float((txtluassisi3.get()))
    ls4 = float((txtluassisi4.get()))
    a = float((txtalas.get()))
    t = float((txttinggi.get()))
    L = round(ls1+ ls2 + ls3 + ls4,2)

    txtLuas.delete(0, END)
    txtLuas.insert(END, L)

def hitung_volume():
    a = float((txtalas.get()))
    T = float((txttinggiprisma.get()))
    t = float((txttinggi.get()))
    V = round(1/6 * a * t * T,2)

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Limas Segitiga")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label Luas Sisi 1
luassisi1= Label(frame, text="Luas Sisi 1:")
luassisi1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 1
txtluassisi1 = Entry(frame)
txtluassisi1.grid(row=0, column=1)

# Label Luas Sisi 2
luassisi2= Label(frame, text="Luas Sisi 2:")
luassisi2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 2
txtluassisi2 = Entry(frame)
txtluassisi2.grid(row=1, column=1)

# Label Luas Sisi 3
luassisi3 = Label(frame, text="Luas Sisi 3:")
luassisi3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 3
txtluassisi3 = Entry(frame)
txtluassisi3.grid(row=2, column=1)

# Label Luas Sisi 4
luassisi4 = Label(frame, text="Luas Sisi 4:")
luassisi4.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 4
txtluassisi4 = Entry(frame)
txtluassisi4.grid(row=3, column=1)

# Label Tinggi Prisma
tinggiprisma = Label(frame, text="Tinggi Prisma:")
tinggiprisma.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox TInggi Prisma
txttinggiprisma = Entry(frame)
txttinggiprisma.grid(row=4, column=1)

# Label Alas
alas = Label(frame, text="Alas:")
alas.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Alas
txtalas = Entry(frame)
txtalas.grid(row=5, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=6, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas:" )
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=8, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=9, column=1)

app.mainloop()