from functions import *

while True:
    game()
    if input("Do you want to play again? (pewex/no): ").lower() != "pewex":
        print("Goodbye!")
        break
