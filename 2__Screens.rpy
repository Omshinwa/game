screen keybinds():
    key 'K_F2' action Function(debugmode)
    # ... etc.


screen screen_tutorial(disp, properties={}):
    add disp:
        properties properties
        
screen screen_day():
    fixed:
        add "#00f"
        xsize 200
        ysize 200
        xpos 20 ypos 20

        text "day":
            size 50 style "outline_text"  xalign 0.5 yalign 0.0

        text "{b}{k=0.0}"+str(game.day)+"{/k}{/b}":
            size 145 style "outline_text"  xalign 0.5 yalign 0.55
    
        if game.state == "living":
            if game.day % game.dateEvery==0:
                text "today!" size 30 xalign 0.45 ypos 155 color "#e970d2" style "outline_text"
            elif game.day % game.dateEvery==game.dateEvery-1:
                text "tomorrow!" size 30 xalign 0.45 ypos 155 color "#e970d2" style "outline_text"
            else:
                text "in " +str(game.dateEvery - game.day % game.dateEvery)+ " days!" size 30 xalign 0.45 ypos 155 color "#e970d2" style "outline_text"

screen screen_deck_stack():
    imagebutton:
        idle "ui/exploring-deck_stack.png"
        hover Transform("ui/exploring-deck_stack.png", matrixcolor=TintMatrix((204,204,255)))
        action Show("screen_show_deck", dissolve, deck.list, "label_null")
        focus_mask True

    fixed:
        xpos 1780
        ypos 70
        xsize 30
        text str(len(deck.list)) size 60 xalign 0.5 style "outline_text"

screen screen_show_deck(what=deck.list, label_callback="label_null", instruction="", background="#000a"):

    # sensitive game.jeu_sensitive
    
    modal True
    $ card_per_line = g.card_per_line

    # $ card_per_line = int( (len(deck.list))/2 + 0.5)
    $ zoom = 1800/(game.card_xsize * card_per_line)
    
    # $ zoom = 1800/(game.card_xsize * 7)
    
    $ line_per_page = int(780 / game.card_ysize / zoom)

    $ offset = card_per_line * line_per_page * g.page
    
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
                                action [SetVariable("g.page", 0), SetVariable("game.jeu_sensitive", False), Call(label_callback, index)]
                                at Transform(zoom=zoom)
        
    imagebutton:
        insensitive im.Grayscale("ui/next.png")
        sensitive g.page+1 < len(what)/(card_per_line * line_per_page)
        hover Transform("ui/next.png", matrixcolor=TintMatrix((255,255,0)))
        action SetVariable("g.page", g.page+1)
        idle "ui/next.png"
        yalign 0.97
        xalign 0.6
    imagebutton:
        sensitive g.page>0
        idle "ui/prev.png"
        insensitive im.Grayscale("ui/prev.png")
        hover Transform("ui/prev.png", matrixcolor=TintMatrix((255,255,0)))
        action SetVariable("g.page", g.page-1)
        yalign 0.97
        xalign 0.4
    
    imagebutton:
        idle "ui/cancel.png"
        hover Transform("ui/cancel.png", matrixcolor=TintMatrix((255,255,0)))
        action [SetVariable("g.page", 0), Hide("screen_show_deck"),SetVariable("game.jeu_sensitive", True)]
        yalign 0.97
        xalign 0.5

    fixed:
        xpos 1650
        ysize 100
        yalign 0.95
        if g.card_per_line >=5:
            imagebutton:
                idle "ui/zoom-in.png"
                hover Transform("ui/zoom-in.png", matrixcolor=TintMatrix((255,255,0)))
                action SetVariable("g.card_per_line", g.card_per_line-1)
        imagebutton:
            idle "ui/zoom-out.png"
            hover Transform("ui/zoom-out.png", matrixcolor=TintMatrix((255,255,0)))
            action SetVariable("g.card_per_line", g.card_per_line+1)
            xpos 100

    text instruction xalign 0.5 style "quirky_command" ypos 790 xsize 1600 at animated_text

screen screen_fullscreen(disp):
    # modal True
    button:
        xsize 1.0
        ysize 1.0
        action [Hide("screen_fullscreen", dissolve), Hide("screen_home_phone")]
    add "#000a"
    add disp:
        xalign 0.5
        yalign 0.5
