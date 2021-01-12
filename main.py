from random import randint

name = input('What is your name ')
print(name,' welcome to Number Guessing game!!')
a = input('Are you familiar with me?(y/n) ')
if a=='n':
 print('So you have to guess a number from 1-100 and you will be provided with only 10 attempt in each level.',end='')
 print('You will have a score of 100 at the start of each level from which level no.*10 is reduced for each wrong attempts.')
print('Let\'s start the game')
b = 'y'
while b=='y':
 for j in range(1,4):
  marks = 100
  count = 0
  c = 0
  i = 1
  print('LEVEL-',j)
  num = randint(1,100)
  guess = int(input('Guess a number between 1-100 ' ))
  while i<12:  
   if guess<num:
    print('Your guess is a low,try again.')
    count += 1
    i += 1
    marks -= j*10
    guess = int(input('Guess a number between 1-100 ' ))
   if guess>num:
    print('Your guess is high,try again.')
    count += 1
    i += 1
    marks -= j*10
    guess = int(input('Guess a number between 1-100 ' ))
   if guess==num:
    print('Your guess is right.Your did great!!')
    count += 1
    c = 1
    print('Your total score: ',marks)
    print('No. of guesses= ',count)
    break
   if i==10:
    print('You used all chances.')
    break
   if i==9:
    print('You have just one more chance, try harder.')
  if c==0:
   print('Sorry you lost game.Better luck next time.')
   print('The number was ',num)
   marks -= j*10
   print('Your total score: ',marks)
 b = input('Do you like to play again?(y/n) ')