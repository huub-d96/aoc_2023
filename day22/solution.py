import copy

data ='''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Parse input data
bricks = []
x_max = y_max = z_max = 0
for line in data.splitlines():

    if line:
        start, end = line.split('~')
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]

        if start[0] > x_max or end[0] > x_max:
            x_max = max(start[0], end[0])
        if start[1] > y_max or end[1] > y_max:
            y_max = max(start[1], end[1])
        if start[2] > z_max or end[2] > z_max:
            z_max = max(start[2], end[2])

        bricks.append([start, end])

bricks = sorted(bricks, key=lambda x: x[1][2])

#Build empty tower with floor
tower = [[['.' for _ in range(z_max+1)] for _ in range(y_max+1)] for _ in range(x_max+1)]
for x in range(x_max+1):
    for y in range(y_max+1):
        tower[x][y][0] = '-'
        
#Set initial bricks       
for i, brick in enumerate(bricks):

    start = brick[0]
    end = brick[1]

    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dz = end[2] - start[2]

    
    if dx < 0 or dy < 0 or dz < 0:
        print('!!!')
        print(dx, dy, dz)

    for step in range(max(dx,dy,dz)+1):

        xs = min(1, dx)*step
        ys = min(1, dy)*step
        zs = min(1, dz)*step
        
        tower[start[0] + xs][start[1] + ys][start[2] + zs] = chr(i+65)

def gravity(bricks, tower):

    fallen_bricks = set()
    for brick_id in range(len(bricks)):

        fall = True
        while(fall):
       
            start = bricks[brick_id][0]
            end = bricks[brick_id][1]

            dx = end[0] - start[0]
            dy = end[1] - start[1]
            dz = end[2] - start[2]
            bottom_z = min(start[2], end[2])

            char = tower[start[0]][start[1]][start[2]]

            if dx < 0 or dy < 0 or bottom_z < 0:
                print('!!!')
                print(dx, dy, dz)

            for step in range(max(dx,dy)+1):

                xs = min(1, dx)*step
                ys = min(1, dy)*step

                if tower[start[0] + xs][start[1] + ys][bottom_z-1] != '.':
                    fall = False
            
            if fall:          
                #print('Falling!', char)
                fallen_bricks.add(char)
                #Update tower                
                for i, c in enumerate(['.', char]):
                    for step in range(max(dx,dy,dz)+1):

                        xs = min(1, dx)*step
                        ys = min(1, dy)*step
                        zs = min(1, dz)*step
                        
                        tower[start[0] + xs][start[1] + ys][start[2] + zs - i] = c

                #Update brick
                bricks[brick_id][0] = [start[0], start[1], start[2]-1]
                bricks[brick_id][1] = [end[0], end[1], end[2]-1]
            
    return bricks, tower, fallen_bricks

#Print tower
def print_tower(tower):
    for z in range(z_max+1):
        #x-view
        for x in range(x_max+1):

            char = '.'
            cnt = 0
            for y in range(y_max+1):
                if tower[x][y][z_max-z] != '.':
                    cnt += 1 if char != tower[x][y][z_max-z] else 0
                    char = tower[x][y][z_max-z]
            if cnt > 1:
                print('?', end='')
            else:
                print(char, end='')  
        print('  ', end='')

        #y-view
        for y in range(x_max+1):

            char = '.'
            cnt = 0
            for x in range(x_max+1):
                if tower[x][y][z_max-z] != '.':
                    cnt += 1 if char != tower[x][y][z_max-z] else 0
                    char = tower[x][y][z_max-z]
            if cnt > 1:
                print('?', end='')
            else:
                print(char, end='')  
        print(' ',z_max-z)

    print()


#Initial fall
bricks, tower, _ = gravity(bricks, tower)
print('Simulating gravity for different tower setups, this can take a while ...')

#Check wether bricks can be removed
disintegrate = 0
fallen = 0
for brick_ID in range(len(bricks)):

    tower_new = copy.deepcopy(tower)

    #Remove the brick from the tower
    start = bricks[brick_ID][0]
    end = bricks[brick_ID][1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dz = end[2] - start[2]

    for step in range(max(dx,dy,dz)+1):

        xs = min(1, dx)*step
        ys = min(1, dy)*step
        zs = min(1, dz)*step
        
        tower_new[start[0] + xs][start[1] + ys][start[2] + zs] = '.'    

    #Remove brick from brick list
    new_bricks = copy.deepcopy(bricks)
    del new_bricks[brick_ID]    

    #Gravity
    new_bricks_g, tower_new_g, fallen_bricks = gravity(copy.deepcopy(new_bricks), copy.deepcopy(tower_new))

    #Add number of fallen bricks
    fallen += len(fallen_bricks)

    #If the towers are the same, brick can be safetly disintegrated
    if tower_new == tower_new_g:
        disintegrate += 1
        
#Print results
print('Part 1:', disintegrate)
print('Part 2:', fallen)

