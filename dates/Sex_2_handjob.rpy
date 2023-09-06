label label_handjob:
    $ date = Date("sex", endTurn = "label_handjob_SexEndTurn", turnLeft=7, isWin = "date.turnLeft <= 0")

    scene bg basement
    show handjob talk as joyce
    with dissolve

    if game.progress[1] == -1:
        j "Hehe"
        j "Let's go somewhere a bit more comfortable for this exam."
        j "I don't want my slave to catch a cold lying on the concrete here."

        j "What do you think the test will be this time?"
        j "Let's free you."

        play sound "rpg/Key.wav"
        show handjob get-hard (1) as anim with dissolve
        pause
        j "You must have felt cramped in there."
        j "With that big juicy dick."
        pause 0.4
        show handjob get-hard (2) as anim
        pause 0.4
        show handjob get-hard (3) as anim
        pause
        j "How come you got hard on your own?"
        j "Do you enjoy being raped?"
        j "Do you want me to rape you more?"
        j "What a disgusting pervert."
        j "Someone like you.."
        j "deserves to be punished."
    else:
        j "There you are, my little slut."
        play sound "rpg/Key.wav"
        show handjob get-hard (1) as anim with dissolve
        pause
        j "How does it feel?"
        pause 0.4
        show handjob get-hard (2) as anim
        pause 0.4
        show handjob get-hard (3) as anim
        pause
        j "Seems like it feels good"
        j "I'll make you feel even better.."

    call label_beginDuel_common() from _call_label_beginDuel_common_7
    $ current_speed = date.animation_speed

    hide anim
    show joyce handjob
    with dissolve
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            if "v2" in renpy.get_attributes("joyce"):
                show joyce handjob v2
            else:
                show joyce handjob

            $ current_speed = date.animation_speed
    
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_7

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop from _call_label_handjob_gameLoop

    # This ends the game.

    return

label label_handjob_SexEndTurn:
    $ game.jeu_sensitive = False

    $ i=0
    while i < date.animation_lust[date.animation_speed]:
        $ date.lust += 1
        $ date.orgasm += 1
        $ i += 1
        pause(1.0/ date.animation_lust[date.animation_speed])
    
    $ date.speedUp()
    if "v2" in renpy.get_attributes("joyce"):
        show joyce handjob v2
    else:
        show joyce handjob
    pause 0.5
    $ date.speedUp()
    if "v2" in renpy.get_attributes("joyce"):
        show joyce handjob v2
    else:
        show joyce handjob
    
    if date.isLost():
        hide screen screen_sex_ui with dissolve

        $ date.animation_speed_hash[0] = 2.2
        $ date.animation_speed = 0
        with dissolve
        
        "!"
        window hide
        window auto
        stop sound
        
        $ date.animation_speed = 1
        pause 0.5
        
        play sound "sex/Poison-cum.wav"
        if "v2" in renpy.get_attributes("joyce"):
            $ phase = 2
            show handjob v2 (1) as joyce at shaking
            show handjob v2 cum (1) as anim at shaking
            pause 1.5
            show handjob v2 talk as joyce at default
            show handjob v2 cum (2) as anim at default
            with dissolve
        else:
            $ phase = 1
            show handjob cum (1) as joyce at shaking
            pause 1.5
            show handjob (4) as joyce at default
            show handjob cum (2) as anim at default
            with dissolve
            pause
            with dissolve
            # show handjob talk as joyce with dissolve
            # show handjob cum (2) as anim
        
        while date.lust>0:
            $ date.lust -= 1
            pause(0)

        $ game.lust = 0
        j "Such a big load"
        j "Wasted here."
        j "You should have saved it for my pussy."
        j "Oh well"
        play sound "rpg/Key.wav"
        if phase == 1:
            hide anim
            show handjob lock as joyce
            with dissolve
        else:
            hide anim
            show handjob v2 lock as joyce
            with dissolve
        j "Build more sperm for me honey."

        call label_newDay("label_prison") from _call_label_newDay_18

    if date.turn == 3:
        show handjob (3) as joyce with dissolve
        j "Are you getting used to this?"
        j "How about this?"
        # play sound "sex/undress.wav"
        show handjob v2 (1) as joyce with dissolve
        pause
        show handjob v2 (2) as joyce
        pause 0.1
        show handjob v2 (3) as joyce
        pause 0.1
        show handjob v2 (4) as joyce
        pause 0.1
        j "Mhh Delicious"
        show joyce handjob v2 as joyce with dissolve
        # pause
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=1.0) from _call_label_add_card_to_deck_13   
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=0.3) from _call_label_add_card_to_deck_14   
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=0.3) from _call_label_add_card_to_deck_15 
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=0.3) from _call_label_add_card_to_deck_16 

        $ date.animation_speed_hash[10] = 2.0

        $ date.speedUp()
        show joyce handjob v2
        pause 0.5
        $ date.speedUp()
        show joyce handjob v2

    elif date.turn > 3:
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=1.0) from _call_label_add_card_to_deck_17   
        pause 0.5
    call label_endTurn_common from _call_label_endTurn_common_6

    if date.isWin():
            
            call label_after_successful_Date_common from _call_label_after_successful_Date_common_6
            stop sound
            show handjob talk as joyce
            show handjob get-hard (3) as anim
            with dissolve
            j "Well done."
            j "You'll move to the next trial."
            j "Until then..."
            play sound "rpg/Key.wav"
            hide anim with dissolve
            j "Take care of him."

            hide joyce with dissolve
                
            call label_newDay("label_prison") from _call_label_newDay_19

    return
