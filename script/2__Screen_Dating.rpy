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

    # if renpy.variant("pc"):
    # if renpy.variant("touch"):

    fixed at date.updateYdisplace():
        xsize 1800
        ysize game.card_ysize
        xalign 0.3
        yanchor 1.0

        fixed:
            xsize int( len(deck.hand)* game.card_xsize + (paddingPerCard*(len(deck.hand)-1)) )
            xalign 0.5

            for index, card in enumerate(deck.hand):
                fixed:
                    xpos int((index)* game.card_xsize + paddingPerCard*index)
                    xsize game.card_xsize
                    ysize game.card_ysize
                    
                    imagebutton:
                        sensitive game.jeu_sensitive

                        if card.cond(index):
                            idle card.img
                            hover card.img_hover
                        else:
                            idle colorizeImg(card.img, ("#000","#bbb"))

                        if not renpy.variant("touch"):
                            hovered [SetVariable("game.isHoverHand", True)]
                            unhovered [SetVariable("game.isHoverHand", False)]
                            if card.cond(index):
                                action [Call('playCardfromHand', index)]

                        else:
                            if not game.isHoverHand:
                                action SetVariable("game.isHoverHand", True)
                            elif card.cond(index):
                                action [Call('playCardfromHand', index)]

screen screen_date_bottom_ui():

    if not renpy.variant("touch"):
        button:
            hovered SetVariable("game.isHoverHand", True)
            unhovered SetVariable("game.isHoverHand", False)
            action Return()
            xsize 1700
            if game.isHoverHand:
                ysize game.card_ysize
            else:
                ysize 200
            yalign 1.0
            xalign 0.35
    
    else:
        button:
            action SetVariable("game.isHoverHand", False)
            xsize 1920
            ysize 1080
            yalign 1.0
            xalign 0.35
        
        button:
            action SetVariable("game.isHoverHand", True)
            xsize 1700
            if game.isHoverHand:
                ysize game.card_ysize
            else:
                ysize 200
            yalign 1.0
            xalign 0.35

    use screen_card_hand()

    fixed:
        xpos 1770
        ypos 860
        imagebutton:
            idle "cards/deck_stack.png"
            hover colorizeImg("cards/deck_stack.png",("#009f5d","#dfd"))
            action [Show("screen_show_deck", dissolve, sorted(deck.deck), "label_show_deck_callback", "CARDS LEFT")]
            sensitive game.jeu_sensitive
        fixed:
            xpos 40
            ypos 40
            xsize 30
            text str(len(deck.deck)) size 80 xalign 0.5 style "style_small_numbers"

label label_show_deck_callback(*args):
    $ game.jeu_sensitive = True
    return

screen screen_dick_ui:

    if game.state == "dating" or game.state == "sexing":
        $ gameOrDate = date
    else:
        $ gameOrDate = game

    $ sizeMultiplier = 1/50
    $ shaft_size = int( 196*(getattr(gameOrDate, "lustMax") * sizeMultiplier) )
    $ fullSizeDick = 122 + shaft_size + 152
    $ croppedSize = int ( fullSizeDick * getattr(gameOrDate, "lust")/getattr(gameOrDate, "lustMax") )
    fixed:
        ypos 20
        xpos 240
        xsize 122 + shaft_size + 152
        if game.state == "sexing" and date.lust + date.lustPerTurn >= date.lustMax:
            image Transform("ui/lust_bar1.png", matrixcolor=ColorizeMatrix("#822", "#fcc") )
            image Transform("ui/lust_bar2.png", matrixcolor=ColorizeMatrix("#822", "#fcc") ) xpos 122 xzoom getattr(gameOrDate, "lustMax")  * sizeMultiplier
            image Transform("ui/lust_bar3.png", matrixcolor=ColorizeMatrix("#822", "#fcc") ) xpos 122+shaft_size
        else:
            image "ui/lust_bar1.png"
            image "ui/lust_bar2.png" xpos 122 xzoom getattr(gameOrDate, "lustMax")  * sizeMultiplier
            image "ui/lust_bar3.png" xpos 122+shaft_size

        if game.state == "sexing" and date.lust + date.lustPerTurn >= date.lustMax:
            image Crop( (0, 0, croppedSize, 120), Transform("ui/lust_full_bar1.png", matrixcolor=ColorizeMatrix("#822", "#fcc") ) ) 
            image Crop( (0, 0, int( (croppedSize - 122) * (1/sizeMultiplier) / getattr(gameOrDate, "lustMax") ), 120), Transform("ui/lust_full_bar2.png"), matrixcolor=ColorizeMatrix("#822", "#fcc") )  xpos 122 xzoom getattr(gameOrDate, "lustMax")  * sizeMultiplier
            image Crop( (0, 0, croppedSize - 122 - shaft_size, 120), Transform("ui/lust_full_bar3.png"), matrixcolor=ColorizeMatrix("#822", "#fcc") )  xpos 122+shaft_size
        else:
            image Crop( (0, 0, croppedSize, 120), "ui/lust_full_bar1.png") 
            image Crop( (0, 0, int( (croppedSize - 122) * (1/sizeMultiplier) / getattr(gameOrDate, "lustMax") ), 120), "ui/lust_full_bar2.png")  xpos 122 xzoom getattr(gameOrDate, "lustMax")  * sizeMultiplier
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
            text "( next turn: +" +str(date.lustPerTurn)+ ")" size 30 xalign 0.45 ypos 100 color "#e970d2" style "outline_text"

            if getattr(date,"lustMultiplier") !=1:
                text "x" + str( getattr(date,"lustMultiplier")   ):
                    size 20+5*getattr(date,"lustMultiplier") style "outline_text" xpos 60 xanchor 0.5 yanchor 0.5 ypos 55 color "#cbb000"

        elif game.state == "living":
            text "( next day: +" +str(eval(game.lustPerDay))+ ")" size 30 xalign 0.45 ypos 100 color "#e970d2" style "outline_text"

screen screen_sex_ui():
    use screen_dick_ui()
    if game.progress[0]==8:
        use screen_orgasm_ui()
    
    if game.progress[0]!=8:
        use screen_turn_counter()
    
    use speed_indicator()
    use screen_date_bottom_ui()
    use screen_buttons_ui()

screen screen_date_ui():
    use screen_trust_ui()
    use screen_turn_counter()
    use screen_date_bottom_ui()
    use screen_buttons_ui()

renpy.hide_screen()

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
        xpos 200
        ypos 20
        xsize 440
        ysize 180

        vbox:
            spacing 0

            for index, stat in enumerate(["lust", "trust", "attraction"]):
                fixed:
                    ysize 60
                    
                    if stat == "lust":
                        $ objectif = date.objectives["lust"]
                        $ textStat = "{k=15.0}LUST{/k}"
                        if getattr(gameOrDate, "lust") > getattr(gameOrDate, "trust") and getattr(gameOrDate, "lust") > getattr(gameOrDate, "attraction"):
                            $ colorStat2 = "#f00a"
                        else:
                            $ colorStat2 = "#666a"
                        $ colorStat = "#ffd561"
                        $ textColor ="#cc3"
                    elif stat == "trust":
                        $ objectif = date.objectives["trust"]
                        $ textStat = "{k=5.0}TRUST{/k}"
                        $ colorStat = "#61e5ff"
                        $ textColor ="#55f"
                        $ colorStat2 = "#aaaa"
                    elif stat == "attraction":
                        $ objectif = date.objectives["attraction"]
                        $ textStat = "{k=-2.0}Attraction{/k}"
                        $ colorStat = "#ff8bf0"
                        $ textColor = "#f3a"
                        $ colorStat2 = "#aaaa"
                    
                    # if game.state != "dating":
                    #     $ objectif = -999

                    bar value getattr(gameOrDate, stat) range range_var xsize 440 ysize 60 left_bar colorStat right_bar colorStat2
                    

                    if objectif == -999:
                        text str( getattr(gameOrDate, stat)):
                            size 50 style "outline_dyslexic" xpos 0.6 yalign 0.8 #ypos 60*index
                    else:
                        text str( getattr(gameOrDate, stat) ) + "/" + str(objectif):
                            size 50 style "outline_dyslexic" xpos 0.6 yalign 0.8 #ypos 60*index 
                            if getattr(gameOrDate, stat) < objectif:
                                color "#f00"
                            else:
                                color "#00ffae"
                    
                    if game.state == "dating":
                        if getattr(date,stat+"Multiplier") !=1:
                            text "x" + str( getattr(date,stat+"Multiplier")   ):
                                size 15*getattr(date,stat+"Multiplier") style "outline_dyslexic" xpos 1.1 xanchor 0.6 yalign 0.7 color textColor
        
                    text textStat:
                        xpos 20
                        yalign 0.8
                        size 40 style "outline_dyslexic"
                        color textColor
        if game.state == "living":
            text "(+" + str(eval(game.lustPerDay)) + ")":
                xalign 1.0
                ypos 10
                size 35 style "outline_dyslexic"
                color "#cc3"

define logTable = [0, 0, 0.01, 0.05, 0.12, 0.18, 0.28, 0.4, 0.53, 0.68, 0.85, 1.1, 1.18, 1.40, 1.85, 2.4, 3.0]
        
screen screen_turn_counter:
    fixed:
        if game.state == "dating" or game.state == "sexing":
            add Color((255/(date.turnLeft*0.05 + 0.95), 228/(1+logTable[date.turnLeft]), 147))
        xsize 180
        ysize 180
        xpos 20 ypos 20

        text "{b}{i}{k=-25.0}"+str(date.turnLeft)+"{/k}{/i}{/b}":
            size 190 style "outline_text" xalign 0.4 ypos 10 color "#000000"
            if date.turnLeft>9:
                size 180  xalign 0.7
            elif date.turnLeft == 1:
                color "#f00"

        text "turn(s) left":
            size 25 style "outline_text" xalign 1.0 yalign 1.07
            
screen screen_gameloop():
    pass

image img_end_turn:
    contains:
        "ui/end_turn.png"
    contains:
        Text(_("END{size=60}\nTURN"), color="#ffffff", outlines=[ (5, "#00000055", 0, 0) ], kerning=-5, size=80, align=(0.5, 1.1), font="font_carrare")
        rotate -90

image button_img_end_turn:
    on idle:
        Transform("img_end_turn",alpha=0.7)
    on hover:
        "img_end_turn"
    on selected_insensitive: #selected_hover, selected_idle, 
        crop (0, 0, 200, 290)
        contains:
            "img_end_turn"
            ypos 0
            linear 0.3 ypos -1.0
        contains:
            "img_end_turn"
            ypos 1.0
            linear 0.3 ypos 0.0
    on insensitive:
        Transform("img_end_turn",alpha=0.7)

    
        
        

screen screen_buttons_ui():

    #END TURN
    button: # at Transform(None,alpha=0.7)
        add "button_img_end_turn"
        align (0, 1.00)
        xsize 200
        ysize 290
        action [SelectedIf(Play('sound',"card/switch.mp3", selected=True)), Call(date.endTurn)]
        sensitive game.jeu_sensitive
            
    if game.progress[0]>=2 or game.debug_mode: #game.state == "sexing" or 
        fixed:
            xpos 1800
            ypos 610
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
                ypos 35
                xsize 50
                text str(date.drink) size 50 xalign 0.5 style "style_small_numbers"
        
    # TRASHCAN
    fixed:
        xpos 1780
        ypos 730
        imagebutton:
            idle "ui/trashcan.png"
            hover "ui/trashcan-hover.png"
            action [Show("screen_show_deck", dissolve, deck.discard_pile, "label_null", "DISCARD PILE")]
            sensitive game.jeu_sensitive
        fixed:
            xpos 25
            ypos 35
            xsize 50
            text str(len(deck.discard_pile)) size 50 xalign 0.5 style "style_small_numbers"

screen screen_glass(id):
    if date.drink>0:
        imagebutton:
            idle "bg/" + id + "-glass-" + str(date.drink) + ".png"
            focus_mask True
            hover tintImg("bg/" + id + "-glass-" + str(date.drink) + ".png", (255*1.5,255*1.5,255))
            action Call("label_drink")
            sensitive game.jeu_sensitive
    else:
        add "bg/" + id + "-glass-0.png"

screen speed_indicator():
    fixed:

        ypos 600
        xalign 1.0
        xysize 100,50*len(date.animation_speed_hash)
        fixed:
            
            text "SPEED" style "outline_text" ypos -300 xalign 1.0 vertical True

            for i in range(len(date.animation_speed_hash)):
                frame:
                    if i == date.animation_speed:
                        background "#f00"
                    else:
                        background Color((25.5*i,15.5*i,20.5*i))
                    xysize 40,50
                    ypos -50*i
                    text str(date.lustPerTurn) font "font_carrare" align 0.5,0.5 color "#fff"

                    if i == date.animation_speed:
                        frame:
                            background "#ff0"
                            xysize 20,20
                            yalign 0.5
                            xpos -70


