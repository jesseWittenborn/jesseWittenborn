#importing random allows us to have a truly random and unpredictable game
import random
#List of choises the computer can choose from
plays = ["r", "p", "s"]
#loop that allows us to repeat the game 3 times

for play in range (3):
#Input statement that takes the users choice   
    choice=input("Enter r for Rock, p for Paper, or s for scisors. or q to quit")
#Condition block that tells the user he has won or lost depending on the winner of the round   
    if choice not in plays:
        #error message in case the user has an invalid entry
        print("Invalid try again")
    #Escape selection if the user would like to stop
    if choice == 'q':
        break

    
    loser = ("LOSER!!!!!!")   
   
    cpu_pick = random.choice(plays)
    if choice == cpu_pick:
        
        print(f"We both selected{choice}. Lets try this again.")
    elif choice == 'r':
        if cpu_pick == 'Paper':
            print(f"{loser}You lose paper covers rock!")
        else:
            print("Rock crushes scisors you win...this time.")
    elif choice == 'p':
        if cpu_pick == "Rock":
            print("You win.. this time paper covers rock")
        else:
            print(f"{loser}You lose!!! Scisors cuts paper")
    elif choice == 's':
        if cpu_pick == "Paper":
            print("You win..this time scisors cuts paper")
        else:
            print(f"{loser}You loser rock crushes scisors!!!")
    if loser >3:
        print("Wow you are terrible!")
  
    
print("Game over")
    
