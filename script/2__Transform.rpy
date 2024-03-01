
#        ::::::::::: ::::::::  :::   :::  ::::::::  :::::::::: 
#            :+:    :+:    :+: :+:   :+: :+:    :+: :+:        
#            +:+    +:+    +:+  +:+ +:+  +:+        +:+        
#            +#+    +#+    +:+   +#++:   +#+        +#++:++#   
#            +#+    +#+    +#+    +#+    +#+        +#+        
#        #+# #+#    #+#    #+#    #+#    #+#    #+# #+#        
#         #####      ########     ###     ########  ########## 


transform shaking:    
    yoffset 0 zoom 1.0
    linear 0.05 zoom 1.01
    repeat

transform trs_fastbreath:
    yoffset 0 zoom 1.0
    linear 0.45 zoom 1.005
    linear 0.45 zoom 1.00
    repeat

transform trs_slowbreath:
    subpixel True
    block:
        yoffset 0 yzoom 1.0
        ease 3 yzoom 1.005 xzoom 1.002
        ease 3 yzoom 1.0 xzoom 1.0
        repeat

transform trs_depied:
    ypos 1080
    yanchor 1.0
    zoom 0.9 xalign 0.5

transform trs_standing: #thats just trs_sitting but when they get up
    ypos 1080
    yanchor 1.0
    zoom 1.0 xalign 0.5

transform trs_sitting:
    # yoffset 100 #137
    ypos 1220
    yanchor 1.0
    zoom 1.0 xalign 0.5

transform trs_bg_blur(strength=4,mask="hard", child=None):
    contains:
        child
    contains:
        AlphaMask(child,"bg_mask_"+mask)
        blur strength

init python:
    def get_joyce_zoom():
        if renpy.get_image_bounds("joyce"):
            return renpy.get_image_bounds("joyce")[3] / 1250 #1250 is the height of the picture
        else:
            return 1.0

transform shock(offset = get_joyce_zoom()):
    zoom offset
    linear 0.1 zoom offset-0.02
    linear 0.1 zoom offset


#        ::::::::   ::::::::  :::::::::  :::::::::: :::::::::: ::::    ::: 
#       :+:    :+: :+:    :+: :+:    :+: :+:        :+:        :+:+:   :+: 
#       +:+        +:+        +:+    +:+ +:+        +:+        :+:+:+  +:+ 
#       +#++:++#++ +#+        +#++:++#:  +#++:++#   +#++:++#   +#+ +:+ +#+ 
#              +#+ +#+        +#+    +#+ +#+        +#+        +#+  +#+#+# 
#       #+#    #+# #+#    #+# #+#    #+# #+#        #+#        #+#   #+#+# 
#        ########   ########  ###    ### ########## ########## ###    #### 


transform trs_transition_dissolve:
    on hide:
        linear .25 alpha 0.0
    on show:
        linear .25 alpha 1.0

transform trs_transition_dick_fill_up(croppedSize):
    subpixel True
    corner1 (0, 0)
    linear 0.5 corner2 (croppedSize, 120) 

transform trsfm_cards_go_down:
    ypos 1080
    ease 0.2 ypos 1220

transform trsfm_cards_go_up:
    ypos 1220
    ease 0.2 ypos 1080

transform trans_card_played(xfrom=0.5, yfrom=1080, xto=0.5, yto=450): #when card is played from hand
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.4 xpos xto ypos yto

transform trans_show_card_2(displayable, offset=0): #floating up and down card
    displayable
    xanchor 0.5 yanchor 0.5 xpos 800 ypos 550
    block:
        ease 1.0 xpos 300 ypos 500
        ease 1.0 xpos 300 ypos 550
        repeat

transform trans_show_card_1(displayable, offset=0): #floating up and down card, card from deck
    displayable
    xanchor 0.5 yanchor 0.5 xpos 1800 ypos 50
    block:
        ease 1.0 xpos 1600 ypos 550
        ease 1.0 xpos 1600 ypos 500
        repeat

transform trans_anim_move_card(xfrom, yfrom, xto, yto, pauseTime=0):
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.4 zoom 1.5 xpos 960 ypos 350
    pause pauseTime
    ease 0.4 zoom 0.2 xpos xto ypos yto alpha 0.0

transform animated_text:
    zoom 1.2
    crop (1.0,0.0,1.0,0.0)
    yoffset -100
    ease 0.7 crop (0,0,1.0,1.0) yoffset 0 zoom 1.0



#        ::::    ::::  ::::::::::: ::::::::   ::::::::  
#        +:+:+: :+:+:+     :+:    :+:    :+: :+:    :+: 
#        +:+ +:+:+ +:+     +:+    +:+        +:+        
#        +#+  +:+  +#+     +#+    +#++:++#++ +#+        
#        +#+       +#+     +#+           +#+ +#+        
#        #+#       #+#     #+#    #+#    #+# #+#    #+# 
#        ###       ### ########### ########   ########  


transform trs_phone:
    on show:
        ypos -1000 xalign 0.9
        ease 0.5 ypos 100
    on hide:
        ypos 100 xalign 0.9
        ease 0.5 ypos -1000

transform throw_away_home(a, b, c):
    zoom 4.0 xalign 0.5 yalign 0.5 rotate 0
    ease 1.0 zoom 0.5 rotate a xalign b yalign c

transform trans_flush_card:
    parallel:
        rotate 0
        pause 0.8
        ease 2.0 rotate 360
    parallel:
        zoom 4.0 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
        ease 1.0 zoom 1.0



transform image_qui_defile:
    ypos 0
    linear 30 ypos -3570 
    repeat

transform give_cards_to_rat:
    zoom 0.7 xpos 1820 ypos 120 xanchor 0.5 yanchor 0.5
    easein 0.5 xpos 700 ypos 800
    function renpy.curry(play_sexsound)(filename="card/draw.mp3") #hacky
    ease 0.1 xpos 680 ypos 820
    alpha 0.0

