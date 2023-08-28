label label_sex_tutorial:
    $ date = Date("sex", endTurn = "label_footjob_SexEndTurn", turnLeft=6, isWin = "date.turnLeft <= 0")

    scene bg prison-ground
    show footjob talk as joyce
    show screen screen_lust_ui
    with dissolve
    pause
    j "Are you ready for your first exam?"
    j "Can you guess what is it?"
    j "Here's a hint"
    show footjob hint as joyce with dissolve
    window hide
    pause
    window auto
    j "So, did you guess?"
    j "I'm gonna rub your dick."
    j "With my feet."
    j "You must have been waiting for this no?" 
    show footjob talk as joyce with dissolve
    j "First, let's release this bad boy."
    play sound "rpg/Key.wav"
    show get-hard (1) as anim with dissolve
    j "Can you get hard for me baby?"
    j "I'll make you feel really good."
    pause 0.4
    show get-hard (2) as anim
    pause 0.4
    show get-hard (3) as anim
    pause 0.4
    show get-hard (4) as anim
    pause 0.4
    show get-hard (5) as anim
    pause
    j "Wow"
    j "You're a good boy with a nice big cock."
    j "I did well picking you"
    j "Let me explain how this work."
    show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
    j "This is your dick strength."
    j "If you get too excited, you'll cum and fail."
    j "How do you get excited? Well for example..."
    hide anim
    show footjob (1) as joyce
    with dissolve

    show footjob (2) as joyce
    pause 0.1
    show footjob (3) as joyce
    pause 0.1
    show footjob (4) as joyce
    pause 0.1
    show footjob (3) as joyce
    pause 0.1
    show footjob (2) as joyce
    pause 0.1
    show footjob (1) as joyce
    pause 0.1
    $ game.lust += 1
    $ date.lust += 1
    with blinds
    j "There, you got a little bit excited."
    j "Depending on the speed I'm going, you'll get more and more excited."
    j "I'll start slow and go faster every turn."
    j "Your goal is to resist for {b}[date.turnLeft] turns{/b}"
    j "Resist this, and you'll get to the next trial."
    j "Fail, and you'll have to do this exam again in 3 days."
    hide screen screen_tutorial with dissolve

    j "Ready?"
    show joyce footjob
    call label_beginDuel_common()
    $ current_speed = date.animation_speed
    jump label_footjob_gameLoop

label label_footjob:

    if game.progress[1] == -1:
        jump label_sex_tutorial

    $ date = Date("sex", endTurn = "label_footjob_SexEndTurn", turnLeft=6, isWin = "date.turnLeft <= 0")
    scene bg basement
    show footjob talk as joyce
    with Dissolve

    j "Hello my good boy"
    j "Are you getting used to your new room?"
    j "You did good holding it in so far."
    j "Are you in pain?"
    j "First, let's release this bad boy."
    play sound "rpg/Key.wav"
    show get-hard (1) as anim with dissolve
    pause
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
    j "You're a good boy with a nice big cock."
    j "Resist this, and you'll get to the next trial."
    j "Fail, and you'll have to start this again."
    hide anim
    show footjob (1) as joyce
    with dissolve
    j "Are you ready?"

    call label_beginDuel_common()
    $ current_speed = date.animation_speed

    j "I'll start moving."
    
    show joyce footjob

    call label_footjob_gameLoop
    return

label label_footjob_gameLoop:
    $ phase = 1
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            if "v2" in renpy.get_attributes("joyce"):
                show joyce footjob v2
            else:
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
            
            if game.progress[1] == -1:
                call label_newDay("label_prison")
            else:
                call label_newDay("label_prison_first_time")

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        jump .gameLoop



label label_footjob_SexEndTurn:
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
        window hide
        window auto
        stop sound
        if phase == 1:
            show footjob (1) as joyce
        else:
            show footjob v2 (1) as joyce
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
        if phase == 1:
            show end-cummed as anim
        else:
            show end-cummed2 as anim
        
        while date.lust>0:
            $ date.lust -= 1
            pause(0)

        $ game.lust = 0
        pause
        j "You naughty boy, you just couldn't resist?"
        j "You just came all over me ew"
        j "I'm all sticky."
        j "You failed this exam."
        j "Time to lock you up again"
        play sound "rpg/Key.wav"
        if date.turn<=5:
            show footjob talk as joyce with dissolve
        else:
            show footjob v2 talk as joyce with dissolve
        j "Try again next time"

        if game.progress[1] == -1:
            call label_newDay("label_prison")
        else:
            call label_newDay("label_prison_first_time")

    if date.turn == 5:
        $ phase = 2
        show footjob (1) as joyce with dissolve
        j "You're holding out well"
        j "How about I make it a bit more challenging?"
        j "Let me get more comfy"
        play sound "sex/undress.wav"
        show footjob v2 (1) as joyce with dissolve
        pause
        
        call label_add_card_to_deck("hand", Card("peek4"), pauseTime=1.0)
        j "ready?"
        # (add cards to deck)

        show joyce footjob v2 as joyce with dissolve
        pause
    elif date.turn > 5:
        call label_add_card_to_deck("hand", Card("peek4"))
        pause 0.5
    call label_endTurn_common
    return
