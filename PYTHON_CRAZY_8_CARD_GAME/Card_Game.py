# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)
    return (deck)
#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
      
     dealer=[]
     other=[]
     for compdeck in deck [0:25]:
         dealer.append (compdeck)
     for userdeck in deck [25:51]:
         other.append (userdeck)
     return (dealer, other)
 


def remove_pairs(lst):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    i = 0
    lst.sort()
    #lst.append(' ')
    no_duplicates= []
    while i < (len(lst)-1):
        if lst[i].strip('\u2660'+'\u2661'+'\u2662'+'\u2663') != lst[i+1].strip('\u2660'+'\u2661'+'\u2662'+'\u2663'):
            no_duplicates.append(lst[i])
            i=i+1
        else:
            i=i+1
    no_duplicates=shuffle_deck(no_duplicates)
    return no_duplicates
                

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    deck=str(deck)
    deck= deck.replace ('[',' ')
    deck=deck.replace (']',' ')
    deck=deck.replace (',',' ')
    deck=deck.replace ("'",'')
    print (deck)
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''


     print ('I have',len(n),'cards:')
     print ('If 1 stands for my first card and', len(n),'for my last card\nWhich of these cards would you like?')
     print('Give me an integer between 1 to',len(n),':')
     choice=input('')
     choice=int(choice)
     while not(choice>=1 and choice<=len(n)):
         print ('Invalid Number. Please pick a number between 1 and',len(n),':')
         choice=input('')
         choice=int(choice)
     return (choice)
         

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     deck=shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
    
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

   
     while len(human)>0 or len(dealer)>0:
         print ('***********************************')
         print ('Your Turn....')
         print (' ')
         print('your current deck of cards is:')
         print_deck(human)
         choice=get_valid_input (dealer)
         if choice==1:
             print('You asked for my',choice,'st card')
         if choice==2:
             print('You asked for my',choice,'nd card')
         if choice==3:
             print('You asked for my',choice,'rd card')
         if choice>=4:
             print('You asked for my',choice,'th card')
        
         pickedcard=dealer[choice-1]
         print ('Here it is',pickedcard)
         human.append (pickedcard)
         dealer.remove (pickedcard)
         print ('With',pickedcard,'added, Your current deck is:')
         print_deck (human)
         print ('And after removing pairs and shuffling, your deck is:')
         human=remove_pairs(human)
         human=shuffle_deck(human)
         print_deck (human)

         wait_for_player()
         if len (dealer)==0:
             break
         if len(human)==0:
             break
         print ('***********************************')
         print ('Now it is my turn....')
         print (' ')
         dealerpick=random.randint (1,len(human))
         if dealerpick==1:
             print ('I took your',dealerpick,'st card')
         if dealerpick==2:
             print('I took your',dealerpick,'nd card')
         if dealerpick==3:
             print('I took your',dealerpick,'rd card')
         if dealerpick>=4:
             print('I took your',dealerpick,'th card')
         dealer.append (human[dealerpick-1])
         human.remove (human[dealerpick-1])
         dealer=remove_pairs(dealer)
         if len(human)==0:
             break
         if len(dealer)==0:
             break
     if len(dealer)==0:
         print('Ups. I do not have any more cards\nYou lost! I, Robot, Have won')
     if len(human)==0:
         print('Ups. You do not have any more cards\nCongratulations! You, Human, have won')
     
     
# main
play_game()
