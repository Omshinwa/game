
label label_newDay(label_callback):
    $ renpy.set_return_stack(renpy.get_return_stack()[-1])
    # $ renpy.pop_call()

    window hide
    scene black
    $ renpy.play("day/newday.wav", channel='sound') 
    # show black
    if game.day % game.dateEvery == 0:
        show screen screen_day
    with dissolve
    window auto

    if game.day % game.dateEvery == 0:
        pause 1.5
        play music "music/clock-tick.mp3" noloop
        $ game.day += 1
        with blinds
    else:
        pause 1.0
        $ game.day += 1
    
    $ game.state = "living"
    with dissolve
    $ game.lust += eval(game.lustPerDay)
    
    # pause
    # jump expression "label_home_tutorial"
    jump expression label_callback

label label_add_card_to_deck( toWhere, card, xfrom=960, yfrom=-100, pauseTime=0, fromWhere=None, index=None,):
    $ game.jeu_sensitive = False
    if toWhere == "list":
        $ xto = 1900
        $ yto = 20
    
    elif toWhere == "deck":
        $ xto = 1900
        $ yto = 1000

    elif toWhere == "hand":
        $ xto = 960
        $ yto = 1000

    else:
        $ raise ValueError("toWhere deck or list not specified")

    if fromWhere == "field":
        $ yfrom = 450
    
    show expression card.img onlayer screens at trans_anim_move_card(xfrom, yfrom, xto, yto, pauseTime)
        
    pause 0.4 + pauseTime
    play sound "card/ghost.mp3"
    pause 0.3
    if toWhere == "list":
        $ deck.list.append( card )
        $ deck.list.sort()
    elif toWhere == "deck":
        if index==None:
            $ rand = renpy.random.randint(0, len(deck.deck))
            $ deck.deck.insert( rand , card )
        else:
            $ deck.deck.insert( index , card )
    elif toWhere == "hand":
        $ deck.hand.append( card )
    else:
        $ raise ValueError("deck or list not specified")
    pause 0.2
    hide expression card.img onlayer screens

    # $ game.jeu_sensitive = True
    return

label label_drink:
    $ game.jeu_sensitive = False
    if date.drink>0:
        play sound "day/gulp.wav"
        $ date.drink -= 1
        pause 1.0
        call label_shuffle from _call_label_shuffle
        return

label label_transform_card(cardID, cardID2, prompt, callback=None):
    show expression trans_show_card_1(Card(cardID).img)  as card onlayer screens
    show expression trans_show_card_2(Card(cardID2).img) as card2 onlayer screens
    if any(c.name == cardID for c in deck.list):
        menu:
            "[prompt]"
            "yes":
                hide card onlayer screens
                hide card2 onlayer screens
                python:
                    for index,card in enumerate(deck.list):
                        if card.name == cardID:
                            deck.list.pop(index)
                            break
                call label_add_card_to_deck(toWhere="list", card=Card(cardID2), xfrom=300, yfrom=500, pauseTime=0.5) from _call_label_add_card_to_deck_1
                if callback != None:
                    call label_newDay(callback) from _call_label_newDay_1
            "no":
                hide card onlayer screens
                hide card2 onlayer screens
    else:
        menu:
            "[prompt]"
            "(you dont have any)":
                hide card onlayer screens
                hide card2 onlayer screens
    return