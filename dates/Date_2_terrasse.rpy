label label_terrasse:
    $ date = Date("date", objectif_trust = 25, objectif_attraction = 20, turnLeft = 5, endTurn = "label_terrasse_endTurn")
    scene bg terrasse
    show fg terrasse-table onlayer master zorder 2
    show screen screen_glass("terrasse") onlayer master zorder 2

    if game.progress[1]>=1:
        show joyce outfit2 smile at sitting
        with dissolve
        j "I remembered to dress lighter this time."
    else:
        show joyce outfit1 smile at sitting
        with dissolve
        j "Hey!"
        j "You found me, come sit there."

    call label_beginDuel_common()

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                call label_after_successful_Date_common

                j smile "Fiou I feel like I drank too much."
                j "I think I'll go home now, it was nice."
                j "We should go somewhere special next time"
                j "I'll think about something."
                j "See ya!"
                call label_newDay("label_home")

        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_terrasse_endTurn:
    call label_date_isLost_common
    
    if game.progress[1]<=0:            
        if date.turn == 0:
            hide screen screen_date_ui with dissolve
            j null "Oh man it's really too hot"
            j "Hold on I'll go to the bathroom."
            show joyce at standing 
            pause
            hide joyce with dissolve
            pause
            show joyce outfit2 at standing as joyce with dissolve
            j smile "hey" 
            j "Sorry it was just too hot."
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
            show joyce smile at sitting with dissolve
            j "So where were we at?" 
            show screen screen_date_ui with dissolve
            pause 0.5
    else:
        call label_reaction


    call label_endTurn_common

    if "outfit2" in renpy.get_attributes("joyce"):
        call label_add_card_to_deck("hand", Card("peek2"), pauseTime = 0.5)

    return