from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class WidgetExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("0")
    # slider_value_txt = StringProperty("0")
    text_input_str = StringProperty("Toto")

    def on_button_click(self):
        if self.compteur_actif:
            self.mon_texte = str(self.compteur)
            self.compteur += 1

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if (widget.state == "normal"):
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
    #    print("slider: " + str(int(widget.value)))
    #   self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text




class MainWidget(Widget):
    pass


# class GridLayoutExemple(GridLayout):
#    pass

class AnchorLayoutExemple(AnchorLayout):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0, 100):
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


class BoxLayoutExemple(BoxLayout):
    pass


""" def __init__(self, **kwarg):
        super().__init__(**kwarg)
        b1 = Button(text="A")
        self.add_widget(b1)
        b2 = Button(text="B")
        self.add_widget(b2)"""


class LeLabApp(App):
    pass


LeLabApp().run()
