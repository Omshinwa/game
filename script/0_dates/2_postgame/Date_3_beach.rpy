transform trs_color_beach:
    matrixcolor ColorizeMatrix(Color(hls=(.66,0.03,1.0)), Color(rgb=(1.11,1.03,1.005)))
    # matrixcolor ContrastMatrix(value=1.1)


label label_beach:
    scene bg beach at trs_bg_blur(strength=2,mask="soft") zorder -1

    show joyce outfit4 at trs_depied, right, RGBColorize(gray=["#ffffff", "#000000"], gray_thresh=[255, 0], red=["#ff0000", "#000000"], green=["#00ff00", "#000000"], blue=["#0000ff", "#000000"]).transform
    show joyce outfit4 as joyce2 at trs_depied, left

#trs_color_beach

    with dissolve
    pause
    j "Hey [povname]! It's here."
    j "I know a good spot."

    scene bg picnic at trs_bg_blur(strength=2,mask="soft") zorder -1
    show bg2 picnic-table
    # show fg2 joyce-shadow
    show joyce sitted smile sunglasses2 posé at trs_depied, trs_contrejour
    show screen screen_glass("picnic", (430,530)) onlayer master
    show fg3 picnic-items
    show fg sunflare onlayer master zorder 2:
        additive 1.0
        alpha 0.4
    j "Fiou! Today is so sunny."
    j "Good thing I brought my sunglasses."
    show joyce holdglasses with dissolve
    pause 0.3
    show joyce posé -holdglasses sunglasses with dissolve
    pause
    j "Do you want to drink something?"

    $ date = Date("date", name="picnic", objectif_trust = 20, objectif_attraction = 16, turnLeft = 6)
    call label_beginDuel_common()

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                call label_after_successful_Date_common
                call label_picnic_isWin
                call label_newDay("label_home")

        show joyce null_eyes posé with dissolve
        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return