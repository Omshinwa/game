label label_blowjob:
    $ date = Date("sex", endTurn = "label_blowjob_SexEndTurn", turnLeft=10, isWin = "date.turnLeft <= 0")

    scene bg basement
    show blowjob talk (1) as joyce
    with dissolve
    # show moan_bubble

    j "Are you ready?"

    play sound "rpg/Key.wav"
    show blowjob get-hard (1) as joyce with dissolve
    pause
    j "You must have been waiting for this no?" 
    j "How does it feel being finally free?"
    j "Now, can you get hard for me baby?"
    pause 0.4
    show blowjob get-hard (2) as joyce
    pause 0.4
    show blowjob get-hard (3) as joyce
    pause

    call label_beginDuel_common()
    $ current_speed = date.animation_speed

    j "ready?"
    show blowjob talk (2) as joyce
    j "I'll start moving."

    show joyce blowjob with dissolve
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            if "v2" in renpy.get_attributes("joyce"):
                show joyce blowjob v2
            else:
                show joyce blowjob

            $ current_speed = date.animation_speed

        if date.isWin():
            
            call label_after_successful_Date_common
            show blowjob v2 talk as joyce
            with dissolve
            j "Well done."
            j "Next time is the last trial."
            j "You waited for this a long time no?"
            play sound "rpg/Key.wav"
            show blowjob v2 lock as joyce
            with dissolve
            j "You'll get to fuck my nice little pussy"

            hide joyce with dissolve
                
            call label_newDay("label_prison")
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop

    # This ends the game.

    return



label label_blowjob_SexEndTurn:
    $ game.jeu_sensitive = False

    $ i=0
    while i < date.animation_speed:
        $ date.lust += 1
        $ date.orgasm += 1
        $ i += 1
        pause(0.1)
    
    $ date.speedUp()
    
    if date.isLost():
        hide screen screen_sex_ui with dissolve

        "i'm gonna cum!"

        if "v2" in renpy.get_attributes("joyce"):
            $ phase = 2
            show blowjob v2 cum (1) as joyce with dissolve
            pause 1.0
            play sound "sex/Poison-cum.wav"
            pause 1.0
            show blowjob v2 cum (2) as joyce
            play sound "sex/swallow.wav"
            pause 0.4
            show blowjob v2 cum (3) as joyce
            pause 0.4
            show blowjob v2 cum (4) as joyce
            with dissolve
            pause
            show blowjob v2 talk as joyce with dissolve
            j "That was yummy"
            j "But you failed again"
            play sound "rpg/Key.wav"
            show blowjob v2 lock as joyce with dissolve
            pause 
        else:
            $ phase = 1
            pause 0.2
            show blowjob cum (1) as joyce
            play sound "sex/Poison-cum.wav"
            pause 1.0
            show blowjob cum (2) as joyce
            with dissolve
            pause
            j "time to lock you"
            play sound "rpg/Key.wav"
            show blowjob lock with dissolve
            pause

        $ game.lust = 0
        call label_newDay("label_prison")

    if date.turn == 2:
        j "You're holding out well"
        # play sound "sex/undress.wav"
        show joyce blowjob v2 as joyce with dissolve
        pause
        call label_add_card_to_deck("hand", Card("peek4"), pauseTime=1.0)
        pause 0.5
    elif date.turn > 5:
        call label_add_card_to_deck("hand", Card("peek4"))
        pause 0.5
    call label_endTurn_common
    return
