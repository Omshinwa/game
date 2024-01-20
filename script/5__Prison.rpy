label label_welcome_prison():
    # $ game.dateEvery = 7
    
    # $ game.lustPerDay = "5"
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
    "You feel sore."
    "You're in a strange place."
    show naked-mugshot at truecenter with Dissolve(1.0)
    "You're naked. Your hands are tied."
    "A device is attached to your penis."
    hide naked-mugshot with dissolve
    j "Oh, you're awake."
    play sound "day/door_opening.wav"
    pause 0.4
    show joyce smirk foxy outfitsm at trs_depied with dissolve
    j "Did you sleep well?"
    "?!"
    j smile "Aww, the poor thing is confused."
    j "I'll explain the situation."
    j "You are now my bitch."
    j "This is my basement."
    j smile "You will sleep here and I'll take care of you like the good pet you are."
    "??!!"
    menu:
        "Ask what does she want":
            j "From now on, you're my plaything."
            j "I'll train you to become a good little slave."
            pass
        "Try and jump on her":
            show joyce whip
            play sound "sex/whip.mp3"
            j -smile "Hey now…"
            j "Did you sleep on the wrong side?"
            j "Do you still not understand who's in control?"
    j "See that chastity belt I've put on you?"
    j "I've got the key for it as well as the key to your cage."
    j smile "I'll come to check on you twice a week. You'll undergo a physical check-up."
    j "This is the only occasion your cock will be free."
    j "If you manage not to cum, you'll move on to the next stage."
    j "{b}At the last stage, you will fuck my pussy.{/b}"
    j key "If you can make me cum, you win the key to your cage."
    j "Understood?"
    j -key "I'll see you in 3 days."

    
    
    play sound "day/door_opening.wav"
    hide joyce with dissolve

    $ g.day_rat_appears = game.day + 4

    jump label_prison

     
label label_prison_rat_introduction():
    $ game.jeu_sensitive = False
    rat "So she caught another one, huh." with dissolve
    rat "You're not the first one to get trapped here."
    hide screen_prison_sans_rat
    show screen screen_prison onlayer master
    with dissolve
    
    rat "Doesn't seem like you've got what it takes, either."
    rat "Many men stronger than you have lost their lives here before."
    rat "Heh. How unfortunate."
    rat "How about I trade you some cards?"
    rat "Give me all your useless cards and I'll trade you new ones."

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
    $ g.prison_cards[0] = [Card("slowsteady"),Card("spaceout"),Card("universeout"),Card("darkhole"),Card("pair"),Card("change")]
    
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

    rat "Good choice."
    rat "If you ever need help, I still have a lot of extra cards."
    rat "…from past prisoners, hehe."
    rat "Just leave some food for me."
    rat "Good luck staying alive"
    $ g.day_rat_appears -= 1
    $ game.jeu_sensitive = True
    jump label_prison

label label_prison():

    $ game.state = "living"
    scene bg prison

    if game.day <= g.day_rat_appears:
        show screen screen_prison_sans_rat onlayer master 
    else:
        show screen screen_prison onlayer master

    show black onlayer screens
    hide black onlayer screens with dissolve

    if game.day == g.day_rat_appears:
        jump label_prison_rat_introduction
    
    $ g.prison_cards = []
    $ availableCards = { key: item for (key, item) in cardList.items() if "value" in cardList[key] }

    $ g.prison_cards.append( Card( list(availableCards.keys())[ (game.day*3 + game.lust*11-7)%(len(availableCards)-1)] ) )

    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[0].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[0].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    $ g.prison_cards.append( Card.get_random_card({"slower":1, "slowsteady":1,"awakening":1,"calm":1, "maxcalm":1, "newday":1, "fibonacci":1, }) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[2].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[2].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )


    $ g.prison_cards.append( Card( list(availableCards.keys())[ (game.day*11 + game.lust*3+7)%(len(availableCards)-1)] ) )
    $ newlist = { key: item for (key, item) in availableCards.items() if availableCards[key]["value"] >= 1 - availableCards[g.prison_cards[4].name]["value"] and availableCards[key]["value"] <= 3 - availableCards[g.prison_cards[4].name]["value"]}
    $ g.prison_cards.append( Card.get_random_card(newlist) )

    # make it more likely to gather all pieces of exodia
    python:
        availableCards = ["exodia1", "exodia2", "exodia3"]

        for index, card in enumerate(g.prison_cards):
            if card.name in availableCards: #if there is an exodia card in prison
                if card.name in [card2.name for card2 in deck.list]: #si la carte est déjà présente dans le deck
                    for exodiaCard in availableCards: # on teste pour chaque carte exodia si elles sont dans le deck ou pas
                        if exodiaCard not in [card2.name for card2 in deck.list]:
                            g.prison_cards[index] = Card(exodiaCard)

    $ del availableCards, newlist

    #sex time
    if game.day % game.dateEvery == 0:
        if game.debug_mode:
            menu:
                "Let Joyce enter":
                    pass
                "Close the door":
                    jump .gameLoop
        $ game.jeu_sensitive = False
        play sound "day/door_opening.wav"
        show joyce foxy outfitsm smile whip at trs_depied with dissolve
        j "Hello, slave."
        j "The milking starts now."
        play sound "sex/Fouet.mp3"
        show joyce push
        with vpunch
        call label_prison_open_door(open=True) from _call_label_prison_open_door

    label .gameLoop:
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    jump .gameLoop

label label_prison_open_door(open=False):
    if game.debug_mode or open:
        hide screen screen_prison
        $ renpy.pop_call()
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
    # $ renpy.movie_cutscene("images/prison/flush.avi", delay=None, loops=0, stop_music=True)
    show screen screen_flushing(deck.list[index].img) with dissolve
    pause(1.0)
    hide screen screen_flushing
    $ deck.list.pop(index)
    $ renpy.call("label_newDay", "label_prison")

label label_prison_toilet:
    call screen screen_show_deck(label_callback="label_prison_remove_card", instruction=_("REMOVE A CARD"), background="img_toilet-static")
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
        idle showInteractible("prison/toilet.png", (0.85,0.95))
        hover Transform("prison/toilet.png", matrixcolor=TintMatrix((255,255,1275))) 
        # hover Transform("prison/toilet.png", zoom=1.05) 
        action [SetDict(done_flag, "prison/toilet.png", 1), Call("label_prison_toilet")]
        focus_mask True
        # hover Transform("prison/toilet.png", matrixcolor=TintMatrix((255,255,1275)))
        # idle "prison/toilet.png"

    imagebutton:
        idle showInteractible("prison/bed.png",(0.1,0.9))
        hover Transform("prison/bed.png", matrixcolor=TintMatrix((255,255,1275)))
        action [SetDict(done_flag, "prison/bed.png", 1), Call("label_prison_bed")]
        focus_mask True

    imagebutton:
        idle showInteractible("prison/metal-door.png",(0.6,0.5))
        hover Transform("prison/metal-door.png", matrixcolor=TintMatrix((255,255,1275)))
        action [SetDict(done_flag, "prison/metal-door.png", 1), Call("label_prison_open_door")]
        focus_mask True

    imagebutton:
        idle showInteractible("prison/food-tray.png",(0.55,0.95))
        hover Transform("prison/food-tray.png", matrixcolor=TintMatrix((255,255,1275)))
        action [SetDict(done_flag, "prison/food-tray.png", 1), Call("label_prison_food")]
        focus_mask True

screen screen_prison:
    use screen_dick_ui
    use screen_day
    use screen_deck_stack
    sensitive game.jeu_sensitive

    imagebutton:  
        idle showInteractible("prison/rat.png", (0.3, 0.95))
        hover Transform("prison/rat.png", matrixcolor=TintMatrix((255,255,1275)))
        action  [SetDict(done_flag, "prison/rat.png", 1), Show("screen_prison_rat_add_cards")]
        focus_mask True

    use screen_prison_sans_rat


screen screen_flushing(card):
    add "img_toilet-flush" zoom 3.0
    add card at trans_flush_card

screen screen_prison_rat_add_cards(sixCards = g.prison_cards):
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

    # fixed:
    #     xpos -400
    #     use screen_add_cards( sixCards[:2], "label_prison_add_card")
    # fixed:
    #     xpos 400
    #     use screen_add_cards( sixCards[2:4], "label_prison_add_card")

    imagebutton:
        idle "ui/cancel.png"
        hover Transform("ui/cancel.png", matrixcolor=TintMatrix((100,300,500)))
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