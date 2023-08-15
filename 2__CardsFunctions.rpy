label label_card_change:
    $ i = 0
    while i < len(deck.hand):
        $ deck.hand[i] = Card.get_random_card()
        $ renpy.pause(0.2, hard=True)
        $ i+=1
    return

label label_card_drink:
    $ date.drink = 3
    play sound "day/pour-drink.wav"
    pause 0.2
    return

label label_shuffle:
    $ i = 0
    while len(deck.hand)>0:
        $ deck.deck.append( deck.hand.pop(0) )
        $ renpy.play("card/draw.mp3", channel='drawcard')
        $ renpy.pause(0.2, hard=True)
        $ i+= 1
    $ deck.shuffle()
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

label label_card_sisyphus(index):
    $ renpy.call('label_add_card_to_deck','deck', deck.discard_pile.pop(index), xfrom=150, yfrom=850, pauseTime=0.2, index=0)
    hide screen screen_show_deck with dissolve
    return

label label_card_ouroboros:
    while len(deck.discard_pile)>1:
        $ deck.deck.append( deck.discard_pile.pop(0) )
        #the last card played is sisyphys which we let in the graveyard
        $ renpy.play("card/shuffle.mp3", channel='drawcard')
        $ renpy.pause(0.1)
    $ deck.shuffle()
    return

label label_card_reload():
    $ i = 2
    while i<=len(deck.discard_pile) and deck.discard_pile[-i].name == "reload":
        $ i += 1
    if i<=len(deck.discard_pile):
        $ card = deck.discard_pile[-i]
    else:
        $ card = Card("reload")

    while i>2:
        $ renpy.play("card/activate.mp3", channel='activatecard')
        $ renpy.show('cardPlayed', what=Card("reload").img, at_list=[trans_card_played(xfrom=150, yfrom=850, xto=540)], zorder=2, layer="screens")
        $ renpy.pause(0.5)
        $ renpy.hide('cardPlayed', layer="screens")
        $ i -= 1
    if card.name == "reload":
        pass
    else:
        $ renpy.play("card/activate.mp3", channel='activatecard')
        $ renpy.show('cardPlayed', what=card.img, at_list=[trans_card_played(xfrom=150, yfrom=850, xto=960)], zorder=2, layer="screens")
        $ renpy.pause(0.5)
        $ renpy.hide('cardPlayed', layer="screens")
        if "index" not in card.eff:
            $ renpy.call('playCard',card, -1)
    return

label label_card_exodia(index):
    if len(deck.hand) >= 2 and deck.discard_pile[-1].name == 'exodia3': # its annoying that to get the card being played you need to do this
        if deck.hand[index-2].name == 'exodia1' and deck.hand[index-1].name == 'exodia2':
            call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
            call label_add_card_to_deck("deck", deck.hand.pop(index-1), pauseTime=0, fromWhere="field")
            call label_add_card_to_deck("deck", deck.hand.pop(index-2), pauseTime=0, fromWhere="field")
            jump .effect
    elif len(deck.hand) >= 2 and deck.discard_pile[-1].name =='exodia2':
        if deck.hand[index-1].name == 'exodia1' and deck.hand[index].name == 'exodia3':
            call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
            call label_add_card_to_deck("deck", deck.hand.pop(index), pauseTime=0, fromWhere="field")
            call label_add_card_to_deck("deck", deck.hand.pop(index-1), pauseTime=0, fromWhere="field")
            jump .effect
    elif len(deck.hand) >= 2 and deck.discard_pile[-1].name == 'exodia1':
        if deck.hand[index].name == 'exodia2' and deck.hand[index+1].name == 'exodia3':
            call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
            call label_add_card_to_deck("deck", deck.hand.pop(index+1), pauseTime=0, fromWhere="field")
            call label_add_card_to_deck("deck", deck.hand.pop(index), pauseTime=0, fromWhere="field")
            jump .effect

    call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
    return

    label .effect:
        
        $ renpy.play("rpg/Holy6.wav", channel='activatecard')

        while date.lust >= 2:
            $ date.lust -= 2
            $ date.lustMax += 2
            $ renpy.pause(0.1, hard=True)
        
        $ date.lustMax += date.lust
        $ date.lust = 0
        $ deck.draw(5-len(deck.hand))
    return

label label_card_fibonacci:
    $ card = game.cardPlaying
    $ value = int( card.txt.split(" ")[0] )
    $ date.increment('lust', value)
    
    $ value -= 1
    $ card.txt = str(value) + " Lust, increases every time it's played."
    $ card.updateArt()
    python:
        for card2 in deck.list:
            if card2.name == "fibonacci":
                value2 = int( card2.txt.split(" ")[0] )
                if value2 == value-1:
                    card2 = card
                    break
    return