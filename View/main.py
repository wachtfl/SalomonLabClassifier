from kivy.app import App
from Model.Settings_m import SettingsM
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

import os


class CustomDropDown(DropDown):
    pass


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(TabbedPanel):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    model = SettingsM()
    e1 = NumericProperty(20)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def build(self):
        return GridLayout()

    def createDropDown(self, list):
        dropdown = CustomDropDown()
        for i in range(len(list)):
            btn = Button(text='Value %s' % str(list[i]), size_hint_y=None, height=44)
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


class EEGApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    EEGApp().run()
