class Player:

    gestures  = ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock']

    def __init__(self, name, gesture):
        self.name = name
        self.gesture = gesture

    def choose_gesture(self):
        return self.gestures[self.gesture]
        