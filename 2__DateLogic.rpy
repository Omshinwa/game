label beginDuel():
    $ game.state = "dating"

    show screen screen_card_hand()
    show screen screen_pleasure_ui()
    show screen screen_orgasm_ui()
    show screen screen_buttons_ui()
    
    show card_zone_bg zorder 2

    $ game.animation_speed = 3
    $ game.pleasure = 0

    $ deck.start()
    $ game.jeu_sensitive = True;
    return

label SexEndTurn:
    $ i=0
    while i < game.animation_speed:
        $ game.pleasure += 1
        $ game.orgasm += 1

        $ i += 1

    $ handSize = len(deck.hand)
    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    return