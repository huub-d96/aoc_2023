data ="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = data.strip().split(',')


def hash256(chars):
    
    current = 0
    for c in chars:
        current += ord(c)
        current *= 17
        current = current % 256
        
    return current

total = 0
boxes = [[] for _ in range(256)]


def print_boxes():
    for i, box in enumerate(boxes):
        if box:
            print(f'Box {i}: {box}')
    print()

def calc_power():
    power = 0
    for i, box in enumerate(boxes):
        if box:
            for j, l in enumerate(box):
                power += (i+1)*(j+1)*int(l[1])

    return power

for seq in data:

    if '=' in seq:
        label, lens = seq.split('=')
        hash_label = hash256(label)
        #print(hash_label)

        replacement = False
        for i, parts in enumerate(boxes[hash_label]):
            if parts[0] == label:
                replacement = True
                boxes[hash_label][i] = [label, lens]
        
        if not replacement:
            boxes[hash_label].append([label, lens])

    else:
        label = seq.split('-')[0]
        hash_label = hash256(label)
        
        for i, parts in enumerate(boxes[hash_label]):
            if parts[0] == label:
                del boxes[hash_label][i]

    #print(f'After {seq}')    
    #print_boxes()
    total += hash256(seq)

print('Part 1:', total)
print('Part 2:', calc_power())
