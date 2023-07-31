init python:
    #
    #       return the number of pixels to put between each card for pretty render
    #
    def getCardPadding(handSize):
        if handSize == 0:
            return 0
        padding = ( 1800 - (handSize+1)*game.card_xsize ) / handSize
        return min(padding, 20)

    def getCardYdisplace():
        if not game.jeu_sensitive:
            return 10
        if game.isHoverHand:
            return -140
        return 10

    focus_card_index = -1

transform trans_card_played:
    xalign 0.5 yanchor 1.0 ypos 1.0
    ease 0.4 ypos 0.5

screen screen_card_hand():
    $ paddingPerCard = getCardPadding(len(deck.hand))
    
    fixed at date.updateYdisplace(): #Transform(ypos = 1220 + date.ydisplace):
        xsize 1800
        ysize game.card_ysize
        yanchor 1.0
        # ypos 1220 + date.ydisplace

        fixed:
            xsize int( len(deck.hand)* game.card_xsize + (paddingPerCard*(len(deck.hand)-1)) )
            xalign 0.5
            for index, card in enumerate(deck.hand):
                if index != focus_card_index:
                    fixed:
                        xpos int((index)* game.card_xsize + paddingPerCard*index)
                        xsize game.card_xsize
                        ysize game.card_ysize
                        add card.img

            if -1<focus_card_index<len(deck.hand):                    
                $ card = deck.hand[focus_card_index]
                fixed:
                    xpos int((focus_card_index)* game.card_xsize + paddingPerCard*focus_card_index)
                    xsize game.card_xsize
                    ysize game.card_ysize
                    add card.img

            #BUTTONS
            for index, card in enumerate(deck.hand):
                fixed:
                    xpos int((index)* game.card_xsize + paddingPerCard*index)
                    xsize game.card_xsize
                    ysize game.card_ysize
                    
                    imagebutton:
                        sensitive game.jeu_sensitive
                        idle "cards/button.png"
                        if card.cond(index):
                            hover "cards/button-hover.png"
                            action [Call('playCardfromHand', index)]
                        else:
                            action NullAction()
                        hovered [SetVariable("game.isHoverHand", True), SetVariable("focus_card_index", index)]
                        unhovered [SetVariable("game.isHoverHand", False), SetVariable("focus_card_index", -1)]

screen screen_date_bottom_ui(endTurn = "label_SexEndTurn"):

    #     cards at the bottom
    button:
        hovered SetVariable("game.isHoverHand", True)
        unhovered SetVariable("game.isHoverHand", False)
        action NullAction()
        xsize 1700
        ysize game.card_ysize
        yalign 1.0
        xalign 0.35
        sensitive game.jeu_sensitive

    use screen_card_hand()

    fixed:
        xpos 1750
        ypos 890
        image "cards/deck_stack.png"
        fixed:
            xpos 35
            ypos 22
            xsize 30
            text str(len(deck.deck)) size 80 xalign 0.5 style "outline_text"

    fixed:
        ypos 710
        xpos 1650
        imagebutton:
            idle "ui/end_turn.png"
            hover "ui/end_turn_hover.png"
            action Call(endTurn)
            sensitive game.jeu_sensitive
    
    # TRASHCAN
    fixed:
        xpos 5
        ypos 950
        imagebutton:
            idle "ui/trashcan.png"
            hover "ui/trashcan-hover.png"
            action [SetVariable("game.jeu_sensitive", False),Show("screen_show_deck", dissolve, deck.discard_pile, "label_null", "DISCARD PILE")]
            sensitive game.jeu_sensitive
        fixed:
            xpos 20
            ypos 30
            xsize 50
            text str(len(deck.discard_pile)) size 50 xalign 0.5 style "outline_text"

    if game.debug_flag:
        drag:
            text "YOUR TURN" size 60 color "#FF0"
            xalign 0.5 yalign 0.5

screen screen_lust_ui:

    $ shaft_size = int( 196*(date.lustMax / 20) )
    $ fullSizeDick = 122 + shaft_size + 152
    $ croppedSize = int ( fullSizeDick * date.lust/date.lustMax )
    fixed:
        # xpos 1920 - 500 - shaft_size
        ypos 20
        xpos 220
        xsize 122 + shaft_size + 152
        image "ui/lust_bar1.png"
        image "ui/lust_bar2.png" xpos 122 xzoom date.lustMax / 20
        image "ui/lust_bar3.png" xpos 122+shaft_size

        
        image Crop( (0, 0, croppedSize, 120), "ui/lust_full_bar1.png") 
        image Crop( (0, 0, int( (croppedSize - 122) * 20 / date.lustMax), 120), "ui/lust_full_bar2.png")  xpos 122 xzoom date.lustMax / 20
        image Crop( (0, 0, croppedSize - 122 - shaft_size, 120), "ui/lust_full_bar3.png")  xpos 122+shaft_size

        # fixed: #cum bar
        #     frame:
        #         xsize croppedSize
        #         ysize 30
        #         background Solid("#3700ff")

        text str(date.lust) + "/" + str(date.lustMax):
            size 50 style "outline_text" xalign 0.45 ypos 40
            if (date.lust/date.lustMax)>0.9:
                color "#ffed68"
            if (date.lust/date.lustMax)>0.7:
                color "#eb7412"
            elif (date.lust/date.lustMax)>0.5:
                color "#c64826"
            else:
                color "#000000"
        
        if game.state == "dating":
            text "( next turn: +" +str(game.animation_speed)+ ")" size 30 xalign 0.45 ypos 100 color "#e970d2" style "outline_text"

screen screen_sex_ui(**kwargs):
    use screen_date_bottom_ui(kwargs["endTurn"])
    use screen_lust_ui()
    use screen_orgasm_ui()
    use screen_buttons_ui()
    use screen_turn_counter()

screen screen_date_ui(**kwargs):
    use screen_date_bottom_ui(kwargs["endTurn"])
    use screen_trust_ui(**kwargs["objectives"])
    use screen_buttons_ui()
    use screen_turn_counter()

screen screen_orgasm_ui:

    $ cropped_size = int( max(0,(1 - (game.orgasm/game.orgasmMax))) * (456) )
    fixed: #cum bar
        xpos 1920 - 600
        ypos 0
        image "ui/orgasm_bar.png" 
        
        # frame:
        #     xsize int( (game.orgasm/game.orgasmMax) * (456) )
        #     ysize 120
            
        #     xpos 456 - int( (game.orgasm/game.orgasmMax) * (456) )
        #     background Solid("#ffaaf5")

        text str(game.orgasm) + "/" + str(game.orgasmMax):
            size 50 style "outline_text" ypos 40
            if (game.orgasm/game.orgasmMax)>0.9:
                color "#ffed68"
            if (game.orgasm/game.orgasmMax)>0.7:
                color "#eb7412"
            elif (game.orgasm/game.orgasmMax)>0.5:
                color "#c64826"
            else:
                color "#000000"

        image Crop( (cropped_size, 0, 456, 120), "ui/orgasm_full_bar.png") xpos cropped_size
    
screen screen_trust_ui(range_var = 100, **kwargs):
    fixed:
        xpos 200
        ypos 20
        xsize 440
        ysize 200
        add "#00f"
        
        text "{k=15.0}LUST{/k}":
            size 40 style "outline_text" ypos 5
            if kwargs["lust"] != 0:
                if date.lust < kwargs["lust"]:
                    color "#f00"
                else:
                    color "#00ffae"
        
        text "{k=5.0}TRUST{/k}":
            size 40 style "outline_text" ypos 67
            if kwargs["trust"] != 0:
                if date.trust < kwargs["trust"]:
                    color "#f00"
                else:
                    color "#00ffae"
        
        text "{vspace=12}{k=-2.0}Attraction{/k}":
            size 40 style "outline_text" ypos 115
            if kwargs["attraction"] != 0:
                if date.attraction < kwargs["attraction"]:
                    color "#f00"
                else:
                    color "#00ffae"
        
        fixed:
            xpos 190
            xsize 240

            bar value date.lust range range_var ypos 10 xpos 0 xsize 480 left_bar "#ffd561" right_bar"#0000" 
            bar value date.trust range range_var ypos 75 xpos 0 left_bar "#61e5ff" xsize 480 right_bar"#0000" 
            bar value date.attraction range range_var ypos 140 xpos 0 left_bar "#ff8bf0" xsize 480 right_bar"#0000" 


            for index, stat in enumerate(["lust", "trust", "attraction"]):

                if stat == "lust":
                    $ objectif = kwargs["lust"]
                elif stat == "trust":
                    $ objectif = kwargs["trust"]
                elif stat == "attraction":
                    $ objectif = kwargs["attraction"]

                if objectif == 0:
                    text str(eval('game.' + stat)):
                        size 50 style "outline_text" xalign 0.5 ypos 60*index
                else:
                    if getattr(game, stat) < objectif:
                        text str(eval('game.' + stat)) + "/" + str(objectif):
                            size 50 style "outline_text" xalign 0.5 ypos 60*index color "#f00"
                    else:
                        text str(eval('game.' + stat)) + "/" + str(objectif):
                            size 50 style "outline_text" xalign 0.5 ypos 60*index color "#00ffae"

        
screen screen_turn_counter:
    fixed:
        add "#00f"
        xsize 200
        ysize 200
        xpos 1900 ypos 20 xanchor 1.0

        text "{b}{i}{k=-25.0}"+str(date.turnLeft)+"{/k}{/i}{/b}":
            size 200 style "outline_text" xalign 0 yalign 0.5
            if (date.turnLeft)==1:
                color "#ffed68"
            if (date.turnLeft)<3:
                color "#eb7412"
            elif (date.turnLeft)<5:
                color "#c64826"
            else:
                color "#000000"
            if date.turnLeft>9:
                size 180 xpos -80

        text "turn(s) left":
            size 25 style "outline_text" xalign 1.0 yalign 0.85
            
screen screen_gameloop():
    pass

label label_gameloop(position): #when you just wait for user to do something
    $ renpy.show(position)
    call screen screen_gameloop()
    call label_gameloop(position)

screen screen_buttons_ui():
    imagebutton:
        xpos 20
        ypos 20
        idle "ui/hide_ui.png"
        hover "ui/hide_ui_hover.png"
        action HideInterface()

    # imagebutton:
    #     xpos 20
    #     ypos 180
    #     idle "ui/prefs.png"
    #     hover im.MatrixColor("ui/prefs.png", im.matrix.invert())
    #     action ShowMenu('preferences')