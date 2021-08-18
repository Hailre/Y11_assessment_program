from kivy.app import App
from kivy.uix.textinput import TextInput

# get user input to use in a list
class MainApp(App):
    def build(self):
        value = TextInput(text='Enter Value here')
        return


MainApp().run()