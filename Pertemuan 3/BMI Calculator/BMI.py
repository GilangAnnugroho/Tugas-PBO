import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hitung_bmi():
    berat = float(berat_entry.get())
    tinggi = float(tinggi_entry.get())
    usia = float(usia_entry.get())
    jenis_kelamin = jenis_kelamin_var.get()  # Dapatkan jenis kelamin yang dipilih

    satuan = satuan_var.get()
    if satuan == "Metric":
        bmi = berat / ((tinggi / 100) ** 2)
    else:
        bmi = (berat / (tinggi ** 2)) * 703

    if usia <= 20:
        if jenis_kelamin == "Laki-Laki":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]

        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]
    else:
        if jenis_kelamin == "Laki-Laki":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]

        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]

    label_hasil.config(text=f"BMI: {bmi:.2f} ({kategori[0]})")

    # Perbarui grafik BMI
    perbarui_grafik_bmi(bmi, nilai_bmi, kategori)

def perbarui_grafik_bmi(bmi, nilai_bmi, kategori):
    plt.clf()
    plt.plot(kategori, nilai_bmi, marker='o', linestyle='-', color='b')
    plt.fill_between(kategori, nilai_bmi, [0] * len(nilai_bmi), alpha=0.2, color='b')
    plt.ylim(0, 40)
    plt.title("Kategori BMI")
    plt.xlabel("Kategori")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.axhline(y=bmi, color='r', linestyle='--', label="BMI Anda")
    plt.legend()

    canvas.draw()

def perbarui_label_tinggi(event):
    satuan = satuan_var.get()
    if satuan == "Metric":
        label_tinggi.config(text="Tinggi (cm):")
    else:
        label_tinggi.config(text="Tinggi (inci):")

app = tk.Tk()
app.title("Kalkulator BMI")
app.geometry("600x650")  # Mengatur ukuran tampilan aplikasi

# Buat frame untuk satuan dan jenis kelamin
frame_satuan_jk = ttk.LabelFrame(app, text="Satuan dan Jenis Kelamin")
frame_satuan_jk.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Buat frame untuk informasi pribadi
frame_personal = ttk.LabelFrame(app, text="Informasi Pribadi")
frame_personal.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Buat dan konfigurasi dropdown satuan
label_satuan = ttk.Label(frame_satuan_jk, text="Satuan:")
label_satuan.grid(row=0, column=0)
satuan_var = tk.StringVar()
satuan_dropdown = ttk.Combobox(frame_satuan_jk, textvariable=satuan_var, values=["Metric", "US"])
satuan_dropdown.grid(row=0, column=1)
satuan_dropdown.set("Metric")
satuan_dropdown.bind("<<ComboboxSelected>>", perbarui_label_tinggi)

# Buat dan konfigurasi radio button jenis kelamin
label_jk = ttk.Label(frame_satuan_jk, text="Jenis Kelamin:")
label_jk.grid(row=1, column=0)

# Buat dan konfigurasi masukan usia
label_usia = ttk.Label(frame_personal, text="Usia:")
label_usia.grid(row=0, column=0)
usia_entry = ttk.Entry(frame_personal)
usia_entry.grid(row=0, column=1)

# Buat dan konfigurasi masukan berat
label_berat = ttk.Label(frame_personal, text="Berat (kg):")
label_berat.grid(row=1, column=0)
berat_entry = ttk.Entry(frame_personal)
berat_entry.grid(row=1, column=1)

# Buat dan konfigurasi masukan tinggi
label_tinggi = ttk.Label(frame_personal, text="Tinggi (cm):")
label_tinggi.grid(row=2, column=0)
tinggi_entry = ttk.Entry(frame_personal)
tinggi_entry.grid(row=2, column=1)

# Buat dan konfigurasi radio button jenis kelamin
jenis_kelamin_var = tk.StringVar()
radio_laki = ttk.Radiobutton(frame_satuan_jk, text="Laki-Laki", variable=jenis_kelamin_var, value="Laki-Laki")
radio_perempuan = ttk.Radiobutton(frame_satuan_jk, text="Perempuan", variable=jenis_kelamin_var, value="Perempuan")
radio_laki.grid(row=1, column=1)
radio_perempuan.grid(row=1, column=2)
jenis_kelamin_var.set("Laki-Laki")  # Pilihan jenis kelamin default

# Buat dan konfigurasi tombol hitung
tombol_hitung = ttk.Button(app, text="Hitung BMI", command=hitung_bmi)
tombol_hitung.grid(row=3, column=0, columnspan=2)

# Buat dan konfigurasi label hasil
label_hasil = ttk.Label(app, text="")
label_hasil.grid(row=4, column=0, columnspan=2)

# Buat grafik BMI
figure = plt.figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=5, column=0, columnspan=2)

app.mainloop()
