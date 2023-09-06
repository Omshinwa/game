label label_blowjob:
    $ date = Date("sex", endTurn = "label_blowjob_SexEndTurn", turnLeft=8, isWin = "date.turnLeft <= 0")

    scene bg basement
    show blowjob talk (1) as joyce
    with dissolve
    # show moan_bubble

    if game.progress[1] == -1:
        j "I love seeing your dick up close."
        j "Now, what could this exam be?"
        play sound "rpg/Key.wav"
        show blowjob get-hard (1) as joyce with dissolve
        pause
        j "My little slut"
        j "Now be a good boy and get hard for me."
        j "So I can rape you nice and tight."
        pause 0.4
        show blowjob get-hard (2) as joyce
        pause 0.4
        show blowjob get-hard (3) as joyce
        pause
        j "It smells so good"
        j "First let's do the balls nice and wet."
        show blowjob (1) as joyce with dissolve
        j "Mhhh"
    else:
        j "I missed this"
        play sound "rpg/Key.wav"
        show blowjob get-hard (1) as joyce with dissolve
        pause
        j "Now get hard so I can suck your sperm."
        pause 0.4
        show blowjob get-hard (2) as joyce
        pause 0.4
        show blowjob get-hard (3) as joyce
        pause
        j "Oh yes."
        j "I feed on your dick."


    call label_beginDuel_common() from _call_label_beginDuel_common_8
    $ current_speed = date.animation_speed

    j "Bon appétit."

    show joyce blowjob with dissolve
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            if "v2" in renpy.get_attributes("joyce"):
                show joyce blowjob v2
            else:
                show joyce blowjob

            $ current_speed = date.animation_speed
    
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_8

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop from _call_label_blowjob_gameLoop

    # This ends the game.

    return



label label_blowjob_SexEndTurn:
    $ game.jeu_sensitive = False

    $ i=0
    while i < date.animation_lust[date.animation_speed]:
        $ date.lust += 1
        $ date.orgasm += 1
        $ i += 1
        pause(1.0/ date.animation_lust[date.animation_speed])
    
    $ date.speedUp()
    if "v2" in renpy.get_attributes("joyce"):
        show joyce blowjob v2
    else:
        show joyce blowjob
    pause 0.5
    $ date.speedUp()
    if "v2" in renpy.get_attributes("joyce"):
        show joyce blowjob v2
    else:
        show joyce blowjob
    
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

        if "v2" in renpy.get_attributes("joyce"):
            $ phase = 2
            show blowjob v2 cum (1) as joyce with dissolve
            pause 0.3
            play sound "sex/Poison-cum.wav"
            show blowjob v2 cum (1) as joyce at shaking
            pause 0.4
            show blowjob v2 cum (1) as joyce at default with dissolve
            pause 2.0
            show blowjob v2 cum (2) as joyce at default
            play sound "sex/swallow.wav"
            pause 0.4
            show blowjob v2 cum (3) as joyce
            pause 0.4
            show blowjob v2 cum (4) as joyce
            with dissolve
            pause
            show blowjob v2 talk as joyce with dissolve
            j "Delicious"
            j "Did I do a good job licking it nice and clean?"
            j "But you failed again."
            play sound "rpg/Key.wav"
            j "Go back to jail, you premature ejaculator"
            show blowjob v2 lock as joyce with dissolve
            pause 
        else:
            $ phase = 1
            show blowjob (4) as joyce with dissolve
            pause 0.3
            play sound "sex/Poison-cum.wav"
            show blowjob cum (1) as joyce at shaking
            pause 0.4
            show blowjob cum (1) as joyce at default with dissolve
            show blowjob cum (2) as joyce at default with dissolve
            with dissolve
            pause
            j "Oh, you got my ass all sticky."
            j "Bad pet."
            play sound "rpg/Key.wav"
            show blowjob lock with dissolve
            j "You're not allowed to cum anymore."
            pause

        $ game.lust = 0
        call label_newDay("label_prison") from _call_label_newDay_20

    if date.turn == 3:
        show blowjob (3) as joyce with dissolve
        j "You're getting better at this, aren't you?"
        j "Then it's time..."
        j "Your dick is so salty and musty now"
        j "I'm gonna squeeze all your cum."
        j "I'm your cum dumpster after all."
        play sound "sex/kiss-dick.wav"
        pause 2.0
        show blowjob v2 (1) as joyce with dissolve
        j "Mhhh"
        show blowjob v2 (2) as joyce
        pause 0.1
        show blowjob v2 (3) as joyce
        pause 0.1
        show blowjob v2 (4) as joyce 
        pause 0.1
        show blowjob v2 (5) as joyce 
        pause 0.1
        show blowjob v2 (6) as joyce
        pause 0.1
        show blowjob v2 (1) as joyce with dissolve
        j "MHHHH"
        show joyce blowjob v2 as joyce with dissolve
        $ date.animation_speed_hash[10] = 2.0

        $ date.speedUp()
        show joyce blowjob v2
        pause 0.5
        $ date.speedUp()
        show joyce blowjob v2
        
        call label_add_card_to_deck("deck", Card("peek4"), pauseTime=1.0) from _call_label_add_card_to_deck_18
        call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.3) from _call_label_add_card_to_deck_19
        call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.3) from _call_label_add_card_to_deck_20
        call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.3) from _call_label_add_card_to_deck_21

    elif date.turn >3:
        call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.5) from _call_label_add_card_to_deck_22
        

        
    call label_endTurn_common from _call_label_endTurn_common_7

    if date.isWin():
        
        call label_after_successful_Date_common from _call_label_after_successful_Date_common_7
        show blowjob v2 talk as joyce
        with dissolve
        j "Aww... No cum for mommy?"
        j "Alright"
        play sound "rpg/Key.wav"
        show blowjob v2 lock as joyce
        with dissolve
        j "Next is the last trial."
        j "You've been waiting for this, haven't you?"
        j "You'll fuck my tight little pussy."
        j "Does this excite you?"
        j "Make me cum first and you're free."
        call label_newDay("label_prison") from _call_label_newDay_21

    return
