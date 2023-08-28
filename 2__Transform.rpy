transform shaking:    
    yoffset 0 zoom 1.0
    linear 0.05 zoom 1.01
    repeat
    # yoffset 0 zoom 1.0
    # linear 0.05 yoffset 3
    # linear 0.05 yoffset 0 zoom 1.001
    # linear 0.05 yoffset -3
    # repeat

transform toobig:
    yalign 0.0
    ypos -100
    zoom 0.9

transform depied:
    ypos 1080
    yanchor 1.0
    zoom 0.9 xalign 0.5

transform standing:
    ypos 1080
    yanchor 1.0
    zoom 1.0 xalign 0.5

transform sitting:
    # yoffset 100 #137
    ypos 1220
    yanchor 1.0
    zoom 1.0 xalign 0.5

transform top:
    zoom 1.0
    xalign 0.5
    yalign 0.0

transform shock(offset = 1.0):
    zoom offset
    linear 0.1 zoom offset-0.02
    linear 0.1 zoom offset

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

transform trans_add_card_to_deck(displayable, xfrom, yfrom, xto, yto, pauseTime=0):
    displayable
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.4 zoom 1.5 xpos 960 ypos 350
    pause pauseTime
    ease 0.4 zoom 0.2 xpos xto ypos yto alpha 0.0

transform animated_text:
    zoom 1.2
    crop (1.0,0.0,1.0,0.0)
    yoffset -100
    ease 0.7 crop (0,0,1.0,1.0) yoffset 0 zoom 1.0

transform switch:
    on show:
        ypos -1000 xalign 0.9
        ease 0.5 ypos 100
    on hide:
        ypos 100 xalign 0.9
        ease 0.5 ypos -1000

transform throw_away_home(a, b, c):
    zoom 4.0 xalign 0.5 yalign 0.5 rotate 0
    ease 1.0 zoom 0.5 rotate a xalign b yalign c

transform image_qui_defile:
    ypos 0
    linear 30 ypos -3570 
    repeat