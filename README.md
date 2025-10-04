# QUIZ-GAME
A Python-based console Quiz Application that allows users to answer multiple-choice questions, track their scores, and see their final result. Simple, interactive, and beginner-friendly.
# Quiz App 🧠

A simple Python console-based Quiz Application that tests the user's knowledge through multiple-choice questions.  
It keeps track of correct answers and displays the final score at the end of the game.

## 🎯 Features
- Interactive console interface  
- Multiple-choice questions  
- Instant feedback after each question  
- Final score summary  
- Easy to add or modify questions  

## 🧰 Technologies Used
- Python 3

## 🧠 Example Code (main.py)
```python
def run_quiz(questions):
    score = 0
    for question, options, answer in questions:
        print("\n" + question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter your answer (1-4): ")
        
        if choice.isdigit() and options[int(choice)-1].lower() == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {answer}")
    print(f"\nYour final score is {score}/{len(questions)}")

questions = [
    ("What is the capital of France?", ["London", "Berlin", "Paris", "Rome"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Earth", "Jupiter"], "Mars"),
    ("Who wrote 'Romeo and Juliet'?", ["Chinua Achebe", "Shakespeare", "T.S. Eliot", "Charles Dickens"], "Shakespeare"),
]

run_quiz(questions)
