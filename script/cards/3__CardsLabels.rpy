# in webbrowser, it cant find the strings of the name of the methods ie "date.increment('lust',-3, negative=True)" it wont find date.increment, i can find attributes tho

label label_card_calm:
    $ date.increment('lust',-3, negative=True)
    return
label label_card_maxcalm:
    $ date.increment('lust',-10, negative=True)
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
    # $ temp = date.lust
    # $ date.lust = 0
    # $ date.increment('lust', temp*2, negative=True)
    $ date.increment('lust', 10, negative=True)
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
    return
label label_card_flirt:
    $ date.increment('attraction',2,False);
    return
label label_card_talk:
    $ date.increment('trust',1)
    return
label label_card_talk2:
    $ date.increment('trust',2)
    return
label label_card_spaceout:
    return

label label_card_undress:
    if "undress" in date.reaction:
        $ renpy.call(date.reaction["undress"]) 
    else:
        call label_reaction_undress