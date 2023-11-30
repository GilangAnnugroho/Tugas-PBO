import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player App")

        self.video_path = ""
        self.cap = None

        # Frame untuk menempatkan elemen-elemen GUI
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Button untuk memilih file video
        self.select_button = tk.Button(self.frame, text="Pilih Video", command=self.select_video)
        self.select_button.grid(row=0, column=0, pady=10)

        # Button untuk memutar video
        self.play_button = tk.Button(self.frame, text="Putar", command=self.play_video)
        self.play_button.grid(row=0, column=1, padx=10)

        # Button untuk menghentikan video
        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop_video)
        self.stop_button.grid(row=0, column=2, padx=10)

        # Panel untuk menampilkan video
        self.panel = tk.Label(self.frame)
        self.panel.grid(row=1, columnspan=3)

    def select_video(self):
        # Membuka dialog pemilihan file video
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])

        if file_path:
            self.video_path = file_path
            self.cap = cv2.VideoCapture(self.video_path)

            # Memutuskan sambungan video jika sebelumnya ada yang terhubung
            if self.cap.isOpened():
                self.cap.release()

            self.play_video()  # Memulai pemutaran video setelah pemilihan file

    def play_video(self):
        if self.cap and not self.cap.isOpened():
            self.cap = cv2.VideoCapture(self.video_path)

        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Mengonversi frame dari BGR ke RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Mengonversi frame ke format yang dapat ditampilkan oleh Tkinter
                image = Image.fromarray(frame_rgb)
                photo = ImageTk.PhotoImage(image)

                # Menampilkan frame di panel
                self.panel.configure(image=photo)
                self.panel.image = photo

                # Memanggil metode ini secara rekursif untuk terus memutar video
                self.root.after(10, self.play_video)
            else:
                # Menghentikan video jika sudah selesai
                self.stop_video()

    def stop_video(self):
        # Menutup koneksi video
        if self.cap and self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
