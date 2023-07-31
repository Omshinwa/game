label label_cowgirl_begin():
    # show screen screen_sex_ui
    call label_beginDuel_common(endTurn = "label_SexEndTurn")
    return

label label_SexEndTurn:
    $ i=0
    while i < game.animation_speed:
        $ date.lust += 1
        $ game.orgasm += 1

        $ i += 1
        pause(0.1)

    label .loseCondition:
        if date.lust > date.trust:
            j "um.. don't you think I can notice?"
            j "Sorry but gotta go"
            j "Maybe we can do this another day?"
        elif date.turnLeft == 0 or len(deck.deck) == 0:
            j "Aw gotta go."
            j "Sorry bu that kinda dragged on"
            j "Maybe we can do this another day?"

    $ date.attractionMultiplier = 1
    $ date.trustMultiplier = 1
    $ date.lustMultiplier = 1

    $ handSize = len(deck.hand)
    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    return

label label_cowgirl:
    $ date = Date(objectif_trust = 10)

    scene bg bbt

    show joyce stand at default_img_pos
    show fg bbt-table 

    # show img_moaning_bubbles

    show moan_bubble
    
    $ renpy.music.play("sex_moans.wav", channel="sexvoice", loop=True)

    j "Hello, you must be Kevin."
    j "I'm Joyce"
    show joyce base at default_img_pos
    j "Hi, this is your first date no?"
    j "I'll tell you how to get a successful date"
    j "Let the date begin!"

    show expression "Joyce/sex/cowgirl/cowgirl (6).png" as joyce at toobig

    j "Finally.. let's get a taste.."
    show expression "Joyce/sex/cowgirl/cowgirl (3).png" as joyce at toobig
    #play enter sex sound
    $ renpy.play("sex_sloppy.wav", channel="sexsfx")
    j "Gnh..ugh.."
    j "You're so big..."
    show joyce cowgirl at toobig
    call label_cowgirl_begin()
    $ current_speed = game.animation_speed
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != game.animation_speed:
            show joyce cowgirl at toobig
            show moan_bubble
            $ current_speed = game.animation_speed

        if game.orgasm >= game.orgasmMax:
            j "i'm..{w=1.0}{nw}"
            j "it's coming !{w=1.0}{nw}"
            show joyce cowgirl-orgasm 
            j "kyaaa{w=1.0}{nw}"
            pause(2)
            show cowgirl-talk at top as joyce
            pause(1)
            j "huff.."
            j "i-i came"
            
            show joyce sitting at default_img_pos
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    call .gameLoop

    # This ends the game.

    return



label label_footjob_start:

    scene bg bbt

    show footjob-start-talk at top
    
    # show locked-legs

    # show img_moaning_bubbles

    show moan_bubble
    
    j "Hello, you must be Kevin."
    j "I'm Joyce"
    hide footjob-start-talk
    show joyce smile at default_img_pos
    j "Hi, this is your first date no?"
    j "I'll tell you how to get a successful date"
    j "Let the date begin!"
    
    show joyce footjob at top
    
    call label_beginDuel()
    $ current_speed = game.animation_speed
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != game.animation_speed:
            show joyce footjob at top
            show moan_bubble
            $ current_speed = game.animation_speed

        if game.orgasm >= game.orgasmMax:
            j "i'm..{w=1.0}{nw}"
            j "it's coming !{w=1.0}{nw}"
            show joyce cowgirl-orgasm 
            j "kyaaa{w=1.0}{nw}"
            pause(2)
            show cowgirl-talk at top as joyce
            pause(1)
            j "huff.."
            j "i-i came"
            
            show joyce sitting at default_img_pos
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop

    # This ends the game.

    return