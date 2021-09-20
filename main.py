from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json, glob
from hoverable import HoverBehavior
from kivy.animation import Animation
from datetime import datetime
from pathlib import Path
import random
from kivy.uix.image import Image
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
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
            self.ids.translated.text = str(data[self.ids.word.text])
        elif get_close_matches(self.ids.word.text, data.keys(), cutoff=0.8) != []:
            self.ids.translated.text = ("Word doesn't exist. Did you mean %s Enter Y if yes, or N if no? " % (get_close_matches(self.ids.word.text, data.keys())[0]))
        else:
            self.ids.translated.text = "The word doesn't exist. Please double check it."

class ImageButton(ButtonBehavior, HoverBehavior,Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()