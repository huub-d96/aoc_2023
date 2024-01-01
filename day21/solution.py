import math 

data ='''
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = [[c for c in line] for line in data.strip().splitlines() if line]

y_max = len(data)
x_max = len(data[0])

#Find start point
for y in range(y_max):
    for x in range(x_max):
        if data[y][x] == 'S':
            start = (x,y)

rep = 5
steps = x_max//2 + x_max*(rep//2)


#Grow 
new_data = [['.' for _ in range(x_max*rep)] for _ in range(y_max*rep)]
for y in range(y_max*rep):
    for x in range(x_max*rep):
        new_data[y][x] = data[y%y_max][x%x_max] if data[y%y_max][x%x_max] != 'S' else '.'

start = (start[0]+x_max*(rep//2), start[0]+y_max*(rep//2))
new_data[start[1]][start[0]] = 'S'
data = new_data
y_max = len(data)
x_max = len(data[0])         

#Fill area
points = set([start])
sol_pt1 = 0
print(f'Walking trough the garden for {steps} steps, this might take a while...')
for step in range(steps):

    next_points = set()

    for (x,y) in points:
        for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)]:

            nx = x + dx
            ny = y + dy
        
            if 0 <= nx < x_max and 0 <= ny < y_max: 
                pass
            else:
                continue
                
            if data[ny][nx] != '#':
                next_points.add((nx, ny))
                
    points = next_points

    if step == 63:
       sol_pt1 = len(points)


      
#Print map
for y in range(y_max):
    for x in range(x_max):
        if (x,y) in points:
            print('O', end="")
        else:
            print(data[y][x], end="")
    print()


#Count
y_step = y_max //rep
x_step = x_max //rep
counts = {}
for yc in range(rep):
    for xc in range(rep):
        cnt = 0
        for y in range(yc*y_step, (yc+1)*y_step):
            for x in range(xc*x_step, (xc+1)*x_step):
                if (x,y) in points:
                    cnt += 1

        counts[f'x{xc}-y{yc}'] = cnt

#Count up the different repeating tiles
actual_steps = 26501365
reps = (actual_steps-x_step//2)/x_step
total = 0

#Fulls
total += counts['x1-y2']*(reps**2) #Even parity
total += counts['x2-y2']*((reps-1)**2) #Odd parity (center)

#tops
total += counts['x2-y0'] + counts['x0-y2'] + counts['x4-y2'] + counts['x2-y4']

#Halfs
total += (reps-1)*counts['x1-y1']
total += (reps-1)*counts['x1-y3']
total += (reps-1)*counts['x3-y1']
total += (reps-1)*counts['x3-y3']

#Corners
total += reps*counts['x0-y1']
total += reps*counts['x0-y3']
total += reps*counts['x4-y1']
total += reps*counts['x4-y3']

#Print results
print('Part 1:', sol_pt1)
print('Part 2:', round(total))
