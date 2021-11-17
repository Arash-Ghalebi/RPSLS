from player import Player
import getpass


class Human(Player):
    def choose_gesture_secret(self):
        while True:
            result = int(getpass.getpass(f"{self.name} - Please select a gesture: ")) - 1
            # result = input(f" {self.name} Please select a gesture: ")
            if result < 0 or result > 4:
                print("Invalid number. Please input again.")
                continue
            return self.gestures[result]