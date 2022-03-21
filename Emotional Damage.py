#Rock, Paper, Scissors
#3/21/2021
#Jesse Wittenborn



def main():

    name = input("My name is Emotional Damage, what's yours?")
    poorBaby = input(" Enter Your Move " + name  + "(select r for rock, s for scissors, or p for paper)")
    if poorBaby == "r":
        print("I chose paper, you lose " + name  + "! Don't be ashamed of who you are, that's your parents job.")
        print("This was fun, come play again soon " + name + "! or else...")
    if poorBaby == "s":
        print("I chose rock, you lose! My dead flip phone is smarter than you! XD ")
        print("This was fun, come play again soon " + name + "! or else...")
    if poorBaby == "p":
        print("I chose scissors, you lose! Your're adoption parents are on their way!")
        print("This was fun, come play again soon " + name + "! or else...")
       


main()
