data = '''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
42 0 7
57 7 4
0 11 42

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data=data.strip().splitlines()

seeds = [int(i) for i in data[0].split(':')[1].strip().split(' ') if i]


# Retrieve maps
maps = []
map = []
for line in data[1:]:

    if line and line[0].isdigit():
        map.append([int(i) for i in line.split(' ') if i])

    elif map and line:
        maps.append(map)
        map = []

if map:
    maps.append(map)

#print(seeds)
#Convert
'''
new_seeds = list(range(seeds[0], seeds[0]+seeds[1]))
print(new_seeds)    
for map in maps:

    for idx in range(len(new_seeds)):

        seed = new_seeds[idx]
        for ranges in map:
        
            d, s, r = ranges

            if seed >= s and seed < s+r:
                new_seeds[idx] += d - s 
                break

    print(new_seeds)         

print('Minimum1:', min(new_seeds))
'''

mins = []
for p_id in range(0, len(seeds), 2):

    print(f'\nPair {p_id//2}')
    s_min = seeds[p_id]
    s_max = seeds[p_id] + seeds[p_id+1] -1

    pairs = [[s_min, s_max]]

    
       
    for map in maps:

        breakpoints = []
        for r in map:
            breakpoints.append(r[1])
            breakpoints.append(r[1]+r[2])
        
        breakpoints = list(set(breakpoints))
        breakpoints.sort()
        #print(breakpoints)

        new_pairs = []
        for i in range(len(pairs)):
            p_min = pairs[i][0]
            p_max = pairs[i][1]
            cur_breaks = [p_min]

            for b in breakpoints:                
                if b > pairs[i][0] and b <= pairs[i][1]:
                    cur_breaks.append(b)

            cur_breaks.append(p_max+1)
            for b_idx in range(len(cur_breaks)-1):
                new_pairs.append([cur_breaks[b_idx], cur_breaks[b_idx+1]-1])
         
        pairs = new_pairs.copy()
                                
        #print(pairs) 
        for i in range(len(pairs)):
            new_seeds = pairs[i].copy()       
        
            for idx in range(len(new_seeds)):
        
                seed = new_seeds[idx]
                for ranges in map:
                
                    d, s, r = ranges
        
                    if seed >= s and seed < s+r:
                        new_seeds[idx] += d - s 
                        break                       

            pairs[i] = new_seeds
        #print(pairs)
    print(min([p[0] for p in pairs]))
    mins.append(min([p[0] for p in pairs]))
       

print('Minimum2:', min(mins), '\n')


    

    
    

