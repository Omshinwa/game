label label_cowgirl_start:
    scene bg bbt

    show joyce standing at default
    show fg bbt-table 

    # show img_moaning_bubbles

    show moan_bubble
    
    j "Hello, you must be Kevin."
    j "I'm Joyce"
    show joyce sitting at default
    j "Hi, this is your first date no?"
    j "I'll tell you how to get a successful date"
    j "Let the date begin!"

    
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