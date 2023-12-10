data = '''
Time:      7  15   30
Distance:  9  40  200
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = data.strip().splitlines()

#Part 1
tt = [int(i) for i in data[0].split(':')[1].split(' ') if i]
dd = [int(i) for i in data[1].split(':')[1].split(' ') if i]

#Part 2
tt = dd = ''
for i in data[0].split(':')[1].split(' '):
    tt += i if i else ''
    
for i in data[1].split(':')[1].split(' '):
    dd += i if i else ''

tt = [int(tt)]
dd = [int(dd)]
print(tt)
print(dd)

mult = 1
for i in range(len(tt)):

    t = tt[i]
    d = dd[i]
    wins = 0

    for ms in range(t+1):

        dist = (t-ms)*ms
        if dist > d:
            wins += 1

    print('wins:', wins)
    mult *= wins

print(mult)
