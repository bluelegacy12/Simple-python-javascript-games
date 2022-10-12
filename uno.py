import random
from time import sleep
from sys import exit
# ^ for exit function

#set up global variables
player_hand = []
player2_hand = []
jack_hand = []
jill_hand = []
discard = []
color = ''
current_hand = []
current_player = []
prev_card = ''
player = ''
options = ('Red', 'Yellow', 'Green', 'Blue')
# line is purely for visual consistency
line = '-----------------------------------------------------------------\n'

# searched the exact number of each card in uno and created a list to contain them
deck = ['Wild Card', 'Wild Card', 'Wild Card', 'Wild Card', 'Wild Draw Four', 'Wild Draw Four', 'Wild Draw Four', 'Wild Draw Four', 'Red 0', 'Red 1', 'Red 1', 'Red 2', 'Red 2', 'Red 3', 'Red 3', 'Red 4', 'Red 4', 'Red 5', 'Red 5', 'Red 6', 'Red 6', 'Red 7', 'Red 7', 'Red 8', 'Red 8', 'Red 9', 'Red 9', 'Red Skip', 'Red Skip', 'Red Reverse', 'Red Reverse', 'Red Draw Two', 'Red Draw Two', 'Blue 0', 'Blue 1', 'Blue 1', 'Blue 2', 'Blue 2', 'Blue 3', 'Blue 3', 'Blue 4', 'Blue 4', 'Blue 5', 'Blue 5', 'Blue 6', 'Blue 6', 'Blue 7', 'Blue 7', 'Blue 8', 'Blue 8', 'Blue 9', 'Blue 9', 'Blue Skip', 'Blue Skip', 'Blue Reverse', 'Blue Reverse', 'Blue Draw Two', 'Blue Draw Two', 'Green 0', 'Green 1', 'Green 1', 'Green 2', 'Green 2', 'Green 3', 'Green 3', 'Green 4', 'Green 4', 'Green 5', 'Green 5', 'Green 6', 'Green 6', 'Green 7', 'Green 7', 'Green 8', 'Green 8', 'Green 9', 'Green 9', 'Green Skip', 'Green Skip', 'Green Reverse', 'Green Reverse', 'Green Draw Two', 'Green Draw Two', 'Yellow 0', 'Yellow 1', 'Yellow 1', 'Yellow 2', 'Yellow 2', 'Yellow 3', 'Yellow 3', 'Yellow 4', 'Yellow 4', 'Yellow 5', 'Yellow 5', 'Yellow 6', 'Yellow 6', 'Yellow 7', 'Yellow 7', 'Yellow 8', 'Yellow 8', 'Yellow 9', 'Yellow 9', 'Yellow Skip', 'Yellow Skip', 'Yellow Reverse', 'Yellow Reverse', 'Yellow Draw Two', 'Yellow Draw Two']

def new_game():
    global deck
    global jack_hand
    global jill_hand
    global player_hand
    global player2_hand
    global discard
    global current_hand
    global current_player
    global line
    global prev_card
    global options
    global player
    
    while True:
        try:
            multiplayer = int(input('Welcome to Uno! How many players will be participating? 1 or 2? '))
        except:
            print('\nInput must be an integer.\n')
        else:
            if multiplayer > 0 and multiplayer < 3:
                break
            print('\nInvalid number of players. Must be a number between 1 and 2.\n')
    print(f'\nYou have chosen a {multiplayer}-player game. You will be playing a game with your opponents, Jack and Jill!')
    while True:
        player = input('\nWhat is the name of player 1? ')
        if player.lower() == 'jack' or player.lower() == 'jill':
            print('\nThat name is already taken, please use a different name.')
            continue
        break
    if multiplayer == 2:
        while True:
            player2 = input('\nAnd player 2? ')
            if player2.lower() == 'jack' or player2.lower() == 'jill' or player2.lower() == player.lower():
                print('\nThat name is already taken, please use a different name.')
                continue
            break
    while True:
        see_all = input("\nWould you like to see your computer opponents' hand as you play? Yes or no: ").lower()
        if see_all[0] == 'y':
            print("\nYou have chosen to see your opponents' hand.\n")
            break
        if see_all[0] == 'n':
            print("\nYou have chosen not to see your opponents' hand.\n")
            break
        print('Invalid option. Please type yes or no')
    sleep(1.5)
    print('Let the games begin!')
    sleep(1)
    random.shuffle(deck)

    # deal cards to every hand
    while len(player_hand) < 5:
        jack_hand.append(deck[0])
        deck.pop(0)
        if multiplayer == 2:
            player2_hand.append(deck[0])
            deck.pop(0)
        jill_hand.append(deck[0])
        deck.pop(0)
        player_hand.append(deck[0])
        deck.pop(0)
    discard.append(deck[0])
    deck.pop(0)
    sleep(1.5)
    print(f'\nThe top card is: {discard[0]}\n')
    # handle color selection if first card is wild
    if 'Wild' in discard[0]:
        color = random.choice(options)
        sleep(1.5)
        print(f'The color is chosen randomly. The color is: {color}\n')
        discard[0] = color
    current_player = [player, 'Jack', 'Jill']
    if multiplayer == 2:
        current_player.insert(2, player2)
    sleep(1.5)
    print(f'The turn order is: {current_player}\n')
    while True:
        if see_all[0] == 'y':
            print(line)
            sleep(1.5)
            print(f"Jack's hand: {jack_hand}")
            print(f"Jill's hand: {current_hand}\n")
        # handle special effect cards and prevent them from repeating on subsequent turns if it is still at top of discard
        if 'Skip' in discard[0]:
            prev_card = discard[0]
            discard[0] = discard[0][0] + discard[0][-1]
            print(f'{current_player[0]} was skipped!\n')
            current_player.append(current_player[0])
            current_player.pop(0)
            continue
        if 'Two' in discard[0]:
            draw(current_player[0], 2)
            prev_card = discard[0]
            discard[0] = discard[0][0] + discard[0][-1]
        if current_player[0] == 'Jack':
            current_hand = jack_hand
        elif current_player[0] == 'Jill':
            current_hand = jill_hand
        elif current_player[0] == player:
            current_hand = player_hand
        else:
            current_hand = player2_hand
        print(line)
        sleep(1.5)
        take_turn(current_player[0])
        # check for uno and win condition
        if len(current_hand) == 1:
            sleep(1.5)
            print(f'UNO! {current_player[0]} has one card left!\n')
        if len(current_hand) == 0:
            sleep(1.5)
            print(f'Game Over! {current_player[0]} has won the game!')
            sleep(1.5)
            return
        # handle reverse card
        if 'Reverse' in discard[0]:
            current_player.reverse()
            prev_card = discard[0]
            discard[0] = discard[0][0] + discard[0][-1]
            continue
        # handle empty deck
        if len(deck) == 0:
            deck = ['Wild Card', 'Wild Card', 'Wild Card', 'Wild Card', 'Wild Draw Four', 'Wild Draw Four', 'Wild Draw Four', 'Wild Draw Four', 'Red 0', 'Red 1', 'Red 1', 'Red 2', 'Red 2', 'Red 3', 'Red 3', 'Red 4', 'Red 4', 'Red 5', 'Red 5', 'Red 6', 'Red 6', 'Red 7', 'Red 7', 'Red 8', 'Red 8', 'Red 9', 'Red 9', 'Red Skip', 'Red Skip', 'Red Reverse', 'Red Reverse', 'Red Draw Two', 'Red Draw Two', 'Blue 0', 'Blue 1', 'Blue 1', 'Blue 2', 'Blue 2', 'Blue 3', 'Blue 3', 'Blue 4', 'Blue 4', 'Blue 5', 'Blue 5', 'Blue 6', 'Blue 6', 'Blue 7', 'Blue 7', 'Blue 8', 'Blue 8', 'Blue 9', 'Blue 9', 'Blue Skip', 'Blue Skip', 'Blue Reverse', 'Blue Reverse', 'Blue Draw Two', 'Blue Draw Two', 'Green 0', 'Green 1', 'Green 1', 'Green 2', 'Green 2', 'Green 3', 'Green 3', 'Green 4', 'Green 4', 'Green 5', 'Green 5', 'Green 6', 'Green 6', 'Green 7', 'Green 7', 'Green 8', 'Green 8', 'Green 9', 'Green 9', 'Green Skip', 'Green Skip', 'Green Reverse', 'Green Reverse', 'Green Draw Two', 'Green Draw Two', 'Yellow 0', 'Yellow 1', 'Yellow 1', 'Yellow 2', 'Yellow 2', 'Yellow 3', 'Yellow 3', 'Yellow 4', 'Yellow 4', 'Yellow 5', 'Yellow 5', 'Yellow 6', 'Yellow 6', 'Yellow 7', 'Yellow 7', 'Yellow 8', 'Yellow 8', 'Yellow 9', 'Yellow 9', 'Yellow Skip', 'Yellow Skip', 'Yellow Reverse', 'Yellow Reverse', 'Yellow Draw Two', 'Yellow Draw Two']
            last_card = discard[0]
            discard.clear()
            discard.append(last_card)
            for card in jack_hand:
                for i in deck:
                    if card == i:
                        deck.pop(deck.index(i))
                        break
            for card in jill_hand:
                for i in deck:
                    if card == i:
                        deck.pop(deck.index(i))
                        break
            for card in player_hand:
                for i in deck:
                    if card == i:
                        deck.pop(deck.index(i))
                        break
            for card in player2_hand:
                for i in deck:
                    if card == i:
                        deck.pop(deck.index(i))
                        break
            for i in deck:
                if last_card == i:
                    deck.pop(deck.index(i))
                    break
            random.shuffle(deck)
            sleep(1.5)
            print('\nThe deck ran out of cards! The discard pile has now been reshuffled back into the deck.\n')
        # shift order
        current_player.append(current_player[0])
        current_player.pop(0)

def take_turn(str):
    global jack_hand
    global jill_hand
    global player_hand
    global player2_hand
    global discard
    global color
    global prev_card
    global current_hand
    global current_player
    global player

    if str == 'Jack' or str == 'Jill':
        # need an index variable to apply to pop function
        i = 0
        for card in current_hand:
            if card[0] == discard[0][0] or card[-1] == discard[0][-1] or 'Wild' in card:
                # handle the isolated scenario of a wild card selecting Blue as top discard and playing wrong color reverse because of both ending with 'e'
                if discard[0] == 'Blue' and 'Blue' not in card and 'Wild' not in card:
                    continue
                discard.insert(0, card)
                current_hand.pop(i)
                print(f'{current_player[0]} played a {discard[0]}\n')
                if 'Wild' in discard[0]:
                    if discard[0] == 'Wild Draw Four':
                        draw(current_player[1], 4)
                    discard[0] = select_color()
                    sleep(1.5)
                    print(f'{current_player[0]} has chosen the color: {discard[0]}\n')
                return
            i += 1
        draw(current_player[0], 1)
        return
    else:
        if str[-1].lower() == 's':
            print(f"{str}' turn!\n")
        else:
            print(f"{str}'s turn!\n")
        # print the current face-up card unless it is an altered face card with its name changed to prevent repeat effects
        if len(discard[0]) > 3 or discard[0] == 'Red':
            print(f"Face-up card: {discard[0]}\n")
        else:
            print(f"Face-up card: {prev_card}\n")
        if str[-1].lower() == 's':
            print(f"{str}' hand: {current_hand}\n")
        else:
            print(f"{str}'s hand: {current_hand}\n")
        while True:
            i = 0
            play = input("Choose a card from your hand, or type 'draw' to take a card and skip your turn: ").lower()
            if play == 'exit':
                print('\nYou have forfeit the game. See you next time!')
                exit()
            if play == 'draw':
                print('')
                draw(current_player[0], 1)
                return
            if play == 'order':
                print(f'\nThe turn order is: {current_player}\n')
                continue
            for card in current_hand:
                if play == card.lower():
                    if card[0] == discard[0][0] or card[-1] == discard[0][-1] or 'Wild' in card:
                        # handle isolated scenario - notes near line 197
                        if discard[0] == 'Blue' and 'Blue' not in card and 'Wild' not in card:
                            continue
                        discard.insert(0, card)
                        current_hand.pop(i)
                        print(f'\n{str} played a {discard[0]}\n')
                        if 'Wild' in discard[0]:
                            if discard[0] == 'Wild Draw Four':
                                draw(current_player[1], 4)
                            discard[0] = select_color()
                            sleep(1.5)
                            print(f'\n{current_player[0]} has chosen the color: {discard[0]}\n')
                        return    
                i += 1    
            print('\nInvalid play. Pick a card in your hand that matches the color or face of the top card in the discard.\nYou can also type "order" to see the turn order, or "exit" to quit.\n')
            
def draw(player_draw, num):
    global player_hand
    global player2_hand
    global jack_hand
    global jill_hand
    global discard
    global deck
    global current_player
    global player
    
    if player_draw == 'Jack':
        for i in range(0, num, 1):
            if len(deck) == 0:
                break
            jack_hand.append(deck[0])
            deck.pop(0)
    elif player_draw == 'Jill':
        for i in range(0, num, 1):
            if len(deck) == 0:
                break
            jill_hand.append(deck[0])
            deck.pop(0)
    elif player_draw == player:
        for i in range(0, num, 1):
            if len(deck) == 0:
                break
            player_hand.append(deck[0])
            deck.pop(0)
    else:
          for i in range(0, num, 1):
            if len(deck) == 0:
                break
            player2_hand.append(deck[0])
            deck.pop(0)
    print(f'{player_draw} draw(s) {num} cards!\n')
    
def select_color():
    global discard
    global current_player
    global current_hand
    global options
    
    if current_player[0] == 'Jack' or current_player[0] == 'Jill':
        for color in current_hand:
            if color[0] == 'R':
                return 'Red'
            if color[0] == 'B':
                return 'Blue'
            if color[0] == 'G':
                return 'Green'
            if color[0] == 'Y':
                return 'Yellow'
        return random.choice(options)        
    else:
        while True:
            pick_color = input('Choose a color: ').lower()
            for color in options:
                if pick_color == color.lower():
                    return color
            print('\nInvalid color option.\n')
            
new_game()
