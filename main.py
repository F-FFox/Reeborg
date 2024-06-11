#print("hello")
#print is a function. Whatever is in the brackets will be affected by the function. There are many built in functions in python already.

#to create your own function:
# start with "def" - because we are *defining* your function

# def + name + () + : then new line and everything indented is part of the function.

def my_function():
  print("Hello")
  print("Bye")

# then to trigger or to "call" the function: name it and add any required parameters in the brakets. in the example above the brakets are empty, so no further input is needed. 

my_function()

"""

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Reeborgs Hurdle 2


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() == False:
#while not at_goal():
    jump()

"""


"""

Hurdle 3



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        jump()


"""


"""

Maze


def turn_right():
    turn_left()
    turn_left()
    turn_left()

#def jump():
#    turn_left()
#    while not right_is_clear():
#        move()
#    turn_right()
#    move()
#    turn_right()
#    while not wall_in_front():
#        move()
#    turn_left()

while not at_goal():
    if wall_in_front() == False:
        while wall_in_front() == False:
            move()
    else:
        while wall_on_right() == True:
            turn_left()
        turn_right()

"""