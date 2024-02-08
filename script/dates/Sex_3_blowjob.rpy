label label_blowjob:
    $ date = Date("sex", endTurn = "label_blowjob_SexEndTurn", turnLeft=8, isWin = "date.turnLeft <= 0")

    scene bg basement
    show joyce blowjob talk 1
    with dissolve
    # show moan_bubble

    if game.progress[1] == -1:
        j "I love seeing your dick up close."
        j "Now, what could this exam be?"
        play sound "rpg/Key.wav"
        show joyce blowjob get-hard 1 with dissolve
        pause
        j "My little slut."
        j "Now be a good boy and get hard for me."
        j "So I can rape you nice and tight."
        pause 0.4
        show joyce blowjob get-hard 2
        pause 0.4
        show joyce blowjob get-hard 3
        pause
        j "It smells so good"
        j "First let's do the balls nice and wet."
        show joyce blowjob 1 with dissolve
        j "Mhhh..."
    else:
        j "I missed this"
        play sound "rpg/Key.wav"
        show joyce blowjob get-hard 1 with dissolve
        pause
        j "Now get hard so I can suck your sperm."
        pause 0.4
        show joyce blowjob get-hard 2
        pause 0.4
        show joyce blowjob get-hard 3
        pause
        j "Oh yes."
        j "I feed on your dick."


    call label_beginDuel_common() from _call_label_beginDuel_common_8
    $ current_speed = date.animation_speed

    j "Bon appetit."

    show joyce -1 with dissolve
    
    label .gameLoop:
        $ game.jeu_sensitive = False
        if len(deck.hand) == 0:
            call expression date.endTurn
        $ game.jeu_sensitive = True
        pause
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
    pause 0.3
    $ date.speedUp()
    pause 0.3
    if "v2" in renpy.get_attributes("joyce"):
        show joyce blowjob v2
    else:
        show joyce blowjob
    
    if date.isLost():
        call label_blowjob_isLost
        call label_newDay("label_prison") from _call_label_newDay_20

    if date.turn == 3:
        call label_blowjob_v2

    elif date.turn >3:
        call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.5) from _call_label_add_card_to_deck_22
        
        
    call label_endTurn_common from _call_label_endTurn_common_7

    if date.isWin():
        
        call label_after_successful_Date_common from _call_label_after_successful_Date_common_7
        call label_blowjob_isWin
        call label_newDay("label_prison") from _call_label_newDay_21

    return

label label_blowjob_isLost:
    hide screen screen_sex_ui with dissolve

    $ date.animation_speed = 0
    $ update_animationSpeed(0.05)
    with dissolve
    
    "!"
    window hide
    window auto
    stop sound
    
    $ date.animation_speed = 1
    pause 0.5

    if "v2" in renpy.get_attributes("joyce"):
        $ phase = 2
        show joyce blowjob v2 cum 1 with dissolve
        pause 0.3
        play sound "sex/Poison-cum.wav"
        show joyce blowjob v2 cum 1 at shaking
        pause 0.4
        show joyce blowjob v2 cum 1 at default with dissolve
        pause 2.0
        show joyce blowjob v2 cum 2 at default
        play sound "sex/swallow.wav"
        pause 0.4
        show joyce blowjob v2 cum 3
        pause 0.4
        show joyce blowjob v2 cum 4
        with dissolve
        pause
        show joyce blowjob v2 talk with dissolve
        j "Delicious"
        j "Did I do a good job licking it nice and clean?"
        j "But you failed again."
        play sound "rpg/Key.wav"
        show joyce blowjob v2 lock with dissolve
        j "Go back to jail, you premature ejaculator"
        pause 
    else:
        $ phase = 1
        show joyce blowjob 4 with dissolve
        pause 0.3
        play sound "sex/Poison-cum.wav"
        show joyce blowjob cum 1 at shaking
        pause 0.4
        show joyce blowjob cum 1 at default with dissolve
        show joyce blowjob cum 2 at default with dissolve
        with dissolve
        pause
        j "Oh, you got my ass all sticky."
        j "Bad pet."
        play sound "rpg/Key.wav"
        show joyce blowjob lock with dissolve
        j "You're not allowed to cum anymore."
        pause
    return

label label_blowjob_isWin:
    show joyce blowjob v2 talk
    with dissolve
    j "Aww... No cum for mommy?"
    j "Alright"
    play sound "rpg/Key.wav"
    show joyce blowjob v2 lock
    with dissolve
    j "Next is the last trial."
    j "You've been waiting for this, haven't you?"
    j "You'll fuck my tight little pussy."
    j "Does this excite you?"
    j "Make me cum first and you're free."
    return

label label_blowjob_v2:
    show joyce blowjob 3 with dissolve
    j "You're getting better at this, aren't you?"
    j "Your dick is so salty and musty."
    j "I can't resist..."
    j "You too right? You want me to eat it."
    j "I'm gonna squeeze all your cum."
    # j "I'm your cum dumpster after all."
    play sound "sex/kiss-dick.wav"
    pause 2.0
    show joyce blowjob v2 1 with dissolve
    j "Mhhh"
    show joyce blowjob v2 2
    pause 0.1
    show joyce blowjob v2 3
    pause 0.1
    show joyce blowjob v2 4 
    pause 0.1
    show joyce blowjob v2 5 
    pause 0.1
    show joyce blowjob v2 6
    pause 0.1
    show joyce blowjob v2 1 with dissolve
    j "It tastes even better."
    show joyce -1 with dissolve

    $ date.speedUp()
    pause 0.5
    $ date.speedUp()
    
    call label_add_card_to_deck("deck", Card("peek4"), pauseTime=1.0) from _call_label_add_card_to_deck_18
    call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.3) from _call_label_add_card_to_deck_19
    call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.3) from _call_label_add_card_to_deck_20
    call label_add_card_to_deck("deck", Card("peek4"), pauseTime=0.3) from _call_label_add_card_to_deck_21
    return