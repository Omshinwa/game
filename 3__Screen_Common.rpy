screen keybinds():
    key 'K_F2' action Function(debugmode)
    # ... etc.


screen screen_day():
    fixed:
        add "#00f"
        xsize 200
        ysize 200
        xpos 20 ypos 20

        text "day":
            size 50 style "outline_text"  xalign 0.5 yalign 0.0

        text "{b}{k=0.0}"+str(game.day)+"{/k}{/b}":
            size 150 style "outline_text"  xalign 0.5 yalign 1.0

screen screen_deck_stack():
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

screen screen_show_deck(what=deck.list, label_callback="label_null", instruction="", background="#000a"):

    modal True
    $ card_per_line = global_var.card_per_line

    # $ card_per_line = int( (len(deck.list))/2 + 0.5)
    $ zoom = 1800/(game.card_xsize * card_per_line)
    
    # $ zoom = 1800/(game.card_xsize * 7)
    
    $ line_per_page = int(780 / game.card_ysize / zoom)

    $ offset = card_per_line * line_per_page * global_var.page
    
    add background
    fixed:
        xsize 1800
        ysize 780
        xalign 0.5
        ypos 20
        
        add "#0005"

        fixed:

            for index, card in enumerate(what):
                if offset<=index<offset+(line_per_page*card_per_line):
                    $ index2 = index % (line_per_page*card_per_line)
                    fixed:
                        xalign index2%card_per_line / (card_per_line-1)
                        ypos int(index2/card_per_line) * int(333*zoom)
                        xsize int(game.card_xsize*zoom)
                        ysize int(game.card_ysize*zoom)
                        yanchor 0.0
                        # xanchor 0.0
                        fixed:
                            imagebutton:
                                idle card.img
                                hover card.img_hover
                                action [SetVariable("global_var.page", 0), Call(label_callback, index)]
                                at Transform(zoom=zoom)
        
    imagebutton:
        insensitive im.Grayscale("ui/next.png")
        sensitive global_var.page+1 < len(what)/(card_per_line * line_per_page)
        hover im.MatrixColor("ui/next.png", im.matrix.tint(1,1,0))
        action SetVariable("global_var.page", global_var.page+1)
        idle "ui/next.png"
        yalign 0.97
        xalign 0.6
    imagebutton:
        sensitive global_var.page>0
        idle "ui/prev.png"
        insensitive im.Grayscale("ui/prev.png")
        hover im.MatrixColor("ui/prev.png", im.matrix.tint(1,1,0))
        action SetVariable("global_var.page", global_var.page-1)
        yalign 0.97
        xalign 0.4
    
    imagebutton:
        idle "ui/cancel.png"
        hover im.MatrixColor("ui/cancel.png", im.matrix.tint(1,1,0))
        action [SetVariable("global_var.page", 0), Hide("screen_show_deck"),SetVariable("game.jeu_sensitive", True)]
        yalign 0.97
        xalign 0.5

    fixed:
        xpos 1650
        ysize 100
        yalign 0.95
        if global_var.card_per_line >=5:
            imagebutton:
                idle "ui/zoom-in.png"
                hover im.MatrixColor("ui/zoom-in.png", im.matrix.tint(1,1,0))
                action SetVariable("global_var.card_per_line", global_var.card_per_line-1)
        imagebutton:
            idle "ui/zoom-out.png"
            hover im.MatrixColor("ui/zoom-out.png", im.matrix.tint(1,1,0))
            action SetVariable("global_var.card_per_line", global_var.card_per_line+1)
            xpos 100

    text instruction xalign 0.5 style "quirky_command" ypos 790 xsize 1600 at animated_text