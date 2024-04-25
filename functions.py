import random

colors = ["green","blue","red","yellow","purple","orange"]
def generate_code():
    return random.sample(colors, 4)

def take_a_guess():
    valid = False
    while not valid:
        guess = input(str("Enter your guess: "))
        guessed_code = guess.split()
        if len(guessed_code) == len(set(guessed_code)) == 4:
            for i in range(4):
                if guessed_code[i] in colors:
                    valid = True
                else:
                    print("Debil, you need to enter valid colors.")
                    valid = False
                    break
        else:
            print("Debil, you need to enter 4 colors.")
    return guessed_code

def compare_codes(code, guessed_code):
    black_pegs = 0
    white_pegs = 0
    for i in range(4):
        if code[i] == guessed_code[i]:
            black_pegs += 1
        elif guessed_code[i] in code:
            white_pegs += 1
    return black_pegs, white_pegs

def print_menu():
    print("Welcome to Mastermind!")
    print("You need to guess the code. The code consists of 4 colors.")
    print("The colors are: green, blue, red, yellow, purple and orange.")
    print("You can use each color only once.")
    print("After each guess you will get feedback in form of black and white pegs.")
    print("Black pegs mean that you have a correct color in a correct place.")
    print("White pegs mean that you have a correct color in a wrong place.")
    print("Good luck!")


def game():
    while True:
        print_menu()
        code = generate_code()
        for i in range(10):
            guessed_code = take_a_guess()
            black_pegs, white_pegs = compare_codes(code, guessed_code)
            print("Black pegs: ", black_pegs)
            print("White pegs: ", white_pegs)
            if black_pegs == 4:
                print("You won!")
                return
        print ("You lost! The code was: ", code)


