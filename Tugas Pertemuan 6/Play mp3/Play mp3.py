import tkinter as tk
from tkinter import filedialog
import pygame
import os
import time

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player App")

        self.music_path = ""
        self.paused = False

        # Inisialisasi Pygame
        pygame.init()

        # Frame untuk menempatkan elemen-elemen GUI
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Label untuk menampilkan nama file
        self.filename_label = tk.Label(self.frame, text="File tidak dipilih")
        self.filename_label.grid(row=0, column=0, pady=10, columnspan=2)

        # Entry untuk memasukkan nama lengkap
        self.fullname_entry = tk.Entry(self.frame, width=30)
        self.fullname_entry.grid(row=1, column=0, pady=10, columnspan=2)

        # Button untuk memilih file musik
        self.select_button = tk.Button(self.frame, text="Pilih Musik", command=self.select_music)
        self.select_button.grid(row=2, column=0, pady=10)

        # Button untuk memutar atau menghentikan musik
        self.play_button = tk.Button(self.frame, text="Putar", command=self.play_pause_music)
        self.play_button.grid(row=2, column=1, padx=10)

        # Label untuk menampilkan durasi pemutaran
        self.duration_label = tk.Label(self.frame, text="Durasi: 0:00")
        self.duration_label.grid(row=3, column=0, columnspan=2)

        # Variable untuk menyimpan waktu mulai pemutaran
        self.start_time = None

        # Memanggil metode untuk memperbarui durasi secara berkala
        self.root.after(1000, self.update_duration)

    def select_music(self):
        # Membuka dialog pemilihan file musik
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])

        if file_path:
            self.music_path = file_path
            self.filename_label.configure(text=os.path.basename(file_path))

    def play_pause_music(self):
        if self.music_path:
            if not pygame.mixer.music.get_busy() or self.paused:
                pygame.mixer.music.load(self.music_path)
                pygame.mixer.music.play()
                self.play_button.configure(text="Jeda")
                self.paused = False
                # Menyimpan waktu mulai pemutaran
                self.start_time = time.time()
            else:
                pygame.mixer.music.pause()
                self.play_button.configure(text="Putar")
                self.paused = True

    def update_duration(self):
        if pygame.mixer.music.get_busy() and not self.paused and self.start_time is not None:
            # Menghitung durasi pemutaran
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            duration_text = f"Durasi: {minutes}:{seconds:02d}"
            self.duration_label.configure(text=duration_text)

        # Memanggil metode ini secara rekursif untuk terus memperbarui durasi
        self.root.after(1000, self.update_duration)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
