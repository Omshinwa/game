label label_welcome_prison():
    $ game.lustPerDay = "1"
    $ game.lust = 0

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
    play sound "day/door_opening.wav"
    pause 0.4
    show joyce smirk foxy outfitsm at depied with dissolve
    j "Did you sleep well?"
    "?!"
    j smile "Poor boy is confused."
    j "Let me explain it to you."
    j "You're now my bitch."
    j "You're currenly in my basement."
    j smile "You will sleep here and I'll take care of you like the good pet you are."
    "??!!"
    menu:
        "Ask what does she want":
            j "You're my plaything now."
            j "I will train you to become a good slave."
            pass
        "Try and jump on her":
            show joyce whip
            play sound "sex/whip.mp3"
            j -smile "Wowo"
            j "Did you sleep on the wrong side?"
            j "Do you still not understand who's in control?"
    j "See that chastity belt I've attached to you?"
    j "I have its key, and the key to your new room."
    j smile "Every three days, I will come pick you, you will go through a physical exam."
    j "I will only free your chastity during those exams."
    j "If you manage not to cum, you'll move to the next stage."
    j "{b}At the last stage, you will fuck my pussy{/b}"
    j key "If then you manage to make me cum, you win the key to your cage."
    j "Understood?"
    j -key "I'll see you in 3 days."
    # j "Oh, and get rid of all those Trust and Attraction cards."
    # j "There's no point to them."
    
    play sound "day/door_opening.wav"
    hide joyce with dissolve

    $ g.rat = game.day + 4

    jump label_prison

     
label label_prison_first_time():

    rat "So there's a new guy huh." with dissolve
    rat "You're not the first one she locks here."
    hide screen_prison_sans_rat
    show screen screen_prison onlayer master
    with dissolve
    
    rat "I don't think you're gonna make it"
    rat "Plenty around died like you here."
    rat "I pity you."
    rat "How about I trade you cards?"
    rat "Give me all your useless cards, I'll trade you new ones."

    $ i = 0
    $ goodCards = ["eyecontact", "touchy", "flirt", "talk", "talk2", "listen"]
    $ toHide = []
    $ score = 0
    while i < len(deck.list):
        if deck.list[i].name in goodCards:
            $ renpy.show("card" + str(len(toHide)), what=deck.list[i].img, at_list=[give_cards_to_rat])
            $ toHide.append("card" + str(len(toHide)))
            $ score += cardList[deck.list[i].name]["value2"]
            $ deck.list.pop(i)
            $ i -= 1
            pause 0.1
        $ i += 1
    
    pause 0.6 + len(toHide)*0.1
    python:
        for i in toHide:
            renpy.hide(i)

    rat "Wow that's lot of shit cards"
    rat "Let me see what I have in stock."

    $ score /= 2

    $ print("score: " + str(score))
    $ g.prison_cards = [[],[Card("calm"),Card("slower")],[]]
    $ availableCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] and cardList[key]["value"]>=0 } #
    $ goodCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] and cardList[key]["value"]>=3 } #
    
    $ i = score
    $ g.prison_cards[0] = [Card("universeout"),Card("universeout"),Card("spaceout"),Card("darkhole"),Card("threeof"),Card("change")]
    
    $ i = score - 2
    while i>score/2:
        $ g.prison_cards[1].append( Card.get_random_card(goodCards) )
        $ i -= cardList[g.prison_cards[1][-1].name]["value"]
    while i>0 and len(g.prison_cards[1])<9:
        $ g.prison_cards[1].append( Card.get_random_card(availableCards) )
        $ i -= cardList[g.prison_cards[1][-1].name]["value"]
        $ i -= 0.5
    $ g.prison_cards[1].sort()
    $ i = score
    while i>score/2:
        $ g.prison_cards[2].append( Card.get_random_card(goodCards) )
        $ i -= cardList[g.prison_cards[2][-1].name]["value"]
    while i>0 and len(g.prison_cards[1])<9:
        $ g.prison_cards[2].append( Card.get_random_card(availableCards) )
        $ i -= cardList[g.prison_cards[2][-1].name]["value"]
        $ i -= 0.5
    $ g.prison_cards[2].sort()
    
    $ del availableCards, goodCards, toHide
    show screen screen_replace_deck(g.prison_cards)

    call screen screen_gameloop()

    rat "Good choice"
    rat "If you ever need help, I still have a lot of extra cards."
    rat "..from past prisonners hehe."
    rat "Just leave me some food around."
    rat "Good luck staying alive"
    $ g.rat -= 1
    jump label_prison

label label_prison():

    $ game.state = "living"
    scene bg prison

    if game.day <= g.rat:
        show screen screen_prison_sans_rat onlayer master 
    else:
        show screen screen_prison onlayer master

    show black onlayer screens
    hide black onlayer screens with dissolve

    if game.day == g.rat:
        jump label_prison_first_time
    elif game.day % game.dateEvery == 0:
        $ game.jeu_sensitive = False
        play sound "day/door_opening.wav"
        show joyce foxy outfitsm smile whip at depied with dissolve
        j "Hello my slave."
        j "The milking starts now."
        play sound "sex/Fouet.mp3"
        show joyce push
        with vpunch
        call label_prison_open_door(open=True) from _call_label_prison_open_door

    $ g.prison_cards = []
    $ availableCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] }

    $ g.prison_cards.append( Card( list(availableCards.keys())[ (game.day*2 + game.lust*11)%(len(availableCards)-1)] ) )

    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[0].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[0].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    
    $ g.prison_cards.append( Card.get_random_card({"slower":1, "slowsteady":1,"awakening":1,"calm":1, "maxcalm":1, "newday":1, "fibonacci":1, }) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[2].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[2].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    # $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] == 2 - availableCards[g.prison_cards[2].name]["value"]}
    # $ g.prison_cards.append( Card.get_random_card(newlist) )
    # $ g.prison_cards.append( Card.get_random_card(availableCards) )
    

    $ del availableCards, newlist

    label .gameLoop:
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    jump .gameLoop

label label_prison_open_door(open=False):
    if game.debug_mode or open:
        hide screen screen_prison
        jump expression "label_" + game.story[game.progress[0]]
    else:
        $ game.jeu_sensitive = False
        play sound "day/locked.wav"
        "It's closed."
        $ game.jeu_sensitive = True
    return

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

label label_prison_food:
    menu:
        "Eat and get stronger? (+1 dick size)"
        "Yes":
            $ game.lustMax += 1
            call label_newDay("label_prison") from _call_label_newDay_5
        "No":
            pass
    return

label label_prison_bed:
    menu:
        "Try to calm down (Cut your lust by 2)"
        "Yes":
            $ game.lust = int(game.lust/2)
            call label_newDay("label_prison") from _call_label_newDay_6
        "No":
            pass
    return

label label_prison_add_card(cards):

    hide screen screen_prison_rat_add_cards with dissolve
    $ i = 0
    while i < len(cards):
        call label_add_card_to_deck( "list", cards[i]) from _call_label_add_card_to_deck_3
        $ i += 1
    call label_newDay("label_prison") from _call_label_newDay_7


label label_prison_add_card_firstTime(cards):

    hide screen screen_replace_deck with dissolve
    $ i = 0
    while i < len(cards):
        call label_add_card_to_deck( "list", cards[i]) from _call_label_add_card_to_deck_4
        $ i += 1
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
    use screen_dick_ui
    use screen_day
    use screen_deck_stack
    sensitive game.jeu_sensitive

    imagebutton:
        idle "prison/toilet.png"
        hover Transform("prison/toilet.png", matrixcolor=TintMatrix((255,255,1275)))
        action Call("label_prison_toilet")
        focus_mask True

    imagebutton:
        idle "prison/bed.png"
        hover Transform("prison/bed.png", matrixcolor=TintMatrix((255,255,1275)))
        action Call("label_prison_bed")
        focus_mask True

    imagebutton:
        idle "prison/metal-door.png"
        hover Transform("prison/metal-door.png", matrixcolor=TintMatrix((255,255,1275)))
        action Call("label_prison_open_door")
        focus_mask True

    imagebutton:
        idle "prison/food-tray.png"
        hover Transform("prison/food-tray.png", matrixcolor=TintMatrix((255,255,1275)))
        action Call("label_prison_food")
        focus_mask True

screen screen_prison:
    use screen_dick_ui
    use screen_day
    use screen_deck_stack
    sensitive game.jeu_sensitive

    imagebutton:  
        idle "prison/rat.png"
        hover Transform("prison/rat.png", matrixcolor=TintMatrix((255,255,1275)))
        action Show("screen_prison_rat_add_cards")
        focus_mask True

    use screen_prison_sans_rat


screen screen_flushing(card):
    add "img_toilet-flush" zoom 3.0
    add card at trans_flush_card

screen screen_prison_rat_add_cards(sixCards = g.prison_cards):
    add "#000a"
    modal True
    
    # fixed:
    #     xpos -550
    #     use screen_add_cards( sixCards[:2], "label_prison_add_card")
    # fixed:
    #     xpos 0
    #     use screen_add_cards( sixCards[2:4], "label_prison_add_card")
    # # fixed:
    # #     xpos 550
    # #     use screen_add_cards( sixCards[4:], "label_prison_add_card")

    fixed:
        xpos -400
        use screen_add_cards( sixCards[:2], "label_prison_add_card")
    fixed:
        xpos 400
        use screen_add_cards( sixCards[2:4], "label_prison_add_card")

    imagebutton:
        idle "ui/cancel.png"
        hover Transform("ui/cancel.png", matrixcolor=TintMatrix((255,255,0)))
        action [Hide("screen_prison_rat_add_cards"),SetVariable("game.jeu_sensitive", True)]
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