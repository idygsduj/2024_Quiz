import random


# checks users have entered a valid option, yes or no.
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


# Displays instructions to user
def instruction():
    print('''
This quiz will ask you a series of basic math questions covering addition, subtraction, and multiplication. You can
choose the number of questions you will get asked, or you can press <enter> to be asked an infinite number of questions. 
To exit infinite mode use the code <xxx>. Enjoy.
    ''')


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        # checks for exit code
        if to_check == "xxx":
            return "xxx"

        try:
            response = int(to_check)

            # checks that the number is more than or equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here

# initialise game variables
mode = "regular"

ques_asked = 0
ques_right = 0
ques_wrong = 0

quiz_history = []

# print quiz title to the user
print()
print(" ➕➖✖️ Basic Facts Math Quiz ➕➖✖️ ")
print()

# asks user if they want to read the instructions and displays them if user does
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# asks user how many questions the quiz will have, allows user to enter for infinite mode
print()
num_ques = int_check("How many questions would you like to be asked? Press <enter> for infinite mode: ")

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

    # print question heading
    print()
    print(ques_heading)

    # choose numbers and type of question for the equation
    # make sure numbers and integers are within the correct limits
    type_list = ["+", "-", "*"]
    type_ques = random.choice(type_list)

    if type_ques == "*":
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
    elif type_ques == "-":
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, num_1-1)
    else:
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, 50)

    # print question with randomly selected numbers and type of question
    print(num_1, type_ques, num_2, "=")

    # finds if user answer is correct
    if type_ques == '+':
        answer = num_1 + num_2
    elif type_ques == '-':
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2

    # get user choice
    user_choice = int_check("Your answer: ")
    print()

    # breaks loop if user enters exit code
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

    # set up round feedback and output it to the user
    # add it to the game history list (include the round number)
    ques_result = f"Total correct: {ques_right} \t|\t Total incorrect: {ques_wrong}"

    if user_choice == answer:
        history_item = f"Question {ques_asked+1}:  {num_1} {type_ques} {num_2}  Your Answer: {user_choice}  ✅Correct✅"

    if user_choice != answer:
        history_item = f"Question {ques_asked+1}:  {num_1} {type_ques} {num_2}  Your Answer: {user_choice}  ❌Incorrect❌ " \
                       f"Correct Answer: {answer}"

    # print the question result
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
    print(f"👍 Percentage correct: {percent_right:.2f} \t "
          f"👎 Percentage incorrect: {percent_wrong:.2f} \t ")

# display quiz history if user wants to see it
print()
show_history = yes_no("Do you want to see the quiz history?")
if show_history == "yes":
    print("\n🧾🧾🧾 Quiz History 🧾🧾🧾")

    for item in quiz_history:
        print(item)

    print()
    print(ques_result)

print()
print(f"Thank you for taking this quiz!")
