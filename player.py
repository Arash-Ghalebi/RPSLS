from gesture import Gesture
class Player:

#inits player class with included list and gets inherented to child classes Human and Ai 
#providing name input
    def __init__(self, name = None):
        self.name = name
        self.gestures  = Gesture.gesture_list()
#method for gesture selection gets inherented to child classes but gets changed for specific use of class
    def choose_gesture(self):
        while True:
            result = input(f"{self.name} - Please select a gesture: ")
            if result.isdigit():
                result = int(result) - 1
            else:
                print("Invalid input. Please input again")
                continue
            if result < 0 or result > 4:
                print("Invalid number. Please input again.")
                continue
            else:
                return self.gestures[result]
        