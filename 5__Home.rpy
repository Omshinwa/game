screen screen_home:
    use screen_trust_ui()
    use screen_day
    use screen_deck_stack

    sensitive not renpy.get_screen("say")

    imagebutton:
        idle "home/door.png"
        hover im.MatrixColor("home/door.png", im.matrix.tint(1,1,0.7))
        action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
        focus_mask True
    imagebutton:
        idle "home/phone.png"
        hover im.MatrixColor("home/phone.png", im.matrix.tint(1,1,5))
        action Call("label_home_phone")
        focus_mask True
    imagebutton:
        idle "home/bed.png"
        hover im.MatrixColor("home/bed.png", im.matrix.tint(1,1,5))
        action Call("label_home_bed")
        focus_mask True

    imagebutton:
        idle "home/trash.png"
        hover im.MatrixColor("home/trash.png", im.matrix.tint(1,1,5))
        action Call("label_prison_toilet")
        focus_mask True

    imagebutton:
        idle "home/comp.png"
        hover im.MatrixColor("home/comp.png", im.matrix.tint(1,1,5))
        action Jump("label_prison") #Show("screen_home_food")
        focus_mask True
    imagebutton:
        idle "home/plant.png"
        hover im.MatrixColor("home/plant.png", im.matrix.tint(1,1,5))
        action Call("label_plant")
        focus_mask True
    imagebutton:
        idle "home/cat.png"
        hover im.MatrixColor("home/cat.png", im.matrix.tint(1,1,5))
        action Call("label_cat")
        focus_mask True

label label_home(newDay = False):
    "hello"
    $ game.state = "living"

    if newDay:
        $ renpy.play("newday.wav", channel='sound') 
        scene bg home
        show screen screen_home onlayer master
        with Fade(0.5, 1.0, 0.5)
        
        $ game.day += 1
    else:
        scene bg home
        show screen screen_home onlayer master
        with fade

    # $ global_var["prison_cards"] = []
    # $ global_var["prison_cards"].append( Card.get_random_card() )
    # $ global_var["prison_cards"].append( Card.get_random_card() )
    # $ global_var["prison_cards"].append( Card.get_random_card() )
    # $ global_var["prison_cards"].append( Card.get_random_card() )

    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop

label label_cat:
    play sound "meow.wav"
    menu:
        "talk to it":
            call label_home_add_cards("smalltalk", "Add a Small Talk to your deck?")
        "listen to it":
            call label_home_add_cards("listen", "Add a Listen to your deck?")
        "look at it":
            call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?")
        "touch it":
            call label_home_add_cards("touchy", "Add a Touchy to your deck?")
        "X":
            return

    return

label label_plant():
    menu:
        "water it":
            call label_home_add_cards("calm", "Add a Calm to your deck?")
        "communicate with it":
            call label_home_add_cards("awakening", "Add an Awakening to your deck?")
        "X":
            return
    return

label label_home_add_cards(cardID, prompt):
    show expression trans_show_card_2(Card(cardID).img) as card
    menu:
        "[prompt]"
        "yes":
            hide card
            call label_add_card_to_deck("list", cardID, 300, 500)
            $ hide_all_screens_but("home")
            $ game.nextDay("label_home")
        "no":
            hide card
            hide screen screen_tutorial
    return

label label_home_phone():
    # show phone-big:
    #     ypos -1000 xalign 0.9
    #     ease 0.5 ypos 100
        
    show screen screen_home_phone

    # pause
    # show phone-big:
    #     ypos 100 xalign 0.9
    #     ease 0.5 ypos -1000
    # pause 0.5
    # hide phone-big
    return

transform phone_in():
    ypos -1000 xalign 0.9
    ease 0.5 ypos 100
transform phone_out():
    ypos 100 xalign 0.9
    ease 0.5 ypos -1000

screen screen_home_phone():
    modal True
    # default toggle = True

    imagebutton at switch:
        idle "home/phone-big.png"
        action [Hide("screen_home_phone")]

    # if toggle:
    #     textbutton "left" action SetScreenVariable('toggle', False ) at switch:
    #         xcenter 0.33 ycenter 0.5
    # if not toggle:
    #     textbutton "right" action SetScreenVariable('toggle', True ) at switch:
    #         xcenter 0.66 ycenter 0.5

transform switch:
    on show:
        ypos -1000 xalign 0.9
        ease 0.5 ypos 100
    on hide:
        ypos 100 xalign 0.9
        ease 0.5 ypos -1000