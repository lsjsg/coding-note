from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        root_widget = Label(text="It is fun to program", font_size=80)
        root_widget.bind(on_touch_down=self.change)
        return root_widget

    def change(self, instance, touch):
        if instance.text == "Programming is fun":
            instance.text = "It is fun to program"
        else:
            instance.text = "Programming is fun"


my_app = TestApp()
my_app.run()
