from turtle import Screen, Turtle
from snake import Snake
import time

def setup_screen():
  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor("black")
  screen.title("Snake Game")
  screen.tracer(0)
  return screen

def setup_controls(screen, snake):
  screen.listen()
  controls = {
    "Up": snake.up,
    "Down": snake.down,
    "Left": snake.left,
    "Right": snake.right
  }
  for key, function in controls.items():
    screen.onkey(function, key)

def main():
  try:
    screen = setup_screen()
    snake = Snake()
    setup_controls(screen, snake)

    game_is_on = True
    while game_is_on:
      screen.update()
      time.sleep(0.1)
      snake.move()

    screen.exitonclick()
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()