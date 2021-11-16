class Player:


    def __init__(self, name = None):
        self.name = name
        self.gestures  = ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock']

    def choose_gesture(self):
        while True:
            result = int(input(f" {self.name} Please select a gesture: ")) - 1
            # result = input(f" {self.name} Please select a gesture: ")
            if result < 0 or result > 4:
                print("Invalid number. Please input again.")
                continue
            return self.gestures[result]
        