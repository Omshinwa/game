label label_handjob:
    $ date = Date("sex", endTurn = "label_handjob_SexEndTurn", turnLeft=10, isWin = "date.turnLeft <= 0")

    scene bg basement
    show handjob talk as joyce
    with dissolve
    # show moan_bubble

    j "Are you ready?"

    play sound "rpg/Key.wav"
    show handjob get-hard (1) as anim with dissolve
    pause
    j "How does it feel being finally free?"
    j "Now, can you get hard for me baby?"
    pause 0.4
    show handjob get-hard (2) as anim
    pause 0.4
    show handjob get-hard (3) as anim
    pause

    call label_beginDuel_common()
    $ current_speed = date.animation_speed

    j "ready?"
    j "I'll start moving."
    hide anim
    show joyce handjob with dissolve
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            if "v2" in renpy.get_attributes("joyce"):
                show joyce handjob v2
            else:
                show joyce handjob

            $ current_speed = date.animation_speed

        if date.isWin():
            
            call label_after_successful_Date_common
            stop sound
            show handjob talk as joyce
            show get-hard (5) as anim
            with dissolve
            j "Well done."
            j "You'll move to the next trial."
            j "Until then..."
            play sound "rpg/Key.wav"
            hide anim with dissolve
            j "Try to not bust out hehee.."

            hide joyce with dissolve
                
            call label_newDay("label_prison")
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop

    # This ends the game.

    return



label label_handjob_SexEndTurn:
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
        stop sound
        
        play sound "sex/Poison-cum.wav"
        if "v2" in renpy.get_attributes("joyce"):
            $ phase = 2
            show handjob v2 (1) as joyce
            show handjob v2 cum (1) as anim
            pause 1.0
            # show handjob v2 (4) as joyce
            show handjob v2 cum (2) as anim
            with dissolve
            pause 1.0
            show handjob v2 talk as joyce
            show handjob v2 cum (2) as anim
            with dissolve
        else:
            $ phase = 1
            show handjob cum (1) as joyce
            pause 1.0
            show handjob (4) as joyce
            show handjob cum (2) as anim
            with dissolve
            pause
            # show handjob talk as joyce with dissolve
            # show handjob cum (2) as anim
        
        while date.lust>0:
            $ date.lust -= 1
            pause(0)

        $ game.lust = 0
        j "soo disappointing hehe"
        j "try again next week."
        j "time to lock you up again"
        play sound "rpg/Key.wav"
        if phase == 1:
            hide anim
            show handjob lock as joyce
            with dissolve
        else:
            hide anim
            show handjob v2 lock as joyce
            with dissolve
        j "I hoped you would have lasted"

        call label_newDay("label_prison")

    if date.turn == 2:
        j "You're holding out well"
        # play sound "sex/undress.wav"
        show joyce handjob v2 as joyce with dissolve
        pause
        call label_add_card_to_deck("hand", Card("peek4"), pauseTime=1.0)
        pause 0.5
    elif date.turn > 5:
        call label_add_card_to_deck("hand", Card("peek4"))
        pause 0.5
    call label_endTurn_common
    return
