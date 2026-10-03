from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello Bos, APK pyapp jadi!")

MyApp().run()
