# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character(None, image="joyce", kind=bubble)
define rat = Character(None, image="rat", kind=bubble)

default povname = "William"
# define pov = Character(None, what_italic=True)#, what_prefix='"', what_suffix='"')
    
default game = Game()
default date = Date()

# The game starts here.

label start:
    
    #set up the deck and keybinds

    default deck = Deck()

    # $ deck.list = [Card("drink"),Card("drink"),Card("drink"),Card("devil"),Card("devil"),Card("fibonacci"),Card("fibonacci"),Card("fibonacci"),Card("fibonacci"),Card("peek"),Card("peek"),]
    
    $ deck.list = [Card("talk"),Card("talk"),Card("talk"),Card("calm"),Card("spaceout"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    Card("spaceout"),Card("listen"),Card("eyecontact"),Card("draw2"),Card("touchy"),Card("pair"),Card("discardAll")]

    # python:
    #     for card in cardList:
    #         deck.list.append(Card(card))

    show screen keybinds()
    show screen screen_debug

    # jump label_prison
    jump label_home

    return