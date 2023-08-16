label label_terrasse:
    $ date = Date(objectif_trust = 20, objectif_attraction = 20, isWin = "date.trust >= 20 and date.attraction >= 20", turnLeft = 6, endTurn = "label_terrasse_endTurn")
    scene bg terrasse
    hide joyce
    show joyce smile 
    show fg terrasse-table onlayer master zorder 2
    show screen screen_glass("terrasse") onlayer master zorder 2
    j "Hello again"
    j "These days it's getting hotter and hotter huh?"

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


label label_terrasse_endTurn:
    call label_date_endTurn
    
    if game.progress[1]<=date.turn:            
        if date.turn == 1:
            hide screen screen_date_ui with dissolve
            j "Oh man it's really too hot"
            j "Hold on I'll go to the bathroom."
            hide joyce
            show joyce stand 
            pause
            hide joyce with dissolve
            pause
            show joyce outfit2 at standing as joyce with dissolve
            j "hey" 
            j "sorry it was just too hot"
            show joyce outfit2
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

    if "outfit2" in renpy.get_attributes("joyce"):
        call label_add_card_to_deck("deck", Card("peek2"))

    call label_endTurn_common

    return
