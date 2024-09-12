# importing module
import random

# taking input and returning a string(the math question)
def get_question(operation, Num1, Num2):
    if operation == 1:
        return f"How much is {Num1} + {Num2}?"
    elif operation == 2:
        return f"How much is {Num1} - {Num2}?"
    elif operation == 3:
        return f"How much is {Num1} * {Num2}?"
    elif operation == 4:
        return f"How much is {Num1} / {Num2:.1f}?"
    else:
        return f"How much is {Num1} {get_random_operator()} {Num2}?"

# function to return random math operator
def get_random_operator():
    return random.choice(['+', '-', '*', '/'])

# generate question based on difficulty and operator selected
def generate_question(difficulty, operation):
    # level 1 is single digit, level 2 has higher numbers
    if difficulty == 1:
        Num1 = random.randint(0, 9)
        Num2 = random.randint(0, 9)
    else:
        Num1 = random.randint(10, 99)
        Num2 = random.randint(10, 99)
        
# generating a random operator from the list
    if operation == 5:
        operation = random.randint(1, 4)

# using '+' operator
    if operation == 1:
        correct_answer = Num1 + Num2
    # using '-' operator
    elif operation == 2:
        correct_answer = Num1 - Num2
    # using '*' operator
    elif operation == 3:
        correct_answer = Num1 * Num2
    #using '/' operator
    elif operation == 4:
        correct_answer = Num1 / Num2
   # using random operator of the four
    else:
        op = get_random_operator()
        if op == '+':
            correct_answer = Num1 + Num2
        elif op == '-':
            correct_answer = Num1 - Num2
        elif op == '*':
            correct_answer = Num1 * Num2
        else:
            correct_answer = Num1 / Num2

    question = get_question(operation, Num1, Num2)
    return question, correct_answer

# takes users answer and returns boolean value stating if answer is correct or not
def check_answer(user_answer, correct_answer):
    # to stop program and exit
    if user_answer == -1:
        print("Exiting program...")
        return False
    # answer is correct
    elif user_answer == correct_answer:
        print("Well done. Keep going.")
        return True
    # answer is wrong and must try again
    else:
        print("Wrong. Try again.")
        return False
    
# main function
def main():
    # print statement to select level
    print("Enter difficulty level (1 or 2):")
    difficulty = int(input())

    # print statement to select operator
    while True:
        print("1 = addition\n2 = subtraction\n3 = multiplication\n4 = division\n5 = mixed operations")
        print("Enter the operation (1 to 5):")
        operation = int(input())

        # print math question
        question, correct_answer = generate_question(difficulty, operation)
        print(question)

        while True:
            user_answer = int(input("Enter your answer (-1 to exit): "))

            # Check if the user wants to exit
            if user_answer == -1:
                print("Exiting program...")
                return  # Exit the entire program
            
            if check_answer(user_answer, correct_answer):
                break

        # Check if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'n':
            print("Exiting program...")
            break

# code will only run when script is executed
if __name__ == '__main__':
    main()