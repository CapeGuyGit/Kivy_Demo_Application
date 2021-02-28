from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.lang.builder import Builder

class LoginPage(Screen):
    pass
class UserPage(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('login.kv')
class LoginApp(App):
    def builder(self):
        return kv_file

LoginApp().run()