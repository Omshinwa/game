label label_footjob:
    $ game.state = "sexing"
    $ date = Date(endTurn = "label_footjob_SexEndTurn", turnLeft=10, isWin = "date.turnLeft <= 0")

    scene bg basement
    show footjob-start-talk as joyce
    with dissolve
    # show moan_bubble

    j "Are you ready for your first test?"
    j "Can you guess what is it?"
    j "Here's a hint"
    show footjob-start-hint as joyce with dissolve
    window hide
    pause
    window auto
    j "So, did you guess?"
    j "I'm gonna masturbate you."
    j "With my feet."
    j "Will you be able to hold it in?"
    show footjob-start-talk as joyce with dissolve
    j "First, let's release this bad boy."
    j "You must have been waiting for this no?" 
    play sound "rpg/Key.wav"
    show get-hard (1) as anim with dissolve
    pause
    j "How does it feel being finally free?"
    j "Now, can you get hard for me baby?"
    pause 0.4
    show get-hard (2) as anim
    pause 0.4
    show get-hard (3) as anim
    pause 0.4
    show get-hard (4) as anim
    pause 0.4
    show get-hard (5) as anim
    pause
    j "Good boy."
    j "You're a good boy with a nice big dick."
    j "Resist this, and you'll get to the next trial."
    j "Fail, and you'll have to start this again."
    hide anim
    show footjob (1) as joyce
    with dissolve
    j "Are you ready?"

    call label_beginDuel_common()
    $ current_speed = date.animation_speed

    show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
    j "This is your dick strength."
    j "If you get too excited, you're gonna cum."
    j "If you cum, you fail the trial."
    j "Your goal is to resist for {b}10 turns{/b}"
    j "Got it?"
    hide screen screen_tutorial with dissolve

    j "Depending on the speed I'm going, each turn you'll gain a certain amount of lust."
    j "Every turn I'll go faster and faster."

    j "I'll put some Faster cards in your deck."
    j "think of it as me just moving naturally faster"
    j "Making you cum faster.. my big dick boy"

    call label_add_card_to_deck("deck", Card("faster"))
    call label_add_card_to_deck("deck", Card("faster"))
    call label_add_card_to_deck("deck", Card("faster"))
    call label_add_card_to_deck("deck", Card("faster"))
    call label_add_card_to_deck("deck", Card("faster"))

    j "ready?"
    j "I'll start moving."
    
    show joyce footjob
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            show joyce footjob
            # show moan_bubble
            $ current_speed = date.animation_speed

        if date.isWin():
            
            call label_after_successful_Date_common
            stop sound
            show footjob-start-talk as joyce
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



label label_footjob_SexEndTurn:
    $ game.jeu_sensitive = False

    $ i=0
    while i < date.animation_speed:
        $ date.lust += 1
        $ game.orgasm += 1
        $ i += 1
        pause(0.1)
    
    $ date.speedUp()
    
    if date.isLost():
        hide screen screen_sex_ui with dissolve

        "i'm gonna cum!"
        stop sound
        if "footjobv2" in renpy.get_attributes("joyce"):
            show expression "footjob v2 (1)" as joyce
        else:
            show expression "footjob (1)" as joyce
        pause 0.2
        play sound "sex/Poison-cum.wav"
        show cum1 as anim
        pause(0.3)
        show cum2 as anim
        pause(0.3)
        show cum3 as anim
        pause(0.3)
        show cum4 as anim
        pause(0.3)
        if "footjobv2" in renpy.get_attributes("joyce"):
            show end-cummed as anim
        else:
            show end-cummed2 as anim
        
        while date.lust>0:
            $ date.lust -= 1
            pause(0)

        $ game.lust = 0
        j "soo disappointing hehe"
        j "try again next week."
        play sound "rpg/Key.wav"
        show footjob-start-talk as joyce with dissolve
        j "time to lock you up again"

        call label_newDay("label_prison")

    if date.turn == 5:
        j "You're holding out well"
        j "How about I make it a bit more challenging?"
        j "Let me get more comfy"
        play sound "sex/undress.wav"
        show joyce footjobv2 as joyce with dissolve
        pause
        call label_add_card_to_deck("hand", Card("peek4"), pauseTime=1.0)
        pause 0.5
    elif date.turn > 5:
        call label_add_card_to_deck("hand", Card("peek4"))
        pause 0.5
    call label_endTurn_common
    return
