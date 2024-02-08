label label_sex_tutorial:

    scene bg prison-ground
    show joyce footjob talk
    show screen screen_dick_ui
    with dissolve
    pause
    j "Are you ready for your first exam?"
    j "Can you guess what is it?"
    j "Here's a hint"
    show joyce footjob hint with dissolve
    window hide
    pause
    window auto
    j "So, did you guess?"
    j "I'm gonna rub your dick."
    j "With my feet."
    j "You must have been waiting for this no?" 
    show joyce footjob talk with dissolve
    j "First, let's release this bad boy."
    play sound "rpg/Key.wav"
    show get-hard 1 as anim with dissolve
    j "Can you get hard for me baby?"
    j "I'll make you feel so good."
    pause 0.4
    show get-hard 2 as anim
    pause 0.4
    show get-hard 3 as anim
    pause 0.4
    show get-hard 4 as anim
    pause 0.4
    show get-hard 5 as anim
    pause
    j "Wow"
    j "You have a nice big cock."
    j "I did well picking you."
    j "Let me explain how this works."
    show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
    j "This is your Lust."
    j "If you get too excited, you'll cum and fail."
    j "How do you get excited? Well for example..."
    hide anim
    show joyce footjob 1
    with dissolve

    show joyce footjob 2
    pause 0.1
    show joyce footjob 3
    pause 0.1
    show joyce footjob 4
    pause 0.1
    show joyce footjob 3
    pause 0.1
    show joyce footjob 2
    pause 0.1
    show joyce footjob 1
    pause 0.1
    $ game.lust += 1
    $ date.lust += 1
    with blinds
    j "There, you got a little bit excited."
    j "Depending on the speed I'm going, you'll get more and more excited."
    j "I'll start slow and go faster every turn."
    j "Your goal is to resist for {b}6 turns{/b}"
    j "Resist this, and you'll get to the next trial."
    j "Fail, and you'll have to take this exam again in 3 days."
    hide screen screen_tutorial with dissolve
    j "Ready?"
    show joyce footjob
    $ date = Date("sex", endTurn = "label_footjob_endTurn", turnLeft=5, isWin = "date.turnLeft <= 0", lustPerTurn=20)
    call label_beginDuel_common() from _call_label_beginDuel_common_5
    hide screen screen_dick_ui
    $ current_speed = date.animation_speed
    jump label_footjob_gameLoop

label label_footjob:

    if game.progress[1] == -1 and not (_in_replay or game.debug_mode):
        jump label_sex_tutorial

    $ date = Date("sex", endTurn = "label_footjob_endTurn", turnLeft=5, isWin = "date.turnLeft <= 0", lustPerTurn=20)
    scene bg prison-ground
    show joyce footjob talk
    with dissolve

    j "Hello, my slave. "
    j "Are you getting used to your new room?"
    j "You did good holding it in so far."
    j "Does it hurt?"
    j "First, let's release this bad boy."
    play sound "rpg/Key.wav"
    show joyce get-hard 1 with dissolve
    pause
    j "Now, can you get hard for me baby?"
    pause 0.4
    show joyce get-hard 2
    pause 0.4
    show joyce get-hard 3
    pause 0.4
    show joyce get-hard 4
    pause 0.4
    show joyce get-hard 5
    pause
    j "Good boy."
    j "You're a good boy with a nice, big cock."
    j "Resist this, and you'll get to the next trial."
    j "Fail, and you'll have to start this again."
    show joyce footjob 1 -get-hard
    with dissolve
    j "Are you ready?"

    call label_beginDuel_common() from _call_label_beginDuel_common_6
    # $ current_speed = date.animation_speed

    j "I'll start moving."
    
    show joyce -1 

    call label_footjob_gameLoop from _call_label_footjob_gameLoop
    return

label label_footjob_gameLoop:
    $ phase = 1
    $ date.animation_speed = 0
    label .gameLoop:
        $ game.jeu_sensitive = False

        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_6

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        jump .gameLoop


label label_footjob_endTurn:
    $ game.jeu_sensitive = False

    $ i=0
    while i < date.lustPerTurn:
        $ date.lust += 1
        $ date.orgasm += 1
        $ i += 1
        pause(0.05)
    
    $ date.speedUp()
    
    if "v2" in renpy.get_attributes("joyce"):
        show joyce footjob v2
    else:
        show joyce footjob
    pause 0.2
    
    if date.isLost():
        call label_footjob_isLost
        call label_newDay("label_prison") from _call_label_newDay_16

    if date.turn == 1:
        call label_footjob_v2

    call label_endTurn_common from _call_label_endTurn_common_5

    if date.turn >= 2:
        call label_add_card_to_deck("hand", Card("peek2"), pauseTime=0.5) from _call_label_add_card_to_deck_12
        pause 0.5

    if date.isWin():
        
        call label_after_successful_Date_common from _call_label_after_successful_Date_common_5
        call label_footjob_isWin
        call label_newDay("label_prison") from _call_label_newDay_17


    return

label label_footjob_isLost:
    hide screen screen_sex_ui with dissolve

    $ update_animationSpeed(0.045)
    $ date.animation_speed = 0
    with dissolve

    pause 0.5

    "!"
    window hide
    window auto
    stop sound
    
    if phase == 1:
        show joyce footjob 1
    else:
        show joyce footjob v2 1
    pause 0.2
    play sound "sex/Poison-cum.wav"
    if phase == 1:
        show joyce footjob 1 at shaking
    else:
        show joyce footjob v2 1 at shaking
    show footjob cum 1 at shaking
    pause(0.15)
    show footjob cum 2
    pause(0.15)
    show footjob cum 3
    pause(0.5)
    show footjob cum 4
    pause(0.3)
    show footjob cummed at default
    
    if phase == 1:
        show joyce footjob 1 at default
    else:
        show joyce footjob v2 1 at default
    pause 0.4
    
    $ game.lust = 0
    pause
    j "You naughty boy, you just couldn't resist, could you?"
    j "You just came all over me ew"
    j "I'm all sticky."
    j "You failed this exam."
    j "Time to lock you up again"
    play sound "rpg/Key.wav"
    if phase == 1:
        show joyce footjob talk with dissolve
    else:
        show joyce footjob v2 talk with dissolve
    j "Try again next time"
    return

label label_footjob_v2:
    $ phase = 2
    show joyce footjob 1 with dissolve
    j "You're holding out well"
    j "How about I make it a bit more challenging?"
    j "I'll show you things you've never seen."
    play sound "sex/undress.wav"
    show joyce footjob v2 1 with dissolve
    pause

    $ date.speedUp()
    $ date.lustPerTurn += 10

    pause 0.5
    return

label label_footjob_isWin:
    stop sound
    show joyce footjob v2 talk
    with dissolve
    j "Well done."
    j "You'll move to the next trial."
    j "Until then..."
    play sound "rpg/Key.wav"
    show joyce footjob v2 talk 2 with dissolve
    j "Try not to burst."

    hide joyce with dissolve
    return