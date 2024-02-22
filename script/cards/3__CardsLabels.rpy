# in webbrowser, it cant find the strings of the name of the methods ie "date.increment('lust',-3, negative=True)" it wont find date.increment, it can find attributes though

label label_card_calm:
    $ date.increment('lust',-3, negative=True)
    return
label label_card_maxcalm:
    $ date.increment('lust',-10)
    $ deck.hand.append(Card('stop'))
    return
label label_card_slower:
    $ date.speedDown(False)
    $ date.lustPerTurn -= 3
    return
label label_card_slowsteady:
    $ date.speedDown(False)
    $ date.speedDown(False)
    $ date.lustPerTurn -= 5
    return
label label_card_fool:
    $ date.speedDown(False)
    $ date.speedDown(False)
    $ date.lustPerTurn -= 5
    return
label label_card_faster:
    $ date.speedUp(False)
    return
label label_card_draw2:
    $ deck.draw(2)
    return
label label_card_devil:
    $ deck.draw(2)
    $ temp = date.lust
    $ date.lust = 0
    play sound "rpg/Lust.wav"
    $ date.increment('lust', temp*2, negative=True)
    $ del temp
    return
label label_card_pair:
    $ deck.draw(2)
    return
label label_card_universeout:
    $ deck.add_to_hand(Card('spaceout'));
    pause 0.2
    $ deck.add_to_hand(Card('spaceout'));
    return
label label_card_peek:
    play sound "rpg/Lust.wav"
    $ date.increment('lust',2)
    return
label label_card_peek2:
    $ date.increment('lust',5)
    return
label label_card_peekred:
    $ date.increment('lust',10)
    return
label label_card_peekblue:
    $ date.increment('lust',10)
    return
label label_card_peek4:
    $ date.increment('lust',15)
    return
label label_card_peek5:
    $ date.increment('lust',30)
    return
label label_card_eyecontact:
    $ date.increment('attraction',1,False);
    if "eyecontact" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_eyecontact"):
        $ renpy.call(date.name + "_eyecontact") 
    else:
        call label_reaction
    return
label label_card_flirt:
    $ date.increment('attraction',2,False);
    if "flirt" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_flirt"):
        $ renpy.call(date.name + "_flirt") 
    else:
        call label_reaction
    return
label label_card_touchy:
    $ date.attractionMultiplier *= 2
    if "touchy" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_touchy"):
        $ renpy.call(date.name + "_touchy") 
    else:
        call label_reaction
    return
label label_card_talk:
    if "talk" in date.playedThisTurn or "talk2" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_talk"):
        $ renpy.call(date.name + "_talk") 
    else:
        call label_reaction_talk
    $ date.increment('trust',1)
    return
label label_card_talk2:
    if "talk" in date.playedThisTurn or "talk2" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_talk"):
        $ renpy.call(date.name + "_talk") 
    else:
        call label_reaction_talk
    $ date.increment('trust',2)
    return
label label_card_listen:
    if "listen" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_listen"):
        $ renpy.call(date.name + "_listen") 
    # else:
    #     call label_reaction_talk
    $ date.trustMultiplier *= 2
    return
label label_card_spaceout:
    return

label label_card_undress:
    if "naked" in renpy.get_attributes("joyce"):
        #already naked
        return

    if renpy.has_label(date.name + "_undress"):
        $ renpy.call(date.name + "_undress") 
    else:
        $ print("no label " + date.name + "_undress")
        call label_reaction_undress
    return

label label_card_awakening(card=None):
    python:
        i = int(len(deck.deck)/2)
        for card in range(i):
            renpy.sound.play("card/shuffle.mp3", channel='drawcard')
            deck.discard_pile.append( deck.deck.pop(-1) )
            renpy.pause(0.1)

        renpy.sound.play("rpg/_Absorption2.wav", channel="drawcard")
        date.increment("lust",-999)
    return

label label_card_nova:
    python:
        # i = 1
        for card in deck.discard_pile:
            if card.name == "spaceout":
                date.increment("lust",-3)
                # i += 1
    return

label label_card_newday:
    if game.state == "sexing":
        python:
            i = renpy.random.randint(0, date.lustMax)
            while i == date.lust:
                i = renpy.random.randint(0, date.lustMax)
            date.lust = i
    else:
        python:
            date.lust = renpy.random.randint(0, max(date.trust, date.attraction))
    return

label label_card_change:
    $ i = 0
    while i < len(deck.hand):
        $ deck.hand[i] = Card.get_random_card({ key: item for (key, item) in cardList.items() if "value" in cardList[key] })
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
    $ date.increment("lust", -i, True)
    return

label label_card_recycle(index):
    $ i = 0
    while len(deck.hand)>index:
        $ deck.discard(-1)
        $ i+=1
    $ deck.draw(i+1)
    return

label label_card_sisyphus(index):
    $ game.jeu_sensitive = True
    $ renpy.show_screen('screen_show_deck', what=deck.discard_pile, var_label_callback='label_card_sisyphus2', instruction='Choose a card to add back', background='#000a', cancelAction=Call("label_card_sisyphus_cancel"))
    call screen screen_gameloop()
    return

label label_card_sisyphus_cancel():
    hide screen screen_show_deck
    $ deck.hand.append(Card("sisyphus"))
    $ deck.discard_pile.pop(-1)
    return

label label_card_sisyphus2(index):
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

label label_card_reload(index):
    $ i = 2
    while i<=len(deck.discard_pile) and deck.discard_pile[-i].name == "reload":
        $ i += 1
    if i<=len(deck.discard_pile):
        $ card = deck.discard_pile[-i]
    else:
        $ card = Card("reload")

    while i>2:
        $ renpy.play("card/activate.mp3", channel='activatecard')
        $ renpy.show('cardPlayed', what=Card("reload").img, at_list=[trans_card_played(xfrom=150, yfrom=850, xto=960)], zorder=2, layer="screens")
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
        $ renpy.call('playCard',card, index)
    return

label label_card_exodia(index):

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

    call label_add_card_to_deck("deck", deck.discard_pile.pop(len(deck.discard_pile)-1), pauseTime=0, fromWhere="field") from _call_label_add_card_to_deck
    return

    label .effect:
        $ achievement.grant_with_notification("Exodia")

        play activatecard "rpg/Flame1.wav"
        queue activatecard ["rpg/Flame1.wav","rpg/Flame1.wav"]

        show exodia1:
            zoom 2.0
            align (0.2, 0.5)
            alpha 0.0
            ease 0.5 yalign 0.4 alpha 1.0
        show exodia2:
            zoom 2.0
            align (0.5, 0.5)
            alpha 0.0
            pause 0.5
            ease 0.5 yalign 0.4 alpha 1.0
        show exodia3:
            zoom 2.0
            align (0.8, 0.5)
            alpha 0.0
            pause 1.0
            ease 0.5 yalign 0.4 alpha 1.0
        
        with dissolve

        pause 1.5
        
        play activatecard "rpg/Holy6.wav"
        
        # $ renpy.play("rpg/Holy6.wav", channel='activatecard')
        show exodia1:
            ease 0.5 zoom 5.0 alpha 0.0
        show exodia2:
            ease 0.5 zoom 5.0 alpha 0.0
        show exodia3:
            ease 0.5 zoom 5.0 alpha 0.0

        while date.lust >= 2:
            $ date.lust -= 2
            $ date.lustMax += 2
            $ game.lustMax += 2
            $ renpy.pause(0.1, hard=True)
        
        $ date.lustMax += date.lust
        $ date.lust = 0
    return

label label_card_fibonacci:
    $ card = date.lastPlayed
    $ value = int( card.txt.split(" ")[0] )
    $ date.increment('lust', value)
    
    $ value -= 1
    $ card.txt = str(value) + _(" Lust, increases every time it's played.")
    $ card.updateArt()
    python:
        for card2 in deck.list:
            if card2.name == "fibonacci":
                value2 = int( card2.txt.split(" ")[0] )
                if value2 == value-1:
                    card2 = card
                    break
    return