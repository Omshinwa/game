label label_firstDate_begin():
    
    call label_beginDuel_common(objectives = date.config["objectives"], endTurn = "label_firstDate_endTurn")

    return

label label_firstDate_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

    label .loseCondition:
        if game.lust > game.trust:
            hide screen screen_date_ui with dissolve
            j "um.. don't you think I can notice?"
            j "Sorry but gotta go"
            j "Maybe we can do this another day?"

            jump label_prison
        elif date.turnLeft == 0 or len(deck.deck) == 0:
            hide screen screen_date_ui with dissolve
            j "OH look at the time."
            j "Sorry but I gotta go."
            j "That kinda dragged on no?"
            j "Maybe we can do this another day? See ya."

            jump label_prison
        else:
            if date.turnLeft == 4:
                j "So youre [povname], you seems interesting."
            if date.turnLeft == 3:
                j "It's getting pretty warm these days huh?"
            if date.turnLeft == 2:
                j "I often come to this boba place."
            if date.turnLeft == 1:
                j "I have a cat, do you have any pet?"

    call label_endTurn_common
    return

label label_firstDate:
    $ date = Date(objectif_trust = 5, isWin = "game.trust >= 5", turnLeft = 5)

    define pov = Character("[povname]")
    
    # python:
    #     povname = renpy.input("What is your name?", length=32)
    #     povname = povname.strip()

        # if not povname:
        #     povname = "William"
    $ povname = "William"

    scene bg bbt
    show joyce stand stare at default
    show fg bbt-table 
    
    # j "Hello, you're [povname] right?"
    # j "I'm Joyce."
    show joyce base smile
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
    
    call label_firstDate_begin()
    if tutorial:
        $ game.jeu_sensitive = False
        j "The aim of the date is to build trust, interest and attraction with the other."
        j "You build trust and attraction by playing the right cards at the right times."
        j "This first date, you'll need to build 10 trust for it to be 'successful'"
        j "You will draw until you have 5 cards in your hand at the beginning of every turn."
        j "When you run out of cards in your deck, the date will end."
        j "Got it? Let's start the date!"
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                j "haha"
                j "That was a nice first date. I feel like I can trust you."
                j "Hey... Here's my number"
                j "Do you want to meet again in the week?"
                j "I'll text you."
                j "See ya."
                $ game.progress += 1
                jump label_prison
            
            show joyce at default
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop

    # This ends the game.

    return

label label_secondDate:
    scene bg bbt
    show joyce 2nd smile at default
    show fg bbt-table 
    j "Hello again"
    j "These days it's getting hotter and hotter huh?"