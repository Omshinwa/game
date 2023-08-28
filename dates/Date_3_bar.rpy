
label label_barDate:
    $ date = Date("date", objectif_attraction = 25, turnLeft = 7, endTurn = "label_barDate_endTurn")
    scene bg bar
    show fg bar-table onlayer master zorder 2
    show screen screen_glass("bar") onlayer master zorder 2

    if whichDress == "red":
        show joyce outfitred at depied onlayer master zorder 2
    else:
        show joyce outfitblue at depied onlayer master zorder 2

    
    with dissolve
    

    j "Hey fancy meeting your there huh?"

    if whichDress == "red":
        show joyce outfitred at sitting onlayer master zorder 0 
    else:
        show joyce outfitblue at sitting onlayer master zorder 0 

    j "dynamic"
    show expression generate_anim3("Joyce/anim/touch-hair/touch-hair (",9, 0.15) at sitting as anim
    pause 0.15*9
    hide anim
    

    j "hehe"
    # hide joyce with dissolve
    # show expression "joyce " + " outfit"+whichDress at sitting

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
    call label_date_isLost_common
    
    if game.progress[1]<=date.turn:            
        if date.turn == 0:
            pass
    else:
        call label_reaction

    call label_endTurn_common

    call label_add_card_to_deck("deck", Card("peek2"))
    # pause 0.5

    return