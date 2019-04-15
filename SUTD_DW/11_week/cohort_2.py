from kivy.app import App
from kivy.uix.label import Label


class NewApp(App):
    def build(self):
        root_widget = Label(font_size=80)
        root_widget.bind(on_touch_move=self.detect)
        return root_widget

    def detect(self, instance, touch):
        if touch.dx >= 40 and touch.dy >= 40:
            instance.text = "Slide Right\nSlide Up"
        elif touch.dx >= 40 and touch.dy < -40:
            instance.text = "Slide Right\nSlide Down"
        if touch.dx < -40 and touch.dy >= 40:
            instance.text = "Slide Left\nSlide Up"
        elif touch.dx < -40 and touch.dy < -40:
            instance.text = "Slide Left\nSlide Down"


My_app = NewApp()
My_app.run()
