label label_cowgirl:
    $ date = Date("sex", endTurn = "label_cowgirl_SexEndTurn", isWin = "date.orgasm>=date.orgasmMax")

    scene bg basement
    show cowgirl talk as joyce
    with dissolve

    j "Are you ready?"

    play sound "rpg/Key.wav"
    show cowgirl get-hard (1) as joyce with dissolve

    if game.progress[1] == -1:
        pause
        j "This time there's not time limit."
        j "Whoever cums first, loses."
        j "[povname]..."
        j "Lemme see your big juicy dick again"
        j "Get hard so I can slide your dick into my pussy"
        j "I'm already wet for you baby."
        j "Don't you want to feel the walls of my pussy?"
    pause 0.4
    show cowgirl get-hard (2) as joyce
    pause 0.4
    show cowgirl get-hard (3) as joyce
    pause

    if game.progress[1] == -1:
        j "Thank you daddy"
        j "Say [povname]."
        j "Do you still like me?"
        j "Do you forgive me for raping you?"
        menu:
            "Fuck me already":
                j "Yes daddy."
                j "Everything for you."
                show cowgirl insert as joyce with dissolve
                j "Please fuck me."
            "You're a bitch":
                j "Oh yes I'm a bitch."
                j "But I'm your only bitch daddy."
                j "Please only fuck my pussy."
                show cowgirl insert as joyce with dissolve
        j "My pussy is only yours."
        j "Do you feel how wet I am?"
    else:
        j "Sorry if I get loud."
        j "I've waited so long for this."
    show cowgirl (6) as joyce 
    pause 0.4
    play sound "sex/sloppy.wav"
    show cowgirl (1) as joyce with dissolve
    pause 0.4
    j "Oh my god yes"
    j "Your dick feels so good."
    show cowgirl (2) as joyce with dissolve
    j "fuck me daddy"

    call label_beginDuel_common() from _call_label_beginDuel_common_9
    $ current_speed = date.animation_speed
    show joyce cowgirl with dissolve
    show moan_bubble
    $ renpy.music.play("sex/moans.wav", channel="sexvoice", loop=True)
    $ phase = 1
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            show joyce cowgirl
            show moan_bubble
            $ current_speed = date.animation_speed

        if date.isWin():
            hide screen screen_sex_ui with dissolve

            if phase == 1:
                $ renpy.music.play("sex/moans2.wav", channel="sexvoice", loop=True)
                $ date.speedUp()
                show joyce
                j "i'm..{w=1.0}{nw}"
                $ date.speedUp()
                show joyce
                j "it's coming !{w=1.0}{nw}"
                $ date.speedUp()
                show cowgirl (3) as joyce with dissolve 
                pause 0.3
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
                $ date.animation_speed = 0
                $ date.orgasm = 0
                $ date.orgasmMax = 50
                $ phase = 2
                
                $ date.animation_speed_hash = { 0:0.5, 1:0.75, 2:1.0, 3:1.3, 4:1.6, 5:2.0}
                show joyce cowgirl
                $ renpy.music.play("sex/moans.wav", channel="sexvoice", loop=True)
            else:
                call label_after_successful_Date_common from _call_label_after_successful_Date_common_8
                $ renpy.music.play("sex/moans3.wav", channel="sexvoice", loop=True)
                $ date.animation_speed_hash = { 0:0.5, 1:0.75, 2:1.0, 3:1.3, 4:1.6, 5:2.0, 6:2.2, 7:2.5}
                j "I'm gonna"
                $ date.speedUp()
                show joyce
                j "mHHHnhh"
                $ date.speedUp()
                show joyce
                j "go inSANE"
                $ date.speedUp()
                show joyce
                j "yOU'RE gonna bREAK my PUssy [povname]"
                $ date.speedUp()
                show joyce
                j "it'sh sho GOOOOOD"
                j "i'm coMING"
                
                $ date.animation_speed = 0
                show joyce
                pause 0.5

                show cowgirl orgasm (3) as joyce at shaking with vpunch
                $ renpy.music.play("sex/moans_climax.wav", channel="sexvoice", loop=True)
                j "gNHUUUUUU{w=2.0}{nw}"
                j "NGOooOOOO{w=1.0}{nw}"
                j "nhhggGGHUUU{w=2.0}{nw}"
                pause(2)
                stop sexvoice fadeout 0.2
                hide moan_bubble
                pause(1)
                show cowgirl orgasm (3) as joyce at default
                pause 0.3
                show cowgirl orgasm (3) as joyce at slowbreath
                $ renpy.music.play("sex/heavy-breathing.wav", channel="sexvoice", loop=True, relative_volume=0.5)
                pause
                stop sexvoice
                play sound "sex/Fouet.mp3" volume 0.4
                show cowgirl orgasm (4) as joyce at default with vpunch
                pause
                show cowgirl orgasm (5) as joyce with dissolve
                pause(0.3)
                play sound "sex/cum-out.mp3"
                show cowgirl orgasm (6) as joyce with dissolve
                pause(0.3)
                show cowgirl orgasm (7) as joyce with dissolve
                pause(0.3)
                show cowgirl orgasm (8) as joyce with dissolve
                pause
                "It seems like she's unconscious..."
                "You take this opportunity to escape."
                window hide
                window auto
                play sound "sex/undress.wav"
                show black
                pause 2.0
                $ game.state = "living"
                $ game.jeu_sensitive = False

                $ g.phoneProgress[0] = 9
                $ g.phoneProgress[1] = 0

                jump label_home_end

            show screen screen_sex_ui with dissolve

        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_9

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop from _call_label_cowgirl_gameLoop

    # This ends the game.

    return



label label_cowgirl_SexEndTurn:
    $ game.jeu_sensitive = False

    $ i=0
    while i < date.animation_lust[date.animation_speed]:
        $ date.lust += 1
        $ date.orgasm += 1
        $ i += 1
        pause(1.0/ date.animation_lust[date.animation_speed])
    
    $ date.speedUp()
    
    if date.isLost():
        hide screen screen_sex_ui with dissolve

        $ date.animation_speed_hash[0] = 2.2
        $ date.animation_speed = 0
        show joyce
        with dissolve
        
        "!"
        window hide
        window auto
        stop sound
        stop sexvoice

        hide moan_bubble
        show joyce at shaking
        with dissolve
        play sound "sex/Poison-cum.wav"
        pause 0.1
        show cowgirl (3) as joyce at shaking with dissolve
        pause 0.5
        show cowgirl (3) as joyce at default
        pause
        j "Daddy, did you cum?"
        j "Are you trying to make me pregnant?"
        j "My belly is full of your sperm."
        show cowgirl cum-out (1) as joyce with dissolve
        pause 0.4
        play sound "sex/cum-out.mp3"
        show cowgirl cum-out (2) as joyce with dissolve
        pause 0.4
        show cowgirl cum-out (3) as joyce with dissolve
        pause
        j "Thanks you daddy, now go back to jail."
        play sound "rpg/Key.wav"
        show cowgirl lock as joyce with dissolve
        pause
        j "Hehe I don't think you'll make me cum ever."
        j "But I'll let you try as many times as you want daddy."
        $ date.lust = 0
        $ game.lust = 0
        call label_newDay("label_prison") from _call_label_newDay_22

    call label_endTurn_common from _call_label_endTurn_common_8
    return