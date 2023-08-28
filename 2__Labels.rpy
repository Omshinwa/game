
label label_newDay(callback):
    window hide
    $ game.day += 1
    $ game.state = "living"
    $ renpy.play("day/newday.wav", channel='sound') 
    show screen screen_home onlayer master
    show black onlayer screens
    with dissolve
    pause 2.0
    # play sound "day/alarm.wav"
    # pause 2.0
    window auto
    
    # $ game.lust += 1

    if game.progress[0]*2>g.phoneProgress[0] and game.day%game.dateEvery==game.dateEvery-1:
        $ g.phoneProgress[0] += 1
        $ g.phoneProgress[1] = 0

    jump expression callback

label label_beginDuel_common():
    $ game.jeu_sensitive = False;

    # if game.progress[0] <= 4:
    #     $ game.state = "dating"
    # else:
    #     $ game.state = "sexing"

    $ date.lust = game.lust
    $ date.lustMax = game.lustMax
    $ date.lustMultiplier = 1
    $ date.trust = game.trust
    $ date.trustMultiplier = 1
    $ date.attraction = game.attraction
    $ date.attractionMultiplier = 1
    $ date.animation_speed = 1

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

    $ deck.draw(5)

    play sound "rpg/Wind1.wav"
    show date-start onlayer screens at truecenter with blinds
    pause 0.4
    play sound "date/datestart2.mp3"
    hide date-start  onlayer screens with moveoutbottom

    if date.lust > date.trust and date.lust > date.attraction:
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
    $ handSize = len(deck.hand)
    play sound "rpg/Item1.wav"
    pause 0.3

    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    
    $ game.jeu_sensitive = True;

    if game.state == "dating":
        show joyce null with dissolve
    # show joyce null with dissolve

    return

label label_after_successful_Date_common():
    hide screen screen_date_ui with dissolve
    hide screen screen_sex_ui with dissolve

    if game.state == "dating":
        play sound "rpg/Holy5.wav"
        show date-nice at truecenter with blinds
        pause 0.3
        hide date-nice with moveoutbottom
    
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
    
    show screen screen_tutorial( trans_add_card_to_deck(card.img, xfrom, yfrom, xto, yto, pauseTime) ) 
        
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
    hide screen screen_tutorial

    # $ game.jeu_sensitive = True
    return

label label_drink:
    $ game.jeu_sensitive = False
    if date.drink>0:
        play sound "day/gulp.wav"
        $ date.drink -= 1
        pause 1.0
        call label_shuffle
        return

label label_date_isLost_common():
    $ game.jeu_sensitive = False

    if date.isLost():
        play sound "rpg/Fall1.wav"
        show date-fail onlayer screens at truecenter with blinds
        pause 0.3
        hide date-fail onlayer screens with moveoutbottom

        if date.lust > date.trust and date.lust > date.attraction:
            show joyce null
            hide screen screen_date_ui with dissolve
            j armscrossed upset "um.. don't you think I can notice?"
            j "Sorry but I'm gonna go. I'm really not in the mood today."
            j "Let's do this another day."

        elif len(deck.deck) == 0 or date.turnLeft == 0:
            show joyce null
            hide screen screen_date_ui with dissolve
            j eyeside armscrossed "OH look at the time."
            j "Sorry but I gotta go."
            j "That kinda dragged on no?"
            j "Maybe we can do this another day? See ya."

        hide joyce with dissolve

        $ date.lust = 0
        $ date.trust = 0
        $ date.attraction = 0
        call label_newDay("label_home")

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
                call label_add_card_to_deck(toWhere="list", card=Card(cardID2), xfrom=300, yfrom=500, pauseTime=0.5)
                if callback != None:
                    call label_newDay(callback)
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