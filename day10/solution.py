#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Format data to list of lists, create extra border to avoid out of range problems
data = [['.', *[i for i in line],'.'] for line in data.strip().splitlines()]
data.insert(0, ['.' for i in data[0]])
data.append(['.' for i in data[0]])

y_max = len(data)
x_max = len(data[0])

def next_points(x,y):
    current_point = data[y][x]

    if current_point == 'S':
        points = []
        #Check up
        if data[y-1][x] in ['|', '7', 'F']:
            points.append([x,y-1])

        #Check right
        if data[y][x+1] in ['-', '7', 'J']:
            points.append([x+1,y])

        #Check down
        if data[y+1][x] in ['|', 'L', 'J']:
            points.append([x,y+1])

        #Check left
        if data[y][x-1] in ['-', 'L', 'F']:
            points.append([x-1,y])
    
        return points
    else:
        match current_point:
            case '|':
                return [[x,y+1], [x, y-1]]
            case '-':
                return [[x+1,y], [x-1, y]]
            case 'L':
                return [[x,y-1], [x+1,y]]
            case 'J':
                return [[x,y-1], [x-1,y]]
            case '7':
                return [[x,y+1], [x-1,y]]
            case 'F':
                return [[x,y+1], [x+1,y]]

#Find starting coords
for y in range(y_max):
    for x in range(x_max): 
        if data[y][x] == 'S':
            start = [x,y]            
            

#Part 1
steps = 1
prev = [start, start]
current = next_points(*start)

p1_route = [start, current[0]]
p2_route = [start, current[1]]

while(True):
   
    #Route 1
    next_pp = next_points(*current[0])
    next_p1 = next_pp[0] if next_pp[0] != prev[0] else next_pp[1]

    #Route 2
    next_pp = next_points(*current[1])
    next_p2 = next_pp[0] if next_pp[0] != prev[1] else next_pp[1]

    #Next steps
    prev = current
    current = [next_p1, next_p2]

    #Save the routes
    p1_route.append(next_p1)
    p2_route.append(next_p2)

    #Increment and break if needed
    steps +=1
    if current[0] == current[1]:
        break

print('Part 1:', steps)
    
#Part 2
route = [*p1_route, *p2_route[::-1]]  

for i in range(len(route)-1):

    x = route[i][0]
    y = route[i][1]

    dx = route[i+1][0] - route[i][0]
    dy = route[i+1][1] - route[i][1]

    #Match every path with specific labels based on direction
    match data[y][x]:    
        case '-':            
            if [x, y-1] not in route:
                data[y-1][x] = 'O' if dx == 1 else 'I'
            if [x, y+1] not in route:
                data[y+1][x] = 'I' if dx == 1 else 'O'
        case '|':
            if [x+1, y] not in route:
                data[y][x+1] = 'O' if dy == 1 else 'I'
            if [x-1, y] not in route:
                data[y][x-1] = 'I' if dy == 1 else 'O'
        case 'L':
            if [x-1, y] not in route:
                data[y][x-1] = 'O' if dy == -1 else 'I'
            if [x-1, y+1] not in route:
                data[y+1][x-1] = 'O' if dy == -1 else 'I'
            if [x, y+1] not in route:
                data[y+1][x] = 'O' if dy == -1 else 'I'
            if [x+1, y-1] not in route:
                data[y-1][x+1] = 'I' if dy == -1 else 'O'
        case 'J':
            if [x+1, y] not in route:
                data[y][x+1] = 'O' if dx == -1 else 'I'
            if [x+1, y+1] not in route:
                data[y+1][x+1] = 'O' if dx == -1 else 'I'
            if [x, y+1] not in route:
                data[y+1][x] = 'O' if dx == -1 else 'I'
            if [x-1, y-1] not in route:
                data[y-1][x-1] = 'I' if dx == -1 else 'O'
        case '7':
            if [x, y-1] not in route:
                data[y-1][x] = 'O' if dy == 1 else 'I'
            if [x+1, y-1] not in route:
                data[y-1][x+1] = 'O' if dy == 1 else 'I'
            if [x+1, y] not in route:
                data[y][x+1] = 'O' if dy == 1 else 'I'
            if [x-1, y+1] not in route:
                data[y+1][x-1] = 'I' if dy == 1 else 'O'  
        case 'F':
            if [x-1, y] not in route:
                data[y][x-1] = 'O' if dx == 1 else 'I'
            if [x-1, y-1] not in route:
                data[y-1][x-1] = 'O' if dx == 1 else 'I'
            if [x, y-1] not in route:
                data[y-1][x] = 'O' if dx == 1 else 'I'
            if [x+1, y+1] not in route:
                data[y+1][x+1] = 'I' if dx == 1 else 'O'          

#Draw route
for i in range(len(route)-1):
   data[route[i][1]][ route[i][0]] = '#'

#Flood rest of the map
for tkn in ['I', 'O']:
    changes = 10
    while(changes > 0):    

        changes = 0
        for y in range(y_max):
            for x in range(x_max):
                if data[y][x] == tkn:
                    for yt in [y-1, y, y+1]:
                        for xt in [x-1, x, x+1]:
                            if yt >= 0 and yt < y_max and xt >= 0 and xt < x_max:
                                if data[yt][xt] not in ['#', 'O', 'I']:
                                    changes += 1
                                    data[yt][xt]  = tkn


#Count inner and outer
inner_cnt = 0
outer_cnt = 0
for y in range(y_max):
    for x in range(x_max):
         if data[y][x] == 'O':
            outer_cnt +=1 

         if data[y][x] == 'I':
            inner_cnt +=1 

#Print map
for y in range(y_max):
    for x in range(x_max):   
        print(data[y][x], end='')
    print()
    #Print map
    for y in range(y_max):
        for x in range(x_max):   
            print(data[y][x], end='')
        print()
print('Inner tiles:', inner_cnt)
print('Outer tiles:', outer_cnt)
            

