from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0  # Score variable

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global score  # Access the global score variable
    head = snake[-1].copy()
    head.x += aim.x
    head.y += aim.y

    if not inside(head) or head in snake:
        game_over()  # Display game-over screen
        return

    snake.append(head)

    if head == food:
        score += 1  # Increment the score
        print('Score:', score)
        print('snake', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    display_score()  # Display the current score
    update()
    ontimer(move, 100)

def display_score():
    penup()
    goto(-190, 190)
    color('white')  # Change text color to white
    write(f'Score: {score}', font=('Arial', 12, 'normal'))

def game_over():
    clear()
    penup()
    goto(0, 0)
    color('red')
    write('GAME OVER', font=('Arial', 24, 'bold'))
    goto(0, -20)
    color('white')  # Change text color to white
    write(f'Final Score: {score}', font=('Arial', 16, 'normal'))
    update()

setup(420, 420, 370, 0)
bgcolor('black')  # Set background color to black
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()