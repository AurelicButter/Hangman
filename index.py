from random import choice

word = choice(open("dictionary.txt", "r").readlines())
answer = list(word[0:len(word) - 1])

def gameStatus(user, wrong):
    if "_" not in user:
        return False
    if wrong == 5:
        return False
    else:
        return True

def determineMatch(wrong):
    print("The word was: " + "".join(answer))

    if wrong == 5:
        print("GAME OVER: Better luck next time!")
    else :
        print("Congradulations! You've won!")

def game():
    guessed = []
    user = ""
    wrong = 0

    for x in range(0, len(answer)):
        user = user + "_"

    while gameStatus(user, wrong) == True:
        print("Current: " + user)
        print("Guessed letters: " + str(guessed))
        guess = input("Letter guess: ")

        if len(guess) != 1 or guess.isalpha() == False:
            print("Try again...")
    
        elif guess in guessed:
            print("Whoops, you've already guessed that.")

        elif guess not in answer:
            guessed.append(guess)
            wrong = wrong + 1
            print("Nope! That's not correct")
    
        else:
            guessed.append(guess)
            for x in range(0, len(answer)):
                if answer[x] == guess:
                    user = user[:x] + guess + user[x + 1:]

            print("Good guess!")

        print()

    return wrong


gameOn = True

while gameOn == True:
    determineMatch(game())

    check = ""
    while check is not "Y" and check is not "N":
        check = input("\n\nWould you like to play again? (Y/N)\n")

        if check is "Y":
            print("\n\n")
            continue
        elif check is "N":
            gameOn = False