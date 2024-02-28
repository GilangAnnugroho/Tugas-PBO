import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
from pytesseract import pytesseract

# Define path to Tesseract executable
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor App")

        # Create widgets
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        self.browse_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.extract_button = tk.Button(root, text="Extract Text", command=self.extract_text)
        self.extract_button.pack(pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize image for display
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        self.image_path = file_path

    def extract_text(self):
        if hasattr(self, 'image_path'):
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.result_text.delete(1.0, tk.END)  # Clear previous text
            self.result_text.insert(tk.END, text)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please select an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()