init python:
    def card_change():
        for i in range(len(deck.hand)):
            deck.hand[i] = Card( renpy.random.choice( list(cardList.keys()) ) )
    
label card_change:
    $ i = 0
    while i < len(deck.hand):
        $ deck.hand[i] = Card( renpy.random.choice( list(cardList.keys()) ) )
        $ renpy.pause(0.2, hard=True)
        $ i+=1
    return

label card_shuffle:
    $ i = 0
    while len(deck.hand)>0:
        $ deck.deck.append( deck.hand.pop(0) )
        $ renpy.pause(0.2, hard=True)
        $ i+= 1
    $ deck.shuffle()
    $ deck.draw(i, 0.1)
    return