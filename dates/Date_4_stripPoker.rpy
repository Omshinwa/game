label label_stripPoker:
    
    scene bg flat close
    pause
    play sound "day/doorbell.mp3"
    pause 0.4
    "You ring the bell"
    play sound "day/door_opening.mp3"
    pause 0.2
    scene bg flat open with dissolve
    pause 0.2
    show joyce night at depied onlayer master zorder 2
    with dissolve
    pause
    j smile "Hey I've been waiting for you"
    j "Come inside."
    $ date = Date("date", objectif_trust = 50, turnLeft = 7, endTurn = "label_stripPoker_endTurn")
    scene bg bedroom
    show joyce smile night at depied
    show fg bedroom-table onlayer master zorder 2
    with blinds
    pause
    j "Do you want a drink?"
    j wink tongue "Of course you do."
    hide joyce
    with dissolve
    pause
    show joyce smile night at depied 
    with dissolve
    j foxy "Here"
    play sound "day/put_on_table.wav"
    show screen screen_glass("house") onlayer master zorder 2
    with dissolve
    
    j "Let's get comfy"
    j "How about we make it a strip game?"
    j "Everytime you succeed, I'll drop a piece of clothing."

    # hide joyce with dissolve
    # show expression "joyce " + " outfit"+whichDress at sitting

    show joyce night at depied onlayer master zorder 0 with dissolve

    call label_beginDuel_common()

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                hide screen screen_date_ui with dissolve

                
                if "night4" in renpy.get_attributes("joyce"):
                    show date-nice at truecenter with blinds
                    hide date-nice with moveoutbottom

                    j "t'es trop forte bewbew"
                    call label_after_successful_Date_common
                    jump label_prison

                elif "night" in renpy.get_attributes("joyce"):
                    j foxy smile "Is it hot or it's just me?"
                    play sound "sex/undress.wav"
                    show joyce night2 with Dissolve(1.0)
                    $ date.objectives["attraction"] = date.attraction + 20
                elif "night2" in renpy.get_attributes("joyce"):
                    j foxy smile "Off another layer."
                    play sound "sex/undress.wav"
                    show joyce night3 with Dissolve(1.0)
                    $ date.objectives["attraction"] = date.attraction + 20
                    $ date.objectives["trust"] = date.trust + 20
                elif "night3" in renpy.get_attributes("joyce"):
                    j foxy smile "Ooh, last one.."
                    play sound "sex/undress.wav"
                    show joyce night4 hideboobs with Dissolve(1.0)
                    $ date.objectives["lust"] = 100


                show screen screen_date_ui with dissolve
            
            show joyce 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_stripPoker_endTurn:
    call label_date_isLost_common
    
    if game.progress[1]<=date.turn:            
        if date.turn == 0:
            pass
    else:
        call label_reaction

    call label_endTurn_common

    call label_add_card_to_deck("deck", Card("peek2"))
    # pause 0.5

    return