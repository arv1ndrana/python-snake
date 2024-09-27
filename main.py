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
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0,int((GAME_WIDTH / SPACE_SIZE)) - 1) * SPACE_SIZE
        y = random.randint(0,int((GAME_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill= FOOD_COLOR, tag= "food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    window.after(SPEED,next_turn,snake,food)


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

window.update()

# For centering the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# ---------------------------------------------------------- #

snake = Snake()
food = Food()
next_turn(snake,food)



window.mainloop()
