import stdio, random

RANGE = 1000000

secret = random.randrange(1, RANGE + 1)
print('Guess a number between 1 and %d' %RANGE)

guess = 0
while guess != secret:
    
    print('what is your guess?', end=' ')
    guess = stdio.readint()
    
    if guess < secret :
        print('Too low')
    elif guess > secret:
        print('Too high')
    else :
        print('you win!')