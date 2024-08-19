#This program is created to implement dice roll game
from random import randint
import time

results = []
userInput = 0

def startUp():
    print("\n\t\t\t********************** Welcome to ROLL FOR WIN. *****************************")
    username = input('\nEnter your player name: ' ) #get user name
    return username

def rollTheDice():
    tempRandomNum = randint(1, 6) 
    return tempRandomNum

def getUsersNumber(roundNum):
    print("\n\t\t\tRound "+str(roundNum))
    print("------------------------------------------------------")
    tempUserInputNumber = input("\nEnter your number: ")

    try: #handle the tempUserInputNumber convertion to integer exception
        inputNum = int(tempUserInputNumber) 
        if( inputNum < 7 ) & ( inputNum > 0 ):
            global userInput #update the global variable
            userInput = inputNum
        else:
            print("\nInvalid input. Please enter a number between 1 to 6.")
            getUsersNumber(roundNum = roundNum) #recall the method to get a valid input
    except :
        print("\nInvalid input. Please enter a number between 1 to 6.")
        getUsersNumber(roundNum = roundNum) #recall the method to get a valid input

def gameEnd(rounds, username):
    print("\n\n**********  Your results  ************\n")
    
    for i,res in enumerate(results) : #enumerate use for get the contain's count of a list
        print("\t\tRound "+ str(i+1) +" : "+res)

    print("\n\nThanks for playing "+username +". Have a nice day.")
       
def main():
    username = startUp() #get user name

    start = input("\nStart the game ? 'Y/N'") 

    if (str(start) == "Y") | (str(start) == "y") :

        roundNumber = 1
        play = True

        while play == True : 
            global userInput
            getUsersNumber(roundNum = roundNumber) #get user input number

            print("\nDice is rolling...")
            time.sleep(2) #Freeze for 3 seconds
            diceNum = rollTheDice() #generate a random number and store in diceNum
            print ("\nYou got : "+str(diceNum))

            if(int(userInput) == int(diceNum)):
                print("\nCongratulations !!! You won...")
                results.append("WON") #add results to the results list
            else:
                print("\nSorry you lost !")
                results.append("LOST") #add results to the results list
            
            tryAgain = input("\nTry another around ? 'Y/N'") #check whether the user is want to play again

            if (str(tryAgain) == "Y") | (str(tryAgain) == "y"):
                play = True #start the next round
                roundNumber += 1 #increment the number of rounds by 1
            else:
                gameEnd(rounds = roundNumber, username = username) #call the game end method
                play = False
        
        return #terminate the function
    else:
        print("\nThanks for playing "+username+". Have a nice day!")
        return 


main() #call the main method