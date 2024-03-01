screen screen_gameloop():
    pass

############################################################################################################
#
#     :::      ::::::::   ::::::::  :::::::::  :::::::::: ::::::::  :::::::::      ::: ::::::::::: ::::::::  :::::::::  
#   :+: :+:   :+:    :+: :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+:   :+: :+:   :+:    :+:    :+: :+:    :+: 
#  +:+   +:+  +:+        +:+        +:+    +:+ +:+       +:+        +:+    +:+  +:+   +:+  +:+    +:+    +:+ +:+    +:+ 
# +#++:++#++: :#:        :#:        +#++:++#:  +#++:++#  :#:        +#++:++#:  +#++:++#++: +#+    +#+    +:+ +#++:++#:  
# +#+     +#+ +#+   +#+# +#+   +#+# +#+    +#+ +#+       +#+   +#+# +#+    +#+ +#+     +#+ +#+    +#+    +#+ +#+    +#+ 
# #+#     #+# #+#    #+# #+#    #+# #+#    #+# #+#       #+#    #+# #+#    #+# #+#     #+# #+#    #+#    #+# #+#    #+# 
# ###     ###  ########   ########  ###    ### ########## ########  ###    ### ###     ### ###     ########  ###    ###
#
###########################################################################################################
                             
screen screen_sex_ui():
    use screen_dick_ui()
    if date.name=="label_cowgirl":
        use screen_orgasm_ui()
    else:
        use screen_turn_counter()
    
    # use speed_indicator()
    use screen_date_bottom_ui()
    use screen_buttons_ui()

screen screen_date_ui():
    use screen_trust_ui()
    use screen_turn_counter()
    use screen_date_bottom_ui()
    use screen_buttons_ui()

############################################################################################################
#
#     ::::::::      :::     :::::::::  :::::::::       :::    :::     :::     ::::    ::: :::::::::  
#    :+:    :+:   :+: :+:   :+:    :+: :+:    :+:      :+:    :+:   :+: :+:   :+:+:   :+: :+:    :+: 
#    +:+         +:+   +:+  +:+    +:+ +:+    +:+      +:+    +:+  +:+   +:+  :+:+:+  +:+ +:+    +:+ 
#    +#+        +#++:++#++: +#++:++#:  +#+    +:+      +#++:++#++ +#++:++#++: +#+ +:+ +#+ +#+    +:+ 
#    +#+        +#+     +#+ +#+    +#+ +#+    +#+      +#+    +#+ +#+     +#+ +#+  +#+#+# +#+    +#+ 
#    #+#    #+# #+#     #+# #+#    #+# #+#    #+#      #+#    #+# #+#     #+# #+#   #+#+# #+#    #+# 
#     ########  ###     ### ###    ### #########       ###    ### ###     ### ###    #### #########  
#
###########################################################################################################

init python:
    #
    #       return the number of pixels to put between each card for pretty render
    #
    def getCardPadding(handSize):
        if handSize == 0:
            return 0
        padding = ( 1800 - (handSize+1)*g.card_xsize ) / handSize
        return min(padding, 20)

    focus_card_index = -1

screen screen_card_hand():
    $ paddingPerCard = getCardPadding(len(deck.hand))

    # if renpy.variant("pc"):
    # if renpy.variant("touch"):

    fixed at date.updateYdisplace():
        xsize 1800
        ysize g.card_ysize
        xalign 0.3
        yanchor 1.0

        # add "#0f05"

        fixed:
            xsize int( len(deck.hand)* g.card_xsize + (paddingPerCard*(len(deck.hand)-1)) )
            xalign 0.5

            for index, card in enumerate(deck.hand):
                imagebutton:
                    xpos int((index)* g.card_xsize + paddingPerCard*index)
                    xsize g.card_xsize
                    ysize g.card_ysize
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

label label_show_deck_callback(*args):
    $ game.jeu_sensitive = True
    return

screen screen_date_bottom_ui():

    if not renpy.variant("touch"):
        button:
            hovered SetVariable("game.isHoverHand", True)
            unhovered SetVariable("game.isHoverHand", False)
            action Return()
            xsize 1650
            if game.isHoverHand:
                ysize g.card_ysize
            else:
                ysize 200
            yalign 1.0
            xpos 120
            # background "#0f03"
    
    else:
        
        dismiss:
            action SetVariable("game.isHoverHand", False)
            modal False
        # button:
        #     action SetVariable("game.isHoverHand", False)
        #     modal False
        #     xsize 1920
        #     ysize 1080
        #     yalign 1.0
        #     xalign 0.35
        #     # background "#f003"
            
        button:
            action SetVariable("game.isHoverHand", True)
            xsize 1700
            if game.isHoverHand:
                ysize g.card_ysize
            else:
                ysize 200
            yalign 1.0
            xpos 150
            background "#00f3"

    use screen_card_hand()

screen screen_date_ui_navigator:
    sensitive game.jeu_sensitive
    key "input_up" action Call("label_date_ui_navigator_up")
    key "input_down" action Call("label_date_ui_navigator_up")
    key "input_left" action Call("label_date_ui_navigator_up")
    key "input_right" action Call("label_date_ui_navigator_up")

label label_date_ui_navigator_up():
    $ game.isHoverHand = True
    return

############################################################################################################
#
#    ::::::::: ::::::::::: ::::::::  :::    :::       :::::::          :::     :::     :::      ::::::::  
#    :+:    :+:    :+:    :+:    :+: :+:   :+:       :+:   :+:         :+:     :+:   :+: :+:   :+:    :+: 
#    +:+    +:+    +:+    +:+        +:+  +:+         +:+ +:+          +:+     +:+  +:+   +:+  +:+        
#    +#+    +:+    +#+    +#+        +#++:++           +#++:  ++#      +#+     +:+ +#++:++#++: :#:        
#    +#+    +#+    +#+    +#+        +#+  +#+         +#+ +#+#+#        +#+   +#+  +#+     +#+ +#+   +#+# 
#    #+#    #+#    #+#    #+#    #+# #+#   #+#       #+#   #+#+          #+#+#+#   #+#     #+# #+#    #+# 
#    ######### ########### ########  ###    ###       ##########           ###     ###     ###  ######## 
#
###########################################################################################################

image img_lust_bar = Flatten(Frame("ui/lust_bar.png",238,0,211,0,tile="integer"))
image img_lust_bar_full = Frame("ui/lust_bar_full.png",122,0,152,0)

image img_lust_bar_full_1 = Crop((0,0,122,125), "ui/lust_bar_full.png")
image img_lust_bar_locked = Frame("ui/lust_bar_locked.png",176,0,152,0,tile="True")

screen screen_dick_ui():

    if game.state == "dating" or game.state == "sexing":
        $ gameOrDate = date
        $ lustPerTurn = date.lustPerTurn
    else:
        $ gameOrDate = game
        $ lustPerTurn = 0

    default sizeMultiplier = 1/100
    $ shaft_size = int( 196*(getattr(gameOrDate, "lustMax") * sizeMultiplier) )
    $ fullSizeDick = 122 + shaft_size + 152
    $ lustRatio = getattr(gameOrDate, "lust")/getattr(gameOrDate, "lustMax")
    $ croppedSize = int ( fullSizeDick * lustRatio )

    if gameOrDate.lust + lustPerTurn >= gameOrDate.lustMax:
        $ matrixcolor = ColorizeMatrix("#822", "#fcc")
    else:
        $ matrixcolor = IdentityMatrix()
    fixed:
        ypos 20
        xpos 240
        xsize 122 + shaft_size + 152
        ysize 125

    ########################################################################################
    ################                                        ################################
    ################           THE ACTUAL DICK              ################################
    ################                                        ################################
    # maybe performance issues?
    ########################################################################################

        image Transform("img_lust_bar", matrixcolor=matrixcolor)
        bar value CustomAnimatedValue(value=getattr(gameOrDate,"lust"), range=getattr(gameOrDate, "lustMax")) xsize fullSizeDick ysize 125 left_bar Transform("img_lust_bar_full", matrixcolor=matrixcolor) right_bar "#0000"  
        showif game.state == "living":
            image Transform("img_lust_bar_locked", matrixcolor=matrixcolor) at trs_transition_dissolve



        fixed:
            xalign 0.5 ypos 30 xsize 300 ysize 50
            # add "#0f0"
            hbox:
                xalign 0.5 
                spacing 5
                text str(getattr(gameOrDate, "lust") ) + "{size=-15}/" + str(getattr(gameOrDate, "lustMax") ) + "{/size}":
                    yalign 1.0 size 50  font "font_venus_cormier" outlines [ (5, "#000000", 0, 3) ]
                    if (lustRatio )>0.5:
                        color Color("#ffed68").interpolate(Color("#ff1e00"), min(1.0,(lustRatio-0.5)*2))
                    else:
                        color Color("#ffffff").interpolate(Color("#ffed68"), min(1.0,lustRatio*2))
                if game.state == "living":
                    text _("{size=-10}({/size}+[game.lustPerDay]{size=-10}){/size}") style "style_pink_ui_day"
                if game.state == "sexing":
                    text _("{size=-10}({/size}+[date.lustPerTurn]{size=-10}){/size}") style "style_pink_ui_day"

                    if getattr(date,"lustMultiplier") !=1:
                        text "x" + str( getattr(date,"lustMultiplier")   ):
                            size 20+5*getattr(date,"lustMultiplier")xpos 60 xanchor 0.5 yanchor 0.5 ypos 55 color "#cbb000" style "outline_text" 

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


###########################################################################################################
#
#        ::::::::::: :::::::::  :::    :::  :::::::: :::::::::::      :::    ::: ::::::::::: 
#            :+:     :+:    :+: :+:    :+: :+:    :+:    :+:          :+:    :+:     :+:     
#            +:+     +:+    +:+ +:+    +:+ +:+           +:+          +:+    +:+     +:+     
#            +#+     +#++:++#:  +#+    +:+ +#++:++#++    +#+          +#+    +:+     +#+     
#            +#+     +#+    +#+ +#+    +#+        +#+    +#+          +#+    +#+     +#+     
#            #+#     #+#    #+# #+#    #+# #+#    #+#    #+#          #+#    #+#     #+#     
#            ###     ###    ###  ########   ########     ###           ########  ########### 
#
###########################################################################################################

init python:
    class CustomAnimatedValue(AnimatedValue):
        def __init__(self, value=0.0, range=1.0, old_value=None, delayPerIncrement=0.02):
            """
            :doc: value

            `maxdelay`
                The maximum delay time

            `delay`
                The delay, scaled with increment
            
            """
            super().__init__(value=value, range=range, delay=1.0, old_value=old_value)
            # self.maxdelay = maxdelay
            self.delayPerIncrement = delayPerIncrement

        def periodic(self, st):
            difference = abs(self.value - self.old_value)

            if self.start_time is None:
                self.start_time = st

            if self.value == self.old_value:
                return
            
            #  the delay is MAXIMUM self.delay
            fraction = (st - self.start_time) /(difference * self.delayPerIncrement)
            fraction = min(1.0, fraction)

            value = self.old_value + fraction * (self.value - self.old_value)

            self.adjustment.change(value)

            if fraction != 1.0:
                return 0

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
                        $ textStat = _("{k=15.0}LUST{/k}")
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

                    bar value CustomAnimatedValue(value=getattr(gameOrDate, stat), range=range_var)  xsize 440 ysize 60 left_bar colorStat right_bar colorStat2 

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
                        size 40 style "outline_dyslexic" #40 for ENG  size 50 for CN
                        color textColor
        if game.state == "living":
            text "([game.lustPerDay])":
                xalign 1.0
                ypos 10
                size 35 style "outline_dyslexic"
                color "#cc3"

define logTable = [0, 0, 0.01, 0.05, 0.12, 0.18, 0.28, 0.4, 0.53, 0.68, 0.85, 1.1, 1.18, 1.40, 1.85, 2.4, 3.0]
        
############################################################################################################
#
#        :::::::::      :::   :::   :::             ::::::::::: :::    ::: :::::::::  ::::    :::      
#        :+:    :+:   :+: :+: :+:   :+:                 :+:     :+:    :+: :+:    :+: :+:+:   :+:      
#        +:+    +:+  +:+   +:+ +:+ +:+                  +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+      
#        +#+    +:+ +#++:++#++: +#++:  +#++:++#++:++    +#+     +#+    +:+ +#++:++#:  +#+ +:+ +#+      
#        +#+    +#+ +#+     +#+  +#+                    +#+     +#+    +#+ +#+    +#+ +#+  +#+#+#      
#        #+#    #+# #+#     #+#  #+#                    #+#     #+#    #+# #+#    #+# #+#   #+#+#      
#        #########  ###     ###  ###                    ###      ########  ###    ### ###    ####      
#
###########################################################################################################

screen screen_day():
    $ local_screen_var = str(game.dateEvery - game.day % game.dateEvery)
    fixed:
        add Color(hsv=(0.6, min(1.0, 10/( max(1,game.day-125) )), 1.0))

        xsize 180
        ysize 180
        xpos 20 ypos 20

        
        text _("d   a   y"):
            size 30 color "#9feaf8"font "font_venus_cormier"  xalign 0.5 yalign 0.02 xsize 180

        text "{b}"+str(game.day)+"{/b}":
            size 140 xpos -10 yalign 0.8 outlines [ (5.5, "#000000", 0, 3.5) ] color "#ffffff"
            # xsize 180   color "#ffffff" font "font_venus_cormier" outlines [ (5.5, "#000000", 0, 3.5) ] 
            if game.day >= 100:
                kerning len(str(game.day))*-10
    
        if game.state == "living":
            fixed:
                if game.day % game.dateEvery==0:
                    text _("today!") style "style_pink_ui_day" xalign 0.5 yalign 1.0 
                elif game.day % game.dateEvery==game.dateEvery-1:
                    text _("tomorrow!") style "style_pink_ui_day" xalign 0.5 yalign 1.0 
                else:
                    text _("in [local_screen_var] days!") style "style_pink_ui_day" xalign 0.5 yalign 1.0 

style style_pink_ui_day:
    size 30 yalign 0.5 color "#de50c4" outlines [ (3, "#ffc5e9", 0, 0) ] font "Venus+Martre.otf"

image img_day_wave:
    xysize (382, 200)
    contains:
        Frame("ui/wavy.png", 0,19,0,0)
        xpos -196
        linear 5.0 xpos 0
        repeat

init python:
    def stupid_function(turnLeftRatio):
        if turnLeftRatio == 0:
            return 20
        else:
            return 0

transform trs_crop_wave(turnLeftRatio):
    subpixel True
    yalign 1.0
    linear 0.5 corner2 (180,1.0-turnLeftRatio) corner1 (0, stupid_function(turnLeftRatio))

screen screen_turn_counter:
    $ turnLeftRatio = (date.turnLeft)/date._turnLeft
    fixed:
        showif game.state == "dating" or game.state == "sexing":
            add Color("#00caff")
            add "img_day_wave" at trs_crop_wave(turnLeftRatio)

        xsize 180
        ysize 180
        xpos 20 ypos 20

        text "{b}{i}{k=-25.0}"+str(date.turnLeft)+"{/k}{/i}{/b}":
            size 190 style "outline_text" xpos 0 ypos 10
            if date.turnLeft>9:
                size 180  xpos -30
            elif date.turnLeft == 0:
                color "#fff"
            elif date.turnLeft>3:
                color Color("#000000")
            else:
                color Color("#000000").interpolate("#f00", (1.1-turnLeftRatio))


        if date.turnLeft <2:
            $ var_text = _("turn left")
        else:
            $ var_text = _("turns left")
        text var_text:
            size 25 font "Venus+Martre.otf" color "#ffffff" xalign 1.0 yalign 1.02
            
image img_end_turn:
    xysize (160, 290)
    contains:
        "ui/end_turn.png"
        xalign 1.0
        ypos 10
    contains:
        Text(_("END{size=60}\nTURN"), color="#ffffff", outlines=[ (5, "#00000055", 0, 0) ], kerning=-5, size=80, pos=(-20, 70), font="font_carrare")
        rotate -90
    # contains:
    #     Solid("#00f8")

image button_img_end_turn:
    on idle:
        Transform("img_end_turn",alpha=0.7)
    on hover:
        "img_end_turn"
    on selected_insensitive: #selected_hover, selected_idle, 
        crop (0, 0, 160, 290)
        contains:
            "img_end_turn"
            ypos 0
            linear 0.3 ypos -290
        contains:
            "img_end_turn"
            ypos 290
            linear 0.3 ypos 0

    on insensitive:
        Transform("img_end_turn",alpha=0.7)


############################################################################################################
#
#        ::::    ::::  ::::::::::: ::::::::   ::::::::  
#        +:+:+: :+:+:+     :+:    :+:    :+: :+:    :+: 
#        +:+ +:+:+ +:+     +:+    +:+        +:+        
#        +#+  +:+  +#+     +#+    +#++:++#++ +#+        
#        +#+       +#+     +#+           +#+ +#+        
#        #+#       #+#     #+#    #+#    #+# #+#    #+# 
#        ###       ### ########### ########   ########  
#
###########################################################################################################

screen screen_buttons_ui():

    #END TURN
    button: # at Transform(None,alpha=0.7)
        add "button_img_end_turn"
        align (0.0, 1.0)
        action [Play('sound',"card/switch.mp3", selected=True), Call(date.endTurn)]
        sensitive game.jeu_sensitive
            
    if game.state == "sexing" or game.debug_mode: # game.progress[0]>=2 or 
        fixed:
            xpos 1790
            ypos 605
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
        ypos 725
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

    # deck stack
    fixed:
        xpos 1765
        ypos 855  # when you move this, be sure that you can select it with arrow keys from menu
        xysize (125, 170)
        imagebutton:
            xysize (125, 170) # when you move this, be sure that you can select it with arrow keys from menu
            idle "cards/deck_stack.png"
            # idle Color("#ff0000")
            hover colorizeImg("cards/deck_stack.png",("#009f5d","#dfd"))
            action [Show("screen_show_deck", dissolve, sorted(deck.deck), "label_show_deck_callback", "CARDS LEFT")]
            sensitive game.jeu_sensitive
        fixed:
            xalign 0.45
            ypos 40
            xsize 30
            text str(len(deck.deck)) size 80 xalign 0.5 style "style_small_numbers"

screen screen_glass(id,position=(0,0)):
    if date.drink>0:
        imagebutton:
            pos position
            idle "bg/" + id + "-glass-" + str(date.drink) + ".png"
            focus_mask True
            hover tintImg("bg/" + id + "-glass-" + str(date.drink) + ".png", (255*1.5,255*1.5,255))
            action Call("label_drink")
            sensitive game.jeu_sensitive
    else:
        add "bg/" + id + "-glass-0.png" pos position

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


