# introduction and rules
import random


print("Welcome to Maths quiz ➕➖✖️➗")
print()


def instruction():
    """Displays the instructions and how to play"""
    print('''

**** Instructions ****

To begin, chose how many rounds you would like to play or press enter for infinite mode 

Your goal is to try to get as many answers correct as possible 

Good Luck!
    ''')


# checks users enter yes (y) or no (n)
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

instructions_ans = yes_no("Do you want to read instructions? ")
if instructions_ans == "yes":
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

            # checks that the number is more than 1
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
rounds_lost = 0
rounds_tied = 0

end_game = "no"
feedback = ""

game_history = []
all_scores = [0]


# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter for an infinite mode: ")

if num_rounds == "":
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

    # addition question
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print("What is ", num1, "+", num2, "=")
    user_answer = int(input(""))
    answer = num1 + num2
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect!")
        rounds_lost +=1

    # if user has entered exit code, end game!!
    if user_answer == "xxx":
        break

    rounds_played += 1

    # Add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"
    game_history.append(history_feedback)

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Display the game history on request
see_history = yes_no("Do you want to see your game history? ")
if see_history == "yes":
    for item in game_history:
        print()

# check users have played at least one round

    # Game History area

    # Calculate statistics
    rounds_won = rounds_played  - rounds_lost
    rounds_lost = rounds_played - rounds_won

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Correct: {rounds_won: } \t"
          f" 👎Incorrect: {rounds_lost: } \t")

else:
    print("You chickened out🐔🐔🐔")

