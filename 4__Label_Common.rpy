label label_beginDuel_common():
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

    show card_zone_bg zorder 3 onlayer master

    $ deck.deck = deck.list.copy()
    $ deck.shuffle()
    $ deck.discard_pile = []
    $ deck.hand = []

    if game.progress[0] < 3:
        show screen screen_date_ui()
    else:
        show screen screen_sex_ui()

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

label label_after_successful_Date_common():
    $ game.lust = date.lust
    $ game.trust = date.trust
    $ game.attraction = date.attraction
    $ game.progress[0] += 1
    $ game.progress[1] = 0
    return

init python:
    def hide_all_screens_but(expection = "#"):
        listOfScreen = ["screen_prison", "screen_home", "tutorial"]
        for screen in listOfScreen:
            if expection not in screen:
                renpy.hide_screen( screen )

label label_add_card_to_deck( deckOrList, card, xfrom=960, yfrom=-100, pauseTime=0, index=None):
    if deckOrList == "list":
        show screen screen_tutorial( trans_add_card_to_deck(card.img, xfrom, yfrom, 1900, 20, pauseTime) ) 
    
    elif deckOrList == "deck":
        show screen screen_tutorial( trans_add_card_to_deck(card.img, xfrom, yfrom, 1900, 1000, pauseTime) ) 

    pause 0.4 + pauseTime
    play sound "card/ghost.mp3"
    pause 0.3
    if deckOrList == "list":
        $ deck.list.append( card )
        $ deck.list.sort()
    elif deckOrList == "deck":
        if index==None:
            $ rand = renpy.random.randint(0, len(deck.deck))
            $ deck.deck.insert( rand , card )
        else:
            $ deck.deck.insert( index , card )
    else:
        $ raise ValueError("deck or list not specified")
    pause 0.2
    hide screen screen_tutorial
    return