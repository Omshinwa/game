label label_prison_open_door:
    hide screen screen_prison
    jump expression "label_" + game.story[game.progress[0]]


label label_prison_remove_card(index):
    hide screen screen_prison
    hide screen screen_show_deck
    # $ renpy.movie_cutscene("images/prison/input.avi")
    show expression deck.list[index].img:
        function trans_flush_card
    show screen screen_flushing(deck.list[index].img) with dissolve
    pause(2.0)
    hide screen screen_flushing
    hide expression deck.list[index].img
    show screen screen_prison with dissolve
    $ game.nextDay("label_prison")


label label_prison_toilet:
    show screen screen_show_deck(label_callback="label_prison_remove_card", instruction=_("REMOVE A CARD"), background="img_toilet-static")
    return

label label_prison_bed:
    menu:
        "Gain +1 dick size?"
        "Yes":
            $ date.lustMax += 1
            $ game.nextDay("label_prison")
        "No":
            pass
    return

init python:
    global_var["prison_cards"] = []
    global_var["prison_cards"].append( Card.get_random_card() )
    global_var["prison_cards"].append( Card.get_random_card() )
    global_var["prison_cards"].append( Card.get_random_card() )
    global_var["prison_cards"].append( Card.get_random_card() )

label label_prison:
    scene bg prison
    show screen screen_prison

    $ global_var["prison_cards"] = []
    $ global_var["prison_cards"].append( Card.get_random_card() )
    $ global_var["prison_cards"].append( Card.get_random_card() )
    $ global_var["prison_cards"].append( Card.get_random_card() )
    $ global_var["prison_cards"].append( Card.get_random_card() )

    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop

label label_prison_add_card(cards):
    $ i = 0
    while i < len(cards):
        $ deck.list.append( cards[i] )
        $ i += 1
    $ deck.list.sort()

    hide screen screen_prison_food
    $ game.nextDay("label_prison")