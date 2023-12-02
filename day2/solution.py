data = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

game_config = {'red': 12, 'green': 13, 'blue': 14}

total_id = 0
total_power = 0
for line in data.strip().splitlines():
    
    game, sets = line.split(': ')

    game_id = int(game.split(' ')[1])
    min_game_config = {'red': 0, 'green': 0, 'blue': 0}

    for s in sets.split(';'):
        for num_color in s.strip().split(','):

            num, color = num_color.strip().split(' ')
            if int(num) > game_config[color]:                
                game_id = 0
                
            if int(num) > min_game_config[color]:
                min_game_config[color] = int(num)

    power = min_game_config['red']*min_game_config['green']*min_game_config['blue']      
    print(min_game_config, power)
    
    total_id += game_id
    total_power += power

print('ID sum:', total_id)
print('Power sum:', total_power)
