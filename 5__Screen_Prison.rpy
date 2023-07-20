init python:
    deck_display_card_zoom = 0.8

transform customzoom:
    zoom deck_display_card_zoom

screen screen_prison:
    imagebutton:
        idle "bg/toilet.png"
        hover im.MatrixColor("bg/toilet.png", im.matrix.tint(1,1,5))
        action Call("label_toilet")
        focus_mask True
    imagebutton:
        idle "bg/bed.png"
        hover im.MatrixColor("bg/bed.png", im.matrix.tint(1,1,5))
        action Call("label_toilet")
        focus_mask True
    imagebutton:
        idle "bg/food-tray.png"
        hover im.MatrixColor("bg/food-tray.png", im.matrix.tint(1,1,5))
        action Call("label_toilet")
        focus_mask True
    imagebutton:
        idle "ui/exploring-deck_stack.png"
        hover im.MatrixColor("ui/exploring-deck_stack.png", im.matrix.tint(0.8,0.8,1))
        action Show("screen_card_deck", None, nullfunction)
        focus_mask True
    fixed:
        xpos 1780
        ypos 70
        xsize 30
        text str(len(deck.list)) size 60 xalign 0.5 style "outline_text"

label label_toilet:
    show screen screen_card_deck(prison_remove_card, "REMOVE A CARD")
    return

init python:
    def nullfunction(index):
        return
    def prison_remove_card(index):
        deck.list.pop(index)

screen screen_card_deck(card_function=nullfunction, instruction=""):
    
    $ zoom = deck_display_card_zoom
    $ paddingPerCard = int( -50 )
    $ ydisplace = getCardYdisplace()
    $ card_per_line = 10
    $ offset = card_per_line * 2 * global_var["page"]

        # cards at the bottom
    button:
        hovered SetVariable("game.isHoverHand", True)
        unhovered SetVariable("game.isHoverHand", False)
        action NullAction()
        xsize 1920
        ysize 300
        yalign 1.0
    
    fixed:
        for index, card in enumerate(deck.list):
            if offset<=index<offset+20:
                $ index2 = index % 20
                fixed:
                    xpos int((index2%card_per_line)* game.card_xsize + paddingPerCard*(index2%card_per_line)) + 70
                    ypos int(index2/card_per_line) * int(333*zoom) + 300
                    xsize int(game.card_xsize*zoom)
                    ysize int(game.card_ysize*zoom)
                    yanchor 0.0
                    xanchor 0.0
                    fixed:
                        imagebutton:
                            idle card.img
                            hover card.img_hover
                            action Function(card_function, index)
                            at customzoom
                        frame:
                            xalign 0.5
                            ypos int(180*zoom)
                            xsize int(210*zoom)
                            ysize int(130*zoom)
                            if len(card.txt)<30:
                                text card.txt style "style_card_effect" size 20 
                            else:
                                text card.txt style "style_card_effect" size 18 
    imagebutton:
        idle "ui/next.png"
        
        if global_var["page"]+1 < len(deck.list)/20:
            hover im.MatrixColor("ui/next.png", im.matrix.tint(1,1,0))
            action SetDict(global_var, "page", global_var["page"]+1)
        else:
            idle im.MatrixColor("ui/next.png", im.matrix.desaturate())
        yalign 0.95
        xalign 0.6
    imagebutton:
        idle "ui/prev.png"
        if global_var["page"]>0:
            hover im.MatrixColor("ui/prev.png", im.matrix.tint(1,1,0))
            action SetDict(global_var, "page", global_var["page"]-1)
        else:
            idle im.MatrixColor("ui/prev.png", im.matrix.desaturate())
        yalign 0.95
        xalign 0.4
    
    imagebutton:
        idle "ui/cancel.png"
        hover im.MatrixColor("ui/cancel.png", im.matrix.tint(1,1,0))
        action Hide("screen_card_deck")
        yalign 0.95
        xalign 0.5

    text instruction size 60 xalign 0.5 style "outline_text" ypos 200 xsize 1800