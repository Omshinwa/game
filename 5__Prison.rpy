label label_prison():

    $ game.state = "living"
    scene bg prison
    show screen screen_prison onlayer master
    show black onlayer screens
    hide black onlayer screens with dissolve



    $ availableCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] }

    $ global_var.prison_cards.append( Card.get_random_card(availableCards) )

    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[global_var.prison_cards[0].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[global_var.prison_cards[0].name]["value"]}
    $ global_var.prison_cards.append( Card.get_random_card(newlist) )

    $ global_var.prison_cards.append( Card.get_random_card(availableCards) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] == 2 - availableCards[global_var.prison_cards[2].name]["value"]}
    $ global_var.prison_cards.append( Card.get_random_card(newlist) )

    
    $ global_var.prison_cards.append( Card.get_random_card(availableCards) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[global_var.prison_cards[4].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[global_var.prison_cards[4].name]["value"]}
    $ global_var.prison_cards.append( Card.get_random_card(newlist) )

    $ del availableCards, newlist

    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop



label label_prison_open_door:
    hide screen screen_prison
    jump expression "label_" + game.story[game.progress[0]]

label label_prison_remove_card(index):
    hide screen screen_prison
    hide screen screen_show_deck
    show expression deck.list[index].img:
        function trans_flush_card
    show screen screen_flushing(deck.list[index].img) with dissolve
    pause(1.0)
    hide screen screen_flushing
    hide expression deck.list[index].img
    $ deck.list.pop(index)
    $ renpy.call("label_newDay", "label_prison")

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

label label_prison_add_card(cards):
    $ i = 0
    while i < len(cards):
        call label_add_card_to_deck( "list", cards[i])
        $ deck.list.append( cards[i] )
        $ i += 1
    $ deck.list.sort()

    hide screen screen_prison_food
    $ game.nextDay("label_prison")



#############################################################################
##                                                                                     
##
##     #######    #####  ######    #######  #######  ###   ##   #######
##     ##       ###      ##   ##   ##       ##       ####  ##   ##
##     #######  ##       ######    #####    #####    ## ## ##   #######
##          ##  ###      ##  ##    ##       ##       ##  ####        ##
##     #######    #####  ##   ##   #######  #######  ##   ###   #######
##
##
#############################################################################

screen screen_prison:
    use screen_lust_ui
    use screen_day
    use screen_deck_stack

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


init python:
    def trans_flush_card(trans, st, at):
        trans.xalign = 0.5
        trans.yalign = 0.5
        trans.zoom = min(4.0, 1.0 / ((st/1.5)+0.1))
        return 0

screen screen_flushing(card):
    add "img_toilet-flush" zoom 3.0
    add Transform(card, function=trans_flush_card)

screen screen_prison_food(sixCards = global_var.prison_cards):
    add "#000a"
    modal True
    
    fixed:
        xpos -550
        use screen_add_cards( sixCards[:2], "label_prison_add_card")
    fixed:
        xpos 0
        use screen_add_cards( sixCards[2:4], "label_prison_add_card")
    fixed:
        xpos 550
        use screen_add_cards( sixCards[4:], "label_prison_add_card")

    imagebutton:
        idle "ui/cancel.png"
        hover im.MatrixColor("ui/cancel.png", im.matrix.tint(1,1,0))
        action [Hide("screen_prison_food"),SetVariable("game.jeu_sensitive", True)]
        yalign 0.95
        xalign 0.5
    text "Choose which set of cards to add" xalign 0.5 style "quirky_command" ypos 150 xsize 1800 at animated_text

screen screen_add_cards(cards, callback=None):
    
    fixed:
        xalign 0.5
        yalign 0.5
        xsize game.card_xsize * len(cards) + 20
        ysize game.card_ysize + 20
        imagebutton:
            idle "#ffffffaa"
            hover "#ff0f"
            action Call(callback, cards)
        for index, card in enumerate(cards):
            add card.img xpos index*game.card_xsize + 10 ypos 10