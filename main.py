from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json, glob
from hoverable import HoverBehavior
from kivy.animation import Animation
from pathlib import Path
import random
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from kivymd.uix.screen import Screen
import difflib
Window.clearcolor = (1, 1, 1, 1)

        

Builder.load_file('design.kv')

class HomeScreen(Screen):
    def dicscreen(self):
        self.manager.current = "dicscreen" 

         
class DicScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "homescreen"

    def translate(self):
        data = json.load(open('data.json'))   
        self.ids.word.text = self.ids.word.text.lower() 
        if self.ids.word.text in data:
            self.ids.translated.text = '\n'.join(['{}: {}'.format(i, val) for i, val in (enumerate(data[self.ids.word.text], start=1))])
        elif self.ids.word.text == "":
            self.ids.translated.text = "Please enter a word."
        elif difflib.get_close_matches(self.ids.word.text, data.keys(), cutoff=0.8) != []:
            self.ids.translated.text = ("Word doesn't exist. Did you mean %s? " % (difflib.get_close_matches(self.ids.word.text, data.keys())[0]))
        else:
            self.ids.translated.text = "The word doesn't exist. Please double check it."


class ImageButton(ButtonBehavior, HoverBehavior,Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        self.icon = "LOGO(2).png"
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
