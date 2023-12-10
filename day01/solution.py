import re

data = '''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

total = 0
nums = {'one': '1', 'two': '2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
for line in data.splitlines():

    if line:
        match_string = r'(?=(\d|'+'|'.join(nums.keys())+'))'
        match = re.findall(match_string, line)

        l = match[0] if match[0].isdigit() else nums[match[0]]
        r = match[-1] if match[-1].isdigit() else nums[match[-1]]

        n = int(l+r)
        total += n   
        
        
print(total)
