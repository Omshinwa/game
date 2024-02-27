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

    "awakening": {"txt":_("Double the next Lust change."), "eff":"date.lustMultiplier *= 2", "value":3,"sort":"30"},
    # "awakening": {"txt":_("Reset your lust to Zero.\nDiscard half your deck."), "value":3,"sort":"30"},

    "draw2": {"txt":_("draw 2 cards"), "eff":"renpy.call('label_card_draw2')", "value":4,"sort":"42"},#
    "devil": {"txt":_("Draw 2 cards, Double your current lust."), "eff":"renpy.call('label_card_devil')", "value":3,"sort":"43"},
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
    "darkhole" : {"txt":_("Discard the rest of your hand.\n-5 Lust for each discarded card."), "eff":"renpy.call('label_card_darkhole')", "value":1, "sort":"64"},
    "spaceout" : {"txt":_("does nothing"), "value":0, "sort":"65"}, #_("")
    "nova" : {"txt":_("-3*X Lust, where X is the number of Space Out cards in the discard pile."), "eff":"renpy.call('label_card_nova')", "value":1, "sort":"66"},
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
    "listen": {"txt":_("For the rest of this turn: Trust gains are doubled"), "value2":2, "sort":"02", "color":"trust"},

    ####            POKER MENU STUFF

    "newgame" : {"txt":_("Start a New Game"), "eff":"renpy.jump('start')","sort":"___", },
    "load" : {"txt":_("Load a Save file"), "eff":"renpy.run(ShowMenu('load'))","sort":"___", },
    "prefs" : {"txt":_("Open Preferences Menu"), "eff":"renpy.run(ShowMenu('preferences'))","sort":"___", },
    "lang" : {"txt":_("Change Language"), "sort":"___", },
    "discord" : {"txt":_("Go see our Discord!"), "eff":"renpy.jump('start')","sort":"___", },
    "achievement" : {"txt":_("Check Achievements")},
    "memory" : {"txt":_("Check Memories")},
    "fullscreen": {"txt":_("Switch between Windowed and Fullscreen mode.")},

    "undress" : {"txt":_("Remove clothing."), "value":0 }
        }

init python:
    CARD_IMG_DICT = {}
    for card in cardList:
        CARD_IMG_DICT[card] = Image("cards/"+card+".png")

label label_card_fullscreen:
    $ renpy.run(Preference("display", "fullscreen"))
    return

label label_card_lang:
    if _preferences.language == 'chinese':
        $ renpy.change_language(None, True)
    else:
        $ renpy.change_language('chinese', True)
    $ deck.hand.append(Card("lang"))
    return

label label_card_achievement:
    # show screen screen_achievement
    # pause
    call screen screen_achievement
    return

label label_card_memory:
    scene
    call screen screen_gallery with dissolve
    return
