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
        action Call("label_home_toilet")
        focus_mask True
    imagebutton:
        idle "home/bed.png"
        hover im.MatrixColor("home/bed.png", im.matrix.tint(1,1,5))
        action Call("label_home_bed")
        focus_mask True

    imagebutton:
        idle "home/trash.png"
        hover im.MatrixColor("home/trash.png", im.matrix.tint(1,1,5))
        action Jump("label_prison_toilet")
        focus_mask True

    imagebutton:
        idle "home/comp.png"
        hover im.MatrixColor("home/comp.png", im.matrix.tint(1,1,5))
        action Jump("label_prison") #Show("screen_home_food")
        focus_mask True
    imagebutton:
        idle "home/plant.png"
        hover im.MatrixColor("home/plant.png", im.matrix.tint(1,1,5))
        action Show("screen_home_food")
        focus_mask True
    imagebutton:
        idle "home/cat.png"
        hover im.MatrixColor("home/cat.png", im.matrix.tint(1,1,5))
        action Call("label_cat")
        focus_mask True
        tooltip "testeeeded"

        
    # This has to be the last thing shown in the screen.
    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]"

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip


label label_home(newDay = False):

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
            show expression trans_show_card_2(Card("smalltalk").img) as card
            menu:
                "Add a Small Talk to your deck?"
                "yes":
                    hide card
                    call label_add_card_to_deck("smalltalk", 300, 500)
                    $ hide_all_screens_but("home")
                    $ game.nextDay("label_home")
                "no":
                    hide card
                    hide screen screen_tutorial
                    return
        "listen to it":
            show expression trans_show_card_2(Card("listen").img) as card
            menu:
                "Add a Listen to your deck?"
                "yes":
                    hide card
                    call label_add_card_to_deck("listen", 300, 500)
                    $ hide_all_screens_but("home")
                    $ game.nextDay("label_home")
                "no":
                    hide card
                    hide screen screen_tutorial
                    return
        "look at it":
            show expression trans_show_card_2(Card("eyecontact").img) as card
            menu:
                "Add an Eye Contact to your deck?"
                "yes":
                    hide card
                    call label_add_card_to_deck("eyecontact", 300, 500)
                    $ hide_all_screens_but("home")
                    $ game.nextDay("label_home")
                "no":
                    hide card
                    hide screen screen_tutorial
                    return
        "touch it":
            show expression trans_show_card_2(Card("touchy").img) as card
            menu:
                "Add a Touchy to your deck?"
                "yes":
                    hide card
                    call label_add_card_to_deck("touchy", 300, 500)
                    $ hide_all_screens_but("home")
                    $ game.nextDay("label_home")
                "no":
                    hide card
                    hide screen screen_tutorial
                    return
        "play with it":
            "It doesn't feel like playing, maybe if you looked at it first?"
            show expression trans_show_card_2(Card("flirt").img) as card
            show expression trans_show_card_2(Card("eyecontact").img) as card2:
                xpos 1600
            menu:
                "Change an Eye Contact in your deck into a Flirt?"
                "yes":
                    hide card
                    hide card2
                    call label_add_card_to_deck("flirt", 300, 500)
                    $ hide_all_screens_but("home")
                    $ game.nextDay("label_home")
                "no":
                    hide card
                    hide card2
                    hide screen screen_tutorial
                    return
    show joyce 
    "cool life"
    "life"
    return
