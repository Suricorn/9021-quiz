# Written by *** for COMP9021
#
# Implements a function display_leftmost_topmost_boundary(*grid)
# whose argument grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# that represent one or more "full polygons" that do not "touch"
# each other.
# The selected polygon's top boundary is as high as possible ,
# and amongst all polygons whose top boundary is as high as possible,
# the selected polygon's top boundary starts as much to the left
# as possible.


def display(*grid):
    max_y = len(grid)
    max_x = len(grid[0])

    for row in grid:
        for i, x in enumerate(row):
            end = '\n' if i == max_x -1 else ' '
            print('{}'.format(x), end=end)
        #print('', end='\n')

def display_leftmost_topmost_boundary(*grid):
    max_y = len(grid)
    max_x = len(grid[0])

    #print('x:{} y:{}'.format(x, y))

    #print(out_grid)

    #print(' ' +  '--' * max_x)

    first_point = None

    edge_grid = []

    for y in range(max_y):

        #print('|', end='')
        row = []
        for x in range(max_x):
            print_star = scan_point(grid, x, y)

            #print('{} {} {}'.format(x, y, print_star))

            if print_star == True:
                if first_point == None:
                    first_point = (x, y)
                row.append('*')
            else:
                row.append(' ')

            #out_grid[0][1] = 'B'

        #for w in row:
            #print('{} '.format(w), end='')
        #print('|')

        edge_grid.append(row)
    #print(' ' + '--' * max_x)

    #print(edge_grid)
    #print(first_point)

    edge_x, edge_y = scan_edge(edge_grid, first_point)

    #print("{} {}".format(edge_x, edge_y))

    for y in range(max_y):
        for x in range(max_x):
            end = '\n' if x == max_x -1 else ' '
            if y <= edge_y and x <= edge_x:
                print('{}'.format(edge_grid[y][x]), end=end)
            else:
                print(' ', end=end)
        #print('', end='\n')


def traverse(grid, visited, point):
    #print(point)

    max_y = len(grid)
    max_x = len(grid[0])

    if point in visited:
        return

    visited.append(point)

    x = point[0]
    y = point[1]

    x1 = x - 1
    x2 = x + 1
    y1 = y - 1
    y2 = y + 1

    eight_points = [(x1, y1), (x, y1), (x2, y1), (x2, y), (x2, y2), (x, y2), (x1, y2), (x1, y)]

    for next_point in eight_points:
        nx = next_point[0]
        ny = next_point[1]

        if nx < 0 or nx >= max_x or ny < 0 or ny >= max_y:
            continue

        if grid[ny][nx] == '*' and next_point not in visited:
            traverse(grid, visited, next_point)


def scan_edge(grid, first_point):

    edge_x = 0
    edge_y = 0


    visited = list()

    traverse(grid, visited, first_point)
    #print("{}: {}".format(len(visited), visited))

    for p in visited:
        edge_x = max(edge_x, p[0])
        edge_y = max(edge_y, p[1])

    return edge_x, edge_y

    

def scan_point(grid, x, y):
    max_y = len(grid)
    max_x = len(grid[0])
    
    x1 = x - 1
    x2 = x + 1
    y1 = y - 1
    y2 = y + 1

    #print("{} {} {} {} ".format(max_x, max_y, x, y))

    point = grid[y][x]

    if point == ' ':
        return False
    else:
        if x1 < 0 or x2 >= max_x or y1 < 0 or y2 >= max_y:
            return True

        if grid[y][x1] == '*' and grid[y][x2] == '*' and grid[y1][x] == '*' and grid[y2][x] == '*':
            return False

    return True


def unit_test(*grid):
    #print('=========')
    display(*grid)
    print('---------')
    display_leftmost_topmost_boundary(*grid)
    print('=========')


if __name__ == "__main__":
    grid_1 = (
            '  *    ',
            ' ****  ',
            '*****  ',
            '****** ',
            ' ****  ',
            ' **    ')

    grid_2 = (
            ' *        ',
            '***   **  ',
            ' *** ***  ',
            ' ***  *   ',
            '****      ',
            ' **       ')
    grid_3 = (
            '      ',
            '  *  *',
            ' ** **',
            ' **** ',
            ' *****',
            '   *  ',
            '**    ',
            '**    ',
            '      ')

    unit_test(*grid_1)
    unit_test(*grid_2)
    unit_test(*grid_3)

