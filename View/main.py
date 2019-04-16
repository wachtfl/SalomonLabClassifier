from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel


class Test(TabbedPanel):
    pass


class EEGApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    EEGApp().run()
