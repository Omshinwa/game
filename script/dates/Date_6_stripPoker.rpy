label label_stripPoker:
    $ stripPoker_got_drugged = False

    if game.progress[1] == -1:
        scene black
        with dissolve
        "This is the address Joyce sent you..."
    scene bg flat close at trs_bg_blur(10)
    with dissolve
    
    if game.progress[1] == -1:
        pause
    play sound "day/doorbell.wav"
    pause 0.8
    
    if game.progress[1] == -1:
        "You ring the bell"
    else:
        pause 1.0

    play sound "day/door_opening.wav"
    pause 0.2
    show bg flat open with dissolve
    pause 0.2
    show joyce night at trs_depied onlayer master zorder 2
    with dissolve
    pause
    
    if game.progress[1] == -1:
        j smile "Hey! I've been waiting for you."
        j "Come in."
    else:
        j foxy smile "Who could it be?"
        j "Make yourself at home, you know the place by now."
    $ date = Date("date", objectif_trust = game.trust + 5, turnLeft = 8, endTurn = "label_stripPoker_endTurn")
    scene bg bedroom  at trs_bg_blur()
    show joyce smile night at trs_depied
    show fg bedroom-table onlayer master zorder 2
    with blinds
    
    if game.progress[1] == -1:
        pause
        j "Do you want a drink?"
        j wink tongue "Of course you do."
        hide joyce
        with dissolve
        pause
        show joyce smile night at trs_depied 
    with dissolve
    j foxy "here"
    play sound "day/put_on_table.wav"
    show screen screen_glass("house") onlayer master zorder 2
    with dissolve
    
    if game.progress[1] == -1:
        j "Please, have a glass of red wine."
        j "I've got an idea I think you'll like..."
        j "How about we make this one a strip game?"
        j "Everytime you succeed, I'll remove a piece of clothing."
    else:
        j "Let's go straight to the strip game."
        j -smile eyeside "That's what you're here for, aren't you?"

    # hide joyce with dissolve
    # show expression "joyce " + " outfit"+whichDress at trs_sitting

    show joyce night at trs_depied onlayer master zorder 0 with dissolve

    call label_beginDuel_common() from _call_label_beginDuel_common_4

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                hide screen screen_date_ui with dissolve

                if "night4" in renpy.get_attributes("joyce"):

                    if stripPoker_got_drugged == False:
                        $ achievement.grant_with_notification("Suspicious")

                    $ date.lust = 0
                    call label_after_successful_Date_common from _call_label_after_successful_Date_common_4
                    
                    j foxy smile "This is so sexy..."
                    j foxy smile "I think you're a good candidate."   

                    if stripPoker_got_drugged == False:
                        j "..."
                        j tired -smile"..."
                        j night5 "Hey..."
                        j "You know what's going on... Don't you?"  

                    show black onlayer screens:
                        alpha 0.4
                    with Dissolve(0.4) 
                    show black onlayer screens:
                        alpha 0.2
                    with Dissolve(0.4) 

                    "You suddenly feel tired..."
                    j foxy "What's wrong?"
                    j foxy "Are you getting too excited? Do you need to sit down?"
                    "You need to lie down."
                    window hide
                    window auto

                    show black onlayer screens:
                        alpha 0.8
                    with Dissolve(0.4) 
                    show black onlayer screens:
                        alpha 0.5
                    with Dissolve(0.4) 


                    j foxy night5 "Did you drink too much?"
                    "..."
                    "You feel like something was wrong with your drink."
                    "You need to go home NOW."
                    window hide
                    window auto

                    show black onlayer screens:
                        alpha 1.0
                    with Dissolve(0.4) 
                    show black onlayer screens:
                        alpha 0.9
                    with Dissolve(0.4) 

                    "You try to get up, but to no avail, you feel like drifting."
                    j "Be a good boy, and go to sleep."

                    show black onlayer screens:
                        alpha 1.0
                    with Dissolve(0.4) 
                    pause
                    j "Everything will be just fine."
                    pause 1.0
                    call label_newDay("label_welcome_prison") from _call_label_newDay_12

                elif "night" in renpy.get_attributes("joyce"):
                    j foxy smile "Is it hot in here or is it just me?"
                    play sound "sex/undress.wav"
                    show joyce night2 with Dissolve(1.0)
                    $ date.objectives["attraction"] = date.attraction + 5
                elif "night2" in renpy.get_attributes("joyce"):
                    j foxy smile "Down another layer."
                    play sound "sex/undress.wav"
                    show joyce night3 with Dissolve(1.0)
                    $ date.objectives["attraction"] = date.attraction + 8
                    $ date.objectives["trust"] = date.trust + 8
                elif "night3" in renpy.get_attributes("joyce"):
                    j foxy smile "Ooh, last one.."
                    play sound "sex/undress.wav"
                    show joyce night4 with Dissolve(1.0)
                    j "For this last one, let's make it..."
                    j "A special requirement."
                    $ date.objectives["lust"] = 100
                    $ date._isLost = "len(deck.deck) == 0 or date.turnLeft == 1"
                    j "Please get as horny as possible."


                show screen screen_date_ui with dissolve
            
            show joyce 

        
        show joyce null with dissolve
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_5

        $ game.jeu_sensitive = True

        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_stripPoker_endTurn:
    call label_date_isLost_common from _call_label_date_isLost_common_4
    
    # call label_reaction from _call_label_reaction_4

    call label_endTurn_common from _call_label_endTurn_common_4
    if "night2" in renpy.get_attributes("joyce"):
        call label_add_card_to_deck("hand", Card("peek2"), pauseTime = 0.5) from _call_label_add_card_to_deck_8
    if "night3" in renpy.get_attributes("joyce"):
        call label_add_card_to_deck("hand", Card("peek4"), pauseTime = 0.5) from _call_label_add_card_to_deck_9
    if "night4" in renpy.get_attributes("joyce"):
        call label_add_card_to_deck("hand", Card("peek5"), pauseTime = 0.5) from _call_label_add_card_to_deck_10

    return