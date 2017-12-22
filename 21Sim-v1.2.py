# blackjack simulator
# please look at the unicode char at http://www.unicode.org/charts/PDF/U1F0A0.pdf
import random
import sys
import os
clear = lambda: os.system('clear')
# card class defined
class card():
    def __init__(self,index,suite,value,face,position):
        self.index = index
        self.suite = suite

        #adjust so the value reflect the numnber of the card
        if value > 12:
            self.value = value -1
        else:
            self.value = value

        self.face = face
        self.position = position

    def status(self):
        print('{0}:{1}{2}@{3} index {4}'.format(self.face,self.suite,self.value,self.position,self.index))

    def change_position(self,new_position):
        self.position = new_position

    def show(self):
       return "{0}{1}".format(dict_suite_char[self.suite],dict_pic_cards[self.value])

    def show_face_down(self):
        return face_down

#class player defined
class player():
    def __init__(self,player_name):
        self.player_name = player_name



# all the playing card char stars with below hex
str_base = '0x1F0'

face_down = chr(127136)

dict_suite_char ={'SPADE':"\u2660",'HEART':"\u2661",'DIAMOND':"\u2662",'CLUB':"\u2663"}

dict_suite = {'SPADE':'A','HEART':'B','DIAMOND':'C','CLUB':'D'}

dict_pic_cards = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}



# create list of numbers from 0 to 9
list_numbers = list(range(0,10))

# create list of letters from a to e
list_letters = list(range(97,102))

# create an empty list to store the hex strings for card
list_hex = list()

# iterate through the list of letters (stored as int), convert to string and add them to the list_numbers
#for letter in list_letters:
#    #print(chr(letter))
#    list_numbers.append(chr(letter))
#print(list_numbers)

# do the same thing using lambda
list_numbers += list(map(lambda letter: chr(letter),list_letters))

# at this point, the list_numbers should look like
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']


# iterate through the list_numbers, if the number is int, convert it to string, store them in list_hex
for letter in list_numbers:
    if type(letter) == int:
        number_char = str(letter)
    else :
        number_char = letter

    list_hex.append(number_char)

#do the same thing with lambda
list_hex = list(map(lambda letter: str(letter) if type(letter) == int else letter,list_numbers))

# at this point, the list_hex should look like this
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e'] <-- Note all the numbers are stored as string
# print(list_hex)


# initalize card list
cards = []

#each card will be assigned an index, a unique number that identifies the card
index = 0

# iterate through the suite and numbers to create all the combination of hex to represent all the cards in a dec.
for suite in dict_suite:
    #print('now displaying cards of  ' + suite)
    str_suite = dict_suite[suite]

    for hex in list_hex:

        # skipping last hex 0 and c
        if hex != '0' and hex != 'c':

            int_card_number = int(hex,16)

            #print('I am {0} of {1}'.format(suite,int_card_number))

            str_card = str_base + str_suite.upper() + hex

            #print(str_card)

            int16_card = int(str_card,16)

            #print(int16_card)

            #print(chr(int16_card))

            #print('{0},{1}.{2}'.format(int_card_number,suite,chr(int16_card)))

            cards.append(card(index,suite,int_card_number,chr(int16_card),'deck'))

            #increment the index
            index += 1


# display all the card in the deck
def show_card_status():
    for card in cards:
         card.status()

# draw a random card in the deck
def draw_card_use_index(cards,player):

    #list_card_in_deck = [card.index for card in cards if  card.position == 'deck']
    # do the above using lambda
    list_card_in_deck = list(filter(lambda card: card.index if card.position == 'deck' else None, cards))

    card_drawn_index = random.choice(list_card_in_deck)

    list_card_drawn = [card for card in cards if card.index == card_drawn_index]

   # list_card_drawn[0].status()

    list_card_drawn[0].change_position(player)

def draw_card(cards,player_name):

    #list_card_in_deck = [card for card in cards if  card.position == 'deck']
    # do the above using lambda
    list_card_in_deck = list(filter(lambda card: card.position == 'deck', cards))
    card_drawn = random.choice(list_card_in_deck)

    #card_drawn.status()

    card_drawn.change_position(player_name)

    print('{0} draws {1}{2}'.format(player_name,card_drawn.face,card_drawn.show()))

    #card_drawn.status()

def draw_card_dealer(cards,player_name):

    #list_card_in_deck = [card for card in cards if  card.position == 'deck']
    # do the above using lambda
    list_card_in_deck = list(filter(lambda card: card.position == 'deck', cards))
    card_drawn = random.choice(list_card_in_deck)

    #card_drawn.status()

    card_drawn.change_position(player_name)

    print('{0} draws {1}'.format(player_name,card_drawn.show_face_down()))

    #card_drawn.status()

def shuffle(cards):
    #for card in cards:
    #    card.change_position('deck')
    lambda card: card.change_position('deck'),cards


def discard_cards(cards):
    list_cards_currently_played = [card for card in cards if card.position != 'deck' and card.position !='discarted']
    for card in list_cards_currently_played:
        card.change_position('discarted')

def show_cards_on_deck(cards):
    return len([card.index for card in cards if card.position == 'deck'])

def show_cards(cards,player):
    list_show_cards =[]
    list_players_card = [card for card in cards if card.position == player.player_name]
    for card in list_players_card:
        list_show_cards.append(card)
    return  list_show_cards

def check_if_someone_is_busted(list_players):
    #print('Checking if someone is busted...')
    for player in list_players:
        if calculate_cards_at_hand(player,False) > 21:
            print('{0} is busted!'.format(player.player_name))

def bool_check_if_someone_is_busted(list_players):
    for player in list_players:
        if calculate_cards_at_hand(player,False) > 21:
            return True

def bool_check_if_there_is_Ace(player):
    ace = [card for card in cards if card.position == player.player_name and card.value == 1]
    if len(ace) > 0:
        return True
    else:
        return False

def calculate_cards_at_hand(player,bool_isAce11):
    #print(player.player_name)
    point = 0
    list_players_card = [card for card in cards if card.position == player.player_name]

    if bool_isAce11:
        for card in list_players_card:
            if card.value > 9 :
                point += 10
            elif card.value == 1:
                point += 11
            else:
                point += card.value
        return point

    else:
        for card in list_players_card:
            if card.value > 9:
                point += 10
            #elif card.value == 1:
            #    point += 11
            else:
                point += card.value
        return point

def calcurate_cards_at_hand_adjust_ace(player):
    point = 0
    list_players_card = [card for card in cards if card.position == player.player_name]

    # if counting ace as 11 bust you, count it as 1

    if bool_check_if_there_is_Ace(player):

        _point = calculate_cards_at_hand(player,True)

        if  _point > 21:

            point = calculate_cards_at_hand(player,False)

        elif _point == 21:

            point = _point

        else:

            point = _point

    else:

        #pic cards count as 10
        for card in list_players_card:
            if card.value > 9:
                point += 10
            else:
                point += card.value

    return point

def calcurate_chance(cards,int_card_value):
    int_card_on_deck = show_cards_on_deck(cards)
    int_card_with_value = len([card.index for card in cards if card.value == int_card_value and card.position == 'deck'])

    print('number of cards on the deck: {0}'.format(int_card_on_deck))
    print('what you need to draw {0}'.format(int_card_value))
    print('number of cards on the deck with that value:{0}'.format(int_card_with_value))
    return '{:.5%}'.format(int_card_with_value/int_card_on_deck)


# main program
clear()
print('Welcome to 21 table!')
input('Press Enter to continue\n')
player_name = input('Please enter your name:')

# player object created
player1_cards = []
player1 = player(player_name)

# dealer object created
dealer_cards = []
dealer = player('Dealer')

# list to contain all the players
list_players = []

list_players.append(player1)
list_players.append(dealer)

print('\nHello {0}, let us begin...'.format(player1.player_name) )

shuffle(cards)

#show_card_status()

#print(show_cards_on_deck(cards))

while True:
#while bool_check_if_someone_is_busted(list_players) != True :
    # needs at least 4 cards to play
      if  show_cards_on_deck(cards) > 3:
            clear()
            print('\nStarting a new game....\n')

            player1_point = 0
            dealer_point = 0

            draw_card(cards,player1.player_name)
            draw_card(cards, dealer.player_name)
            draw_card(cards, player1.player_name)
            draw_card_dealer(cards, dealer.player_name)

            player1_point = calcurate_cards_at_hand_adjust_ace(player1)
            dealer_point = calcurate_cards_at_hand_adjust_ace(dealer)

            cards_left = show_cards_on_deck(cards)
            #keep playing till you get 21 or busted or you decide to stand
            while bool_check_if_someone_is_busted(list_players) != True and cards_left > 0:

                if player1_point == 21:
                    print('Conguratulations {0}! You have 21!'.format(player1.player_name))
                    break
                else:
                    print('\n{0} has {1}'.format(player1.player_name, player1_point))

                    #print('\n')
                    if player1_point > 11:
                        print('You will need to draw {0} to get 21'.format(21-player1_point))

                        print('The change of you drawing {0} is {1}'.format(21-player1_point,calcurate_chance(cards,21-player1_point)))

                    res = input('\nHit or Stand? (Enter h or s key)\n')

                    cards_left = show_cards_on_deck(cards)

                    if cards_left > 1:

                        if res == 'h':
                            draw_card(cards,player1.player_name)

                            player1_point = calcurate_cards_at_hand_adjust_ace(player1)

                            if player1_point == 21:
                                print('Congratulations {0}! You have 21!'.format(player1.player_name))
                                break
                            else:
                                print('{0} has {1}'.format(player1.player_name, player1_point))

                        elif res == 's':
                            print('{0}, you decided to stand.'.format(player1.player_name))
                            break

                        else:
                            print('please either h or s and press enter')

                    check_if_someone_is_busted(list_players)
                    #print('end of while loop')

        # The player has finished playing his part. Dealer will deal from here
        # show dealer hands
            print('\n')
            print('Dealer section starting')
            print('\n')
            list_dealer_cards = show_cards(cards,dealer)
            dealer_cards = ''
            dealer_points = 0
            for card in list_dealer_cards:
                dealer_cards += card.face + card.show()

            if dealer_point < 17 :
                print('{0} has {1} ({2})'.format(dealer.player_name, dealer_cards, dealer_point))
                print('Dealer will deal now...')

            while dealer_point < 17 and show_cards_on_deck(cards) >0:
                draw_card(cards,dealer.player_name)
                dealer_point = calcurate_cards_at_hand_adjust_ace(dealer)
                #print('{0}'.format(dealer_point))

            list_dealer_cards = show_cards(cards, dealer)
            dealer_cards = ''
            for card in list_dealer_cards:
                dealer_cards += card.face + card.show()

            if dealer_point == 21:
                print('Dealer has 21!')
                if player1_point == 21:
                    print('{0} also has 21, you tied!'.format(player1.player_name))
                else:
                    print('{0} has {1}. You lose!'.format(player1.player_name,player1_point))
            elif dealer_point < 21:
                print('{0} has {1} ({2})'.format(dealer.player_name, dealer_cards, dealer_point))

                if player1_point > dealer_point and player1_point < 21:
                    print('{0} have {1}. You win!'.format(player1.player_name, player1_point))
                elif player1_point == 21:
                    print('{0} have {1}. You win!'.format(player1.player_name,player1_point))
                elif dealer_point > player1_point and player1_point < 21:
                    print('{0} has {1}. You lose!'.format(dealer.player_name,dealer_point))
                elif dealer_point == player1_point:
                    print('You tied!')
                else:
                    print('{0} has {1}. You are busted!'.format(player1.player_name, player1_point))
            else:
                print('Dealer is busted!')
                if player1_point > 21:
                    print('{0} also busted!'.format(player1.player_name))
                else:
                    print('You won!')

            discard_cards(cards)
            print('\n')
            input('Press Enter to continue\n')
      else:
            print('Sorry, no more cards in the deck')
            break




print('Sorry, no more cards in the deck')
