import copy

data ='''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = [line for line in data.strip().splitlines() if line]

parts = [line[1:-1] for line in data if line[0] == '{']
workflows = {line.split('{')[0]:line.split('{')[1][:-1] for line in data if line[0].isalpha()}

total = 0
for part_set in parts:

    for part in part_set.split(','):
        exec(part)   

    flow_tag = 'in'
    run = True
    while(run):
    
        workflow = workflows[flow_tag]

        instructions = workflow.split(',')

        for inst in instructions:

            if ':' in inst:
                comp, result = inst.split(':')
                test = eval(comp)
                if not test:
                    continue
            else:
                result = inst

            if result == 'A':
                total += x+m+a+s
                run = False
                break
            elif result == 'R':
                run = False
                break
            else:
                flow_tag = result
                break
    
print('Part 1:', total)

###Part 2###

accepted_combs = []
def check_parts(tag, parts):

    workflow = workflows[tag]
    instructions = workflow.split(',')
    parts_left = copy.deepcopy(parts)
        
    for inst in instructions:        
        parts_pass = copy.deepcopy(parts_left)
        
        #Comparison
        if ':' in inst:
            comp, result = inst.split(':')            

            if '>' in comp:

                item, value = comp.split('>')

                if parts_left[item][1] > int(value):
                    parts_pass[item][0] = max(parts_pass[item][0], int(value)+1)
                    
                    if result == 'A':
                        accepted_combs.append(parts_pass)
                    elif result == 'R':
                        pass
                    else:         
                        check_parts(result, parts_pass)

                    if parts_left[item][0] <= int(value):
                        parts_left[item][1] = int(value)    
            else:
                item, value = comp.split('<')

                if parts_left[item][0] < int(value):
                    parts_pass[item][1] = min(parts_pass[item][1], int(value)-1)
                        
                    if result == 'A':
                        accepted_combs.append(parts_pass)
                    elif result == 'R':
                        pass
                    else:
                        check_parts(result, parts_pass)

                    if parts_left[item][1] >= int(value):
                        parts_left[item][0] = int(value)
        #endpoint        
        else:
            result = inst

            if result == 'A':
                accepted_combs.append(parts_left)
            elif result == 'R':
                pass
            else:
                check_parts(result, parts_left)


check_parts('in', {'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]})

total_ways = 0
for c in accepted_combs:
    ways = 1
    for item in c.keys():
        ways *= c[item][1] - c[item][0] + 1
    total_ways += ways

print('Part 2:', total_ways)
