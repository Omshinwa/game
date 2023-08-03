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

    # $ deck.list = [Card("faster"),Card("slower"),Card("distract"),Card("peek"),Card("devil"),Card("newday"),Card("calm"),Card("maxcalm"),Card("pair"),Card("change"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("devil"),Card("faster"),Card("devil"),Card("devil"),Card("devil"),Card("devil"),Card("devil"),Card("slower"),Card("slower"),Card("faster"),Card("devil"),Card("devil"),]
    # $ deck.list = [Card("peek"),Card("smalltalk"),Card("smalltalk"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    # Card("spaceout"),Card("listen"),Card("flirt"),Card("hobbies"),Card("eyecontact"),Card("drink"),Card("touchy"),Card("listen")]
    
    $ deck.list = [Card("peek"),Card("smalltalk"),Card("smalltalk"),Card("spaceout"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    Card("spaceout"),Card("listen"),Card("flirt"),Card("hobbies"),Card("eyecontact"),Card("drink"),Card("touchy"),Card("listen")]

    # python:
    #     for card in cardList:
    #         deck.list.append(Card(card))

    show screen keybinds()
    $ game.progress = [0,0]

    # jump label_prison
    jump label_home

    return