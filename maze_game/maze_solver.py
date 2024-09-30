
## Maze solving recursive algorithm
## Reference mentioned in report.pdf

def get_starting_finishing_points(maze):
    _start = [i for i in range(len(maze[0])) if maze[0][i] == 'c']
    _end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'c']
    return [0, _start[0]], [len(maze) - 1, _end[0]]

def escape(maze,rat_path,finish):
    current_cell = rat_path[len(rat_path) - 1]

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == 'c':
        maze[current_cell[0] + 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] + 1, current_cell[1]])
        escape(maze,rat_path,finish)

    if maze[current_cell[0]][current_cell[1] + 1] == 'c':
        maze[current_cell[0]][current_cell[1] + 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] + 1])
        escape(maze,rat_path,finish)

    if maze[current_cell[0] - 1][current_cell[1]] == 'c':
        maze[current_cell[0] - 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] - 1, current_cell[1]])
        escape(maze,rat_path,finish)

    if maze[current_cell[0]][current_cell[1] - 1] == 'c':
        maze[current_cell[0]][current_cell[1] - 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] - 1])
        escape(maze,rat_path,finish)

    # If we get here, this means that we made a wrong decision, so we need to
    # backtrack
    current_cell = rat_path[len(rat_path) - 1]
    if current_cell != finish:
        cell_to_remove = rat_path[len(rat_path) - 1]
        rat_path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'
    
    return maze

## Generates the path files

def generate_pathfile(maze_input,level):
    maze = [row[:] for row in maze_input]
    start,finish = get_starting_finishing_points(maze)
    rat_path = [start]
    maze = escape(maze, rat_path, finish)
    maze[start[0]][start[1]] = 'p'

    pos = start

    with open(f'paths/path_level_{level}.txt', 'w') as path_file:
        path_file.truncate(0)
        path_file.write('START'+'\n')
        commands=['start']
        while(pos!=finish):
            n = len(commands)
            i,j = pos[0],pos[1]  
            if i < len(maze) - 1 and maze[i + 1][j] == 'p':
                if commands[n-1] != 'UP':
                    pos = [i + 1, j]
                    path_file.write('DOWN' + '\n')
                    commands.append('DOWN')
                    
            if j < len(maze[0]) - 1 and maze[i][j + 1] == 'p':
                if commands[n-1] != 'LEFT': 
                    pos = [i, j + 1]
                    path_file.write('RIGHT' + '\n')
                    commands.append('RIGHT')
                     
            if j > 0 and maze[i][j - 1] == 'p':
                if commands[n-1] != 'RIGHT': 
                    pos = [i, j - 1]
                    path_file.write('LEFT' + '\n')
                    commands.append('LEFT') 
                    
            if i > 0 and maze[i - 1][j] == 'p':
                if commands[n-1] != 'DOWN':
                    pos = [i - 1, j]
                    path_file.write('UP' + '\n')
                    commands.append('UP') 
        
        path_file.write('END'+'\n')
                    
                           