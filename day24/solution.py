import numpy as np
import math
from sympy.solvers import solve
from sympy import Symbol

data ='''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()


equations = []
for line in data.strip().splitlines():

    ps, vs = line.split(' @ ')
    px, py, pz = [int(s) for s in ps.split(', ')]
    vx, vy, vz = [int(s) for s in vs.split(', ')]

    #print(px, py, pz, vx, vy, vz)

    equations.append({'p0':[px, py, pz], 'v':[vx, vy, vz]})

test_min = 200000000000000
test_max = 400000000000000
count = 0
for i in range(len(equations)):
    for j in range(i+1, len(equations)):
        eq1 = equations[i]
        eq2 = equations[j]

        #print(eq1)
        #print(eq2)

        v1 = np.array(eq1['v'][:2]).T
        c1 = np.array(eq1['p0'][:2]).T
        v2 = np.array(eq2['v'][:2]).T
        c2 = np.array(eq2['p0'][:2]).T
        
        # in this case the solved x is [-1.  1.], error is 0, and rank is 2
        x, err, rank = np.linalg.lstsq(np.array([v1, -v2]).T, c2-c1, rcond=None)[:3]

        # Check if intersection exists
        if rank == 2:           

            # Intersection in the future
            if x[0] > 0 and x[1] > 0:
                cross = v1 * x[0] + c1
                if test_min < cross[0] < test_max and test_min < cross[1] < test_max:  
                    count += 1
    
print(f'There are {count} crossings in the test area')

#Part 2
px = Symbol('px')
py = Symbol('py')
pz = Symbol('pz')
vx = Symbol('vx')
vy = Symbol('vy')
vz = Symbol('vz')

# Create equations to solve, we need at least three points to make sure that all
# points are on the same line
eqs = []
for eq in [equations[0], equations[1], equations[2]]:
    x1, y1, z1 = eq['p0']
    vx1, vy1, vz1 = eq['v']

    eqs.extend([
    (x1 - px)*(vy - vy1) - (y1 - py)*(vx - vx1), 
    (x1 - px)*(vz - vz1) - (z1 - pz)*(vx - vx1),  
    (y1 - py)*(vz - vz1) - (z1 - pz)*(vy - vy1),    
    ])

solution = solve(eqs, [px, py, pz, vx, vy, vz])
print('Solution part 2:', sum(solution[0][:3]))

