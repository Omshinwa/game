transform trsfm_cards_go_down:
    ypos 1080
    ease 0.2 ypos 1210

transform trsfm_cards_go_up:
    ypos 1210
    ease 0.2 ypos 1080

transform trans_card_played:
    xalign 0.5 yanchor 1.0 ypos 1.0
    ease 0.4 ypos 0.5

transform trans_show_card_1(displayable):
    displayable
    xanchor 0.5 xzoom 1.0 xpos 300 ypos 500
    ease 1.0 xzoom 0.0
    "cards/card_bg.png"
    ease 1.0 xzoom 1.0
    ease 1.0 xzoom 0.0
    displayable
    ease 1.0 xzoom 1.0
    repeat

transform trans_show_card_2(displayable):
    displayable
    xanchor 0.5 yanchor 0.5 xpos 300 ypos 550
    ease 1.0 xpos 300 ypos 500
    ease 1.0 xpos 300 ypos 550
    repeat

transform trans_add_card_to_deck(displayable, xfrom=300, yfrom=550):
    displayable
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.5 zoom 1.5 xpos 960 ypos 350
    ease 0.5 zoom 0.2 xpos 1900 ypos 20 alpha 0.0
    