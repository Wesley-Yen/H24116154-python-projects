import random
import os

def read_maze_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            maze = {}
            for r, line in enumerate(lines):
                for c, char in enumerate(line.strip()):
                    maze[(r, c)] = 0  # Initialize all cells as empty
            return maze, len(lines), len(lines[0].strip())
    except IOError:
        print("Error: File not found. Please enter a valid file name.")
        return None, None, None

def generate_random_path(maze, N, M):
    path = [(0, 0)]
    maze[(0, 0)] = 2
    current = (0, 0)
    while current != (N-1, M-1):
        r, c = current
        next_steps = []
        if r + 1 < N and maze[(r+1, c)] == 0:
            next_steps.append((r+1, c))
        if c + 1 < M and maze[(r, c+1)] == 0:
            next_steps.append((r, c+1))
        if not next_steps:
            print("Error: Unable to generate a path.")
            return False
        next_step = random.choice(next_steps)
        path.append(next_step)
        maze[next_step] = 2
        current = next_step
    return True

def add_random_obstacles(maze, N, M, min_obstacles):
    count = 0
    while count < min_obstacles:
        r = random.randint(0, N-1)
        c = random.randint(0, M-1)
        if maze[(r, c)] == 0:
            maze[(r, c)] = 1
            count += 1

def print_maze(maze, N, M):
    for r in range(N):
        for c in range(M):
            if maze[(r, c)] == 0:
                print(' ', end='')
            elif maze[(r, c)] == 1:
                print('X', end='')
            elif maze[(r, c)] == 2:
                print('O', end='')
        print()

def main():
    while True:
        filename = input("Enter the maze file name (grid78.txt or grid89.txt): ")
        maze, N, M = read_maze_file(filename)
        if maze is not None:
            break

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles: "))
            if min_obstacles < 0 or min_obstacles >= N * M:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if not generate_random_path(maze, N, M):
        return

    add_random_obstacles(maze, N, M, min_obstacles)

    while True:
        print("Options:")
        print("1. Print the maze")
        print("2. Set an obstacle")
        print("3. Remove an obstacle")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_maze(maze, N, M)
        elif choice == '2':
            try:
                r = int(input("Enter row: "))
                c = int(input("Enter column: "))
                if (r, c) not in maze:
                    raise KeyError
                if maze[(r, c)] == 2:
                    print("Error: Cannot place obstacle on the path.")
                else:
                    maze[(r, c)] = 1
            except (ValueError, KeyError):
                print("Invalid coordinates or cell. Try again.")
        elif choice == '3':
            try:
                r = int(input("Enter row: "))
                c = int(input("Enter column: "))
                if (r, c) not in maze:
                    raise KeyError
                if maze[(r, c)] == 2:
                    print("Error: Cannot remove path cell.")
                else:
                    maze[(r, c)] = 0
            except (ValueError, KeyError):
                print("Invalid coordinates or cell. Try again.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
