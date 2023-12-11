data ='''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Format data to list of lists, create extra border to avoid out of range problems
data =  [[c for c in line] for line in data.strip().splitlines()]

y_max = len(data)
x_max = len(data[0])

###Expand the universe###

#Check rows
empty_rows = []
for y in range(y_max):
    detect_g = False
    for x in range(x_max):
        if data[y][x] == '#':
            detect_g=True
            break

    if not detect_g:
        empty_rows.append(y)

for r in empty_rows:
    data[r] = ['*' for _ in range(x_max)]
        
#Check columns
empty_columns = []
for x in range(x_max):
    detect_g = False
    for y in range(y_max):
        if data[y][x] == '#':
            detect_g=True
            break

    if not detect_g:
        empty_columns.append(x)

for c in empty_columns:
    for j in range(y_max):
        data[j][c] = '*'

###Find galaxies###
coords = []
for y in range(y_max):
    for x in range(x_max):
        if data[y][x] == '#':
            coords.append([x,y])

###Compute the path lenght
path_length = 0
age = 1_000_000 #Set to 2 for part 1, 1_000_000 for part 2
while(coords):
    coord1 = coords[-1]
    coords.pop()

    for coord2 in coords:
        path_length += abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])

        for c in empty_columns:
            if c > min(coord1[0], coord2[0]) and c < max(coord1[0], coord2[0]):
                path_length += age-1

        for r in empty_rows:
            if r > min(coord1[1], coord2[1]) and r < max(coord1[1], coord2[1]):
                path_length += age-1

print('Galaxy age:', age)
print('Shortest path total:', path_length)

###Print map###
#for y in range(y_max):
#    for x in range(x_max):   
#        print(data[y][x], end='')
#    print()        

