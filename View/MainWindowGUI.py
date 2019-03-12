from View.Settings import SettingsScreen
import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.config import Config
from kivy.core.window import Window

# I am here!!:)
class MainWindowScreen(Screen):
    pass

class MainWindowApp(App):
    def build(self):
        sm = ScreenManager()
        Window.size = (900, 700)
        Config.write()
        sm.add_widget(MainWindowScreen())
        sm.add_widget(SettingsScreen(name='settingsScreen'))
        return sm

app = MainWindowApp()
app.run()

