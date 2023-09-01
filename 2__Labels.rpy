
label label_newDay(callback):
    $ renpy.set_return_stack(renpy.get_return_stack()[-1])

    window hide
    scene black
    $ renpy.play("day/newday.wav", channel='sound') 
    # show black
    if game.day % game.dateEvery == 0:
        show screen screen_day
    with dissolve
    window auto

    if game.day % game.dateEvery == 0:
        pause 1.5
        # show layer screens:
        #     zoom 2.0 xalign 0.0 yalign 0.0
        #     ease 1.0 zoom 1.0
        play music "music/clock-tick.mp3" noloop
        $ game.day += 1
        with blinds
    else:
        pause 1.0
        $ game.day += 1
    
    $ game.state = "living"
    with dissolve
    $ game.lust += eval(game.lustPerDay)
    
    jump expression callback

label label_beginDuel_common():
    $ game.jeu_sensitive = False;

    $ date.lust = game.lust
    $ date.lustMax = game.lustMax
    $ date.lustMultiplier = 1
    $ date.trust = game.trust
    $ date.trustMultiplier = 1
    $ date.attraction = game.attraction
    $ date.attractionMultiplier = 1
    
    $ date.animation_speed = 3

    $ deck.drink = 3

    if game.progress[1] == -1:
        $ game.progress[1] = 0

    $ deck.deck = deck.list.copy()
    $ deck.shuffle()
    $ deck.discard_pile = []
    $ deck.hand = []

    if game.state == "dating":
        show screen screen_date_ui()
    else:
        show screen screen_sex_ui()
    hide screen screen_day
    with dissolve

    $ deck.draw(5)

    play sound "rpg/Wind1.wav"
    show date-start onlayer screens at truecenter with blinds
    pause 0.4
    play sound "date/datestart2.mp3"
    hide date-start  onlayer screens with moveoutbottom

    if game.state == "dating":
        if date.lust > date.trust and date.lust > date.attraction:
            pause 0.5
            play sound "rpg/Sonic1-onTheEdge.wav"
            show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
            hide screen screen_tutorial with dissolve
    elif game.state == "sexing":
        if date.lust > date.lustMax:
            pause 0.5
            play sound "rpg/Sonic1-onTheEdge.wav"
            show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
            hide screen screen_tutorial with dissolve
    return

label label_endTurn_common():

    # if not renpy.get_screen("screen_date_ui"):
    #     show screen screen_date_ui with dissolve



    $ date.attractionMultiplier = 1
    $ date.trustMultiplier = 1
    $ date.lustMultiplier = 1
    $ date.turn += 1
    $ game.progress[1] = max(date.turn, game.progress[1])

    # $ done_flag["thisTurn"] = set()

    $ handSize = len(deck.hand)

    if game.state == "sexing" and date.lust + date.animation_lust[date.animation_speed] >= date.lustMax:
        play sound "rpg/Sonic1-onTheEdge.wav" volume 0.5
        pause 0.5
    else:
        play sound "rpg/Item1.wav"
        pause 0.3

    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    
    $ game.jeu_sensitive = True;

    if game.state == "dating":
        show joyce null with dissolve

    return

label label_after_successful_Date_common():
    hide screen screen_date_ui
    hide screen screen_sex_ui
    hide screen screen_dick_ui
    with dissolve

    if game.state == "dating":
        play sound "rpg/Holy5.wav"
        show date-nice at truecenter onlayer screens with blinds
        pause 0.3
        hide date-nice onlayer screens with moveoutbottom
    
    if BALANCE["keepStat"]:
        $ game.lust = max(0,date.lust)
        $ game.trust = date.trust 
        $ game.attraction = date.attraction
    else:
        $ game.lust = 0 #date.lust
        $ game.trust = 0 #date.trust
        $ game.attraction = 0 #date.attraction
    
    $ date.objectives["lust"] = -999
    $ date.objectives["trust"] = -999
    $ date.objectives["attraction"] = -999

    $ game.progress[0] += 1
    $ game.progress[1] = -1
    $ g.phoneProgress[0] += 1
    $ g.phoneProgress[1] = 0

    if game.state == "dating":
        show joyce null with dissolve
    return


label label_add_card_to_deck( toWhere, card, xfrom=960, yfrom=-100, pauseTime=0, fromWhere=None, index=None,):
    $ game.jeu_sensitive = False
    if toWhere == "list":
        $ xto = 1900
        $ yto = 20
    
    elif toWhere == "deck":
        $ xto = 1900
        $ yto = 1000

    elif toWhere == "hand":
        $ xto = 960
        $ yto = 1000

    else:
        $ raise ValueError("toWhere deck or list not specified")

    if fromWhere == "field":
        $ yfrom = 450
    
    show expression card.img onlayer screens at trans_anim_move_card(xfrom, yfrom, xto, yto, pauseTime)
        
    pause 0.4 + pauseTime
    play sound "card/ghost.mp3"
    pause 0.3
    if toWhere == "list":
        $ deck.list.append( card )
        $ deck.list.sort()
    elif toWhere == "deck":
        if index==None:
            $ rand = renpy.random.randint(0, len(deck.deck))
            $ deck.deck.insert( rand , card )
        else:
            $ deck.deck.insert( index , card )
    elif toWhere == "hand":
        $ deck.hand.append( card )
    else:
        $ raise ValueError("deck or list not specified")
    pause 0.2
    hide expression card.img onlayer screens

    # $ game.jeu_sensitive = True
    return

label label_drink:
    $ game.jeu_sensitive = False
    if date.drink>0:
        play sound "day/gulp.wav"
        $ date.drink -= 1
        pause 1.0
        call label_shuffle from _call_label_shuffle
        return

label label_date_isLost_common(label_callback = "label_home"):
    $ game.jeu_sensitive = False

    if date.isLost():
        play sound "rpg/Fall1.wav"
        show date-fail onlayer screens at truecenter with blinds
        pause 0.3
        hide date-fail onlayer screens with moveoutbottom

        if date.lust > date.trust and date.lust > date.attraction:
            show joyce null
            hide screen screen_date_ui with dissolve
            if game.progress[0]<4:
                j armscrossed upset "um.. don't you think I can notice?"
                j "Sorry but I'm gonna go. I'm really not in the mood today."
                j "Let's do this another day."
            else:
                j foxy armscrossed "You're getting a bit too horny no?"
                j smile "Seems like today's not your day."
                j tongue "hehe, try next time."
                j smirk "My door is always open for you."

        elif len(deck.deck) == 0 or date.turnLeft <= 1:
            show joyce null
            hide screen screen_date_ui with dissolve
            if game.progress[0]<4:
                j eyeside armscrossed "OH look at the time."
                j "Sorry but I gotta go."
                j "That kinda dragged on no?"
                j "Maybe we can do this another day? See ya."
            else:
                j foxy armscrossed "Oh look at the time!"
                j smile "Seems like today's not your day."
                j tongue "hehe, try next time."
                j smirk "My door is always open for you."

        hide joyce with dissolve

        if not BALANCE["keepStat"]:
            $ date.lust = 0
            $ date.trust = 0
            $ date.attraction = 0
        call label_newDay(label_callback) from _call_label_newDay

    return

label label_transform_card(cardID, cardID2, prompt, callback=None):
    show expression trans_show_card_1(Card(cardID).img)  as card onlayer screens
    show expression trans_show_card_2(Card(cardID2).img) as card2 onlayer screens
    if any(c.name == cardID for c in deck.list):
        menu:
            "[prompt]"
            "yes":
                hide card onlayer screens
                hide card2 onlayer screens
                python:
                    for index,card in enumerate(deck.list):
                        if card.name == cardID:
                            deck.list.pop(index)
                            break
                call label_add_card_to_deck(toWhere="list", card=Card(cardID2), xfrom=300, yfrom=500, pauseTime=0.5) from _call_label_add_card_to_deck_1
                if callback != None:
                    call label_newDay(callback) from _call_label_newDay_1
            "no":
                hide card onlayer screens
                hide card2 onlayer screens
    else:
        menu:
            "[prompt]"
            "(you dont have any)":
                hide card onlayer screens
                hide card2 onlayer screens
    return