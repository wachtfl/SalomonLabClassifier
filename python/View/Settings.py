from Model.Settings_m import SettingsM
from Model.Data import Data

import kivy
kivy.require('1.10.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

class CustomDropDown(DropDown):
    pass

class SettingsScreen(Screen):
    model = SettingsM(["svm"])
    e1 = NumericProperty(20)

    def build(self):
        return GridLayout()

    def createDropDown(self, list):
        dropdown = CustomDropDown()
        for i in range(len(list)):
            btn = Button(text='Value %s' %str(list[i]) , size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
            mainbutton = Button(text='Hello', size_hint=(None, None))
            mainbutton.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

    def listAlgorithms(self):
        print(self.model.getAlgorithms())

    def listFeatures(self):
        print(self.model.getFeatures())

    def onSubmit(self):
        print("test set is: ", self.e1)

    def on_slider_value_changed(self, instance, value):
        self.e1 = value

