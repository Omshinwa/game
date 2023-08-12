
label label_barDate:
    $ date = Date(objectif_attraction = 20, isWin = "date.attraction >= 20", turnLeft = 7, endTurn = "label_barDate_endTurn")
    scene bg bar
    show fg bar-table onlayer master zorder 2
    show screen screen_glass("bar") onlayer master zorder 2
    
    show joyce fancy at standing onlayer master zorder 2
    j "Hey fancy meeting your there huh?"
    j "hehe"
    
    show joyce fancy smile at sitting onlayer master zorder 0

    call label_beginDuel_common()

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
            
            show joyce 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_barDate_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

    label .loseCondition:
        if date.lust > date.trust or date.turnLeft == 0 or len(deck.deck) == 0:

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
        show joyce stand 
        pause
        hide joyce with dissolve
        pause
        show joyce_2nd_stand as joyce with dissolve
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
        call label_add_card_to_deck("deck", Card("peek2"))
        "(a Peek card was added to your deck)"
        window hide
        show screen screen_date_ui with dissolve
        pause 0.5

    elif date.turnLeft < 5:
        call label_add_card_to_deck("deck", Card("peek2"))
        pause 0.5

    call label_endTurn_common

    return