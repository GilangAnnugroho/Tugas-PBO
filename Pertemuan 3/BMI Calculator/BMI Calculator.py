import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

"""
Saya menggunakan Virtual Environtment
untuk menjalankan program matplotlib
karena tidak terbaca pada VScode saya
"""

def perbarui_label():
    if pilihan_unit.get() == "US Units":
        label_berat.config(text="Berat (lbs):")
        label_tinggi.config(text="Tinggi (in):")
    elif pilihan_unit.get() == "Metric Units":
        label_berat.config(text="Berat (kg):")
        label_tinggi.config(text="Tinggi (cm):")

def hitung_bmi(event=None):
    berat = float(berat_entry.get())
    tinggi = float(tinggi_entry.get())
    umur = int(umur_entry.get())

    if pilihan_unit.get() == "US Units":
        bmi = (berat / (tinggi ** 2)) * 703
    elif pilihan_unit.get() == "Metric Units":
        bmi = berat / ((tinggi/100) ** 2)

    label_bmi.config(text=f"BMI: {bmi:.2f}")

    if umur >= 18:
        if bmi < 16:
            kategori = "Kurus Parah"
            nilai_kategori = "<16"
        elif 16 <= bmi < 17:
            kategori = "Kurus Sedang"
            nilai_kategori = "16-17"
        elif 17 <= bmi < 18.5:
            kategori = "Kurus Ringan"
            nilai_kategori = "17-18.5"
        elif 18.5 <= bmi < 25:
            kategori = "Normal"
            nilai_kategori = "18.5-25"
        elif 25 <= bmi < 30:
            kategori = "Kelebihan Berat Badan"
            nilai_kategori = "25-30"
        elif 30 <= bmi < 35:
            kategori = "Obesitas Kelas 1"
            nilai_kategori = "30-35"
        elif 35 <= bmi < 40:
            kategori = "Obesitas Kelas 2"
            nilai_kategori = "35-40"
        elif bmi >= 40:
            kategori = "Obesitas Kelas 3"
            nilai_kategori = ">40"

    label_kategori.config(text=f"Kategori: {kategori} ({nilai_kategori})")

    kategori_bmi = ['<16', '16-17', '17-18.5', '18.5-25', '25-30', '30-35', '35-40', '>40']
    nilai_bmi = [16, 17, 18.5, 25, 30, 35, 40, 45]

    plt.figure(figsize=(5, 4))
    plt.plot(kategori_bmi, nilai_bmi, marker='o', color='b', linestyle='-')
    plt.xlabel('Kategori')
    plt.ylabel('Nilai BMI')
    plt.title('Grafik BMI')
    plt.grid()

    plt.scatter(nilai_kategori, bmi, color='r')
    plt.axhline(y=bmi, color='r', linestyle='--')

    plt.xticks(rotation=45, ha="right", fontsize=8)

    canvas = FigureCanvasTkAgg(plt.gcf(), master=mainframe)
    canvas.draw()
    canvas.get_tk_widget().grid(column=1, row=9, columnspan=2, rowspan=6, sticky=(tk.W, tk.E, tk.N, tk.S))

root = tk.Tk()
root.title("Kalkulator BMI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

pilihan_unit = ttk.Combobox(mainframe, values=["US Units", "Metric Units"], state="readonly")
pilihan_unit.grid(column=1, row=1, sticky=(tk.W, tk.E))
pilihan_unit.current(1)  # Atur nilai default ke "Metric Units"
pilihan_unit.bind("<<ComboboxSelected>>", lambda e: perbarui_label())

pilihan_gender = ttk.Combobox(mainframe, values=["Pria", "Wanita"], state="readonly")
pilihan_gender.grid(column=1, row=4, sticky=(tk.W, tk.E))
pilihan_gender.current(0)

label_berat = ttk.Label(mainframe, text="Berat (kg):")
label_berat.grid(column=1, row=2, sticky=tk.W)

label_tinggi = ttk.Label(mainframe, text="Tinggi (cm):")
label_tinggi.grid(column=1, row=3, sticky=tk.W)

ttk.Label(mainframe, text="Umur:").grid(column=1, row=5, sticky=tk.W)

berat_entry = ttk.Entry(mainframe, width=7, style="Custom.TEntry")
berat_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
tinggi_entry = ttk.Entry(mainframe, width=7, style="Custom.TEntry")
tinggi_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))
umur_entry = ttk.Entry(mainframe, width=7, style="Custom.TEntry")
umur_entry.grid(column=2, row=5, sticky=(tk.W, tk.E))

s = ttk.Style()
s.configure("Custom.TEntry", foreground="black", highlightcolor="black")

ttk.Button(mainframe, text="Hitung BMI", command=hitung_bmi).grid(column=2, row=6, sticky=tk.W)

label_bmi = ttk.Label(mainframe, text="")
label_bmi.grid(column=2, row=7, sticky=(tk.W, tk.E))

label_kategori = ttk.Label(mainframe, text="")
label_kategori.grid(column=2, row=8, sticky=(tk.W, tk.E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

perbarui_label()
umur_entry.bind('<Return>', hitung_bmi)
root.mainloop()