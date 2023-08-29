define cardList = { 

    "calm": {"txt":"-3 lust, can get into negatives", "eff":"date.increment('lust',-3, negative=True)", "value":1, "sort":"20"},
    "maxcalm":{"txt":"-10 lust, add one STOP card in your hand", "eff":"date.increment('lust',-10); deck.hand.append(Card('stop'))", "value":1, "sort":"201"},#card also work if you have multiple

    "fibonacci": {"txt": "-1 Lust, increases every time it's played.", "eff":"renpy.call('label_card_fibonacci')", "value":3,"sort":"202"},
    
    "newday": {"txt":"Change your current Lust with a random number.", "eff":"date.lust = renpy.random.randint(0, date.lustMax)", "value":2,"sort":"203"},

    "slower": {"txt":"go slower", "eff":"date.speedDown(True)", "value":1, "sort":"21"},
    "slowsteady": {"txt":"IF this is your leftmost card: \nGo much slower. ", "cond":"index == 0", "eff":"date.speedDown(True); date.speedDown(True)", "value":1, "sort":"22"},
    "faster": {"txt":"go faster", "eff":"date.speedUp(True)", "value":-1, "sort":"24"},

    "awakening": {"txt":"This turn: double Lust and Speed changes.", "eff":"date.lustMultiplier *= 2", "value":2,"sort":"30"},

    "draw2": {"txt":"draw 2 cards", "eff":"deck.draw(2)", "value":4,"sort":"42"},
    "devil": {"txt":"Draw 2 cards, Double your current lust.", "eff":"deck.draw(2); date.increment('lust',date.lust, useMultiplier=False)", "value":1,"sort":"43"},
    "pair": {"txt":"IF you have a pair in your hand: draw 2 cards", "cond":"deck.hasPair()>1", "eff":"deck.draw(2)", "value":2,"sort":"44"},
    "threeof": {"txt":"IF you have three of a kind in your hand: draw 3 cards", "cond":"deck.hasPair()>2", "eff":"deck.draw(3)", "value":1,"sort":"45"},

    "draw5": {"txt":"Get to max speed, draw until you have 5 cards in hand.", "eff":"date.animation_speed = len(date.animation_speed_hash)-1; deck.draw(5-len(deck.hand))", "value":1,"sort":"48"},

    "drink" : {"txt":"Fully refill your glass.", "eff":"renpy.call('label_card_drink')", "value":2, "sort":"40"},

    "change": {"txt":"Change all the cards in your hand with random cards.", "eff":"renpy.call('label_card_change')", "value":2,"sort":"50"},
    
    "recycle": {"txt":"All the cards on the right of this card are discarded, then redraw as many.", "eff":"renpy.call('label_card_recycle', index)", "value":2,"sort":"41"},
    
    "sisyphus": {"txt":"Choose a card played, put it back on top of your deck.", "eff":"renpy.show_screen('screen_show_deck', what=deck.discard_pile, label_callback='label_card_sisyphus', instruction='Choose a card to add back', background='#000a')", "value":1,"sort":"61"},
    "reload": {"txt":"The top card in the discard pile is played again.", "cond":"len(deck.discard_pile)>0", "eff":"renpy.call('label_card_reload')", "value":2, "sort":"62"},
    # "ouroboros": {"txt":"Shuffle back all the cards played into the deck.", "eff":"renpy.call('label_card_ouroboros')", "value":3,},

    "exodia3" : {"txt":"{b}WORLD{/b}\ninto Power.\nright order to\neffect.", "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5, "sort":"93"},
    "exodia2" : {"txt":"{b}OF THE{/b}\ncurrent Lust\npieces in the\nthis", "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5, "sort":"92"},
    "exodia1" : {"txt":"{b}ORIGIN{/b}\nConvert your\nYou need all 3\nactivate", "eff":"renpy.call('label_card_exodia', index)", "value":0, "rarity":"rare", "sort":"91"},

    "universeout" : {"txt":"Add 2 Space Out cards in your hand.", "eff":"deck.add_to_hand(Card('spaceout')); deck.add_to_hand(Card('spaceout'))", "value":0, "sort":"63"},
    "darkhole" : {"txt":"Discard your hand, - (number of discarded cards)² Lust ", "eff":"renpy.call('label_card_darkhole')", "value":2, "sort":"64"},
    "spaceout" : {"txt":"does nothing", "eff":"", "value":0, "sort":"65"},


    "peek": {"txt":"you peek..\n+2 lust", "eff":"date.increment('lust',2)", },
    "peek2": {"txt":"you peek.. +5 lust", "eff":"date.increment('lust',5)", },
    "peekred": {"txt":"get +10 lust", "eff":"date.increment('lust',10)"},
    "peekblue": {"txt":"get +10 lust", "eff":"date.increment('lust',10)",},
    "peek4": {"txt":"get +15 lust", "eff":"date.increment('lust',20)",},
    "peek5": {"txt":"get +30 lust", "eff":"date.increment('lust',30)",},

    "peek5-1": {"txt":"get +5 lust", "eff":"date.increment('lust',20)", "value":-1,},
    "peek5-2": {"txt":"get +10 lust", "eff":"date.increment('lust',20)", "value":-2,},
    "feelgood": {"txt":"get +20 lust", "eff":"date.increment('lust',20)", "value":-3,},
    

    "stop": {"txt":"Can't be played", "cond":"False", "eff":"", "value":-2,"sort":"zzz"},

    "eyecontact": {"txt":"+1 attraction", "eff":"date.increment('attraction',1,False);","value2":1, "sort":"03"},
    "flirt": {"txt":"+2 attraction", "eff":"date.increment('attraction',2,False);","value2":2, "sort":"04"},
    "kiss" : {"txt":"+4 attraction", "eff":"date.increment('attraction',4,False);","value2":3, "sort":"05"},
    "touchy" : {"txt":"This turn, Attraction gains are doubled.", "eff":"date.attractionMultiplier *= 2","value2":2, "sort":"6"},

    "talk": {"txt":"+1 trust", "eff":"date.increment('trust',1)","value2":1, "sort":"00"},
    "talk2": {"txt":"+2 trust", "eff":"date.increment('trust',2)","value2":2, "sort":"01"},
    "listen": {"txt":"This turn: double Trust gains.", "eff":"date.trustMultiplier *= 2","value2":2, "sort":"02"},
        }

label label_card_change:
    $ i = 0
    while i < len(deck.hand):
        $ deck.hand[i] = Card.get_random_card()
        $ renpy.pause(0.2, hard=True)
        $ i+=1
    return

label label_card_drink:
    play sound "day/pour-drink.wav"

    if game.state == "dating":
        while date.drink<3:
            $ date.drink += 1
            with wipeup
    else:
        $ date.drink = 3
        pause 0.5
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

label label_card_darkhole:
    $ i = len(deck.hand)
    while len(deck.hand)>0:
        $ deck.discard(0)
        $ date.increment("lust", -i, False)
    $ date.increment("lust", 0, True)
    return

label label_card_recycle(index):
    $ i = 0
    while len(deck.hand)>index:
        $ deck.discard(-1)
        $ i+=1
    $ deck.draw(i)
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
    # if len(deck.hand) >= 2 and deck.discard_pile[-1].name == 'exodia3': # its annoying that to get the card being played you need to do this
    #     if deck.hand[index-2].name == 'exodia1' and deck.hand[index-1].name == 'exodia2':
    #         call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
    #         call label_add_card_to_deck("deck", deck.hand.pop(index-1), pauseTime=0, fromWhere="field")
    #         call label_add_card_to_deck("deck", deck.hand.pop(index-2), pauseTime=0, fromWhere="field")
    #         jump .effect
    # elif len(deck.hand) >= 2 and deck.discard_pile[-1].name =='exodia2':
    #     if deck.hand[index-1].name == 'exodia1' and deck.hand[index].name == 'exodia3':
    #         call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
    #         call label_add_card_to_deck("deck", deck.hand.pop(index), pauseTime=0, fromWhere="field")
    #         call label_add_card_to_deck("deck", deck.hand.pop(index-1), pauseTime=0, fromWhere="field")
    #         jump .effect
    # elif len(deck.hand) >= index+2 and deck.discard_pile[-1].name == 'exodia1':
    #     if deck.hand[index].name == 'exodia2' and deck.hand[index+1].name == 'exodia3':
    #         call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field")
    #         call label_add_card_to_deck("deck", deck.hand.pop(index+1), pauseTime=0, fromWhere="field")
    #         call label_add_card_to_deck("deck", deck.hand.pop(index), pauseTime=0, fromWhere="field")
    #         jump .effect

    if len(deck.hand) >= 2 and deck.discard_pile[-1].name == 'exodia3': # its annoying that to get the card being played you need to do this
        if deck.hand[index-2].name == 'exodia1' and deck.hand[index-1].name == 'exodia2':
            $ deck.discard(index-1)
            $ deck.discard(index-2)
            jump .effect
    elif len(deck.hand) >= 2 and deck.discard_pile[-1].name =='exodia2':
        if deck.hand[index-1].name == 'exodia1' and deck.hand[index].name == 'exodia3':
            $ deck.discard(index)
            $ deck.discard(index-1)
            jump .effect
    elif len(deck.hand) >= index+2 and deck.discard_pile[-1].name == 'exodia1':
        if deck.hand[index].name == 'exodia2' and deck.hand[index+1].name == 'exodia3':
            $ deck.discard(index+1)
            $ deck.discard(index)
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