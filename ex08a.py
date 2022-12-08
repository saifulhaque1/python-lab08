from graphics import *

def main():
    win = GraphWin()

    rect = Rectangle(Point(0, 0), Point(200, 200))
    rect.setFill("red")
    rect.setOutline("white")
    rect.setWidth(5)
    rect.draw(win)
    rect = Rectangle(Point(25, 25), Point(175, 175))
    rect.setFill("white")
    rect.setOutline("white")
    rect.draw(win)
    rect = Rectangle(Point(50, 50), Point(150, 150))
    rect.setFill("red")
    rect.setOutline("red")
    rect.draw(win)
    input("Press <Enter> to quit")
    win.close()

main()