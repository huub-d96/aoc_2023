data = '''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data=data.strip().splitlines()

total_points = 0
copies = [1 for _ in range(len(data))]
for card, line in enumerate(data):
    win_nums, my_nums = line.split('|')

    win_nums = [int(i) for i in win_nums.split(':')[1].strip().split(' ') if i]
    my_nums = [int(i) for i in my_nums.strip().split(' ') if i]

    n_wins = 0
    for n in my_nums:
        n_wins += 1 if n in win_nums else 0

    if n_wins > 0:
        #Part 1
        total_points += 2**(n_wins-1)

        #Part 2
        for j in range(n_wins):
            copies[card+j+1] += copies[card]

print('Total points:', total_points)
print('Total cards:', sum(copies))
