# checks users enter yes (y) or no (n)

def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# def math_equation():

# Displays instructions to user
def instruction():
    print('''

**** Instructions ****

here
    ''')

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

            # checks that the number is more than or equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# def string_checker(question, valid_ans=('yes', 'no')):
#
#     error = f"Please enter a valid option from the following list: {valid_ans}"
#
#     while True:
#
#         # get user response amd make sure it's lowercase
#         user_response = input(question).lower()
#
#         for item in valid_ans:
#             # check is the user response is a word in the list
#             if item == user_response:
#                 return item
#
#             # check if the user response is the same as
#             # the first letter of an item in the list
#             elif user_response == item[0]:
#                 return item
#
#         # print error if user does not enter something that is valid
#         print(error)
#         print()

# main routine goes here


# initialise game variables
mode = "regular"

ques_asked = 0
ques_right = 0
ques_wrong = 0

# # creates lists to hold user and computer scores and game history
# user_scores = []
# comp_scores = []
# game_history = []
# (made spam bug?)

print()
print(" ➕➖ Basic Facts Math Quiz ✖️➗ ")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print()
num_ques = int_check("How many questions would you like to be asked? Press <enter> for infinite mode: ")
print()

if num_ques == "infinite":
    mode = "infinite"
    num_ques = 5

# game loop starts here
while ques_asked < num_ques:

    # rounds headings (based on mode)
    if mode == "infinite":
        ques_heading = f"\n♾♾♾ Round {ques_asked + 1} (Infinite Mode) ♾♾♾"
    else:
        ques_heading = f"\n🎯🎯🎯 Round {ques_asked + 1} of {num_ques} 🎯🎯🎯"

    print(ques_heading)

    # get user choice
    user_choice = int_check("choose: ")

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

# # loop game until we have a winner
# while ques_asked < num_ques:
#     # Add one to the number of ques (for our heading)
#     num_ques += 1
#     print(f"Round {num_ques}")
