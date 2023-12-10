from math import gcd

data = '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = data.strip().splitlines()

directions = data[0].strip()

nodes = {}
for line in data[2:]:

    source, dest = line.strip().split(' = ')
    l, r = dest.translate({ord('('): None, ord(')'): None}).split(', ')
    nodes[source] = [l, r]

#print(nodes)

#Part 1
cur_node = 'AAA'
step = 0
while(cur_node != 'ZZZ'):

    direction = directions[step % len(directions)]
    
    next_node = nodes[cur_node][0 if direction == 'L' else 1]

    cur_node = next_node
    step += 1
    
print('Part 1:', step)

#Part 2
#Find steps for each starting point
cur_nodes = [n for n in nodes.keys() if n[2]=='A']

steps_needed = []
for cur_node in cur_nodes:
    step = 0
    while(cur_node[2] != 'Z'):

        direction = directions[step % len(directions)]
        
        next_node = nodes[cur_node][0 if direction == 'L' else 1]

        cur_node = next_node
        step += 1

    steps_needed.append(step)
    
#Compute least common multiple
lcm = 1
for i in steps_needed:
    lcm = lcm*i//gcd(lcm, i)

print('Part 2:', lcm)
