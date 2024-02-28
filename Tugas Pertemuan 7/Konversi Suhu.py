import tkinter as tk

# Buat instance dari Tkinter
root = tk.Tk()
root.title("Temperature Converter")

# Buat label untuk input suhu
label_temperature = tk.Label(root, text="Enter Temperature:")
label_temperature.pack(pady=10)

# Buat entry untuk memasukkan suhu
entry_temperature = tk.Entry(root)
entry_temperature.pack(pady=10)

# Buat label untuk memilih jenis suhu dari
label_from = tk.Label(root, text="From:")
label_from.pack()

# Buat dropdown untuk memilih jenis suhu dari
options = ["Celsius", "Fahrenheit", "Kelvin"]
combo_from = tk.StringVar()
combo_from.set(options[0])  # Set default value
dropdown_from = tk.OptionMenu(root, combo_from, *options)
dropdown_from.pack(pady=10)

# Buat label untuk memilih jenis suhu ke
label_to = tk.Label(root, text="To:")
label_to.pack()

# Buat dropdown untuk memilih jenis suhu ke
combo_to = tk.StringVar()
combo_to.set(options[1])  # Set default value
dropdown_to = tk.OptionMenu(root, combo_to, *options)
dropdown_to.pack(pady=10)

# Buat textbox untuk menampilkan hasil konversi
entry_result = tk.Entry(root, state=tk.DISABLED)
entry_result.pack()

def convert_temperature():
    try:
        # Ambil nilai dari inputan pengguna
        input_temperature = float(entry_temperature.get())

        # Ambil jenis suhu yang dipilih
        input_scale = combo_from.get()
        output_scale = combo_to.get()

        # Lakukan konversi suhu
        if input_scale == "Celsius" and output_scale == "Fahrenheit":
            result = (input_temperature * 9/5) + 32
        elif input_scale == "Celsius" and output_scale == "Kelvin":
            result = input_temperature + 273.15
        elif input_scale == "Fahrenheit" and output_scale == "Celsius":
            result = (input_temperature - 32) * 5/9
        elif input_scale == "Fahrenheit" and output_scale == "Kelvin":
            result = (input_temperature - 32) * 5/9 + 273.15
        elif input_scale == "Kelvin" and output_scale == "Celsius":
            result = input_temperature - 273.15
        elif input_scale == "Kelvin" and output_scale == "Fahrenheit":
            result = (input_temperature - 273.15) * 9/5 + 32
        else:
            result = input_temperature  # Jika jenis suhu sama, hasilnya tetap

        # Ubah state entry_result menjadi NORMAL
        entry_result.config(state=tk.NORMAL)

        # Update textbox dengan hasil konversi
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{result:.2f} {output_scale}")

        # Kembalikan state entry_result menjadi DISABLED
        entry_result.config(state=tk.DISABLED)

    except ValueError:
        # Tangani jika pengguna memasukkan sesuatu yang bukan angka
        entry_result.config(state=tk.NORMAL)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Please enter a valid temperature")
        entry_result.config(state=tk.DISABLED)

# Buat tombol konversi suhu
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=20)

# Jalankan aplikasi Tkinter
root.mainloop()
