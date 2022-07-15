from itertools import count


print('Welcome to my computer quiz! ')

playing = input('Do you want to play? ')

if playing != 'yes':
    print('Game exited')
    quit()

print('okay lets play')
    
count = 0
answer = input('What is the full form of CPU?  ')
if answer == 'central processing unit':
    print('your answer is correct')
    count +=1
else:
    print('wrong answer')

answer = input('What does GPU stands for?  ')
if answer == 'graphics processing unit':
    print('your answer is correct')
    count +=1
else:
    print('wrong answer')

answer = input('What is the full form of CPU?  ')
if answer == 'central processing unit':
    count +=1
    print('your answer is correct')
else:
    print('wrong answer')

answer = input('What does RAM stands for?  ')
if answer == 'random access memory':
    print('your answer is correct')
    count +=1
else:
    print('wrong answer')

answer = input('What does ROM stand for?  ')
if answer == 'read only memory':
    print('your answer is correct')
    count +=1
else:
    print('wrong answer')

print('you got ',count,'correct answer')
