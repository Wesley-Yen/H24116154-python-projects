import random

def generate_path(maze, N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary.
    path = [(0, 0)]
    maze[(0, 0)] = 2
    
    i, j = 0, 0
    while (i, j) != (N-1, M-1):
        if i < N-1 and j < M-1:
            if random.choice([True, False]):
                i += 1
            else:
                j += 1
        elif i < N-1:
            i += 1
        elif j < M-1:
            j += 1
        path.append((i, j))
        maze[(i, j)] = 2

    return path

def add_obstacles(maze, min_obstacles, N, M):
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    count = 0
    
    while count < min_obstacles:
        try:
            cell = random.choice(empty_cells)
            maze[cell] = 1
            empty_cells.remove(cell)
            count += 1
        except IndexError:
            print("No more empty cells available to place obstacles.")
            break

def set_obstacle(maze, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to place an obstacle (i j): ").split())
        if not (0 <= i < N and 0 <= j < M):
            raise IndexError
        if maze[(i, j)] == 2:
            print("Cannot place obstacle on the path.")
        elif maze[(i, j)] == 1:
            print("Obstacle already present.")
        else:
            maze[(i, j)] = 1
    except ValueError:
        print("Invalid input. Please enter integer coordinates.")
    except IndexError:
        print("Coordinates out of bounds.")

def remove_obstacle(maze, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to remove an obstacle (i j): ").split())
        if not (0 <= i < N and 0 <= j < M):
            raise IndexError
        if maze[(i, j)] == 2:
            print("Cannot remove obstacle from the path.")
        elif maze[(i, j)] == 0:
            print("No obstacle present at the specified coordinates.")
        else:
            maze[(i, j)] = 0
    except ValueError:
        print("Invalid input. Please enter integer coordinates.")
    except IndexError:
        print("Coordinates out of bounds.")

def print_maze(maze, N, M):
    for i in range(N):
        row = ''
        for j in range(M):
            if maze[(i, j)] == 0:
                row += '   '
            elif maze[(i, j)] == 1:
                row += ' X '
            else:
                row += ' O '
        print(row)

def main():
    while True:
        filename = input("Enter the maze blueprint filename (e.g., grid77.txt): ")
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            break
        except IOError:
            print("File not found. Please enter a valid filename.")

    N = len(lines)
    M = len(lines[0].strip().split())
    maze = {}
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip().split()):
            maze[(i, j)] = int(char)

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0 or min_obstacles > N * M:
                raise ValueError
            break
        except ValueError:
            print("Invalid number. Please enter a non-negative integer within the valid range.")

    generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)
    print("Initial maze with obstacles:")
    print_maze(maze, N, M)

    while True:
        print("\nOptions:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Print maze")
        print("4. Exit")
        
        option = input("Enter your choice: ")
        if option == '1':
            set_obstacle(maze, N, M)
        elif option == '2':
            remove_obstacle(maze, N, M)
        elif option == '3':
            print_maze(maze, N, M)
        elif option == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter a valid choice.")

if __name__ == "__main__":
    main()
