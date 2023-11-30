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
        self.side_length_label = Label(text="Enter Side Length:")
        self.side_length_input = TextInput(multiline=False)

        self.result_label = Label(text="Result: Volume will be displayed here")

        calculate_button = Button(text="Calculate Volume")
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
            result_text = f"Result: The volume of the cube is {volume:.2f} cubic units"
        except ValueError:
            result_text = "Result: Please enter a valid numeric value for the side length."

        self.result_label.text = result_text


if __name__ == '__main__':
    CubeVolumeCalculator().run()
