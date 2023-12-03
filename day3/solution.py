data = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data=data.strip().splitlines()

y_max = len(data) - 1
x_max = len(data[0]) - 1

#Part 1
valid_map = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]
kernel = [-1,0,1]

#Map which field mark valid numbers
for y in range(y_max+1):
    for x in range(x_max+1):
        if not(data[y][x].isdigit() or data[y][x] == '.'):
            for i in kernel:
                for j in kernel:
                    y_draw = y+i
                    x_draw = x+j

                    if y_draw >= 0 and y_draw <= y_max and x_draw >= 0 and x_draw <= x_max:
                        valid_map[y_draw][x_draw] = '#'

#Find numbers in schematic and add if valid
total = 0
for y in range(y_max+1):
    num = ""
    valid = False
    for x in range(x_max+1):

        if data[y][x].isdigit():
            num += data[y][x]
            if valid_map[y][x] == '#':
                valid = True
        
        if (not data[y][x].isdigit() or x == x_max) and num:
            
            if valid:
                total += int(num)
                valid=False            
            num = ""
            
            

print('Part sum:', total)

#Part 2
def find_nums(map):
    nums = []
    for y in range(y_max+1):
        num = ""
        valid = False
        for x in range(x_max+1):

            if data[y][x].isdigit():
                num += data[y][x]
                if map[y][x] == '#':
                    valid = True
            
            if (not data[y][x].isdigit() or x == x_max) and num:
                
                if valid:
                    nums.append(int(num))
                    valid=False            
                num = ""

    return nums

total = 0
for y in range(y_max+1):
    for x in range(x_max+1):
        if data[y][x] == '*':
            valid_map = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]
            for i in kernel:
                for j in kernel:
                    y_draw = y+i
                    x_draw = x+j

                    if y_draw >= 0 and y_draw <= y_max and x_draw >= 0 and x_draw <= x_max:
                        valid_map[y_draw][x_draw] = '#'

            nums = find_nums(valid_map)

            if len(nums) == 2:
                total += nums[0]*nums[1]
            
print('Gearbox ratio sum:', total)
