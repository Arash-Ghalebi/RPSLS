from player import Player
import random

class Ai(Player):

    def choose_gesture(self):
        gesture = random.randint(0,4)
        return self.gestures[gesture]