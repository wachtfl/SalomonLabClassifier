import os

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel

from Model.Settings_m import SettingsM


class CustomDropDown(DropDown):
    def select(self, feature):
        print(feature, ' was selected')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    text_input = ObjectProperty(None)


class Root(TabbedPanel):
    file_to_save = 0
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    model = SettingsM()
    e1 = NumericProperty(20)
    file_name1 = StringProperty('no file')
    file_name2 = StringProperty('no file')

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self, num):
        self.file_to_save = num
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def showLoadExplanationPopup(self):
        content = Button(text='Close me!')
        popup = Popup(content=content, auto_dismiss=False)
        self._popup.open()

    def load(self, path, filename):
        print('path chosen: ', path, 'file chosen: ', filename)
        print('type is: ', type(filename[0]))
        if self.file_to_save == 1:
            self.file_name1 = path
        elif self.file_to_save == 2:
            self.file_name2 = path

 #       with open(os.path.join(path, filename[0])) as stream:
 #           self.file_text = stream.read()

    def build(self):
        return GridLayout()

    def createDropDown(self, list, but):
        dropdown = CustomDropDown()
        for i in range(len(list)):
            btn = Button(text='Value %s' % str(list[i]), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
#            mainbutton = Button(text='Hello', size_hint=(None, None))
#            mainbutton.bind(on_release=dropdown.open)
#            dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        dropdown.open(but)

    def listAlgorithms(self, btn):
        self.createDropDown(self.model.getAlgorithms(), btn)
        print(self.model.getAlgorithms())

    def listFeatures(self, btn):
        self.createDropDown(self.model.getFeatures(), btn)
        print(self.model.getFeatures())

    def onSubmit(self):
        print("test set is: ", self.e1)

    def on_slider_value_changed(self, instance, value):
        self.e1 = value


class EEGApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    EEGApp().run()
