class Player:

    gestures  = ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock']

    def __init__(self, name, gesture = None, numplayer):
        self.name = name
        self.gesture = gesture
        self.numplayer = numplayer

    def choose_gesture(self):
        return self.gestures[self.gesture]

    
        