data = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

#Load the data
f = open('data.txt', 'r')
data = f.read()
f.close()

data = data.strip().splitlines()

#Label card hand function
def hand_type(hand):

    hand = sorted(hand)

    #Five of a kind
    if all(c == hand[0] for c in hand):
        return 1 #'Five of a kind'

    #Four of a kind
    if all(c == hand[0] for c in hand[:4]) or all(c == hand[1] for c in hand[1:]):
            return 2 # 'Four of a kind'

    #Full-house // Three of a kind
    first_three = all(c == hand[0] for c in hand[:3])
    mid_three =  all(c == hand[1] for c in hand[1:4])
    last_three = all(c == hand[2] for c in hand[2:])

    if first_three or mid_three or last_three:

        if first_three and hand[3] == hand [4] or last_three and hand[0] == hand [1]:
            return 3 #'Full house'
        else:
            return 4 #'Three of a kind'

    #Two pair
    if len(set(hand)) == 3:
        return 5 #'Two pair'

    #One pair
    if len(set(hand)) == 4:
        return 6 #'One pair'

    #High card
    if len(set(hand)) == 5:
            return 7 #'High'
    

    return 0 #'HAND!'

#Label the card types
cards = []
hand_map = {'A':'A', 'K':'B', 'Q':'C', 'J':'Z', 'T':'E', '9':'F', '8':'G', '7':'H', '6':'I', '5':'J', '4':'K', '3':'L', '2':'M'}
for i, line in enumerate(data):

    #Retrieve data
    hand = line.strip().split(' ')[0]
    bid = line.strip().split(' ')[1]

    #Get all joker card combinations
    joker_hands = [hand]
    if 'J' in hand:
        colors = set(list(hand))
        colors.remove('J')
        joker_hands.extend( [*[hand.replace('J', i) for i in colors]])

    #Consider all joker card combinations and find best type
    best_type = 10
    for h in joker_hands:
        new_hand = ""
        for j ,_ in enumerate(h):
            new_hand += hand_map[h[j]]
        
        h_type = hand_type(new_hand)
        if h_type < best_type:
            best_type = h_type
            best_new_hand = new_hand

    #Map the original hand to new values for sorting algorithm
    new_hand = ""
    for j ,_ in enumerate(h):
                new_hand += hand_map[hand[j]]

    #Store this card information
    cards.append({'orig': hand, 'hand': new_hand, 'bid': bid, 'type': best_type})

#Sort the cards
cards = sorted(cards, key=lambda k: (k['type'], *[k['hand'][i] for i in range(5)]), reverse=True)

#Count the winnings
total_winnings = 0
for i, card in enumerate(cards):

    total_winnings += int(card['bid'])*(i+1)

print('Total winnings:', total_winnings)
