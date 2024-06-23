import curses
import random

# Constants for game elements
SNAKE_CHAR = '█'
NORMAL_FOOD_CHAR = 'π'
SPECIAL_FOOD_CHAR = 'X'
OBSTACLE_CHAR = '▓'

# Initialize the game window
stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Get screen dimensions
height, width = stdscr.getmaxyx()

# Define the snake and its initial position
snake = [(height // 2, width // 2 + i) for i in range(3)]
snake_direction = curses.KEY_RIGHT

# Function to place food on the screen
def place_food(food_type):
    while True:
        food = (random.randint(1, height - 2), random.randint(1, width - 2))
        if food not in snake and food not in obstacles:
            stdscr.addch(food[0], food[1], food_type)
            return food

# Initialize obstacles
obstacles = []
obstacle_count = int(0.05 * height * width)
for _ in range(obstacle_count // 5):
    if random.choice([True, False]):
        start = (random.randint(1, height - 2), random.randint(1, width - 6))
        for i in range(5):
            obstacles.append((start[0], start[1] + i))
    else:
        start = (random.randint(1, height - 6), random.randint(1, width - 2))
        for i in range(5):
            obstacles.append((start[0] + i, start[1]))

for obstacle in obstacles:
    stdscr.addch(obstacle[0], obstacle[1], OBSTACLE_CHAR)

# Place food on the screen
normal_food = place_food(NORMAL_FOOD_CHAR)
special_food = place_food(SPECIAL_FOOD_CHAR)

# Game loop
def main(stdscr):
    global snake_direction, normal_food, special_food
    normal_food_eaten = 0
    special_food_eaten = 0
    paused = False
    speed = 100

    while True:
        if not paused:
            # Handle snake movement
            new_head = (snake[0][0], snake[0][1])
            if snake_direction == curses.KEY_UP:
                new_head = (new_head[0] - 1, new_head[1])
            elif snake_direction == curses.KEY_DOWN:
                new_head = (new_head[0] + 1, new_head[1])
            elif snake_direction == curses.KEY_LEFT:
                new_head = (new_head[0], new_head[1] - 1)
            elif snake_direction == curses.KEY_RIGHT:
                new_head = (new_head[0], new_head[1] + 1)

            # Wrap around the screen boundaries
            new_head = (new_head[0] % height, new_head[1] % width)

            # Check for collisions
            if new_head in snake or new_head in obstacles:
                break

            # Move the snake
            snake.insert(0, new_head)
            stdscr.addch(new_head[0], new_head[1], SNAKE_CHAR)

            # Handle food consumption
            if new_head == normal_food:
                normal_food_eaten += 1
                normal_food = place_food(NORMAL_FOOD_CHAR)
            elif new_head == special_food:
                special_food_eaten += 1
                special_food = place_food(SPECIAL_FOOD_CHAR)
                if len(snake) > 1:
                    tail = snake.pop()
                    stdscr.addch(tail[0], tail[1], ' ')
            else:
                tail = snake.pop()
                stdscr.addch(tail[0], tail[1], ' ')

        # Handle user input
        key = stdscr.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if not paused:
                snake_direction = key
        elif key == ord(' '):
            paused = not paused
        elif key == ord('+') and speed > 10:
            speed -= 10
        elif key == ord('-') and speed < 500:
            speed += 10

        # Refresh screen
        stdscr.refresh()
        curses.napms(speed)

    # End of game
    stdscr.clear()
    stdscr.addstr(height // 2, width // 2 - 10, f"Game Over! Normal food eaten: {normal_food_eaten}")
    stdscr.addstr(height // 2 + 1, width // 2 - 10, f"Special food eaten: {special_food_eaten}")
    stdscr.addstr(height // 2 + 2, width // 2 - 10, "Press any key to exit")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)

# Clean up the window
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
