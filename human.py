from player import Player
import getpass

#inherents Player class functions and extends choose gesture method to hide player ones input from others 
class Human(Player):
    def choose_gesture_secret(self):
        while True:
            result = getpass.getpass(f"{self.name} - Please select a gesture: ")
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