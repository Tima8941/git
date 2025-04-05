from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Rate(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation="vertical"
        btnBox=BoxLayout()
        lbl_title=Label(text="Як тобі цей кіт?????? (або не кіт)", font_size=32, halign="center", size_hint=[1,0.1])

        self.buttons=[]

        self.img=Image(source="photo/cat2.jpg", size_hint=[1,0.6])
        self.add_widget(lbl_title)
        self.add_widget(self.img)

        for i in range(5):
            btn=Button(text=str(i+1), background_normal="images/star0.png",
                        background_down="images/star0.png", color=[0,0,0,0], 
                        on_press=self.rating)
            self.buttons.append(btn)
            btnBox.add_widget(btn)
        self.add_widget(btnBox)
    def rating(self,btn):
        index=int(btn.text)-1
        for i in range(len(self.buttons)):
            if i<=index:
                self.buttons[i].background_normal="images/star1.png"
                self.buttons[i].background_down="images/star1.png"
            else:
                self.buttons[i].background_normal="images/star0.png"
                self.buttons[i].background_down="images/star0.png"

class LikeApp(App):
    def build(self):
        self.mainBox=BoxLayout(orientation="vertical")
        rate=Rate()
        self.mainBox.add_widget(rate)
        return self.mainBox


LikeApp().run()

