inport random


numberToGuess = random.randint(1,100)
numberToGuess = 0
guessed = False

while not guessed:
    #läs in från användarn
    n = input()

    #ge feedback
    if n > numberToGuess:
        print("Your guess was to high, try again..")
    elif n < numberToGuess:
        print("your guess was to low, try again..")
    else: # n== numberToGuess
        print("Rätt!, it took you {} tries".format(numberToGuess))
        guessed = Tru