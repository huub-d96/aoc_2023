import math

data ='''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''

data ="""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

data1='''
broadcaster -> a, b
%a -> con
%b -> con
&con -> rx
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = [line for line in data.strip().splitlines() if line]

#Build network
modules = {}
for line in data:

    module, targets = line.split(' -> ')
    targets = [target for target in targets.split(', ')]

    if module[0] == '%':
        module = module[1:]
        if module not in modules.keys():
            modules[module] = {'type': 'FF',
                               'on': False,
                               'outputs': targets}
        else:
            modules[module]['outputs'] = modules[module]['outputs'].extend(targets)

    elif module[0] == '&':
        module = module[1:]
        if module not in modules.keys():
            modules[module] = {'type': 'CONJ',
                                'mem': {},
                                'outputs': targets}
        else:
            modules[module]['outputs'] = modules[module]['outputs'].extend(targets)

    else:
        if module not in modules.keys():
            modules[module] = {'type': 'BROADCASTER','outputs': targets}
        else:
            modules[module]['outputs'] = modules[module]['outputs'].extend(targets)

    



#Generate memory
for m in modules.keys():

    for out in modules[m]['outputs']:

        if out in modules.keys():
            if modules[out]['type'] == 'CONJ':
                modules[out]['mem'][m] = 'L'

#Print modules
#print(modules)

#Simulate signals
lows = 0
highs = 0

end_mods = {m:0 for m in modules.keys() if 'rs' in modules[m]['outputs']}

for presses in range(10000):

    sig_queue = [['button', 'broadcaster', 'L']]

    while(sig_queue):

        sig = sig_queue.pop(0)

        if sig[1] in modules.keys():

            mod_from = sig[0]
            mod_to = modules[sig[1]]
            pulse = sig[2]


            if mod_to['type'] == 'FF':
                if pulse == 'L':

                    #Set output signal
                    if mod_to['on']:
                        sig_out = 'L'
                    else:
                        sig_out = 'H'    

                    #Set outputs
                    for output in mod_to['outputs']:
                        sig_queue.append([sig[1], output, sig_out])                           

                    #Toggle module
                    mod_to['on'] = not mod_to['on']

            elif mod_to['type'] == 'CONJ':
                if pulse in ['L', 'H']:
            
                    #Update memory
                    mod_to['mem'][mod_from] = pulse
                                        
                    if all(mem=='H' for mem in mod_to['mem'].values()):
                        sig_out = 'L'
                    else:
                        sig_out = 'H'

                    #Set outputs
                    for output in mod_to['outputs']:
                        sig_queue.append([sig[1], output, sig_out])

            elif mod_to['type'] == 'BROADCASTER': 
                if pulse in ['L', 'H']:
                    sig_out = pulse

                    #Set outputs
                    for output in mod_to['outputs']:
                        sig_queue.append([sig[1], output, sig_out])

            else:
                print('QUE?')
                

        
        #print(f'{sig[0]} -{sig[2]} -> {sig[1]}')

        if sig[1] == 'rs' and sig[2] == 'H':
            if end_mods[sig[0]] == 0:
                end_mods[sig[0]] = presses + 1

        if presses < 1000:
            if sig[2] == 'H':
                highs += 1
            elif sig[2] == 'L':
                lows += 1
            

        #print(sig_queue)

    #print()

print('Part 1:', lows*highs)
print('Part 2:', math.lcm(*end_mods.values()))

#for k,v  in modules.items():
#    print(k,v)
