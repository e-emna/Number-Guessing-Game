from random import randint

 
def game():
    #Opening to game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. \n")
    
    #Picking the number
    number = randint(1,100)
    
    #Selecting difficulty level to determine chances and level
    print("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances) \n")
    difficulty = int(input("Enter your choice: "))
    match difficulty:
        case 1:
            chances = 10
            level = "Easy"
        case 2:
            chances = 5
            level = "Medium"
        case 3:
            chances = 3
            level = "Hard"
        case _:
            print("Please select the difficulty level: \n 1. Easy (10 chances) \n 2. Medium (5 chances) \n 3. Hard (3 chances) \n")
            difficulty = int(input("Enter your choice: "))
            
    print("Great! You have selected the "+level+" difficulty level. \nLet's start the game!") 
    
    #Guessing
    guess = int(input("Enter your guess: "))
    attempt = 1
    endGame = False
    while not (endGame or attempt>=chances):
        if guess!=number:
            if guess > number:
               a = "less"
            elif guess < number:
               a = "greater"
               
            print("Incorrect! The number is ",a," than ",guess)
            guess = int(input("Enter your guess: "))
            attempt = attempt + 1
        elif guess == number:
            print("Congratulations! You guessed the correct number in ",attempt," attempts.")
            endGame = True
            break
    if attempt>=chances:
        print("You reached your attempts limit!")
        print("The number is: ",number)
    
play = True
while play:
    game()
    #Play again
    answer = str(input("Continue to play? Yes / No "))
    match answer.upper():
        case "YES":
            play = True
        case "NO":
            play = False
        case _:
            print('Invalid answer')
            answer = str(input("Continue to play? Yes / No "))

