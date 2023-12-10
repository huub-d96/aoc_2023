data = '''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

#Format data to list of ints
data = [[int(i) for i in line.split(' ')] for line in data.strip().splitlines()]

#Recursive function to predict the next input from a list
def predict(vals):

    if len(set(vals)) == 1:
        return vals[0]

    diffs = [vals[i+1]-vals[i] for i in range(len(vals)-1)]

    return vals[-1] + predict(diffs)

#Part 1
total = 0
for d in data:
    prediction = predict(d)
    total += prediction

print('Part 1:', total)

#Part 2: Just invert the list
total = 0
for d in data:
    prediction = predict(d[::-1])
    total += prediction

print('Part 2:', total)
