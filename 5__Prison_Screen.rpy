screen screen_prison:
    use screen_lust_ui
    use screen_day
    imagebutton:
        idle "prison/toilet.png"
        hover im.MatrixColor("prison/toilet.png", im.matrix.tint(1,1,5))
        action Call("label_prison_toilet")
        focus_mask True
    imagebutton:
        idle "prison/bed.png"
        hover im.MatrixColor("prison/bed.png", im.matrix.tint(1,1,5))
        action Call("label_prison_bed")
        focus_mask True

    imagebutton:
        idle "prison/metal-door.png"
        hover im.MatrixColor("prison/metal-door.png", im.matrix.tint(1,1,5))
        action Jump("label_prison_open_door")
        focus_mask True

    imagebutton:
        idle "prison/food-tray.png"
        hover im.MatrixColor("prison/food-tray.png", im.matrix.tint(1,1,5))
        action Show("screen_prison_food")
        focus_mask True

    imagebutton:
        idle "ui/exploring-deck_stack.png"
        hover im.MatrixColor("ui/exploring-deck_stack.png", im.matrix.tint(0.8,0.8,1))
        action Show("screen_show_deck", dissolve, deck.list, "label_null")
        focus_mask True
    fixed:
        xpos 1780
        ypos 70
        xsize 30
        text str(len(deck.list)) size 60 xalign 0.5 style "outline_text"


init python:
    def trans_flush_card(trans, st, at):
        trans.xalign = 0.5
        trans.yalign = 0.5
        # trans.ypos = min(500, int( 1080-st*400 ))
        trans.zoom = min(4.0, 1.0 / ((st/1.5)+0.1))
        return 0

screen screen_flushing(card):
    add "img_toilet-flush" zoom 3.0
    add Transform(card, function=trans_flush_card)

screen screen_prison_food():
    add "#000a"
    modal True
    
    fixed:
        xpos -300
        use screen_add_cards( global_var["prison_cards"][:2] )
    fixed:
        xpos 300
        use screen_add_cards( global_var["prison_cards"][2:] )

    imagebutton:
        idle "ui/cancel.png"
        hover im.MatrixColor("ui/cancel.png", im.matrix.tint(1,1,0))
        action [Hide("screen_prison_food"),SetVariable("game.jeu_sensitive", True)]
        yalign 0.95
        xalign 0.5
    text "Choose which cards to add" size 120 xalign 0.5 style "outline_text" ypos 0 xsize 1800

screen screen_add_cards(cards):
    
    fixed:
        xalign 0.5
        yalign 0.5
        xsize game.card_xsize * len(cards) + 20
        ysize game.card_ysize + 20
        imagebutton:
            idle "#ffffffaa"
            hover "#ff0f"
            action Call("label_prison_add_card", cards)
        for index, card in enumerate(cards):
            add card.img xpos index*game.card_xsize + 10 ypos 10