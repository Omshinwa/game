label label_first_date:
    define pov = Character("[povname]")
    
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Watashi"

    scene bg bbt
    show joyce standing at default
    show fg bbt-table 
    
    j "Hello, you're [povname] right?"
    j "I'm Joyce."
    show joyce smile
    j "This is your first date no?"
    show joyce
    menu:
        "Yes":
            show joyce smile 
            j "Then I'll tell you how to get a successful date."
            $ tutorial = True
        "No":
            show joyce smile 
            j "Oh you're experienced"
            j "Then let the date begin!"
            $ tutorial = False
    show joyce 
    
    call label_beginDuel()
    if tutorial:
        $ game.jeu_sensitive = False
        j "The aim of the date is to build trust, interest and attraction with the other."
        j "You build trust and romance by playing the right cards at the right times."
        j "This first date, you'll need to build 10 trust for it to be 'successful'"
        j "You will draw until you have 5 cards in your hand at the beginning of every turn."
        j "When you run out of cards in your deck, the date will end."
        j "Got it? Let's start the date!"
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
        
    jump .gameLoop

    # This ends the game.

    return

label label_second_date:
    scene bg bbt
    show joyce 2nd smile at default
    show fg bbt-table 
    j "Hello again"
    j "These days it's getting hotter and hotter huh?"