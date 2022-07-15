import random
print('welcome to the game')
print('Th Game Of Rock, Paper, Scissor')

values = ['rock','paper','scissor']
player_score = 0
computer_score = 0

while True:
    your_choice = input('Enter your choice [rock,paper,scissor] or press Q to quit----').lower()
    comp = random.randint(0,2)
    computer_choice = values[comp]
    if your_choice == 'q': 
        break

    if your_choice not in values:
        continue

    print('computer choose',computer_choice)
    if computer_choice == your_choice:
        print('Its a draw')
    elif your_choice == 'rock' and computer_choice == 'scissor':
        print('you win')
        player_score +=1
    elif your_choice == 'paper' and computer_choice == 'rock':
        print('you win')
        player_score +=1
    elif your_choice == 'scossor' and computer_choice == 'paper':
        print('you win')
        player_score +=1
    else:
        print('you lost')
        computer_score +=1

print('your score is',player_score)
print('computer\'s score is ',computer_score)
print('Goodbye')
