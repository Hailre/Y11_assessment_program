from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty


# Define Different Screens
class WindowManager(ScreenManager):
    pass


class FirstWindow(Screen):
    pass

# Create a Label to display the text.
# Open the file, read the file into a variable.
# Set the text attribute of the Label to the variable.
class LoadPrevious(Screen):
    pass


class SecondWindow(Screen):
    pass


# Designate .kv design file
kv = Builder.load_file('flashcard_application.kv')


class FlashcardApplication(App):
    def get_text_inputs(self):
        my_list = [self.root.ids.first_input_id.text, self.root.ids.second_input_id.text]
        print(my_list)
    pass

    def build(self):
        return kv


if __name__ == '__main__':
    FlashcardApplication().run()
