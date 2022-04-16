import random
randNumber = random.randint(1,100)
# print(randNumber)
guesses = 0
userGuess = None 
    # Important as userGuess is defined inside the loop but it is being used in the entry statement.
    # So it has to be initialized before the while loop as well.

while(userGuess!=randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses+=1
    if(userGuess==randNumber):
        print("You guessed it right.")
    else:
        print("You guessed it wrong.")
        if(randNumber<userGuess):
            print("Enter a smaller number")
        else:
            print("Enter a larger number")
        
print(f"You guessed the number in {guesses} attempts")