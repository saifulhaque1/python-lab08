from graphics import *

def main():

    win = GraphWin()

    for row in range(0,8):
       for col in range(0,8):
            if(row+col)%2==0:
                rect = Rectangle(Point(row*25,col*25),Point((row+1)*25,(col+1)*25))
                rect.setFill("white")
                rect.setOutline("white")
                rect.draw(win)
            else:
                rect = Rectangle(Point(row*25,col*25),Point((row+1)*25,(col+1)*25))
                rect.setFill("black")
                rect.setOutline("black")
                rect.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()