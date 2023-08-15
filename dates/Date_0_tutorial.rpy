label label_tutorial:
    $ game.state = "dating"
    $ date = Date(objectif_trust = 3, isWin = "date.trust >= 3", turnLeft = 5, endTurn = "label_tutorial_endTurn")

    scene bg park
    show joyce base smile at standing
    with dissolve
    # show screen screen_home onlayer master
    # show black onlayer screens
    # hide black onlayer screens with dissolve
    
    j "Hello, you're [povname] right?"
    # j "I'm Joyce."

    if game.progress[1] == 0:
        j "This is your first date no?"
        menu:
            "Yes":
                j "I'll tell you how a date works."
                $ tutorial = True
            "No":
                show joyce smile 
                j "Oh you're experienced"
                j "Then let the date begin!"
                $ tutorial = False

        show joyce 
    else:
        $ tutorial = False
        show joyce base
        j "hi again"
        j "I hope this date goes better than the last"
    
    call label_beginDuel_common()

    if tutorial:
        $ game.jeu_sensitive = False
        show screen screen_tutorial("misc/tutorial-cards.png") with dissolve
        play sound "rpg/Item1.wav"
        j neutral armscrossed "During a date, you play cards from your hand that have various effects."
        show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
        j "The aim of a date is to build {b}{color=#55f}{u}trust{/u}{/color}{/b} and {b}{color=#f3a}{u}attraction{/u}{/color}{/b}."
        j "{b}{color=#cc3}{u}Lust{/u}{/color}{/b} is a negative trait."
        j "If you have {b}more lust than trust{/b}, the girl will notive you're being too pervy."
        j "They will be upset and the date will be over."
        j "So don't act too horny. At least not on your first dates!"
        j "This date, you only need to build 3 trust for it to be successful."
        show screen screen_tutorial("misc/tutorial-end-turn.png") with dissolve
        j "The date is also over when you {b}run out of card{/b}."
        j "After every turn, you draw until you have 5 cards in hand."
        hide screen screen_tutorial with dissolve
        show joyce smile base
        j "Got it?\nLet's start the date!"
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():

                call label_after_successful_Date_common

                j "haha"
                j "That was a nice first date. I feel like I can trust you."
                j "Hey... Here's my number"
                j "Do you want to meet again in the week?"
                j "I'll text you."
                j "See ya."
                hide joyce with dissolve
                
                jump label_home_tutorial
            
            show joyce 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop


label label_tutorial_endTurn:
    call label_date_endTurn

    if date.turn == 0:
        show joyce stare neutral
        j smile "So youre [povname], nice to meet you"
        j "I was a bit worried before coming here, but you seem nice."

    call label_endTurn_common
    return
