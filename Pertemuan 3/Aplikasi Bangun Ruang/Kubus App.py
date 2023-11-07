import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    r = float(txtrusuk.get())
    L = round(6 * r**2,2)

    txtLuas.delete(0, END)
    txtLuas.insert(END, L)

def hitung_volume():
    r = float(txtrusuk.get())
    V = round(r**3,2)

    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create
app = tk.Tk()

# Judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app)
frame.pack (padx=20, pady=20)

# Label Rusuk
rusuk = Label(frame, text="Rusuk:")
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Rusuk
txtrusuk = Entry(frame)
txtrusuk.grid(row=0, column=1)

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