data = '''
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''

data1 = """
R 4 (#70c710)
D 4 (#0dc571)
L 4 (#5713f0)
U 4 (#d2c081)
"""

f = open('data.txt', 'r')
data = f.read()
f.close()

data = data.strip().splitlines()

ground = [['#']]

#Part 1: With visualisation
def add_col_right(ground):
    return [[*row, '.'] for row in ground]

def add_col_left(ground):
    return [['.', *row] for row in ground]

def add_row_down(ground):
    return ground + [['.' for _ in range(len(ground[0]))]]

def add_row_up(ground):
    return [['.' for _ in range(len(ground[0]))]] + ground

dirs = {'R': (1,0), 'L': (-1, 0), 'U':(0,-1), 'D':(0,1)}
current = (0,0)
for line in data:
    direction, length, color = line.split(' ')
    length = int(length)
    direction = dirs[direction]

    for dig in range(length):
        
        nx = current[0] + direction[0]
        ny = current[1] + direction[1]

        x_max = len(ground[0])
        y_max = len(ground)

        if nx == x_max:
            ground = add_col_right(ground)
        if nx == -1:
            ground = add_col_left(ground)
            current = (current[0]+1, current[1])
        if ny == y_max:
            ground = add_row_down(ground)
        if ny == -1:
            ground = add_row_up(ground)
            current = (current[0], current[1]+1)

        current = (current[0]+direction[0], current[1]+direction[1])
        ground[current[1]][current[0]] = '#'

#Fill
xs = len(ground[0]) // 2
ys = len(ground[0]) // 2

#Seed filling point
ground[ys][xs] = 'X'

active = True
while(active):
    active = False
    for y in range(len(ground)):
        for x in range(len(ground[0])):
            if ground[y][x] == 'X':
               for (nx, ny) in [(0,1), (0,-1), (1,0), (-1,0)]:
                   
                    xx = x + nx
                    yy = y + ny

                    if 0 <= xx < len(ground[0]) and 0 <= yy < len(ground):

                        if ground[y+ny][x+nx] == '.':
                            ground[y+ny][x+nx] = 'X'
                            active = True
cnt = 0
for y in range(len(ground)):
    for x in range(len(ground[0])):
        if ground[y][x] in  ['#', 'X']:
            cnt += 1

        print(ground[y][x], end='')
    print()

print('Part 1:', cnt)

#Part 2: Using polygon formula

current = (0,0)
coords = []
walk = 0
for line in data:
    _, _, color = line.split(' ')
    color = color[1:-1]

    direction = ['R', 'D', 'L', 'U'][int(color[-1])]

    length = int(color[1:-1], 16)

    if direction == 'R':
        new = (current[0]+length, current[1]) 
    elif direction == 'L':
        new = (current[0]-length, current[1])   
    elif direction == 'U':
        new = (current[0], current[1]+length)
    elif direction == 'D':
        new = (current[0], current[1]-length)    

    coords.append(new)
    walk += length
    current = new

area = 0
coords = coords[::-1]
for i in range(len(coords)):
    x = coords[i][0]
    y = coords[i][1]
    xx = coords[(i+1)%len(coords)][0]
    yy = coords[(i+1)%len(coords)][1]

    
    area += (y + yy) * (x - xx)
    
area = 0.5*area

print('Part 2:', area+walk*0.5+1)
