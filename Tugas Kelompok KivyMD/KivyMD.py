from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CubeVolumeCalculator(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create widgets
        self.side_length_label = Label(text="Masukkan Panjang Sisi :")
        self.side_length_input = TextInput(multiline=False)

        self.result_label = Label(text="Hasil :")

        calculate_button = Button(text="Hitung Volume")
        calculate_button.bind(on_press=self.calculate_volume)

        # Add widgets to the layout
        layout.add_widget(self.side_length_label)
        layout.add_widget(self.side_length_input)
        layout.add_widget(calculate_button)
        layout.add_widget(self.result_label)

        return layout

    def calculate_volume(self, instance):
        try:
            side_length = float(self.side_length_input.text)
            volume = side_length ** 3
            result_text = f"Hasil : Volume kubusnya adalah {volume:.2f} kubik"
        except ValueError:
            result_text = "Hasil : Masukkan nilai numerik yang valid untuk panjang sisinya."

        self.result_label.text = result_text


if __name__ == '__main__':
    CubeVolumeCalculator().run()
