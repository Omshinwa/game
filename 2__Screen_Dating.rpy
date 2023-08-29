init python:
    #
    #       return the number of pixels to put between each card for pretty render
    #
    def getCardPadding(handSize):
        if handSize == 0:
            return 0
        padding = ( 1800 - (handSize+1)*game.card_xsize ) / handSize
        return min(padding, 20)

    focus_card_index = -1

screen screen_card_hand():
    $ paddingPerCard = getCardPadding(len(deck.hand))
    
    fixed at date.updateYdisplace():
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

screen screen_date_bottom_ui():

    add "card_zone_bg" yalign 1.0
    #     cards at the bottom
    button:
        hovered SetVariable("game.isHoverHand", True)
        unhovered SetVariable("game.isHoverHand", False)
        action Return()
        # action NullAction()
        xsize 1700
        if game.isHoverHand:
            ysize game.card_ysize
        else:
            ysize 200
        yalign 1.0
        xalign 0.35

    use screen_card_hand()

    fixed:
        xpos 1750
        ypos 890
        imagebutton:
            idle "cards/deck_stack.png"
            hover Transform("cards/deck_stack.png", matrixcolor=TintMatrix((204,255,357)))
            action [Show("screen_show_deck", dissolve, sorted(deck.deck), "label_null", "CARDS LEFT")]
            sensitive game.jeu_sensitive
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
            action Call(date.endTurn)
            sensitive game.jeu_sensitive
    
    if game.state == "sexing":
        fixed:
            xpos 20
            ypos 830
            if date.drink>0:
                imagebutton:
                    idle "ui/water-bottle.png"
                    hover "ui/water-bottle-hover.png"
                    action Call("label_drink")
                    sensitive game.jeu_sensitive
            else:
                add "ui/water-bottle-empty.png"
            fixed:
                xpos 20
                ypos 30
                xsize 50
                text str(date.drink) size 50 xalign 0.5 style "outline_text"
        

    # TRASHCAN
    fixed:
        xpos 5
        ypos 950
        imagebutton:
            idle "ui/trashcan.png"
            hover "ui/trashcan-hover.png"
            action [Show("screen_show_deck", dissolve, deck.discard_pile, "label_null", "DISCARD PILE")]
            sensitive game.jeu_sensitive
        fixed:
            xpos 20
            ypos 30
            xsize 50
            text str(len(deck.discard_pile)) size 50 xalign 0.5 style "outline_text"

screen screen_debug:
    if game.debug_mode:
        drag:
            fixed:
                xsize 500
                ysize 200
                xalign 0.0 yalign 0.3
                text "game.isHoverHand: "  + str(game.isHoverHand) + "\ngame.jeu_sensitive: " + str(game.jeu_sensitive) + "\ngame.progress: "+str(game.progress[0]) + "," + str(game.progress[1]):
                    size 40 color "#FF0" ypos 0

                imagebutton:
                    xsize 100
                    ysize 100
                    action Jump("label_welcome_prison")
                    idle "#00f"

screen screen_dick_ui:

    if game.state == "dating" or game.state == "sexing":
        $ gameOrDate = date
    else:
        $ gameOrDate = game

    $ shaft_size = int( 196*(getattr(gameOrDate, "lustMax") / 20) )
    $ fullSizeDick = 122 + shaft_size + 152
    $ croppedSize = int ( fullSizeDick * getattr(gameOrDate, "lust")/getattr(gameOrDate, "lustMax") )
    fixed:
        # xpos 1920 - 500 - shaft_size
        ypos 20
        xpos 220
        xsize 122 + shaft_size + 152
        if game.state == "sexing" and date.lust + date.animation_lust[date.animation_speed] >= date.lustMax:
            image Transform("ui/lust_bar1.png", matrixcolor=ColorizeMatrix("#822", "#fcc") )
            image Transform("ui/lust_bar2.png", matrixcolor=ColorizeMatrix("#822", "#fcc") ) xpos 122 xzoom getattr(gameOrDate, "lustMax")  / 20
            image Transform("ui/lust_bar3.png", matrixcolor=ColorizeMatrix("#822", "#fcc") ) xpos 122+shaft_size
        else:
            image "ui/lust_bar1.png"
            image "ui/lust_bar2.png" xpos 122 xzoom getattr(gameOrDate, "lustMax")  / 20
            image "ui/lust_bar3.png" xpos 122+shaft_size

        if game.state == "sexing" and date.lust + date.animation_lust[date.animation_speed] >= date.lustMax:
            image Crop( (0, 0, croppedSize, 120), Transform("ui/lust_full_bar1.png", matrixcolor=ColorizeMatrix("#822", "#fcc") ) ) 
            image Crop( (0, 0, int( (croppedSize - 122) * 20 / getattr(gameOrDate, "lustMax") ), 120), Transform("ui/lust_full_bar2.png"), matrixcolor=ColorizeMatrix("#822", "#fcc") )  xpos 122 xzoom getattr(gameOrDate, "lustMax")  / 20
            image Crop( (0, 0, croppedSize - 122 - shaft_size, 120), Transform("ui/lust_full_bar3.png"), matrixcolor=ColorizeMatrix("#822", "#fcc") )  xpos 122+shaft_size
        else:
            image Crop( (0, 0, croppedSize, 120), "ui/lust_full_bar1.png") 
            image Crop( (0, 0, int( (croppedSize - 122) * 20 / getattr(gameOrDate, "lustMax") ), 120), "ui/lust_full_bar2.png")  xpos 122 xzoom getattr(gameOrDate, "lustMax")  / 20
            image Crop( (0, 0, croppedSize - 122 - shaft_size, 120), "ui/lust_full_bar3.png")  xpos 122+shaft_size

        # fixed: #cum bar
        #     frame:
        #         xsize croppedSize
        #         ysize 30
        #         background Solid("#3700ff")

        text str(getattr(gameOrDate, "lust") ) + "/" + str(getattr(gameOrDate, "lustMax") ):
            size 50 style "outline_text" xalign 0.45 ypos 40
            if (getattr(gameOrDate, "lust") /getattr(gameOrDate, "lustMax") )>0.9:
                color "#ffed68"
            if (getattr(gameOrDate, "lust") /getattr(gameOrDate, "lustMax") )>0.7:
                color "#eb7412"
            elif (getattr(gameOrDate, "lust") /getattr(gameOrDate, "lustMax") )>0.5:
                color "#c64826"
            else:
                color "#000000"
        
        if game.state == "sexing":
            text "( next turn: +" +str(date.animation_lust[date.animation_speed])+ ")" size 30 xalign 0.45 ypos 100 color "#e970d2" style "outline_text"

            if getattr(date,"lustMultiplier") !=1:
                text "x" + str( getattr(date,"lustMultiplier")   ):
                    size 20+5*getattr(date,"lustMultiplier") style "outline_text" xpos 60 xanchor 0.5 yanchor 0.5 ypos 55 color "#ffed68"

        elif game.state == "living":
            text "( next day: +" +str(eval(game.lustPerDay))+ ")" size 30 xalign 0.45 ypos 100 color "#e970d2" style "outline_text"

screen screen_sex_ui():
    use screen_date_bottom_ui()
    use screen_dick_ui()
    if game.progress[0]==8:
        use screen_orgasm_ui()
    use screen_buttons_ui()
    
    if game.progress[0]!=8:
        use screen_turn_counter()

screen screen_date_ui():
    use screen_date_bottom_ui()
    use screen_trust_ui()
    use screen_buttons_ui()
    use screen_turn_counter()

screen screen_orgasm_ui:

    $ cropped_size = int( max(0,(1 - (date.orgasm/date.orgasmMax))) * (456) )
    fixed: #cum bar
        xpos 1920 - 700
        ypos 0
        
        if game.state == "sexing" and date.orgasm + date.animation_lust[date.animation_speed] >= date.orgasmMax:
            image Transform("ui/orgasm_bar.png", matrixcolor=ColorizeMatrix("#822", "#fcc"))
        else:
            image "ui/orgasm_bar.png" 
        

        text str(date.orgasm) + "/" + str(date.orgasmMax):
            size 50 style "outline_text" ypos 60 xpos 160
            if (date.orgasm/date.orgasmMax)>0.9:
                color "#ffed68"
            if (date.orgasm/date.orgasmMax)>0.7:
                color "#eb7412"
            elif (date.orgasm/date.orgasmMax)>0.5:
                color "#c64826"
            else:
                color "#000000"


        if game.state == "sexing" and date.orgasm + date.animation_lust[date.animation_speed] >= date.orgasmMax:
            image Crop( (cropped_size, 0, 456, 120), Transform("ui/orgasm_full_bar.png",matrixcolor=ColorizeMatrix("#822", "#fcc"))) xpos cropped_size 
        else:
            image Crop( (cropped_size, 0, 456, 120), "ui/orgasm_full_bar.png") xpos cropped_size

        if game.state == "sexing":
            text "( next turn: +" +str(date.animation_lust[date.animation_speed])+ ")" size 30 xpos 120 ypos 120 color "#e970d2" style "outline_text"


screen screen_trust_ui(range_var = 100):
    default textStat = ""
    default colorStat = "#fff"
    default colorStat2 = "#fff"
    default textColor = "000"

    if game.state == "dating" or game.state == "sexing":
        $ gameOrDate = date
    else:
        $ gameOrDate = game

    fixed:
        xpos 220
        ypos 21
        xsize 400
        ysize 200

        vbox:

            for index, stat in enumerate(["lust", "trust", "attraction"]):
                
                fixed:
                    ysize 66
                    
                    if stat == "lust":
                        $ objectif = date.objectives["lust"]
                        $ textStat = "{k=15.0}LUST{/k}"
                        if getattr(gameOrDate, "lust") > getattr(gameOrDate, "trust") and getattr(gameOrDate, "lust") > getattr(gameOrDate, "attraction"):
                            $ colorStat2 = "#ff0000"
                        else:
                            $ colorStat2 = "#666"
                        $ colorStat = "#ffd561"
                        $ textColor ="#cc3"
                    elif stat == "trust":
                        $ objectif = date.objectives["trust"]
                        $ textStat = "{k=5.0}TRUST{/k}"
                        $ colorStat = "#61e5ff"
                        $ textColor ="#55f"
                        $ colorStat2 = "#aaa"
                    elif stat == "attraction":
                        $ objectif = date.objectives["attraction"]
                        $ textStat = "{k=-2.0}Attraction{/k}"
                        $ colorStat = "#ff8bf0"
                        $ textColor = "#f3a"
                        $ colorStat2 = "#aaa"
                    
                    # if game.state != "dating":
                    #     $ objectif = -999

                    bar value getattr(gameOrDate, stat) range range_var xsize 400 ysize 66 left_bar colorStat right_bar colorStat2
                    

                    if objectif == -999:
                        text str( getattr(gameOrDate, stat)):
                            size 50 style "outline_text" xalign 0.8 #ypos 60*index
                    else:
                        text str( getattr(gameOrDate, stat) ) + "/" + str(objectif):
                            size 50 style "outline_text" xalign 0.8 #ypos 60*index 
                            if getattr(gameOrDate, stat) < objectif:
                                color "#f00"
                            else:
                                color "#00ffae"
                    
                    if game.state == "dating":
                        if getattr(date,stat+"Multiplier") !=1:
                            text "x" + str( getattr(date,stat+"Multiplier")   ):
                                size 15*getattr(date,stat+"Multiplier") style "outline_text" xpos 1.1 xanchor 0.5 yalign 0.5 color textColor
        
                    text textStat:
                        xalign 0.1
                        yalign 0.5
                        size 40 style "outline_text"
                        color textColor
        if game.state == "living":
            text "(+" + str(eval(game.lustPerDay)) + ")":
                xalign 1.0
                ypos 10
                size 35 style "outline_text"
                color "#cc3"

        
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
            elif (date.turnLeft)<3:
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

screen screen_glass(id):
    if date.drink>0:
        imagebutton:
            idle "bg/" + id + "-glass-" + str(date.drink) + ".png"
            focus_mask True
            hover im.MatrixColor("bg/" + id + "-glass-" + str(date.drink) + ".png", im.matrix.tint(1.5,1.5,1))
            action Call("label_drink")
            sensitive game.jeu_sensitive
    else:
        add "bg/" + id + "-glass-0.png"