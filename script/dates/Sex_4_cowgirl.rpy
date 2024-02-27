label label_cowgirl:
    $ date = Date("sex", name="cowgirl", endTurn = "label_cowgirl_SexEndTurn", isWin = "date.orgasm>=date.orgasmMax")

    scene bg living-room
    show joyce cowgirl talk
    with dissolve

    j "Ready?"

    play sound "rpg/Key.wav"
    show joyce get-hard 1 with dissolve

    if game.progress[1] == -1:
        pause
        j "This time there's no time limit."
        j "Whoever cums first, loses."
        j "[povname]..."
        j "I'm already wet."
        j "Let me see that big juicy dick again"
        j "Get hard for me"
        j "I want to slide it right into my pussy."
    pause 0.4
    show joyce get-hard 2
    pause 0.4
    show joyce get-hard 3
    pause

    if game.progress[1] == -1:
        j "[povname],"
        j "Do you still like me?"
        j "Do you forgive me for raping you?"
        menu:
            "Fuck me already":
                j "Yes daddy."
                j "Anything for you."
                show joyce insert with dissolve
                j "Please fuck me."
            "You're a bitch":
                j "Oh yes I'm a bitch."
                j "But I'm your bitch, daddy."
                j "Forget any other girl."
                show joyce insert with dissolve
        j "My pussy is only yours."
        j "Can you feel how wet I am?"
    else:
        j "Sorry if I get loud."
        j "I've been waiting so long for this."
    play sound "sex/sloppy.wav"
    show joyce 6 with dissolve
    pause 0.4
    j "Oh my god yes."
    play sound "sex/sloppy.wav"
    show joyce 1 with dissolve
    pause 0.4
    j "Your dick feels so good."
    show joyce 2 with dissolve
    j "Fuck me daddy."

    call label_beginDuel_common() from _call_label_beginDuel_common_9
    $ current_speed = date.animation_speed
    show joyce with dissolve
    show moan_bubble
    $ renpy.music.play("sex/moans.wav", channel="sexvoice", loop=True)
    $ phase = 1
    label .gameLoop:
        $ game.jeu_sensitive = False

        if date.isWin():
            hide screen screen_sex_ui with dissolve
            if phase == 1:
                call label_cowgirl_v2
            elif phase == 2:
                call label_cowgirl_isWin
                "You take this opportunity to escape."
                window hide
                window auto
                play sound "sex/undress.wav"
                show black
                pause 2.0
                $ game.state = "living"
                $ game.jeu_sensitive = False
                $ g.phoneProgress[0] = 10
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
    show joyce cowgirl
    pause 0.5
    $ date.speedUp()
    show joyce cowgirl
    
    if date.isLost():
        hide screen screen_sex_ui with dissolve
        call label_cowgirl_isLost
        $ date.lust = 0
        $ game.lust = 0
        call label_newDay("label_prison") from _call_label_newDay_22

    call label_endTurn_common from _call_label_endTurn_common_8
    return

label label_cowgirl_v2:
    $ renpy.music.play("sex/moans2.wav", channel="sexvoice", loop=True)
    $ date.speedUp()
    show joyce
    j "I'm..{w=1.0}{nw}"
    $ date.speedUp()
    show joyce
    j "It's coming !{w=1.0}{nw}"
    $ date.speedUp()
    show joyce 3 with dissolve 
    pause 0.3
    show joyce orgasm 2 at shaking with vpunch
    $ renpy.music.play("sex/moans_climax.wav", channel="sexvoice", loop=True)
    hide moan_bubble
    j "Kyaaa{w=1.0}{nw}"
    pause(2.76)
    stop sexvoice fadeout 0.2
    show joyce -orgasm at default with dissolve
    pause(1)
    j "Huff.."
    j "T-that doesn't count"
    j "W-we keep going.."
    $ date.animation_speed = 2
    $ date.orgasm = 0
    $ date.orgasmMax = 100
    $ phase = 2
    
    call label_add_card_to_deck("deck", Card("stop"), pauseTime=1.0) from _call_label_add_card_to_deck_23
    call label_add_card_to_deck("deck", Card("stop"), pauseTime=0.3) from _call_label_add_card_to_deck_24
    call label_add_card_to_deck("deck", Card("stop"), pauseTime=0.3) from _call_label_add_card_to_deck_25
    call label_add_card_to_deck("deck", Card("stop"), pauseTime=0.3) from _call_label_add_card_to_deck_26
    call label_add_card_to_deck("deck", Card("stop"), pauseTime=0.3) from _call_label_add_card_to_deck_27
    call label_add_card_to_deck("deck", Card("stop"), pauseTime=0.3) from _call_label_add_card_to_deck_28
    
    
    $ date.speedDown()
    # show joyce -2
    $ renpy.music.play("sex/moans.wav", channel="sexvoice", loop=True)
    return

label label_cowgirl_isWin:
    call label_after_successful_Date_common from _call_label_after_successful_Date_common_8
    $ renpy.music.play("sex/moans3.wav", channel="sexvoice", loop=True)
    
    $ date.animation_speed = 0
    j "I'm gonna"
    $ update_animationSpeed(0.1 / 1.8)
    show joyce
    j "mHHHnhh"
    $ update_animationSpeed(0.1 / 2.0)
    show joyce
    j "go inSANE"
    $ update_animationSpeed(0.1 / 2.2)
    show joyce
    j "yOU'RE gonna bREAK my PUssy [povname]"
    # j "[povname] you're too thick!"
    # j "You're gonna break me!!"
    $ update_animationSpeed(0.1 / 2.5)
    show joyce
    j "it'sh sho GOOOOOD"
    j "i'm coMING"
    
    show joyce
    pause 0.5

    show joyce orgasm 3 at shaking with vpunch
    $ renpy.music.play("sex/moans_climax.wav", channel="sexvoice", loop=True)
    j "gNHUUUUUU{w=2.0}{nw}"
    j "NGOooOOOO{w=1.0}{nw}"
    j "nhhggGGHUUU{w=2.0}{nw}"
    pause(2)
    stop sexvoice fadeout 0.2
    hide moan_bubble
    pause(1)
    show joyce orgasm 3 at default
    pause 0.3
    show joyce orgasm 3 at trs_fastbreath
    $ renpy.music.play("sex/heavy-breathing.wav", channel="sexvoice", loop=True, relative_volume=0.5)
    pause
    stop sexvoice
    play sound "sex/_Fouet.mp3" volume 0.4
    show joyce orgasm 4 at default with vpunch
    pause
    show joyce orgasm 5 with dissolve
    pause(0.3)
    play sound "sex/cum-out.mp3"
    show joyce orgasm 6 with dissolve
    pause(0.3)
    show joyce orgasm 7 with dissolve
    pause(0.3)
    show joyce orgasm 8 with dissolve
    pause
    "It seems like she's unconscious..."
    return

label label_cowgirl_isLost:
    $ update_animationSpeed(0.045)
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
    play sound "sex/_Poison-cum.wav"
    pause 0.1
    show joyce 3 at shaking with dissolve
    pause 0.7
    show joyce 3 at default
    pause
    j "Daddy, you just came!"
    j "Are you trying to make me pregnant?"
    j "My belly feels so warm now."
    show joyce cum-out 1 with dissolve
    pause 0.4
    play sound "sex/cum-out.mp3"
    show joyce cum-out 2 with dissolve
    pause 0.4
    show joyce cum-out 3 with dissolve
    pause
    j "Look at all this cum."
    play sound "rpg/Key.wav"
    show joyce lock with dissolve
    pause
    j "Alright daddy it's time to go back to your kennel."
    j "Frankly,"
    j "I don't think you'll ever make me cum."
    j "But I'll let you try as many times as you want daddy."
