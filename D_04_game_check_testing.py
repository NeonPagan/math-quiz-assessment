# define game mode checker
def game_mode():
    while True:




# define game checker
def game_check(question):
    while True:
        error = "Please enter one of the game modes."

        to_check = input(question)

        # check for infinite mode
        if to_check == "addition":
            return "nice addition"

        try:
            response = game_mode(to_check)

            # checks that the game is on the list
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)




game_mode = game_check("Do you want to practise addition, subtraction or multiplication? ")

game_mode = ["addition", "subtraction", "mult", "xxx"]



