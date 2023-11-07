import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    phi = 3.14
    r = float(txtjarijari.get())
    L = round((4 * phi * r**2),2)

    txtLuas.delete(0, END)
    txtLuas.insert(END, L)

def hitung_volume():
    phi = 3.14
    r = float(txtjarijari.get())
    V = round((4/3 * phi * r**3),2)

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label Jari-Jari
jarijari = Label(frame, text="Jari-Jari:")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Jari-Jari
txtjarijari = Entry(frame)
txtjarijari.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas:" )
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=2, column=1)

# Output Volume
volume= Label(frame, text="Volume:" )
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)
#  Textbox Volume 
txtVolume = Entry(frame)
txtVolume.grid(row=3, column=1)

app.mainloop()