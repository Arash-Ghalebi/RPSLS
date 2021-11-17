from player import Player
import random

class Ai(Player):
#Overided the base choose gesture method to use a random value
    def choose_gesture(self):
        gesture = random.randint(0,4)
        return self.gestures[gesture]