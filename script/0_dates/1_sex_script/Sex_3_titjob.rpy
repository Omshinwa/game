"""
You looked at my boobs all this time
But you didnt expect to finally get a touch on them like this huh?
"""
label label_titjob:
    $ date = Date("sex", name="titjob", endTurn = "label_titjob_endTurn", turnLeft=7, isWin = "date.turnLeft <= 0")

    scene bg basement
    show joyce titjob talk
    with dissolve

    if game.progress[1] == -1:
        pause
        j "Hello sweetheart ♥"
        $ temp = game.day - g.day_rat_appears
        j "Have you noticed? It's been [temp] days we've been living together."
        j "[temp] days you haven't washed you're little dick."
        $ del temp
        play sound "rpg/soubi-01.ogg"
        show joyce titjob get-hard 1 with dissolve
        pause
        j -1 2 "Phew it smells here."
        j "But you're doing a good job so far."
        j -2 1 "You resisted cumming from my feet."
        j "And also from my hands."
        j "Now..."
        j -1 3 "What is today going to be?"
        show joyce -3 4 with dissolve
        pause 0.1
        j -4 3 "Whoops"
        j "Did you see anything?"
        show joyce -3 5 with dissolve
        show joyce -5 6 with dissolve
        pause
        j "Mhh, I guess you did."
        j "You don't miss a peek huh?"
        j -6 7 "So, do you know what's going to happen to you?"
        menu:
            "You're going to rape me with your tits.":
                j "Ding ding ding. You're correct."
        j "I'm gonna rape you."
        j -7 8 "With my big, slutty tits."

    else:
        j "Hello sweetheart ♥"
        play sound "rpg/soubi-01.ogg"
        show handjob get-hard 1 with dissolve
        pause
        j "You liked my tits so much you wanted to see them again huh?"
        j -1 2 "It's okay, we all have our weaknesses."
        show joyce -2 3 with dissolve
        j "And my weakness is..."
        pause 0.2
        show joyce -3 4 with dissolve
        pause 1.0
        show joyce -4 5 with dissolve
        pause 0.2
        show joyce -5 6 with dissolve
        j "This big juicy dick."

    call label_beginDuel_common()

    show joyce -get-hard -7 with dissolve
    
    label .gameLoop:
        $ game.jeu_sensitive = False
    
        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        # pause
        call screen screen_gameloop
        
    call .gameLoop

    return

label label_titjob_endTurn:
    
    $ date.speedUp()
    pause(0.5)
    $ date.speedUp()
    
    if date.isLost():
        call label_handjob_Lost
        call label_newDay("label_prison")

    if date.turn == 3:
        call label_handjob_v2

    elif date.turn > 3:
        call label_add_card_to_deck("deck", Card("peek2"), pauseTime=1.0)
        pause 0.5

    if date.isWin():
            
            call label_after_successful_Date_common
            call label_handjob_Win    
            call label_newDay("label_prison")

    return


label label_titjob_v2:
    show joyce 1 with dissolve
    j "Are you warmed up yet?"
    j "It's time to bring out the big guns."
    play sound "sex/undress.wav"
    show joyce v2 talk with fade
    pause
    j "Wow."
    j "Even my cow titties can't cover your whole dick."
    show joyce 2
    pause 0.1
    show joyce 3
    pause 0.1
    show joyce 4
    pause 0.1
    j "Do you feel the squeeze?"
    show joyce -4 talk with dissolve
    j "I'm gonna squeeze your cum out."
    show joyce -talk
    with dissolve
    pause
    return

label label_titjob_Lost:

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
    if has_attribute("v2"):
        show joyce v2 1 at shaking
        show titjob v2 cum 1 at shaking
        pause 1.5
        show joyce v2 talk at default
        show titjob v2 cum 2 at default
        with dissolve
    else:
        show joyce 1 at shaking
        show titjob cum 1 at shaking
        pause 1.5
        show joyce 1  at default
        show titjob cum 2 at default
        with dissolve
    
    while date.lust>0:
        $ date.lust -= 1
        pause(0)

    $ game.lust = 0
    
    
    j "Oh you're poured it all over my pretty face."
    j "What am I going to do?"
    if has_attribute("v2"):
        show titjob tongue v2 1 as tongue
        pause 0.5
        show titjob tongue v2 2 as tongue
        pause 0.5
        show titjob tongue v2 3 as tongue
        pause 0.5
    else:
        show titjob tongue 1 as tongue
        pause 0.5
        show titjob tongue 2 as tongue
        pause 0.5
        show titjob tongue 3 as tongue
        pause 0.5

    j wink "Not bad."
    play sound "rpg/soubi-01.ogg"
    hide tongue
    if has_attribute("v2"):
        show joyce lock
        show titjob cum v2 lock
        with dissolve
    else:
        show joyce lock
        show titjob cum lock
        with dissolve
        
    j "Go back to your cage now my pet."

    return

label label_titjob_Win:
    $ date.animation_speed = 0
    stop sound
    show joyce titjob talk
    with dissolve
    j "Hehe, well done, even my boobs weren't enough."
    j "Can you guess the next trial?"
    j "Think about it in your cage."
    play sound "rpg/soubi-01.ogg"
    show joyce lock with dissolve
    j "Until then."
    return

label label_titjob_undress:
    
    show joyce 1 with dissolve

    if has_attribute("v2"):
        j "Is seeing my boobs not enough for you?"
    else:
        j "Oh so now you want to see both boobs huh?"

    show black onlayer screens with dissolve
    $ date.naked = True
    
    show joyce naked
    pause 0.2
    play sound "sex/undress.wav"
    pause 1.0
    hide black onlayer screens with dissolve
    j "There, satisfied?"
    show joyce -1
    pause
    return