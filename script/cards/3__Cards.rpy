define cardList = { 
    # calling a method of game or date in a string doesnt work in browser

    "calm": {"txt":_("-3 Lust. Can go into negatives."), "eff":"renpy.call('label_card_calm')", "value":1, "sort":"20"},
    "maxcalm":{"txt":_("-10 Lust, add one STOP card in your hand"), "eff":"renpy.call('label_card_maxcalm')", "value":1, "sort":"201"},#card also work if you have multiple

    "fibonacci": {"txt": "-1 Lust, this permanently increases by 1 every time it's played.", "eff":"renpy.call('label_card_fibonacci')", "value":1,"sort":"202"},
    
    "newday": {"txt":_("Change your current Lust with a random number"), "eff":"renpy.call('label_card_newday')", "value":1,"sort":"203"},


    "slower": {"txt":_("Go slower, -3 Lust per turn."), "eff":"renpy.call('label_card_slower')", "value":1, "sort":"21"},
    "slowsteady": {"txt":_("IF this is your leftmost card: \nGo much slower, -5 Lust per turn"), "cond":"index == 0", "eff":"renpy.call('label_card_slowsteady')", "value":1, "sort":"22"},
    "fool": {"txt": _("IF you have 3 cards or less in hand: \nGo much slower, -5 Lust per turn"), "cond":"len(deck.hand)<=3", "eff":"renpy.call('label_card_fool')", "value":1, "sort":"23" },
    "faster": {"txt":_("Go faster, +3 Lust per turn."), "eff":"renpy.call('label_card_faster')", "value":-1, "sort":"24"},

    "stop": {"txt":_("Can't be played"), "cond":"False", "eff":"", "value":-3,"sort":"zzz", "color":"bad"},

    "awakening": {"txt":_("This turn: double Lust and Speed changes."), "eff":"date.lustMultiplier *= 2", "value":3,"sort":"30"},

    "draw2": {"txt":_("draw 2 cards"), "eff":"renpy.call('label_card_draw2')", "value":4,"sort":"42"},#
    "devil": {"txt":_("Draw 2 cards, Gain 10 Lust."), "eff":"renpy.call('label_card_devil')", "value":3,"sort":"43"},
    "pair": {"txt":_("IF you have a pair in your hand: draw 2 cards"), "cond":"deck.hasPair()>1", "eff":"renpy.call('label_card_pair')", "value":3,"sort":"44"},
    "recycle": {"txt":_("Discard all the cards on the right of this card, then redraw as many +1"), "eff":"renpy.call('label_card_recycle', index)", "value":1,"sort":"45"},


    "drink" : {"txt":_("Fully refill your glass."), "eff":"renpy.call('label_card_drink')", "value":2, "sort":"40"}, #把杯子倒满

    "change": {"txt":_("Change all the cards in your hand with random cards."), "eff":"renpy.call('label_card_change')", "value":1,"sort":"50"},
    
    
    "sisyphus": {"txt":_("Choose a card played, put it back on top of your deck."), "eff":"renpy.call('label_card_sisyphus', index)", "value":2,"sort":"61"},
    "reload": {"txt":_("The most recent card in the discard pile is played again."), "cond":"len(deck.discard_pile)>0", "eff":"renpy.call('label_card_reload', index)", "value":2, "sort":"62"},

    "ouroboros": {"txt":_("Shuffle back all the cards played into the deck."), "eff":"renpy.call('label_card_ouroboros')", },#"value":3,

    "exodia3" : {"txt":_("{b}WORLD{/b}\ninto Power.\nthe right\nthis effect"), "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5, "sort":"93"},
    "exodia2" : {"txt":_("{b}OF THE{/b}\ncurrent Lust\n3 pieces in\nactivate"), "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5, "sort":"92"},
    "exodia1" : {"txt":_("{b}ORIGIN{/b}\nConvert your\nYou need all\n order to"), "eff":"renpy.call('label_card_exodia', index)", "value":0, "rarity":"rare", "sort":"91"},

    "universeout" : {"txt":_("Add 2 Space Out cards in your hand."), "eff":"renpy.call('label_card_universeout')", "value":1, "sort":"63"},
    "darkhole" : {"txt":_("Discard your hand, -5 Lust per discarded card."), "eff":"renpy.call('label_card_darkhole')", "value":1, "sort":"64"},
    "spaceout" : {"txt":_("does nothing"), "value":0, "sort":"65"}, #_("")
    "nova" : {"txt":_("-X² Lust, where X is the number of Space Out cards in the discard pile."), "eff":"renpy.call('label_card_nova')", "value":1, "sort":"66"},
    #alternatively it could be every space out in deck hand and graveyard


    "peek": {"txt":_("you peek..\n+2 Lust"), "eff":"renpy.call('label_card_peek')", "color":"lust"},
    "peek2": {"txt":_("you peek.. +5 Lust"), "eff":"renpy.call('label_card_peek2')", "value":-1, "color":"lust"},
    "peekred": {"txt":_("get +10 Lust"), "eff":"renpy.call('label_card_peekred')", "color":"lust"},
    "peekblue": {"txt":_("get +10 Lust"), "eff":"renpy.call('label_card_peekblue')", "color":"lust"},
    "peek4": {"txt":_("get +15 Lust"), "eff":"renpy.call('label_card_peek4')", "value":-2, "color":"lust"},
    "peek5": {"txt":_("get +30 Lust"), "eff":"renpy.call('label_card_peek5')", "value":-3, "color":"lust"},


    "eyecontact": {"txt":_("+1 attraction"), "eff":"renpy.call('label_card_eyecontact')","value2":1, "sort":"03", "color":"attraction"},
    "flirt": {"txt":_("+2 attraction"), "eff":"renpy.call('label_card_flirt')","value2":2, "sort":"04", "color":"attraction"},
    # "kiss" : {"txt":_("+4 attraction"), "eff":"date.increment('attraction',4,False);","value2":3, "sort":"05"},
    "touchy" : {"txt":_("For the rest of this turn: Attraction gains are doubled."),"value2":2, "sort":"06", "color":"attraction"}, #

    "talk": {"txt":_("+1 trust"), "eff":"renpy.call('label_card_talk')","value2":1, "sort":"00", "color":"trust"}, #+1 trust
    "talk2": {"txt":_("+2 trust"), "eff":"renpy.call('label_card_talk2')","value2":2, "sort":"01", "color":"trust"},
    "listen": {"txt":_("For the rest of this turn: Trust gains are doubled"), "sort":"02", "color":"trust"},

####            POKER MENU STUFF

    "newgame" : {"txt":_("Start a New Game"), "eff":"renpy.jump('start')","sort":"___", },
    "continue" : {"txt":_("Continue from Last Save"), "eff":"renpy.run(FileLoad(renpy.newest_slot(),newest=False,slot=True))","sort":"___", },
    "load" : {"txt":_("Load a Save file"), "eff":"renpy.run(ShowMenu('load'))","sort":"___", },
    "prefs" : {"txt":_("Open Preferences Menu"), "eff":"renpy.run(ShowMenu('preferences'))","sort":"___", },
    "lang" : {"txt":_("Change Language"), "sort":"___", },
    "discord" : {"txt":_("Go see our Discord!"), "eff":"renpy.jump('start')","sort":"___", },
    "achievement" : {"txt":_("Check Achievements")},
    "memory" : {"txt":_("Check Memories")},

    "undress" : {"txt":_("Remove clothing."), "value":0 }
        }
label label_card_lang:
    if _preferences.language == 'chinese':
        $ renpy.change_language(None, True)
    else:
        $ renpy.change_language('chinese', True)
    return

label label_card_achievement:
    "bite"
    # show screen screen_achievement
    # pause
    call screen screen_achievement
    return

label label_card_memory:
    scene
    call screen screen_gallery with dissolve
    return

init python:
    CARD_IMG_DICT = {}
    for card in cardList:
            CARD_IMG_DICT[card] = Image("cards/"+card+".png")

label label_card_nova:
    python:
        i = 1
        for card in deck.discard_pile:
            if card.name == "spaceout":
                date.increment("lust",-i)
                i += 1
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
    while len(deck.hand)>0:
        $ deck.discard(0)
        $ date.increment("lust", -5, False)
    $ date.increment("lust", 0, True)
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
        $ achievement.grant("Exodia")

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