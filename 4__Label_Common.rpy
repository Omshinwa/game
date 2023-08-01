# **config has **date.objectives, endTurn = "label_firstDate_endTurn"
#
label label_beginDuel_common(**kwargs):
    $ game.jeu_sensitive = False;
    $ game.state = "dating"

    $ date.lust = game.lust
    $ date.lustMax = game.lustMax
    $ date.lustMultiplier = 1
    $ date.trust = game.trust
    $ date.trustMultiplier = 1
    $ date.attraction = game.attraction
    $ date.attractionMultiplier = 1
    $ game.animation_speed = 3

    show card_zone_bg zorder 2

    $ deck.deck = deck.list.copy()
    $ deck.shuffle()
    $ deck.discard_pile = []
    $ deck.hand = []

    if game.progress[0] < 3:
        show screen screen_date_ui(**kwargs)
    else:
        show screen screen_sex_ui(**kwargs)

    $ deck.draw(5)

    return

label label_endTurn_common():
    $ date.attractionMultiplier = 1
    $ date.trustMultiplier = 1
    $ date.lustMultiplier = 1

    $ handSize = len(deck.hand)
    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    
    $ game.jeu_sensitive = True;
    return


init python:
    def hide_all_screens_but(expection = "#"):
        listOfScreen = ["screen_prison", "screen_home", "tutorial"]
        for screen in listOfScreen:
            if expection not in screen:
                renpy.hide_screen( screen )

label label_add_card_to_deck( cardName, xbase, ybase):
    hide screen screen_tutorial
    show screen screen_tutorial( trans_add_card_to_deck(Card(cardName).img, xbase, ybase) ) 
    pause 0.5
    play sound "draw.mp3"
    pause 0.45
    $ deck.list.append( Card(cardName) )
    $ deck.list.sort()
    pause 0.2
    return