from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        layout = BoxLayout()
        layout.add_widget(Button(text="settings", font_size=72,
                                 on_press=self.change_to_setting))
        layout.add_widget(
            Button(text="Quit", font_size=72, on_press=self.quit_app))
        self.add_widget(layout)

    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = "settings"

    def quit_app(self, value):
        App.get_running_app().stop()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        layout = BoxLayout()
        layout.add_widget(Label(text="setting screen", font_size=24))
        layout.add_widget(Button(text="Back to menu",
                                 font_size=24, on_press=self.change_to_menu))
        self.add_widget(layout)

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = "menu"


class SwitchScreenApp(App):
    def build(self):
        sm = ScreenManager()
        ms = MenuScreen(name='menu')
        st = SettingsScreen(name='settings')
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    SwitchScreenApp().run()
