import math

data ='''
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Format data to list of lists
data =  data.strip().splitlines()

maps = []
c_map = []
for line in data:

    if line:
        c_map.append(line)
    else:
        maps.append(c_map)
        c_map = []
        
maps.append(c_map)
total = 0
smudge_total = 0
for map in maps:

    y_max = len(map)
    x_max = len(map[0])

    #Check colums pairs
    for x in range(x_max-1):
        col1 = []
        col2 = []
        for y in range(y_max):
            col1.append(map[y][x])
            col2.append(map[y][x+1])

        #Check the reflection
        is_col_match=True
        is_c_smudge_match = 2
        for i in range(0, min(x+1, x_max-(x+1))):
            
            for y in range(y_max):
                if map[y][x-i] != map[y][x+1+i]:
                    is_col_match=False
                    is_c_smudge_match -= 1

        #Check matches
        if is_col_match:
            total += x+1

        if is_c_smudge_match == 1:
            smudge_total += x+1
            

    #Check colums pairs
    for y in range(y_max-1):    
    
        #Check the reflection
        is_row_match=True
        is_r_smudge_match = 2
        for i in range(0, min(y+1, y_max-(y+1))):
            
            for x in range(x_max):
                if map[y-i][x] != map[y+1+i][x]:
                    is_row_match=False
                    is_r_smudge_match -= 1

        #Check matches
        if is_row_match:
            total += (y+1)*100

        if is_r_smudge_match == 1:
            smudge_total += (y+1)*100

print('Part 1:', total)
print('Part 2:', smudge_total)
