# in webbrowser, it cant find the strings of the name of the methods ie "date.increment('lust',-3, negative=True)" it wont find date.increment, i can find attributes tho

label label_card_calm:
    $ date.increment('lust',-3, negative=True)
    return
label label_card_maxcalm:
    $ date.increment('lust',-10)
    $ deck.hand.append(Card('stop'))
    return
label label_card_slower:
    $ date.speedDown(True)
    $ date.lustPerTurn -= 3
    return
label label_card_slowsteady:
    $ date.speedDown(True)
    $ date.speedDown(True)
    $ date.lustPerTurn -= 5
    return
label label_card_fool:
    $ date.speedDown(True)
    $ date.speedDown(True)
    $ date.lustPerTurn -= 5
    return
label label_card_faster:
    $ date.speedUp(True)
    return
label label_card_draw2:
    $ deck.draw(2)
    return
label label_card_devil:
    $ deck.draw(2)
    $ temp = date.lust
    $ date.lust = 0
    $ date.increment('lust', temp*2, negative=True)
    $ del temp
    return
label label_card_pair:
    $ deck.draw(2)
    return
label label_card_universeout:
    $ deck.add_to_hand(Card('spaceout'));
    pause 0.2
    $ deck.add_to_hand(Card('spaceout'));
    return
label label_card_peek:
    $ date.increment('lust',2)
    return
label label_card_peek2:
    $ date.increment('lust',5)
    return
label label_card_peekred:
    $ date.increment('lust',10)
    return
label label_card_peekblue:
    $ date.increment('lust',10)
    return
label label_card_peek4:
    $ date.increment('lust',15)
    return
label label_card_peek5:
    $ date.increment('lust',30)
    return
label label_card_eyecontact:
    $ date.increment('attraction',1,False);
    if "eyecontact" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_eyecontact"):
        $ renpy.call(date.name + "_eyecontact") 
    else:
        call label_card_reaction
    return
label label_card_flirt:
    $ date.increment('attraction',2,False);
    if "flirt" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_flirt"):
        $ renpy.call(date.name + "_flirt") 
    else:
        call label_card_reaction
    return
label label_card_touchy:
    $ date.attractionMultiplier *= 2
    if "touchy" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_touchy"):
        $ renpy.call(date.name + "_touchy") 
    else:
        call label_card_reaction
    return
label label_card_talk:
    $ date.increment('trust',1)
    if "talk" in date.playedThisTurn or "talk2" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_talk"):
        $ renpy.call(date.name + "_talk") 
    else:
        call label_card_reaction_talk
    return
label label_card_talk2:
    $ date.increment('trust',2)
    if "talk" in date.playedThisTurn or "talk2" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_talk"):
        $ renpy.call(date.name + "_talk") 
    else:
        call label_card_reaction_talk
    return
label label_card_listen:
    $ date.trustMultiplier *= 2
    if "listen" in date.playedThisTurn:
        pass
    elif renpy.has_label(date.name + "_listen"):
        $ renpy.call(date.name + "_listen") 
    else:
        call label_card_reaction_talk
    return
label label_card_spaceout:
    return

label label_card_undress:
    if "naked" in renpy.get_attributes("joyce"):
        #already naked
        return

    if renpy.has_label(date.name + "_undress"):
        $ renpy.call(date.name + "_undress") 
    else:
        $ print("no label " + date.name + "_undress")
        call label_reaction_undress


    # if "undress" in date.reaction:
    #     $ renpy.call(date.reaction["undress"]) 
    # else:
    #     call label_reaction_undress