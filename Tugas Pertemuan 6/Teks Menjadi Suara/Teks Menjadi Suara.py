import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import pyttsx3

class TextToSpeechApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Text to Speech")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Masukkan Teks:", self)
        self.text_input = QLineEdit(self)

        self.speak_button = QPushButton("Ucapkan", self)
        self.speak_button.clicked.connect(self.speak_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.speak_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def speak_text(self):
        # Mengambil teks dari input pengguna
        text_to_speak = self.text_input.text()

        # Menggunakan pyttsx3 untuk mengubah teks menjadi suara
        engine = pyttsx3.init()
        engine.say(text_to_speak)
        engine.runAndWait()

def main():
    app = QApplication(sys.argv)
    window = TextToSpeechApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
