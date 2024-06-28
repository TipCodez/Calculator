from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation

from kivy.lang.builder import Builder

Builder.load_file('./calculator.kv')
# window size
Window.size = (350, 550)

#background color
Window.clearcolor = (1, 1, 1, 1)


class CalculatorWidget(Widget):
    #clear method
    def clear(self):
        self.ids.input_box.text = ""
        #Animation of button
        anim = Animation(color=(1, 0, 0, 1)) + Animation(color=(0, 1, 0, 1))
        anim.repeat = 3
        self.ids.animate.press = anim
        self.ids.animate.press.start(self.ids.animate)

    #Getting button values method
    def button_value(self, number):
        previous_number = self.ids.input_box.text
        

        ##condition for current number
        if "Invalid Expression ‼‼" in previous_number:
            previous_number = ""
        if previous_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{previous_number}{number}"

    # Get operators methods
    def get_operator(self, operator):
        previous_number = self.ids.input_box.text
        self.ids.input_box.text = f"{previous_number}{operator}"

    # Delete method
    def delete_last_number(self):
        previous_number = self.ids.input_box.text
        previous_number = previous_number[:-1]
        self.ids.input_box.text = previous_number

        #animation of button
        anim1 = Animation(color=(1, 0, 0, 1)) + Animation(color=(0, 1, 0, 1))
        anim1.repeat = True
        self.ids.delete.press = anim1
        self.ids.delete.press.start(self.ids.delete)

    def evaluate_results(self):
        previous_number = self.ids.input_box.text
        try:
            self.ids.input_box.text = str(eval(previous_number))
        except:
            self.ids.input_box.text = "Invalid Expression ‼‼"

    def positive_negative(self):
        previous_number = self.ids.input_box.text
        if "-" in previous_number:
            self.ids.input_box.text = f"{previous_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{previous_number}"


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
