from tkinter import *
import random

GAME_WIDTH = 400
GAME_HEIGHT = 400
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "GREEN"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "BLACK"

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass

window = Tk()

window.title("Snake Game")
window.resizable(False,False) 

score = 0
direction = "down"
label = Label(window, text = "Score: {}".format(score),font=("Liberation Mono",40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.mainloop()
