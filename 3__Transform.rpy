transform toobig:
    yalign 0.0
    ypos -100
    zoom 0.9

transform default_img_pos:
    xalign 0.5
    yanchor 1.0
    ypos 1080 - 200
    zoom 1.0

transform top:
    zoom 1.0
    xalign 0.5
    yalign 0.0


transform trsfm_cards_go_down:
    # on hide:
    #     ypos 1080
    ypos 1080
    ease 0.2 ypos 1220

transform trsfm_cards_go_up:
    # on hide:
    #     ypos 1080
    ypos 1220
    ease 0.2 ypos 1080

transform trans_card_played:
    xalign 0.5 yanchor 0.5 ypos 1080
    ease 0.4 ypos 450

transform trans_show_card_2(displayable):
    displayable
    xanchor 0.5 yanchor 0.5 xpos 300 ypos 550
    ease 1.0 xpos 300 ypos 500
    ease 1.0 xpos 300 ypos 550
    repeat

transform trans_add_card_to_deck(displayable, xfrom, yfrom, xto, yto, pauseTime=0):
    displayable
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.4 zoom 1.5 xpos 960 ypos 350
    pause pauseTime
    ease 0.4 zoom 0.2 xpos xto ypos yto alpha 0.0
    