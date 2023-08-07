label label_firstDate:
    $ game.state = "dating"
    $ date = Date(objectif_trust = 8, isWin = "date.trust >= 8", turnLeft = 5, endTurn = "label_firstDate_endTurn")

    define pov = Character("[povname]")
    
    # python:
    #     povname = renpy.input("What is your name?", length=32)
    #     povname = povname.strip()

        # if not povname:
        #     povname = "William"
    $ povname = "William"

    scene bg bbt
    show joyce stand stare at default_img_pos
    show fg bbt-table onlayer master zorder 2
    
    # j "Hello, you're [povname] right?"
    # j "I'm Joyce."

    if game.progress[1] == 0:
        show joyce base smile
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
        show joyce neutral
        show screen screen_tutorial("misc/tutorial-cards.png") with dissolve
        j "During a date, you play cards from your hand that have various effects."
        show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
        j "The aim of a date is to build {b}{color=#55f}{u}trust{/u}{/color}{/b} and {b}{color=#f3a}{u}attraction{/u}{/color}{/b}."
        j "{b}{color=#cc3}{u}Lust{/u}{/color}{/b} is a negative trait."
        j "If you have {b}more lust than trust{/b}, the girl will notive you're being too pervy."
        j "They will be upset and the date will be over."
        j "So don't act too horny. At least not on your first dates!"
        j "This date, you only need to build 8 trust for it to be successful."
        show screen screen_tutorial("misc/tutorial-end-turn.png") with dissolve
        j "The date is also over when you {b}run out of card{/b}."
        j "After every turn, you draw until you have 5 cards in hand."
        hide screen screen_tutorial with dissolve
        show joyce smile 
        j "Got it?\nLet's start the date!"
    
    play sound "datestart.mp3"
    show date-start at truecenter with blinds
    pause 0.4
    play sound "datestart2.mp3"
    hide date-start with moveoutbottom
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                hide screen screen_date_ui with dissolve

                show date-nice at truecenter with blinds
                hide date-nice with moveoutbottom

                j "haha"
                j "That was a nice first date. I feel like I can trust you."
                j "Hey... Here's my number"
                j "Do you want to meet again in the week?"
                j "I'll text you."
                j "See ya."
                call label_after_successful_Date_common
                jump label_home
            
            show joyce at default_img_pos
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop


label label_firstDate_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

    label .loseCondition:
        if date.lust > date.trust or date.turnLeft == 0 or len(deck.deck) == 0:

            play sound "gameover.mp3"
            show date-fail at truecenter with blinds
            pause 0.3
            hide date-fail with moveoutbottom

            show joyce neutral
            show joyce armscrossed upset

            if date.lust > date.trust:
                hide screen screen_date_ui with dissolve
                j "um.. don't you think I can notice?"
                j "Sorry but gotta go"
                j "Maybe we can do this another day?"

            elif date.turnLeft == 0 or len(deck.deck) == 0:
                hide screen screen_date_ui with dissolve
                j "OH look at the time."
                j "Sorry but I gotta go."
                j "That kinda dragged on no?"
                j "Maybe we can do this another day? See ya."
            
            $ game.progress[1] += 1
            $ game.nextDay("label_home")

        else:
            if date.turnLeft == 4:
                j "So youre [povname], you often do blind dates like that?"
            if date.turnLeft == 3:
                j "I often come to this bubble tea place."
            if date.turnLeft == 2:
                j "I have a cat, do you have any pet?"
            if date.turnLeft == 1:
                j "I eat too much sugar lately"

    call label_endTurn_common
    return

screen screen_tutorial(disp, properties={}):
    add disp:
        properties properties











label label_secondDate:
    $ date = Date(objectif_trust = 10, objectif_attraction = 5, isWin = "date.trust >= 10 and date.attraction >= 5", turnLeft = 6, endTurn = "label_secondDate_endTurn")
    scene bg cafe
    hide joyce
    show joyce smile at default_img_pos
    show fg cafe-table onlayer master zorder 2
    j "Hello again"
    j "These days it's getting hotter and hotter huh?"

    call label_beginDuel_common()
    play sound "datestart.mp3"
    show date-start at truecenter with blinds
    pause 0.4
    play sound "datestart2.mp3"
    hide date-start with moveoutbottom

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                hide screen screen_date_ui with dissolve

                show date-nice at truecenter with blinds
                hide date-nice with moveoutbottom

                j "t'es trop forte bewbew"

                call label_after_successful_Date_common
                jump label_prison
            
            show joyce at default_img_pos
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_secondDate_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

    label .loseCondition:
        if date.lust > date.trust or date.turnLeft == 0 or len(deck.deck) == 0:

            play sound "gameover.mp3"
            show date-fail at truecenter with blinds
            pause 0.3
            hide date-fail with moveoutbottom

            show joyce neutral
            show joyce armscrossed upset

            if date.lust > date.trust:
                hide screen screen_date_ui with dissolve
                j "um.. don't you think I can notice?"
                j "Sorry but gotta go"
                j "Maybe we can do this another day?"

            elif date.turnLeft == 0 or len(deck.deck) == 0:
                hide screen screen_date_ui with dissolve
                j "OH look at the time."
                j "Sorry but I gotta go."
                j "That kinda dragged on no?"
                j "Maybe we can do this another day? See ya."
            
            $ game.progress[1] += 1
            $ game.nextDay("label_home")
                
    if date.turnLeft == 5:
        hide screen screen_date_ui with dissolve
        j "Oh man it's really too hot"
        j "Hold on I'll go to the bathroom."
        hide joyce
        show joyce stand at default_img_pos
        pause
        hide joyce with dissolve
        pause
        show joyce_2ndstand as joyce at default_img_pos with dissolve
        j "hey" 
        j "sorry it was just too hot"
        show joyce 2nd
        j "I had to remove a few layers"
        # show boob-shoot at truecenter with moveinright
        show layer master:
            zoom 2.0 xalign 0.5 yalign 0.5
        with dissolve
        pause
        j "what's wrong?"
        "n-nothing"
        j "hm okay"
        j "Let's keep going shall we?"
        show layer master:
            zoom 1.0
        with dissolve
        show joyce smile
        j "So where were we at?"
        call label_add_card_to_deck("deck", "peek2")
        "(a Peek card was added to your deck)"
        window hide
        show screen screen_date_ui with dissolve
        pause 0.5

    elif date.turnLeft < 5:
        call label_add_card_to_deck("deck", "peek2")
        pause 0.5

    call label_endTurn_common

    return
