# introduction and rules
import random


print("Welcome to Maths quiz ➕➖✖️➗")
print()


def instruction():
    """Displays the instructions and how to play"""
    print('''

**** Instructions ****

To begin, chose how many rounds you would like to play or press enter for Normal mode 

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
    """Makes sure that the number of rounds is more than zero"""
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for Normal mode
        if to_check == "":
            return "Normal"

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



# Ask user for number of rounds / Normal mode
num_rounds = int_check("How many rounds would you like? Push <enter for an Normal mode: ")

if num_rounds == "Normal":
    mode = "Normal"
    num_rounds = 10

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "Normal":
        rounds_heading = f"\n➕➖✖️➗ Round {rounds_played + 1} of {num_rounds} ➕➖✖️➗"
    else:
        rounds_heading = f"\n➕➖✖️➗ Round {rounds_played + 1} of {num_rounds} ➕➖✖️➗"

    print(rounds_heading)
    print()

    # addition question
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    addition_question = int_check(f"What is {num1} + {num2} =")
    answer = num1 + num2
    if addition_question == answer:
        print("Correct!")
        feedback = "✔️✔️You got that right ✔️✔️"
    else:
        print("Incorrect!")
        feedback = "❌❌You got that wrong ❌❌"
        rounds_lost +=1

# before calculating history and statistics

    # Game History area
    round_feedback = f"{addition_question} vs {answer}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    # Set up round feedback and output it user
    print (round_feedback)
    game_history.append(history_item)


    rounds_played += 1

# calculate stats if user has played at least one round
if len(game_history) > 0:

    # Display the game history on request
    see_history = yes_no("Do you want to see your statistics? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

        print()
        print("Thanks for playing.")

        # Calculate statistics
        rounds_won = rounds_played - rounds_lost
        rounds_lost = rounds_played - rounds_won

        # Output Game Statistics
        print("📊📊📊 Game Statistics 📊📊📊")
        print(f"👍 Correct: {rounds_won: } \t"
              f" 👎Incorrect: {rounds_lost: } \t")





