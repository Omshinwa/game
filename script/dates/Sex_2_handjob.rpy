# format for sex dates:

# label_POSITION
# label_POSITION_endTurn
# label_POSITION_v2       : when we enter the second phase
# label_POSITION_isLost
# label_POSITION_isWin

label label_handjob:
    $ date = Date("sex", name="handjob", endTurn = "label_handjob_endTurn", turnLeft=7, isWin = "date.turnLeft <= 0", lustPerTurn=10)

    scene bg basement
    show joyce handjob talk
    with dissolve

    if game.progress[1] == -1:
        j "Hehe"
        j "Let's go somewhere a bit more comfortable for this exam."
        j "I don't want my slave to catch a cold lying on the concrete here."

        j "What do you think the test will be this time?"
        j "Let's free you."

        play sound "rpg/Key.wav"
        show handjob get-hard 1 with dissolve
        pause
        j "You must have felt cramped in there."
        j "With that big juicy dick."
        pause 0.4
        show handjob get-hard 2
        pause 0.4
        show handjob get-hard 3
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
        show handjob get-hard 1 with dissolve
        pause
        j "How does it feel?"
        pause 0.4
        show handjob get-hard 2
        pause 0.4
        show handjob get-hard 3
        pause
        j "Seems like it feels good"
        j "Do you want me to touch your dick?"
        j "Oh yes you do, my little slut."
        j "I'll make you feel even better."

    call label_beginDuel_common() from _call_label_beginDuel_common_7
    $ current_speed = date.animation_speed
    $ update_animationSpeed()

    hide handjob
    show joyce -talk
    with dissolve

    # "this works somehow"

    # hide joyce
    # pause
    # show joyce handjob
    # "a"
    # hide joyce
    # show joyce handjob talk
    # "b"
    # show joyce -talk

    
    label .gameLoop:
        $ game.jeu_sensitive = False
    
        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop from _call_label_handjob_gameLoop

    return


label label_handjob_endTurn:
    $ game.jeu_sensitive = False

    call label_sex_endTurn()

    $ date.speedUp()
    $ date.lustPerTurn += 3
    pause(0.5)
    
    if date.isLost():
        call label_handjob_isLost
        call label_newDay("label_prison") from _call_label_newDay_18

    if date.turn == 3:
        call label_handjob_v2

    elif date.turn > 3:
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=1.0) from _call_label_add_card_to_deck_17   
        pause 0.5
    call label_endTurn_common from _call_label_endTurn_common_6

    if date.isWin():
            
            call label_after_successful_Date_common from _call_label_after_successful_Date_common_6
            call label_handjob_isWin    
            call label_newDay("label_prison") from _call_label_newDay_19

    return


label label_handjob_v2:
    hide handjob
    show joyce 3 with dissolve
    j "Are you getting used to this?"
    j "How about this?"
    show joyce v2 1 with dissolve
    pause
    show joyce 2
    pause 0.1
    show joyce 3
    pause 0.1
    show joyce 4
    pause 0.1
    j "Mhh Delicious."
    show joyce -4
    $ date.speedUp()
    $ date.lustPerTurn += 3
    with dissolve
    return

label label_handjob_isLost:

    hide screen screen_sex_ui
    $ update_animationSpeed(0.045)
    with dissolve
    
    "!"
    window hide
    window auto
    stop sound
    
    $ date.animation_speed = 0
    pause 0.5
    
    play sound "sex/_Poison-cum.wav"
    if "v2" in renpy.get_attributes("joyce"):
        $ phase = 2
        show joyce v2 1 at shaking
        show handjob v2 cum 1 at shaking
        pause 1.5
        show joyce v2 talk at default
        show handjob v2 cum 2 at default
        with dissolve
    else:
        $ phase = 1
        show handjob cum 1 at shaking
        show joyce 4 at shaking
        pause 1.5
        show joyce 4 at default
        show handjob cum 2 at default
        with dissolve
        pause 0.3
        with dissolve
    
    while date.lust>0:
        $ date.lust -= 1
        pause(0)

    $ game.lust = 0
    
    if phase == 1:
        show handjob eyeside v1 as eyes with dissolve
    j "Such a big load."
    j "Wasted here."
    j "You should have saved it for my pussy."
    j "Oh well."
    play sound "rpg/Key.wav"
    if phase == 1:
        hide eyes 

        show joyce talk
        show handjob cum talk
        with dissolve
    else:
        hide eyes 
        show joyce v2 lock
        with dissolve
        
    j "Build more sperm for me honey."

    return

label label_handjob_isWin:
    $ date.animation_speed = 0
    stop sound
    show joyce handjob talk
    show handjob get-hard 3
    with dissolve
    j "Well done."
    j "You'll move to the next trial."
    j "Until then..."
    play sound "rpg/Key.wav"
    hide handjob with dissolve
    j "Take care of him."
    
    # hide joyce with dissolve
    return