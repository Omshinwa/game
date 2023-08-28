label label_welcome_prison():
    $ game.state = "living"
    $ game.jeu_sensitive = False
    scene bg prison
    show screen screen_prison_sans_rat onlayer master
    show black onlayer screens
    hide black onlayer screens with Dissolve(2.0)
    "?"
    window hide
    window auto
    pause
    "You wake up, your body hurts."
    "You're in a strange place."
    show naked-mugshot at truecenter with Dissolve(1.0)
    "You're naked, your hands are tied."
    "An appartus is attached to your penis."
    hide naked-mugshot with dissolve
    j "Oh you woke up."
    show joyce smirk foxy outfitsm at depied with dissolve
    j "Did you sleep well?"
    menu:
        "Ask what's happening":
            pass
        "Try and jump on her":
            show joyce whip
            play sound "sex/whip.mp3"
            j "Wowo"
            j "Did you sleep on the wrong side?"
    j smile "Right now you're my little slave, you're gonna stay in my basement."
    j "You will sleep here and I'll feed you like the good pet you are."
    j "Every three days, I will come pick you, you will go through a physical exam."
    j "I will only free your chastity during those exams."
    j "If you manage not to cum, you'll move to the next stage."
    j "There's 4 different examinations in total."
    j "{b}At the last exam, we will have sex{/b}"
    j key "If at the last exam you manage to make me cum, then you win the key to your cage."
    j -key "Understood?"
    j "The milking starts now."
    play sound "sex/Fouet.mp3"
    show joyce push
    with vpunch
    jump label_sex_tutorial
        
label label_prison_first_time():

    $ game.state = "living"
    scene bg prison
    show screen screen_prison_sans_rat onlayer master
    show black onlayer screens
    hide black onlayer screens with dissolve
    pause 1.0
    rat "So there's a new guy huh." with dissolve
    rat "You're not the first one she locks here."
    hide screen_prison_sans_rat
    show screen screen_prison onlayer master
    with dissolve
    
    rat "I don't think you're gonna make it"
    rat "How about I trade you cards?"
    rat "Give me all your useless cards, I'll trade you new ones."

    $ score = 0
    $ i = []
    python:
        for card in deck.list:
            if "value2" in cardList[card.name]:
                score += cardList[card.name]["value2"]
            else:
                i.append(card)
    $ deck.list = i.copy()
    $ print("score: " + str(score))
    $ g.prison_cards = [[],[Card("calm"),Card("slower")],[]]
    $ availableCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] and cardList[key]["value"]>=0 } #
    $ goodCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] and cardList[key]["value"]>=2 } #
    # $ score /= 2
    $ i = score
    $ g.prison_cards[0] = [Card("universeout"),Card("universeout"),Card("spaceout"),Card("darkhole"),Card("recycle"),Card("threeof"),Card("change")]
    
    $ i = score - 2
    while i>score/2:
        $ g.prison_cards[1].append( Card.get_random_card(goodCards) )
        $ i -= cardList[g.prison_cards[1][-1].name]["value"]
    while i>0:
        $ g.prison_cards[1].append( Card.get_random_card(availableCards) )
        $ i -= cardList[g.prison_cards[1][-1].name]["value"]
        $ i -= 0.5
    $ i = score
    while i>score/2:
        $ g.prison_cards[2].append( Card.get_random_card(goodCards) )
        $ i -= cardList[g.prison_cards[2][-1].name]["value"]
    while i>0:
        $ g.prison_cards[2].append( Card.get_random_card(availableCards) )
        $ i -= cardList[g.prison_cards[2][-1].name]["value"]
        $ i -= 0.5
    
    $ del availableCards, goodCards
    show screen screen_replace_deck(g.prison_cards)

    call screen screen_gameloop()

    # label .gameLoop:
    #     call screen screen_gameloop()
    # jump .gameLoop

    rat "Good choice"
    rat "If you ever need help, I still have a lot of extra cards"
    rat "..from past prisonners hehe."
    rat "Just leave me some food around."
    rat "Good luck staying alive"
    jump label_prison

label label_prison():

    $ game.state = "living"
    scene bg prison
    show screen screen_prison onlayer master
    show black onlayer screens
    hide black onlayer screens with dissolve


    $ g.prison_cards = []
    $ availableCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] }

    $ g.prison_cards.append( Card.get_random_card(availableCards) )

    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[0].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[0].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    # $ g.prison_cards.append( Card.get_random_card(availableCards) )
    $ g.prison_cards.append( Card.get_random_card({"slower":1, "calm":1}) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] == 2 - availableCards[g.prison_cards[2].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    
    $ g.prison_cards.append( Card.get_random_card(availableCards) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[4].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[4].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    $ del availableCards, newlist

    label .gameLoop:
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    jump .gameLoop


label label_prison_open_door:
    hide screen screen_prison
    jump expression "label_" + game.story[game.progress[0]]

label label_prison_remove_card(index):
    hide screen screen_prison
    hide screen screen_show_deck
    # show expression deck.list[index].img:
    #     function trans_flush_card
    show screen screen_flushing(deck.list[index].img) with dissolve
    pause(1.0)
    hide screen screen_flushing
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
            call label_newDay("label_prison")
        "No":
            pass
    return

label label_prison_add_card(cards):
    $ i = 0
    while i < len(cards):
        call label_add_card_to_deck( "list", cards[i])
        $ i += 1

    hide screen screen_prison_food
    call label_newDay("label_prison")


label label_prison_add_card_firstTime(cards):
    $ i = 0
    while i < len(cards):
        call label_add_card_to_deck( "list", cards[i])
        $ i += 1

    hide screen screen_replace_deck
    return


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

screen screen_prison_sans_rat:
    use screen_lust_ui
    use screen_day
    use screen_deck_stack

    add "prison/toilet.png"
    add "prison/bed.png"
    add "prison/metal-door.png"
    add "prison/food-tray.png"

screen screen_prison:
    use screen_lust_ui
    use screen_day
    use screen_deck_stack
    sensitive game.jeu_sensitive

    imagebutton:  
        idle "prison/rat.png"
        hover im.MatrixColor("prison/rat.png", im.matrix.tint(1,1,5))
        action Show("screen_prison_food")
        focus_mask True

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

screen screen_prison_food(sixCards = g.prison_cards):
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

screen screen_add_cards_small(cards, callback=None):
    
    fixed:
        xalign 0.5
        yalign 0.5
        xsize int(game.card_xsize * len(cards)*0.8) + 20
        ysize int(game.card_ysize*0.8) + 20
        imagebutton:
            idle "#ffffffaa"
            hover "#ff0f"
            action Call(callback, cards)
        for index, card in enumerate(cards):
            add card.img zoom 0.8 xpos int(index*game.card_xsize*0.8) + 10 ypos 10

screen screen_replace_deck(threePacks):
    add "#000a"
    modal True
    
    fixed:
        ypos -260
        use screen_add_cards_small( threePacks[0], "label_prison_add_card_firstTime")
    fixed:
        ypos 30
        use screen_add_cards_small( threePacks[1], "label_prison_add_card_firstTime")
    fixed:
        ypos 320
        use screen_add_cards_small( threePacks[2], "label_prison_add_card_firstTime")

    text "Choose which set of cards to add" xalign 0.5 style "quirky_command" ypos 10 xsize 1800 at animated_text