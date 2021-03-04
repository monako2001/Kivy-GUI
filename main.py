import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '400')

# Creating Layout class
class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        try:
            self.display.text = str(eval(calculation))
        except Exception:
            self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()