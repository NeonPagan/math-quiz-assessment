# introduction and rules
import random

print("Welcome to Maths quiz ➕➖✖️➗")
print()


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, questions
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    """Displays the instructions and how to play"""
    print(''''

**** Instructions ****

To begin, choose whether you would like addition, subtraction, multiplication or division

Then choose how many rounds you'd like to play <enter>
for infinite mode. 

Your goal is to try to get the answer correct

Good Luck!
    ''')


want_instructions = yes_no("Do you want to read instructions? ")

# check users enter yes (Y) or no (n)
if want_instructions == "yes" or "y":
    instruction()

# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than equal to 13
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main Routine starts here

# addition
num1 = random.randint(1,10)
num2 = random.randint(1,10)

# Initialise game variables
mode = "regular"
rounds_played = 0


print("Welcome to Maths quiz ➕➖✖️➗")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter for an infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode)♾️♾️♾️"
    else:
        rounds_heading = f"\n➕➖✖️➗ Round {rounds_played + 1} of {num_rounds} ➕➖✖️➗"

    print(rounds_heading)
    print()

    # get user answer
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print("What is ", num1, "+", num2, "=")
    user_answer = int(input(""))
    answer = num1 + num2
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect!")



    # If user answer is the exit code, break the loop
    if user_answer == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


# addition
num1 = random.randint(1,10)
num2 = random.randint(1,10)
print("What is ",num1, "+" ,num2,"=")
user_answer = int(input(""))
answer = num1 + num2
if user_answer == answer:
    print("Correct!")
else:
    print("Incorrect!")

# subtraction
num1 = random.randint(1,30)
num2 = random.randint(1,30)
print("What is ", num1, "-" ,num2,"=")
user_answer = int(input(""))
answer = num1 - num2
if user_answer == answer:
    print("Correct!")
else:
    print("Incorrect!")


# multiplication
num1 = random.randint(1,30)
num2 = random.randint(1,30)
print("What is ", num1, "*" ,num2,"=")
user_answer = int(input(""))
answer = num1 * num2 / num1
if user_answer == answer:
    print("Correct!")
else:
    print("Incorrect!")

# num1 * num2 / num1
# main routine starts here



