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


def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response amd make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check is the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

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

quiz_history = []

print()
print(" ➕➖✖️ Basic Facts Math Quiz ➕➖✖️ ")
print()

# asks user if they want to read the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# asks user how many questions the quiz will have, allows user to enter for infinite mode
print()
num_ques = int_check("How many questions would you like to be asked? Press <enter> for infinite mode: ")
print()

if num_ques == "infinite":
    mode = "infinite"
    num_ques = 5


# quiz loop starts here
# loop game until the number of questions are asked

while ques_asked < num_ques:

    # question headings (based on mode)
    if mode == "infinite":
        ques_heading = f"\n♾♾♾ Question {ques_asked + 1} (Infinite Mode) ♾♾♾"
    else:
        ques_heading = f"\n🎯🎯🎯 Question {ques_asked + 1} of {num_ques} 🎯🎯🎯"

    print()
    print(ques_heading)

    # choose numbers and type of question for the equation
    # make sure numbers and integers are within the correct limits
    type_list = ["+", "-", "*"]
    type_ques = random.choice(type_list)

    if type_ques == "*":
        num_1 = random.randint(1, 12)
        num_2 = random.randint(1, 12)
    elif type_ques == "-":
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, num_1)
    else:
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, 50)

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

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

# tells user if answer is correct
    if user_choice == answer:
        ques_right += 1
        print("👍👍 You're correct 👍👍")

    else:
        ques_wrong += 1
        print("👎👎 You're incorrect 👎👎 ")
        print(f"The correct answer was {answer}")


# displays current correct/incorrect statistics
#     print(f"Total Correct: {ques_right} \t|\t Total Incorrect: {ques_wrong}")

    # set up round feedback and output it user.
    # add it to the game history list (include the round number)

    # set up round feedback and output it user.
    # add it to the game history list (include the round number)
    ques_result = f"Total correct: {ques_right} \t|\t Total incorrect: {ques_wrong}"
    history_item = f"Ques: {ques_asked} - {ques_result}"

    print(ques_result)
    quiz_history.append(history_item)

    ques_asked += 1

    # if users are in infinite mode, increase number of questions
    if mode == "infinite":
        num_ques += 1

# quiz loop ends here

# quiz history / statistics area
print()
if len(quiz_history) > 0:
    # calculate statistics
    ques_right = ques_asked - ques_wrong
    percent_right = ques_right / ques_asked * 100
    percent_wrong = ques_wrong / ques_asked * 100

    # output quiz statistics
    print()
    print("📊📊📊 Quiz Statistics 📊📊📊")
    print(f"👍 Correct: {percent_right:.2f} \t "
          f"👎 Incorrect: {percent_wrong:.2f} \t ")


# display quiz history if user wants to see it
print()
show_history = yes_no("Do you want to see the quiz history?")
if show_history == "yes":
    print("\n🧾🧾🧾 Quiz History 🧾🧾🧾")

    for item in quiz_history:
        print(item)

    print()

print()
print(f"Thank you for taking this quiz!")
