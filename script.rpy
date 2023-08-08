# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character(None, image="joyce", kind=bubble) # Eileen
$ config.tag_transform["joyce"] = "myLoc"
$ config.tag_transform["fg"] = "myLoc"
    
default game = Game()
default date = Date()

# The game starts here.

label start:
    
    #set up the deck and keybinds

    default deck = Deck()

    # $ deck.list = [Card("drink"),Card("drink"),Card("drink"),Card("devil"),Card("devil"),Card("fibonacci"),Card("fibonacci"),Card("fibonacci"),Card("fibonacci"),Card("peek"),Card("peek"),]
    
    # $ deck.list = [Card("peek"),Card("smalltalk"),Card("smalltalk"),Card("spaceout"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    # Card("spaceout"),Card("listen"),Card("flirt"),Card("hobbies"),Card("eyecontact"),Card("drink"),Card("touchy"),Card("listen")]

    python:
        for card in cardList:
            deck.list.append(Card(card))

    show screen keybinds()
    $ game.progress = [0,0]

    # jump label_prison
    jump label_home

    return