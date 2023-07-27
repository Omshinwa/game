label label_beginDuel_common():
    $ game.state = "dating"
    show card_zone_bg zorder 2
    $ deck.start()
    $ game.jeu_sensitive = True;
    return

label label_beginDuel():
    show screen screen_sex_ui
    call label_beginDuel_common

    $ game.lust = 0
    $ game.orgasm = 0
    $ game.trust = 0
    $ game.attraction = 0
    return


label label_cowgirl_start:
    scene bg bbt

    show joyce stand at default
    show fg bbt-table 

    # show img_moaning_bubbles

    show moan_bubble
    
    j "Hello, you must be Kevin."
    j "I'm Joyce"
    show joyce base at default
    j "Hi, this is your first date no?"
    j "I'll tell you how to get a successful date"
    j "Let the date begin!"

    show expression "Joyce/sex/cowgirl/cowgirl (6).png" as joyce at toobig

    j "Finally.. let's get a taste.."
    show expression "Joyce/sex/cowgirl/cowgirl (3).png" as joyce at toobig
    #play enter sex sound
    j "Gnh..ugh.."
    j "You're so big..."
    
    show joyce cowgirl at toobig
    
    call label_beginDuel()
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
            
            show joyce sitting at default
    
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
    show joyce smile at default
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
            
            show joyce sitting at default
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop

    # This ends the game.

    return