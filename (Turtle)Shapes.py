#  Jesse Wittenborn
#  3/8/2022
#  My Geometric shapes

import turtle

def main():
    print (" Red and Blue Stars ")
    matt= turtle.Turtle()
    matt.color("red")

    side = 100
    angle = -80

    for count in range(11):
        matt.forward(side)
        matt.left(angle)
    watt= turtle.Turtle()
    watt.color("blue")

    side = 100
    angle = 80
    minty= turtle.Turtle()
    minty.color("green")

    side = 100
    angle = 80

    for count in range(11):
        watt.backward(side)
        watt.right(angle)

    for count in range(11):
        minty.forward(side)
        minty.left(angle)	
    
     
    
main()
