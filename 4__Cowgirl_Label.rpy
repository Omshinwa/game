label label_cowgirl_begin():
    # show screen screen_sex_ui
    call label_beginDuel_common()
    return

label label_cowgirl_SexEndTurn:
    
    $ date.attractionMultiplier = 1
    $ date.trustMultiplier = 1
    $ date.lustMultiplier = 1

    $ i=0
    while i < date.animation_speed:
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

    $ handSize = len(deck.hand)
    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    return

label label_cowgirl:
    $ date = Date(objectif_trust = 10, endTurn = "label_cowgirl_SexEndTurn")

    scene bg bbt

    show joyce stand 
    show fg bbt-table 

    show moan_bubble

    j "Hello, you must be Kevin."
    j "I'm Joyce"
    show joyce base 
    j "Hi, this is your first date no?"
    j "I'll tell you how to get a successful date"
    j "Let the date begin!"

    show expression "Joyce/sex/cowgirl/cowgirl (6).png" as joyce at toobig

    j "Finally.. let's get a taste.."
    show expression "Joyce/sex/cowgirl/cowgirl (3).png" as joyce at toobig
    #play enter sex sound
    $ renpy.play("sex/slap.wav", channel="sexsfx")
    j "Gnh..ugh.."
    j "You're so big..."
    show joyce cowgirl at toobig
    call label_cowgirl_begin()
    $ current_speed = date.animation_speed
    
    $ renpy.music.play("sex/moans.wav", channel="sexvoice", loop=True)
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            show joyce cowgirl at toobig
            show moan_bubble
            $ current_speed = date.animation_speed

        if game.orgasm >= game.orgasmMax:
            $ renpy.music.play("sex/moans3.wav", channel="sexvoice", loop=True)
            j "i'm..{w=1.0}{nw}"
            j "it's coming !{w=1.0}{nw}"
            show joyce cowgirl-orgasm 
            $ renpy.music.play("sex/moans_climax.wav", channel="sexvoice", loop=True)
            j "kyaaa{w=1.0}{nw}"
            pause(2)
            $ renpy.music.stop(channel="sexvoice")
            show cowgirl-talk at top as joyce
            pause(1)
            j "huff.."
            j "i-i came"
            
            show joyce sitting 
    
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
    show joyce smile 
    j "Hi, this is your first date no?"
    j "I'll tell you how to get a successful date"
    j "Let the date begin!"
    
    show joyce footjob at top
    
    call label_beginDuel()
    $ current_speed = date.animation_speed
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        if current_speed != date.animation_speed:
            show joyce footjob at top
            show moan_bubble
            $ current_speed = date.animation_speed

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
            
            show joyce sitting 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop

    # This ends the game.

    return