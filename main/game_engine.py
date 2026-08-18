import random
from config import EASY, MEDIUM, HARD, CHANCES, YES, NO
import sys


class NumberGuess():


    def __init__(self):
        
        self.random_number = random.randint(1, 100)
        self.chances = 0
        

    def start (self):
        """Message printed on start of the round"""

        return ("Welcome to the Number Guessing Game!\nI'm thinking of the number between 1 and 100\n\nSelect your difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

    def difficulty (self):
        """Takes user input and defines number of chances to win the game"""

        while True:
            value = input("Choose your difficulty:")
            try:
                value = int(value)
            except ValueError:
                print ("Enter valid number!")
                continue
            if value == EASY:
                self.chances = CHANCES[0]
                return(f"You've selected Easy level. Now you have {CHANCES[0]} chances")
                
            if value == MEDIUM:
                self.chances = CHANCES[1]
                return (f"You've selected Medium level. Now you have {CHANCES[1]} chances")
                
            if value == HARD:
                self.chances = CHANCES[-1]
                return (f"Wow! You've choosen Hard level. Now you have {CHANCES[-1]} chances")
                
            else:
                print("Please enter valid number")

    def is_won (self):
        """Defines if the user won"""

        while self.chances > 0:
            answer = input("Enter your guess:")

            try:
                answer = int(answer)
            except ValueError:
                self.chances -= 1
                print("Enter valid value")
                continue

            if answer == self.random_number:
                return "Congratulations! You won!"
            if answer != self.random_number and answer < self.random_number: 
                self.chances -= 1
                print (f"Incorrect guess. The number is greater than {answer}. You have {self.chances} chances")
            if answer != self.random_number and answer > self.random_number:
                self.chances -= 1
                print (f"Incorrect guess. The number is less than {answer}. You have {self.chances} chances")
        else: return f"You've lost! The number was {self.random_number}"

    def try_again(self):
         while True:
            try:
                try_again = input("Would you like to try again? y/n:")
        
                if try_again in YES:
                    break
        
                if try_again in NO:
                    sys.exit(0)
            except ValueError: 
                print("Enter valid value")
            except KeyboardInterrupt: 
                print("Interrupted!")
                sys.exit(130)



        

        


def main():

    while True:
        try:
            round = NumberGuess()
            
            
            print(round.start())
            print(round.difficulty())
            print(round.is_won())
            print(round.try_again())
            
            
        except ValueError: print("Enter valid values")
        except KeyboardInterrupt: 
            print("Interrupted")
            sys.exit(130)

       




if __name__ == "__main__":
    main()




