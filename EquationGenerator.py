import tkinter as tk
import random
from tkinter import messagebox

#Function to return random math operator
def get_random_operator():
    return random.choice(['+', '-', '*', '/'])

#Generate question based on difficulty and operator selected
def generate_question(difficulty, operation):
    if difficulty == 1:
        Num1 = random.randint(0, 9)
        Num2 = random.randint(0, 9)
    else:
        Num1 = random.randint(10, 99)
        Num2 = random.randint(10, 99)

    if operation == 5:
        operation = random.randint(1, 4)

    if operation == 1:
        correct_answer = Num1 + Num2
        question = f"{Num1} + {Num2}"
    elif operation == 2:
        correct_answer = Num1 - Num2
        question = f"{Num1} - {Num2}"
    elif operation == 3:
        correct_answer = Num1 * Num2
        question = f"{Num1} * {Num2}"
    elif operation == 4:
        correct_answer = Num1 / Num2
        question = f"{Num1} / {Num2:.1f}"
    else:
        op = get_random_operator()
        if op == '+':
            correct_answer = Num1 + Num2
            question = f"{Num1} + {Num2}"
        elif op == '-':
            correct_answer = Num1 - Num2
            question = f"{Num1} - {Num2}"
        elif op == '*':
            correct_answer = Num1 * Num2
            question = f"{Num1} * {Num2}"
        else:
            correct_answer = Num1 / Num2
            question = f"{Num1} / {Num2:.1f}"

    return correct_answer, question

#Function to check the user's answer
def check_answer(user_answer, correct_answer):
    try:
        if float(user_answer) == correct_answer:
            return True
        else:
            return False
    except ValueError:
        return False

#Function to handle button click to generate a question
def generate():
    difficulty = int(difficulty_var.get())
    operation = int(operation_var.get())
    
    global correct_answer
    correct_answer, question = generate_question(difficulty, operation)
    
    question_label.config(text=question)
    answer_entry.delete(0, 'end')

#Function to handle checking the answer
def submit():
    user_answer = answer_entry.get()
    
    if check_answer(user_answer, correct_answer):
        messagebox.showinfo("Correct!", "Well done! You got it right.")
    else:
        messagebox.showerror("Incorrect", "Wrong answer. Try again.")

#Setting up the GUI window
root = tk.Tk()
root.title("Math Equation Generator")

#Set the window size and allow resizing
root.geometry("500x400")
root.resizable(True, True)

#Difficulty Level Selection
difficulty_label = tk.Label(root, text="Select Difficulty Level:")
difficulty_label.pack(pady=10)

difficulty_var = tk.StringVar(value='1')
difficulty_frame = tk.Frame(root)
difficulty_frame.pack()
difficulty_radiobutton1 = tk.Radiobutton(difficulty_frame, text="Level 1", variable=difficulty_var, value='1')
difficulty_radiobutton2 = tk.Radiobutton(difficulty_frame, text="Level 2", variable=difficulty_var, value='2')
difficulty_radiobutton1.pack(side=tk.LEFT, padx=10)
difficulty_radiobutton2.pack(side=tk.LEFT, padx=10)

#Operation Selection
operation_label = tk.Label(root, text="Select Operation:")
operation_label.pack(pady=10)

operation_var = tk.StringVar(value='1')
operation_frame = tk.Frame(root)
operation_frame.pack()
operation_radiobutton1 = tk.Radiobutton(operation_frame, text="Addition", variable=operation_var, value='1')
operation_radiobutton2 = tk.Radiobutton(operation_frame, text="Subtraction", variable=operation_var, value='2')
operation_radiobutton3 = tk.Radiobutton(operation_frame, text="Multiplication", variable=operation_var, value='3')
operation_radiobutton4 = tk.Radiobutton(operation_frame, text="Division", variable=operation_var, value='4')
operation_radiobutton5 = tk.Radiobutton(operation_frame, text="Mixed", variable=operation_var, value='5')

operation_radiobutton1.pack(side=tk.LEFT, padx=10)
operation_radiobutton2.pack(side=tk.LEFT, padx=10)
operation_radiobutton3.pack(side=tk.LEFT, padx=10)
operation_radiobutton4.pack(side=tk.LEFT, padx=10)
operation_radiobutton5.pack(side=tk.LEFT, padx=10)

#Generate Equation Button
generate_button = tk.Button(root, text="Generate Question", command=generate)
generate_button.pack(pady=10)

#Equation
question_label = tk.Label(root, text="Your question will appear here.", font=("Arial", 14))
question_label.pack(pady=20)

#Enter Answer
answer_label = tk.Label(root, text="Enter Your Answer:")
answer_label.pack(pady=5)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit Answer", command=submit)
submit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
