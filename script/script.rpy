define j = Character(None, image="joyce", kind=bubble)
define rat = Character(None, image="rat", kind=bubble)

default povname = "William"

default game = Game()
default date = Date("date")

# The game starts here.

label start:
    $ game = Game()
    $ quick_menu = True
    # call screen Content_Warning()
    scene black
    with dissolve
    $ deck = Deck()


    $ deck.list = [Card("chat"),Card("chat"),Card("chat"),Card("calm"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    Card("spaceout"),Card("listen"),Card("eyecontact"),Card("draw2"),Card("flirt"),Card("pair"),Card("recycle")]

    # python:
    #     for card in cardList:
    #         deck_default.append(Card(card))
    
    $ povname = renpy.input("What is your name?", length=32)
    with dissolve
    $ povname = povname.strip()

    if not povname:
        $ povname = "William"

    call label_show_act(Solid("#fff"), color.marine)

    jump expression "label_" + g.story[0]
    # jump label_home
    # jump label_prison_rat_introduction

    return

label label_show_act(bg, textColor):
    scene expression bg with dissolve
    show screen screen_act_display(textColor) with Dissolve(1.0)
    pause 0.3
    play sound "day/clock-tick_short.wav"
    $ game.act += 1
    with blinds
    hide screen screen_act_display with Dissolve(1.5, time_warp=_warper.easeout_cubic)
    return

screen screen_act_display(textColor="#fff"):
    default change = game.act

    fixed:
        xsize 1000
        xalign 0.5

        if game.act == 0:
            text "Act":
                size 300 xpos 50 yalign 0.4 color textColor font "font_venus_cormier" 
        else:
            text "Act "+str(game.act):
                size 300 xpos 50 yalign 0.4 color textColor font "font_venus_cormier"
            # xsize 180   color "#ffffff" font "font_venus_cormier" outlines [ (5.5, "#000000", 0, 3.5) ] 
        
        if change != game.act:
            if game.act == 1:
                text "Who is she?":
                    size 150 xalign 0.5 yalign 0.6 color color.sky font "Venus+Martre.otf" 
            elif game.act == 2:
                text "Where am I?":
                    size 150 xalign 0.5 yalign 0.6 color "#000" font "Venus+Martre.otf" 
            elif game.act == 3:
                text "What are we?":
                    size 150 xalign 0.5 yalign 0.6 color "#000" font "Venus+Martre.otf" 