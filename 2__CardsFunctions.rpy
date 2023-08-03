label label_card_change:
    $ i = 0
    while i < len(deck.hand):
        $ deck.hand[i] = Card.get_random_card()
        $ renpy.pause(0.2, hard=True)
        $ i+=1
    return

label label_card_reload:
    $ i = 0
    while len(deck.hand)>0:
        $ deck.deck.append( deck.hand.pop(0) )
        $ renpy.play("draw.mp3", channel='drawcard')
        $ renpy.pause(0.2, hard=True)
        $ i+= 1
    # $ deck.shuffle()
    $ deck.draw(i, 0.2)
    return

label label_card_discardAll:
    $ i = 0
    while len(deck.hand)>0:
        $ deck.discard(0)
        $ i+= 1
        $ date.increment("lust", -1, False)
    
    $ date.increment("lust", 0, True)
    return

label label_card_darkhole:
    $ i = 0
    while len(deck.hand)>0:
        if deck.hand[0].name == "spaceout":
            $ i+=1
        $ deck.discard(0)
    while i > 0:
        $ date.increment("lust", -5, False)
        pause 0.2
        $ i-=1
    $ date.increment("lust", 0, True)
    return

label label_card_sisyphus:
    while len(deck.discard_pile)>1:
        $ deck.deck.append( deck.discard_pile.pop(0) )
        #the last card played is sisyphys which we let in the graveyard
        $ renpy.play("shuffle.mp3", channel='drawcard')
        $ renpy.pause(0.1)
    $ deck.shuffle()
    return

label label_card_exodia(index):
    if deck.hand[index-1].name == 'exodia3' and deck.hand[index].name == 'exodia2' and deck.hand[index+1].name == 'exodia1':
        $ date.increment("lust",-100)
        $ renpy.pause(0.1)
        $ game.speedDown()
        $ renpy.pause(0.1)
        $ game.speedDown()
        $ renpy.pause(0.1)
    else:
        call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1).name)
        # $ renpy.play("shuffle.mp3", channel='drawcard')
        $ renpy.pause(0.1)