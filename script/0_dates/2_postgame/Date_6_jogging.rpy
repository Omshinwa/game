label label_jogging:
    scene bg chemin-1 at trs_bg_blur(6, "soft")
    # scene Color("#00f")
    # show fg terrasse-table onlayer master zorder 2
    "this is a planned date: jogging, right now it's still in development"
    # show joyce outfitsport running breath at trs_depied
    # show bg at trs_bg_blur(4, "hard")
    # j "hard"
    # show bg chemin-pixel4 at trs_bg_blur(4, "hard")
    # j "chemin-pixel2"
    # show bg chemin-pixel4 at trs_bg_blur(4, "hard")
    # j "Let's go for a run!"
    # show bg chemin-pixel4
    # j "Let's go for a run! 2"


    # show bg chemin-10 at trs_bg_blur(4, "soft")
    # j undress foxy smile sweaty "Fiou, I'm so sweaty!"
    # show bg chemin-10 at trs_bg_blur(0)
    # j undress foxy smile "It's so hot!"
    # j outfitsport2 -undress "hehe"
    # j running "RUN"
    # $ test = renpy.game.context().current
    # j "[test]"
    
    show joyce outfitsport running breath at trs_depied
    j "Come on, we're almost there!"
    $ date = Date("date", objectif_trust = game.trust + 5, turnLeft = 8, endTurn = "label_jogging_endTurn")
    call label_beginDuel_common() 

    # hide screen screen_date_ui with dissolve
    # call label_add_card_to_deck("hand", Card("peek"+whichDress),pauseTime = 0.5)

    label .gameLoop:
        $ game.jeu_sensitive = False
        if date.isWin():
            call label_after_successful_Date_common
            call label_newDay("label_home")
        show joyce outfitsport running breath with dissolve
        if len(deck.hand) == 0:
            pass
        
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        jump .gameLoop

label label_jogging_endTurn:
    call label_add_card_to_deck("hand", Card("tired"),pauseTime = 0.5)
    return
    # call label_date_isLost_common