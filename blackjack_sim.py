'''blackjack sim with insurance bets only (so far...)
        to be continued: card-counting and probabilities?'''
'''Note to future self: 
when calcing probabilities of winning: remember that first card to the house is unknown to rest of players.'''

import random

class Player:
    instances = []
    def __init__(self, name, cards, cards_str, insurance):
        self.name = name
        self.cards = cards
        self.cards_str = cards_str
        self.insurance = insurance
        Player.instances.append(self)
    
    def __str__(self):
        return f"Player: name='{self.name}' , cards= {self.cards} , insurance = {self.insurance}"
    
    def cards_string(self):
        self.cards_str = self.cards
        self.cards_str = ['Ace' if x=='a' else x for x in self.cards_str]
        self.cards_str = ['10' if x=='0' else x for x in self.cards_str]
        self.cards_str = ['Jack' if x=='j' else x for x in self.cards_str]
        self.cards_str = ['Queen' if x=='q' else x for x in self.cards_str]
        self.cards_str = ['King' if x=='k' else x for x in self.cards_str]
        return self.cards_str

    @classmethod
    def check_insurance(cls, insurance_check):
        return [obj for obj in cls.instances if obj.insurance == insurance_check]
    
    '''add a 'split' function'''
    '''def split(self):
            insert card at next hit in between cards'''
    
players = []
house =   Player('',[],[],'3')
player1 = Player('',[],[],'3')
player2 = Player('',[],[],'3')
player3 = Player('',[],[],'3')
player4 = Player('',[],[],'3')
player5 = Player('',[],[],'3')
player6 = Player('',[],[],'3')

def int_checker():
    while True:
        try:
            npc_num = int(input('How many players are there - not including house: '))
            if npc_num<1 or npc_num>7:
                print('Please enter a valid number of players')
            else:
                return npc_num
        except ValueError:
            print("Enter whole numbers please!")   

def card_checker(cards,rand_cards):
    while True:
        try:
            rand_card = random.choice(cards)
            return rand_card,cards
        except IndexError:
            print("~~~~\nRan out of cards!\n~~~~\nAdding another deck...\n~~~~")
            cards = 'aaaa222233334444555566667777888899990000jjjjqqqqkkkk'

def checkin():
    npc_num = int_checker()
    name = input("Please enter Player 1's name: ")
    player1.name = name
    players.append(player1)
    if npc_num>1:
        name = input("Please enter Player 2's name: ")
        player2.name = name
        players.append(player2)
        if npc_num>2:
            name = input("Please enter Player 3's name: ")
            player3.name = name
            players.append(player3)
            if npc_num>3:
                name = input("Please enter Player 4's name: ")
                player4.name = name
                players.append(player4)
                if npc_num>4:
                    name = input("Please enter Player 5's name: ")
                    player5.name = name
                    players.append(player5)
                    if npc_num>5:
                        name = input("Please enter Player 6's name: ")
                        player6.name = name
                        players.append(player6)
    return npc_num

def house_cards(cards):
    rand_cards = []
    print('The House Goes First.')
    for c in range(2):
        rand_card,cards = card_checker(cards,rand_cards)
        print(f'Card dealt: {rand_card}')
        rand_cards.append(rand_card)
        cards = cards.replace(rand_card,'',1)
    house.cards = rand_cards
    house.cards_str = house.cards_string()
    print(f"The House's cards: {house.cards_str}")
    print('.\n.\n.')
    return cards

def deal_cards(i,cards):
    rand_cards = []
    print(f"{i.name}'s turn")
    for c in range(2):
        rand_card,cards = card_checker(cards,rand_cards)
        print(f'Card dealt: {rand_card}')
        rand_cards.append(rand_card)
        cards = cards.replace(rand_card,'',1)
    i.cards = rand_cards
    i.cards_str = i.cards_string()
    print(f"{i.name}'s cards: {i.cards_str}")
    print('.\n.\n.')
    return cards

def hit():
    print('wip')
    
def insurance_bets(i):
    choice = input(f'{i.name}, would you like to place an insurance bet? ')
    if choice.lower() == 'yes':
        print('~~~~')
        i.insurance = '0'
        if house.cards[1] == 'a':
            if house.cards[0] == '0' or house.cards[0] == 'j' or house.cards[0] == 'q' or house.cards[0] == 'k':
                i.insurance = '1'
        elif house.cards[1] == 'j' or house.cards[1] == '0' or house.cards[1] == 'q' or house.cards[1] == 'k':
            if house.cards[0] == 'a':
                i.insurance = '1'
        else:
            print('some sort of error?')
    elif choice.lower() == 'no':
        print(f'{i.name} has abstained.')
        print('~~~~')
        i.insurance = '2'
    else:
        print('Please enter either a yes or no. ')
        insurance_bets(i)

def wash(cards,npc_num):
    washing = input('Clean cards? ')
    if washing.lower() == 'yes':
        cards = 'aaaa222233334444555566667777888899990000jjjjqqqqkkkk'
        print('~~~~')
        return roundstart(cards,npc_num)
    elif washing.lower() == 'no':
        print('~~~~')
        return roundstart(cards,npc_num)
    else:
        print('Please enter either a yes or no. ')
        wash(cards,npc_num)

def gamerestart(cards,npc_num):
    sure = input('Game will restart, are you sure? ')
    if sure.lower() == 'yes':
        print('Restarting...')
        print('~~~~')
        main_game()
    elif sure.lower() == 'no':
        return roundrestart(cards,npc_num)
    else:
        print('Please enter either a yes or no. ')
        gamerestart(cards,npc_num)

def roundrestart(cards,npc_num):
    restart = input('Start another round? ')
    if restart.lower() == 'yes':
        print('~~~~')
        wash(cards,npc_num)
    elif restart.lower() == 'no':
        gamerestart(cards,npc_num)
    else:
        print('Please enter either a yes or no. ')
        roundrestart(cards,npc_num)

def roundstart(cards,npc_num):
    print('\nStarting Round...\n')
    print(cards)
    cards = house_cards(cards)
    for i in players:
        cards = deal_cards(i,cards)
    # print(f'cards left over: {cards}')
    if house.cards[1] == 'a' or house.cards[1] == '0' or house.cards[1] == 'j' or house.cards[1] == 'q' or house.cards[1] == 'k':    
        print('Insurance bet?\n~~~~')
        for i in players:
            insurance_bets(i)
        insur_abstain = Player.check_insurance('2')
        if len(insur_abstain) == npc_num:
            print('Everyone has abstained.')
            print(f'.\n.\nThe other card was a {house.cards_str[0]}.')
        else:
            print(f'.\n.\nThe other card was a {house.cards_str[0]}.')
            insur_win = Player.check_insurance('1')
            if len(insur_win)!= 0:
                print('Players who won their insurance bets:')
                for i in insur_win:
                    print(f' - {i.name}')
            else:
                print('~~~~\nLosses to those who betted insurance:')
                for i in players:
                    if i.insurance == '0':
                        print(f' - {i.name}')
    else:
        print('No insurance bet.')
    # for blah blah blah
    roundrestart(cards,npc_num)

def main_game():
    print('WIP BLACKJACK SIM - a coding exercise\n~~~~')
    cards = 'aaaa222233334444555566667777888899990000jjjjqqqqkkkk'
    npc_num = checkin()
    roundstart(cards,npc_num)
        
main_game()
