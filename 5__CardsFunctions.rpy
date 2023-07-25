label label_card_change:
    $ i = 0
    while i < len(deck.hand):
        $ deck.hand[i] = game.get_random_card()
        $ renpy.pause(0.2, hard=True)
        $ i+=1
    return

label label_card_shuffle:
    $ i = 0
    while len(deck.hand)>0:
        $ deck.deck.append( deck.hand.pop(0) )
        $ renpy.pause(0.2, hard=True)
        $ i+= 1
    $ deck.shuffle()
    $ deck.draw(i, 0.1)
    return

label label_card_discardAll:
    $ i = 0
    while len(deck.hand)>0:
        $ deck.discard(0)
        $ i+= 1
    $ deck.draw(i, 0.1)
    return

label label_card_ouroboros:
    while len(deck.discard_pile)>0:
        $ deck.deck.append( deck.discard_pile.pop(0) )
        $ renpy.play("shuffle.mp3", channel='drawcard')
        $ renpy.pause(0.1)
    $ deck.shuffle()
    return