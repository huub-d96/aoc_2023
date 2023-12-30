import copy
from heapq import heappop, heappush as push
data = '''
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''

#Load the data
f = open('data.txt', 'r')
#data = f.read()
f.close()

G = {i + j*1j: int(c) for i,r in enumerate(data.strip().splitlines()) for j,c in enumerate(r.strip())}

def f(min, max, end=[*G][-1], x=0):
    todo = [(0,0,0,1), (0,0,0,1j)]
    seen = set()

    while todo:
        val, x_val, pos, dir = heappop(todo)

        if (pos==end): 
            print(val, x_val, pos, dir)
            return val
            
        if (pos, dir) in seen: 
            continue


        seen.add((pos,dir))

        for d in 1j/dir, -1j/dir:
            for i in range(min, max+1):
                if pos+d*i in G:
                    v = sum(G[pos+d*j] for j in range(1,i+1))
                    push(todo, (val+v, (x:=x+1), pos+d*i, d))

print(f(1, 3), f(4, 10))
