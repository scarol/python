import random

# give a range
# system generates a random num between a given range
# keep looping until terminate with correct ans
    # ask for user input to guess the num bw the range
    # if user input is not a num
    #   print invalid num msg
    # else if user input is > sys gen num
    #   print too high msg
    # else if user input is < sys gen num
    #   print too low msg
    # else if user input == sys gen num
    #   print success and exit

num1 = 100
num2 = 250
sysNum = random.randint(num1, num2)
while True:
    try:
        userGuess = int(input(f'Guess the number between {num1} and {num2}: '))
        if userGuess < num1 or userGuess > num2:
            print('Number out of given range ! Try again..')
        elif userGuess <  sysNum:
            print('Too low! Try again..')
        elif userGuess >  sysNum:
            print('Too high! Try again..')
        elif userGuess ==  sysNum:
            print('Well Done !')
            break
    except ValueError:
        print('Enter a valid number!')
