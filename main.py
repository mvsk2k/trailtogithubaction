from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import random

KV = """
MDScreen:
    AnchorLayout:
        anchor_x: 'center' 
        anchor_y: 'top'
        MDTopAppBar:
            title: "Dice Roller"
    Image:
        id: dice_state
        size_hint_y: 0.3
        size_hint_x: 0.3
        pos_hint: {'center_x': 0.5, 'center_y': 0.5 }
        source: "./dice_1.png"       
    MDRaisedButton:
        id: roll_button
        text: 'ROLL'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.play()

"""

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    def play(self):

        diceface = random.choice(["dice_1.png", "dice_2.png", "dice_3.png", "dice_4.png",
                                             "dice_5.png", "dice_6.png"])
        filename = "./" + diceface
        self.kvs.ids.dice_state.source = filename

ma = MainApp()
ma.run()



