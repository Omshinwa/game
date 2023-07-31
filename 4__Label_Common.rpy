# **config has **date.config["objectives"], endTurn = "label_firstDate_endTurn"
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

    $ game.jeu_sensitive = True;
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