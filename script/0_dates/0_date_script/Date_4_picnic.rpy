transform trs_contrejour:
    # matrixcolor BrightnessMatrix(-0.15)
    matrixcolor ColorizeMatrix(Color(hsv=(0,0,-0.1)),"#f0e8dc")
transform trs_contrejour_pluie:
    matrixcolor ColorizeMatrix(Color(hsv=(0,0,0.0)),"#eff3e6")
    
image fg2 joyce-shadow = ShowingSwitch("joyce sitted","fg2 picnic-joyce-shadow-sitted",
    "joyce","fg2 picnic-joyce-shadow-stand",
    None ,"#fff0")

image water_droplet:
    pos (1400, -200)
    "water_drop_1"
    linear 1.0 pos(1300,920)
    "water_drop_2"
    pause 0.1
    "water_drop_3"
    pause 0.1
    alpha 0.0

label label_picnic:
    scene bg pre-picnic at trs_bg_blur(strength=2,mask="soft") zorder -1
    show joyce smile outfit3 at trs_depied
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

label label_picnic_isWin:
    show fg:
        alpha 0.2
    with dissolve
    j "Oh hoh, it's getting cloudy suddenly."
    
    hide fg
    show bg picnic-2 at trs_bg_blur(strength=2,mask="soft")
    with dissolve
    
    j -posé "I think it's\nstarting to rain..."
    camera at trs_contrejour_pluie
    with dissolve

    j "It's getting dark..."
    show rain zorder -1 with dissolve
    play music "date/rain_bgm.ogg" fadein 1.0
    pause
    j surprised sunglasses2 holdglasses opened "Oh my god."
    j "Let's go hide somewhere."
    show joyce standup at trs_depied with dissolve:
        ypos -800
    pause
    camera:
        ypos 755
    show bg picnic-3:
        ypos -755
    hide rain
    show rain2 zorder -1:
        ypos -755
    with dissolve
    j -surprised -holdglasses standup "Come on, it's raining even harder!"
    camera

    scene bg picnic-4 at trs_bg_blur(strength=2,mask="none", child=None)
    show joyce wet at trs_depied:
        matrixcolor ColorizeMatrix(Color(hsv=(0,0,-0.05)),"#dcebf0")
    pause
    j breath "Huff... Huff..."
    j "It should be fine here."
    j worried "I'm sorry, I should have checked the weather forecast."
    j -worried "Look at us now." 
    j happy smile "We're both so wet haha."
    show joyce eyesdown with dissolve
    pause 0.5
    show joyce surprised -smile with dissolve
    j wet defend blush "!"
    j "Oh my god."
    j "I can't believe this!"
    j happy smile "Hahaha."
    j -happy "Next time I'll remember to take an umbrella for sure."
    j "AND to wear a bra!"
    j happy "Today was awful!"
    j -surprised "..."
    j -happy "Actually..."
    show joyce -defend with dissolve
    j foxy "At least you'll remember something good about it."
    j "Go on, stare at me."
    j "It's my fault we're both wet."
    return

label label_picnic_endTurn:
    call label_endTurn_common
    if date.turn == 2:
        hide screen screen_date_ui with dissolve
        show water_droplet
        pause 1.5
        j "?"
        j null_mouth "Did you feel something?"
        show screen screen_date_ui with dissolve
    return
