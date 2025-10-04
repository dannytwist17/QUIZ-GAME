import json
import random


def load_questions(filename='questions.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('❌ Questions file not found!')
        return[]


def quiz_game():
    questions = load_questions()
    if not questions:
        return
    
    random.shuffle(questions)
    print('🎉 Welcome to the Quiz Game! 🎉\n')
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f'Q{i}: {q["question"]}')
        
        options = q['options'][:]
        random.shuffle(options)
        
        for idx, option in enumerate(options, start=1):
            print(f'{chr(64+idx)}) {option}')
            
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer in ['A', 'B', 'C', 'D']:
            selected = options[ord(answer) - 65]
            if selected == q["answer"]:
                print('✅ Correct!\n')
                score += 1
            else:
                print(f'❌ Wrong! Correct answer: {q["answer"]}\n')
        else:
            print('⚠️ Invalid choice! Skipping...\n')
            
            
    print(f'🏆 You scored {score}/{len(questions)} ({(score/len(questions))*100:.1f}%)')
    if score == len(questions):
        print('🔥 Excellent job!')
    elif score >= len(questions)//2:
        print("👍 Good effort!")
    else:
        print("📚 Keep practicing!")
        
    again = input('\nDo you want to play again? (Yes/No): ').strip().upper()
    if again == 'YES':
        quiz_game()
        
quiz_game()