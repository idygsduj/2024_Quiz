import math
import random


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    return max_raw


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


# def ques_check(correct, incorrect):
#     if ques == correct:
#         ques_result = "Correct"
#     else ques == incorrect:
#         ques_result = "Incorrect"


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

# num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# type_ques = ["+", "-"]

# num_1 = random.randint(1, 6)
# num_2 = random.randint(1, 6)
# type_ques = ["+", "-", "*"]

# num_1 = random.choice(list_a[:-1])
# num_2 = random.choice(list_b[:-1])
# type_ques = random.choice(list_c[:-1])

# main routine goes here


# initialise game variables
mode = "regular"

ques_asked = 0
ques_right = 0
ques_wrong = 0

# # creates lists to hold user results and game history
# user_scores = []
# comp_scores = []
# game_history = []
# (made spam bug?)

print()
print(" ➕➖✖️ Basic Facts Math Quiz ➕➖✖️ ")
print()

# asks user if they want to read the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# asks user how many questions the quiz will have, allows enter for infinite mode
print()
num_ques = int_check("How many questions would you like to be asked? Press <enter> for infinite mode: ")
print()

if num_ques == "infinite":
    mode = "infinite"
    num_ques = 5


# game loop starts here
# loop game until the number of questions are asked

while ques_asked < num_ques:

    # question headings (based on mode)
    if mode == "infinite":
        ques_heading = f"\n♾♾♾ Question {ques_asked + 1} (Infinite Mode) ♾♾♾"
    else:
        ques_heading = f"\n🎯🎯🎯 Question {ques_asked + 1} of {num_ques} 🎯🎯🎯"

    print()
    print(ques_heading)

    # displays math question
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    type_list = ["+", "-", "*"]
    type_ques = random.choice(type_list)

    # num_1: int = random.randint(1, 12)
    # num_2: int = random.randint(1, 12)
    # type_ques = ["+", "-", "*"]

    # print(random.choice(num_1[:-1]), random.choice(type_ques), random.choice(num_2[:-1]), "=")
    # num_1 = random.randint(1, 6)
    # num_2 = random.randint(1, 6)
    print(num_1, type_ques, num_2, "=")


    # finds if user answer is correct
    if type_ques == '+':
        answer = num_1 + num_2
    elif type_ques == '-':
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2

    # answer_1: list[int] = num1 + num2
    # answer_2: list[int] = num1 - num2
    # # answer_3 : list[int] = num1 * num2

    # get user choice
    user_choice = int_check("Your answer: ")
    print()

    # result = ques_result(ques_right, ques_wrong)
    # actual = calc_guesses(low_num, high_num)


# tells user if answer is correct
    if user_choice == answer:
        ques_right += 1
        print("👍👍 You're correct 👍👍")

    else:
        ques_wrong += 1
        print("👎👎 You're incorrect 👎👎 ")
        print(f"The correct answer was {answer}")


# displays current correct/incorrect statistics
    print(f"Total Correct: {ques_right} \t|\t Total Incorrect: {ques_wrong}")

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

# round_result = f"Round {num_rounds} - User: {user_points} \t Computer {computer_points}"
#     game_history.append(round_result)
#

# # loop game until we have a winner
# while ques_asked < num_ques:
#     # Add one to the number of ques (for our heading)
#     num_ques += 1
#     print(f"Round {num_ques}")n