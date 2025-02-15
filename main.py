from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from canvas_exemples import *
from nevigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass


class LeLabApp(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        # return CanvasExemple7()


LeLabApp().run()
