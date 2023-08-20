

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
    $ game.state = "dating"
    $ date = Date(objectif_trust = 10, endTurn = "label_cowgirl_SexEndTurn")

    scene bg basement

    show footjob-start-talk as joyce

    # show moan_bubble

    j "Are you ready for your first test?"
    j "Can you guess what is it?"
    j "Here's a hint"
    show footjob-start-hint as joyce
    window hide
    pause
    window auto
    j "So, did you guess?"
    j "yes"
    j "I'm gonna masturbate you with my feet"
    j "First, let's release this bad boy."
    j "You must have been waiting for this no?"
    show joyce cowgirl at toobig
    j "Such nice shape."
    hide anim
    j "Please resist this if you want a taste of my pussy."
    show footjob (1) as joyce
    j "Are you ready?"

    show expression "Joyce/sex/cowgirl/cowgirl (6).png" as joyce at toobig

    j "Finally.. let's get a taste.."
    show expression "Joyce/sex/cowgirl/cowgirl (3).png" as joyce at toobig
    #play enter sex sound
    $ renpy.play("sex/slap.wav", channel="sexsfx")
    j "Gnh..ugh.."
    j "You're so big..."
    show joyce cowgirl at toobig
    call label_beginDuel_common()
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
