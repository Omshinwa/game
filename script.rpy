﻿define BALANCE = {"keepStat":True}

define j = Character(None, image="joyce", kind=bubble)
define rat = Character(None, image="rat", kind=bubble)

default povname = "William"
    
default game = Game()
default date = Date("date")

# The game starts here.

label start:
    $ quick_menu = True
    # call screen Content_Warning()
    scene black
    with dissolve
    $ deck = Deck()


    $ deck.list = [Card("talk"),Card("talk"),Card("talk"),Card("calm"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    Card("spaceout"),Card("listen"),Card("eyecontact"),Card("draw2"),Card("flirt"),Card("pair"),Card("recycle")]

    # python:
    #     for card in cardList:
    #         deck.list.append(Card(card))
    
    $ povname = renpy.input("What is your name?", length=32)
    with dissolve
    $ povname = povname.strip()

    if not povname:
        $ povname = "William"

    $ game.day = 0

    jump label_tutorial
    # jump label_home
    # jump label_prison_rat_introduction
    # jump test_sprites

    return