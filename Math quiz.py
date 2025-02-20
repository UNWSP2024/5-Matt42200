import random


def ask_question():
    """Generates two random numbers, asks the user to add them, and checks the answer."""
    num1 = random.randint(100, 999)  # Random number between 100 and 999
    num2 = random.randint(100, 999)  # Random number between 100 and 999
    
    print(f"\n {num1}\n+{num2}\n------")
    
    user_answer = int(input("What is the sum? "))
    
    correct_answer = num1 + num2
    
    if user_answer == correct_answer:
        print("Congratulations! You got the answer right.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")


ask_question()