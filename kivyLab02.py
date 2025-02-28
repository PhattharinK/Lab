from kivy.app import App
from kivy.core.text import layout_text
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
#
# class TutorialApp(App):
#     def build(self):
#         b = BoxLayout()
#         t = TextInput(font_size=150)
#         f = FloatLayout()
#         s = Scatter()
#         l = Label(text="Hello!",
#         font_size=150)
#         f.add_widget(s)
#         s.add_widget(l)
#         b.add_widget(f)
#         b.add_widget(t)
#         return b

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(text='Hello',
        font_size=300)
        l = Label(font_size=300)
        b.add_widget(t)
        b.add_widget(l)
        t.bind(text=l.setter('text'))
        return b
if __name__ == "__main__":
    TutorialApp().run()