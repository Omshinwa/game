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
                j armscrossed upset "Um... don't you think I can notice?"
                j "Sorry but I'm gonna go. I'm really not in the mood today."
                j "Let's do this another day."
            else:
                if game.progress[1]<3:
                    j foxy armscrossed "You're getting a bit too horny, aren't you?"
                    j smile "Seems like today's not your day."
                    j tongue "Hehe, try next time. "
                    j smirk "My door is always open for you."
                else:
                    j foxy armscrossed "Ooh bad play."
                    j smile "You should take your time."
                    j "You don't need to burst everything in one go."
                    j "Just focus on each step, one at a time."
                    j wink tongue "Big boy."


        elif len(deck.deck) == 0 or date.turnLeft <= 1:
            show joyce null
            hide screen screen_date_ui with dissolve
            if game.progress[0]<4:
                j eyeside armscrossed "Oh, look at the time!"
                j "Sorry, I gotta go."
                j "That kinda dragged on anyway, right?"
                j "Maybe we can do this another day? See ya."
            else:
                if game.progress[1]<3:
                    j foxy armscrossed "Oh, look at the time!"
                    j smile "Seems like today's not your day."
                    j tongue "Hehe, try next time."
                    j smirk "My door is always open for you."
                else:
                    j foxy armscrossed "Ooh time's up."
                    j smile "You should take your time."
                    j "You don't need to burst everything in one go."
                    j "Just focus on each step, one at a time."
                    j wink tongue "Big boy."

        hide joyce with dissolve

        if not BALANCE["keepStat"]:
            $ date.lust = 0
            $ date.trust = 0
            $ date.attraction = 0
        call label_newDay(label_callback) from _call_label_newDay

    return