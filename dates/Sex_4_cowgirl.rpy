label label_cowgirl:
    $ date = Date("sex", endTurn = "label_cowgirl_SexEndTurn", isWin = "date.orgasm>=date.orgasmMax")

    scene bg basement
    show cowgirl talk as joyce
    with dissolve

    j "Are you ready?"

    play sound "rpg/Key.wav"
    show cowgirl get-hard (1) as joyce with dissolve
    pause
    j "You must have been waiting for this no?" 
    j "How does it feel being finally free?"
    j "Now, can you get hard for me baby?"
    pause 0.4
    show cowgirl get-hard (2) as joyce
    pause 0.4
    show cowgirl get-hard (3) as joyce
    pause

    call label_beginDuel_common()
    $ current_speed = date.animation_speed

    j "ready?"
    show cowgirl insert as joyce
    j "Finally I get to taste this dick"
    j "I've waited so long for this"
    show cowgirl (6) as joyce 
    play sound "sex/slap.wav"
    j "Oh my god yes"
    j "Your dick feels so good."
    pause

    show joyce cowgirl with dissolve
    show moan_bubble
    $ renpy.music.play("sex/moans.wav", channel="sexvoice", loop=True)

    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            show joyce cowgirl
            show moan_bubble
            $ current_speed = date.animation_speed

        if date.isWin():
            if date.orgasmMax == 20:
                $ renpy.music.play("sex/moans2.wav", channel="sexvoice", loop=True)
                $ date.speedUp()
                show joyce
                j "i'm..{w=1.0}{nw}"
                $ date.speedUp()
                show joyce
                j "it's coming !{w=1.0}{nw}"
                $ date.speedUp()
                show joyce
                show cowgirl orgasm (2) at shaking as joyce with vpunch
                $ renpy.music.play("sex/moans_climax.wav", channel="sexvoice", loop=True)
                hide moan_bubble
                j "kyaaa{w=1.0}{nw}"
                pause(2.76)
                stop sexvoice fadeout 0.2
                show cowgirl (2) as joyce at default with dissolve
                pause(1)
                j "huff.."
                j "t-that doesn't count"
                j "w-we keep going.."
                show joyce cowgirl
                $ date.orgasm = 0
                $ date.orgasmMax = 30
            else:
                call label_after_successful_Date_common
                $ renpy.music.play("sex/moans3.wav", channel="sexvoice", loop=True)
                j "I'm gonna{w=1.0}{nw}"
                $ date.speedUp()
                show joyce
                j "mHHHnhh{w=1.0}{nw}"
                $ date.speedUp()
                show joyce
                j "go inSANE{w=1.0}{nw}"
                $ date.speedUp()
                show joyce
                j "yOU'RE gonna bREAK my PUssy{w=2.0}{nw}"
                $ date.speedUp()
                show joyce
                j "i'm coMING{w=1.0}{nw}"
                pause
                show cowgirl orgasm (3) as joyce at shaking with vpunch
                $ renpy.music.play("sex/moans_climax.wav", channel="sexvoice", loop=True)
                j "gNHUUUUUU{w=1.0}{nw}"
                j "It's shoo goood{w=1.0}{nw}"
                j "nhhggGGHUUU{w=1.0}{nw}"
                j "NGOooOOOO{w=1.0}{nw}"
                pause(2)
                stop sexvoice fadeout 0.2
                hide moan_bubble
                pause(1)
                show cowgirl orgasm (3) as joyce at default
                pause
                play sound "sex/Fouet.mp3" volume 0.5
                show cowgirl orgasm (4) as joyce at default with vpunch
                pause
                show cowgirl orgasm (5) as joyce with dissolve
                pause(0.3)
                show cowgirl orgasm (6) as joyce with dissolve
                pause(0.3)
                show cowgirl orgasm (7) as joyce with dissolve
                pause(0.3)
                show cowgirl orgasm (8) as joyce with dissolve
                pause(0.3)
                "It seems like she's unconscious..."
                "You take this opportunity to escape"
                play sound "sex/undress.wav"
                show black onlayer screens

                $ game.state = "living"
                $ game.jeu_sensitive = False
                scene bg prison
                show screen screen_prison_sans_rat onlayer master
                show black onlayer screens
                hide black onlayer screens with Dissolve(2.0)
                
                jump label_home_end
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop

    # This ends the game.

    return



label label_cowgirl_SexEndTurn:
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

        $ phase = 1
        pause 0.2
        show cowgirl (3) as joyce
        play sound "sex/Poison-cum.wav"
        pause 1.0
        j "Are you trying to make me pregnant?"
        j "My belly is full of your sperm"
        show cowgirl cum-out (1) as joyce with dissolve
        pause 0.4
        show cowgirl cum-out (2) as joyce with dissolve
        pause 0.4
        show cowgirl cum-out (3) as joyce with dissolve
        pause
        j "time to lock you"
        play sound "rpg/Key.wav"
        show cowgirl lock with dissolve
        pause

        $ game.lust = 0
        call label_newDay("label_prison")

    if date.turn == 2:
        j "You're holding out well"
        # play sound "sex/undress.wav"
        show joyce cowgirl v2 as joyce with dissolve
        pause
        call label_add_card_to_deck("hand", Card("peek4"), pauseTime=1.0)
        pause 0.5
    elif date.turn > 5:
        call label_add_card_to_deck("hand", Card("peek4"))
        pause 0.5
    call label_endTurn_common
    return