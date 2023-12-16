import sys

data = r'''
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
'''
#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = [[d for d in line] for line in data.strip().splitlines()]

y_max = len(data)
x_max = len(data[0])

sys.setrecursionlimit(10000)

def draw_next(x, y, next_x, next_y):

    dx = next_x - x
    dy = next_y - y

    if x >= 0 and y >=0 and x < x_max and y < y_max:

        #Stop if we go the same direction again
        if (x,y,dx,dy) in pathway:
            return 0

        pathway.add((x,y, dx, dy))

        # Stop when we hit a wall
        if next_x < 0 or next_x >= x_max or next_y < 0 or next_y >= y_max:
            return 0

    #Determine the next tile
    next_tile = data[next_y][next_x]    

    match next_tile:
        case '|':
            if dy != 0: #Moving vertically
                return draw_next(next_x, next_y, next_x, next_y+dy)
            else:
                return draw_next(next_x, next_y, next_x, next_y+1) + draw_next(next_x, next_y, next_x, next_y-1)
        case '-':
            if dy != 0: #Moving vertically
                return draw_next(next_x, next_y, next_x+1, next_y) + draw_next(next_x, next_y, next_x-1, next_y)
            else:
                return draw_next(next_x, next_y, next_x+dx, next_y) 
        case '/':
            return draw_next(next_x, next_y, next_x-dy, next_y-dx)
        case '\\':
            return draw_next(next_x, next_y, next_x+dy, next_y+dx)
        case other:
            return draw_next(next_x, next_y, next_x+dx, next_y+dy)
            

#Left side
max_energy = 0
for y in range(y_max):
    pathway = set()
    draw_next(-1,y,0,y)
    unique_path = set([(x,y) for x,y,_,_ in pathway])

    energy=len(unique_path)
    if energy > max_energy:
        max_energy=energy

#Right side
for y in range(y_max):
    pathway = set()
    draw_next(x_max, y, x_max-1, y)
    unique_path = set([(x,y) for x,y,_,_ in pathway])

    energy=len(unique_path)
    if energy > max_energy:
        max_energy=energy
        
#Top side
for x in range(x_max):
    pathway = set()
    draw_next(x, -1, x, 0)
    unique_path = set([(x,y) for x,y,_,_ in pathway])

    energy=len(unique_path)
    if energy > max_energy:
        max_energy=energy

#Bottom side
for x in range(x_max):
    pathway = set()
    draw_next(x, y_max, x, y_max-1)
    unique_path = set([(x,y) for x,y,_,_ in pathway])

    energy=len(unique_path)
    if energy > max_energy:
        max_energy=energy

print('Max energized tiles:', max_energy)



