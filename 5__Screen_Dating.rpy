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
            return 0
        if game.isHoverHand:
            return 0
        return 150

    focus_card_index = -1

transform trans_card_played:
    xalign 0.5 yanchor 1.0 ypos 1.0
    ease 0.4 ypos 0.5

screen screen_card_hand:
    sensitive game.jeu_sensitive
    
    $ paddingPerCard = getCardPadding(len(deck.hand))
    $ ydisplace = getCardYdisplace()

        # cards at the bottom
    button:
        hovered SetVariable("game.isHoverHand", True)
        unhovered SetVariable("game.isHoverHand", False)
        action NullAction()
        xsize 1920
        ysize 300
        yalign 1.0
    
    fixed:
        xsize 1800
        ysize 200
        yalign 1.0

        fixed:
            ypos -140 + ydisplace
            # ypos 750
            xsize int( len(deck.hand)* game.card_xsize + (paddingPerCard*(len(deck.hand)-1)) )
            xalign 0.5
            for index, card in enumerate(deck.hand):
                if index != focus_card_index:
                    drag:
                        xpos int((index)* game.card_xsize + paddingPerCard*index)
                        xsize game.card_xsize
                        ysize game.card_ysize
                        add card.img
                        frame:
                            xalign 0.5
                            ypos 180
                            xsize 210
                            ysize 130
                            if len(card.txt)<30:
                                text card.txt style "style_card_effect" size 25 
                            else:
                                text card.txt style "style_card_effect"

            if -1<focus_card_index<len(deck.hand):                    
                $ card = deck.hand[focus_card_index]
                drag:
                    xpos int((focus_card_index)* game.card_xsize + paddingPerCard*focus_card_index)
                    xsize game.card_xsize
                    ysize game.card_ysize
                    add card.img
                    frame:
                        xalign 0.5
                        ypos 180
                        xsize 210
                        ysize 130
                        if len(card.txt)<30:
                            text card.txt style "style_card_effect" size 25 
                        else:
                            text card.txt style "style_card_effect"

            #BUTTONS
            for index, card in enumerate(deck.hand):
                drag:
                    xpos int((index)* game.card_xsize + paddingPerCard*index)
                    xsize game.card_xsize
                    ysize game.card_ysize
                    
                    imagebutton:
                        idle "cards/button.png"
                        if eval(card.cond):
                            hover "cards/button-hover.png"
                            action [Call('playCardfromHand', index)]
                        else:
                            action NullAction()
                        hovered [SetVariable("game.isHoverHand", True), SetVariable("focus_card_index", index)]
                        unhovered [SetVariable("game.isHoverHand", False), SetVariable("focus_card_index", -1)]

    fixed:
        xpos 1750
        ypos 890
        image "cards/deck_stack.png"
        fixed:
            xpos 35
            ypos 22
            xsize 30
            text str(len(deck.deck)) size 80 xalign 0.5 style "outline_text"
        
        imagebutton:
            ypos -180
            xpos -100
            idle "ui/end_turn.png"
            action Call("SexEndTurn")
            hover "ui/end_turn_hover.png"

    if game.debug_flag:
        drag:
            text "YOUR TURN" size 60 color "#FF0"
            xalign 0.5 yalign 0.5

screen screen_pleasure_ui:

    $ shaft_size = int( 196*(game.pleasureMax / 20) )
    $ fullSizeDick = 122 + shaft_size + 152
    $ croppedSize = int ( fullSizeDick * game.pleasure/game.pleasureMax )
    fixed:
        # xpos 1920 - 500 - shaft_size
        ypos 20
        xpos 220
        xsize 122 + shaft_size + 152
        image "ui/pleasure_bar1.png"
        image "ui/pleasure_bar2.png" xpos 122 xzoom game.pleasureMax / 20
        image "ui/pleasure_bar3.png" xpos 122+shaft_size

        
        image Crop( (0, 0, croppedSize, 120), "ui/pleasure_full_bar1.png") 
        image Crop( (0, 0, int( (croppedSize - 122) * 20 / game.pleasureMax), 120), "ui/pleasure_full_bar2.png")  xpos 122 xzoom game.pleasureMax / 20
        image Crop( (0, 0, croppedSize - 122 - shaft_size, 120), "ui/pleasure_full_bar3.png")  xpos 122+shaft_size

        fixed: #cum bar
            frame:
                xsize croppedSize
                ysize 30
                background Solid("#3700ff")

        text str(game.pleasure) + "/" + str(game.pleasureMax):
            size 50 style "outline_text" xalign 0.45 ypos 40
            if (game.pleasure/game.pleasureMax)>0.9:
                color "#ffed68"
            if (game.pleasure/game.pleasureMax)>0.7:
                color "#eb7412"
            elif (game.pleasure/game.pleasureMax)>0.5:
                color "#c64826"
            else:
                color "#000000"
        
        
        text "( next turn: +" +str(game.animation_speed)+ ")" size 30 xalign 0.45 ypos 100 color "#e970d2" style "outline_text"


# image orgasm_full_bar = Crop(( (game.orgasm/game.orgasmMax) * (456), 0, 456, 120), "ui/orgasm_full_bar.png")

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


style style_card_effect:
    xalign 0.5
    size 22
    line_spacing  -5
    textalign 0.5

screen screen_gameloop():
    pass

label label_gameloop(position): #when you just wait for user to do something
    $ renpy.show(position)
    call screen screen_gameloop()
    call label_gameloop(position)

screen screen_buttons_ui():
    button:
        xpos 20
        ypos 20
        image "ui/hide_ui.png"
        action HideInterface()