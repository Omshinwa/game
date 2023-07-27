# **config has **date.config["objectives"], endTurn = "label_firstDate_endTurn"
#
label label_beginDuel_common(**kwargs):
    $ game.jeu_sensitive = False;
    $ game.state = "dating"

    $ game.lust = 0
    $ game.lustMultiplier = 1
    $ game.trust = 0
    $ game.trustMultiplier = 1
    $ game.attraction = 0
    $ game.attractionMultiplier = 1
    $ game.animation_speed = 3

    show card_zone_bg zorder 2

    $ deck.deck = deck.list.copy()
    $ deck.shuffle()
    $ deck.discard_pile = []
    $ deck.hand = []

    if game.progress < 3:
        show screen screen_date_ui(**kwargs)
    else:
        show screen screen_sex_ui(**kwargs)

    $ deck.draw(5)

    $ game.jeu_sensitive = True;
    return

label label_endTurn_common():
    $ game.attractionMultiplier = 1
    $ game.trustMultiplier = 1
    $ game.lustMultiplier = 1

    $ handSize = len(deck.hand)
    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    
    $ game.jeu_sensitive = True;
    return