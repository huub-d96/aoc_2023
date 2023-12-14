data ='''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Format data to list of lists
data = [[d for d in line] for line in  data.strip().splitlines()]

y_max = len(data)
x_max = len(data[0])

#Print the map
def print_map():
    
    for y in range(y_max):
        for x in range(x_max):
            print(data[y][x], end='')
        print()
    print()

#Calculate load
def calc_load():
    
    total_load = 0
    for y in range(y_max):
        num_rocks = data[y].count('O')
        line_load = num_rocks*(y_max-y)
        total_load += line_load

    return total_load


def move_north(x_start, y_start):

    x = x_start
    y = y_start
    while(True):
        #Cannot go AOB or move if a rock is in the way
        if y-1 < 0:
            break
        if data[y-1][x] in ['#', 'O']:
            break   

        #Move rock one step 
        data[y-1][x] = 'O'
        data[y][x] = '.'
        #print(f'Move North ({x},{y}) -> ({x},{y-1})')
        y -= 1 #Follow rock one step north

def move_south(x_start, y_start):

    x = x_start
    y = y_start
    while(True):
        #Cannot go AOB or move if a rock is in the way
        if y+1 >= y_max:
            break
        if data[y+1][x] in ['#', 'O']:
            break   

        #Move rock one step 
        data[y+1][x] = 'O'
        data[y][x] = '.'
        #print(f'Move South ({x},{y}) -> ({x},{y+1})')
        y += 1 #Follow rock one step south

def move_west(x_start, y_start):
        
    x = x_start
    y = y_start
    while(True):
        #Cannot go AOB or move if a rock is in the way
        if x-1 < 0:
            break
        if data[y][x-1] in ['#', 'O']:
            break   

        #Move rock one step 
        data[y][x-1] = 'O'
        data[y][x] = '.'
        #print(f'Move West ({x},{y}) -> ({x-1},{y})')
        x -= 1 #Follow rock one step west       

def move_east(x_start, y_start):    
    x = x_start
    y = y_start
    while(True):
        #Cannot go AOB or move if a rock is in the way
        if x+1 >= x_max:
            break
        if data[y][x+1] in ['#', 'O']:
            break   

        #Move rock one step 
        data[y][x+1] = 'O'
        data[y][x] = '.'
        #print(f'Move East ({x},{y}) -> ({x+1},{y})')
        x += 1 #Follow rock one step east        
        
            
#Slide rocks
cycles = 1000000000
hash_map = []
loads = []
for cycle in range(cycles):

    tilts = [move_north, move_west, move_south, move_east]
    for i in range(4):

        tilt = tilts[i]
        invert = True if i >= 2 else False
            
        for y in range(y_max):

            if invert:
                y = y_max - y - 1
                
            for x in range(x_max):

                if invert:
                    x = x_max - x - 1

                #Hit a moving rock
                if data[y][x] == 'O':
                    tilt(x,y)
    
    #Check with hash_map
    data_tuple = tuple([tuple([d for d in line]) for line in  data])
    data_hash = hash(data_tuple)

    #We can stop after we find a repeated pattern
    if data_hash in hash_map:
        
        first_match = hash_map.index(data_hash)
        period = cycle - first_match
        print(f'Cycle {cycle} is the same as Cycle {first_match}, repeating every {period} cycles')
        break
    else:
        hash_map.append(data_hash)
        loads.append(calc_load())

#Print the final results
equivalent = (cycles-1-first_match)%period + first_match
print(f'Total load after {cycles} cycles: {loads[equivalent]}')
