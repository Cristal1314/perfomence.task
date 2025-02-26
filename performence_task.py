#Memory Match Game: Build a game where users match pairs of numbers.
from random import * # Imports all the public names( functioins, classes, and varibles)
from turtle import * # brings objects from the module
greetings = input(" Hello, user would you like to play a game?: ")
if greetings == "yes":
    print("great let start playing")
else:
    print("Okie, come next time")
#To set the screen:
screen = Screen() 

#Choose a color for the background
screen.bgcolor("white")
 
 # To create the square for the game 
def Square(x,y):
    up()
    goto(x,y)
    down()
    color('red','blue')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Define a function to check the index number as a keep 
def numbering(x,y):
    return int((x+200) // 50 + ((y+200) // 50) * 8)
# defining the function to help to keep check of the index number
def location(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 -200
# To make a interactive user click
def click(x,y):
    spot = numbering(x,y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] =spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    clear()
    goto(0,0)
    stamp()

    for count in range(64):
        if hide[count]:
            x,y = location(count)
            Square(x,y)
    mark = state['mark']

    if mark is not None and hide[mark]:
        x,y = location(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font= ('Arial', 30, 'normal'))

    update()
    ontimer(draw, 10)
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


# To shuffle the numbers inside the tiles
shuffle(tiles)
tracer(False)
onscreenclick(click)
draw()
done()

print(" THANK YOU FOR PLAYING. COME AGAIN NEXT TIME")