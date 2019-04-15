from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)


class Myapp(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(MyLabel(text="Amount"))
        self.amount = a = TextInput(text="0")
        layout.add_widget(a)

        layout.add_widget(MyLabel(text="Year"))
        self.year = y = TextInput(text="0")
        layout.add_widget(y)

        layout.add_widget(MyLabel(text="Rate"))
        self.rate = r = TextInput(text="0")
        layout.add_widget(r)

        layout.add_widget(MyLabel(text="Future value"))
        self.future = f = TextInput(text="0")
        layout.add_widget(f)

        layout.add_widget(Button(text="calculate", on_press=self.calculate))

        return layout

    def calculate(self, instance):
        amount = float(self.amount.text)
        rate = float(self.rate.text)
        year = float(self.year.text)
        self.future.text = str(amount*(1+rate/100/12)**(year*12))


myapp = Myapp()
myapp.run()
