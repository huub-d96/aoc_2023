import functools

data ='''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Format data to list of lists
data =  data.strip().splitlines()

total = 0

@functools.lru_cache(maxsize=None) #Today I learned to cache
def calc_arrangements(springs, groups):

    #Exit conidtion if we run out of groups
    if not groups:
        return 1 if '#' not in springs else 0

    #Exit if we run out of springs to check
    if not springs:
        return 0
    
    def fit_block():

        block = springs[:groups[0]]
        block = block.replace('?','#')

        #Check if blocks fit exactly into group
        if block.count('#') != groups[0]:
            return 0

        #Check for last group
        if len(springs) == groups[0]:
            return 1 if len(groups) == 1 else 0

        if springs[groups[0]] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return calc_arrangements(springs[groups[0]+1:], groups[1:])

        return 0

    #Choose your path! 
    if springs[0] == '#':
        return fit_block()
    elif springs[0] == '.':
        return calc_arrangements(springs[1:], groups)
    elif springs[0] == '?':
        return fit_block() + calc_arrangements(springs[1:], groups)
    else:
        print('Que?')
    
    return output

total = 0
for line in data:

    #Parse data
    springs, groups = line.split(' ')
    groups = tuple([int(i) for i in groups.split(',')]*5)

    #Hacky way to put the springs together, but I'm done with the puzzle
    springs = springs+'?'+springs+'?'+springs+'?'+springs+'?'+springs

    #Calculate number of possible arrangements
    arrangements = calc_arrangements(springs, groups)
    total += arrangements

print('Total arrangements:', total)
    

   
