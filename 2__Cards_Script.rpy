init python:
    # default 
    cardList = { 
        # get preview of next cards to come?
        # the string 'index' is replaced with the index of the card in hand

        "faster": {"txt":"go faster", "eff":"date.speedUp(True)", "value":-1,},
        "slower": {"txt":"go slower", "eff":"date.speedDown(True)", "value":1,},

        "slowsteady": {"txt":"IF this is your leftmost card: \nGo much slower. ", "cond":"index == 0", "eff":"date.speedDown(True); date.speedDown(True)", "value":2,},

        "draw2": {"txt":"draw 2 cards", "eff":"deck.draw(2)", "value":3,},

        "devil": {"txt":"Draw 2 cards, Double your current lust.", "eff":"deck.draw(2); date.lust *= 2", "value":1,},

        "newday": {"txt":"Change your current Lust with a random number.", "eff":"date.lust = renpy.random.randint(0, date.lustMax)", "value":2,},

        "awakening": {"txt":"This turn: double Lust and Speed changes.", "eff":"date.lustMultiplier *= 2", "value":2,},
        "calm": {"txt":"-2 lust, can get into negatives", "eff":"date.increment('lust',-2, allowNegative=True)", "value":1,},

        "maxcalm":{"txt":"-7 lust, add one STOP card in your hand", "eff":"date.increment('lust',-7); deck.hand.append(Card('stop'))", "value":1,},#card also work if you have multiple

        "fibonacci": {"txt": "-1 Lust, increases every time it's played.", "eff":"renpy.call('label_card_fibonacci')", "value":3,},

        "pair": {"txt":"IF you have a pair in your hand: draw 2 cards", "cond":"deck.hasPair()>1", "eff":"deck.draw(2)", "value":2,},
        "threeof": {"txt":"IF you have three of a kind in your hand: draw 3 cards", "cond":"deck.hasPair()>2", "eff":"deck.draw(3)", "value":1,},

        "change": {"txt":"Change all the cards in your hand with random cards.", "eff":"renpy.call('label_card_change')", "value":2,},
        
        "discardAll": {"txt":"Discard the whole hand, -1 Lust for each card.", "eff":"renpy.call('label_card_discardAll')", "value":2,},
        
        "sisyphus": {"txt":"Choose a card played, put it back on top of your deck.", "eff":"renpy.show_screen('screen_show_deck', what=deck.discard_pile, label_callback='label_card_sisyphus', instruction='Choose a card to add back', background='#000a')", "value":2,},
        "ouroboros": {"txt":"Shuffle back all the cards played into the deck.", "eff":"renpy.call('label_card_ouroboros')", "value":3,},

        "draw5": {"txt":"Get to max speed, draw until you have 5 cards in hand.", "eff":"date.animation_speed = 5; deck.draw(5-len(deck.hand))", "value":1,},

        "stop": {"txt":"Can't be played", "cond":"False", "eff":"", "value":-2,},
    
        "exodia3" : {"txt":"{b}WORLD{/b}\ninto Power.\nright order to\neffect.", "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5,},
        "exodia2" : {"txt":"{b}OF THE{/b}\ncurrent Lust\npieces in the\nthis", "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5,},
        "exodia1" : {"txt":"{b}ORIGIN{/b}\nConvert your\nYou need all 3\nactivate", "eff":"renpy.call('label_card_exodia', index)", "value":0, "rarity":"rare",},

        "universeout" : {"txt":"Add 2 Space Out cards in your hand.", "eff":"deck.add_to_hand(Card('spaceout')); deck.add_to_hand(Card('spaceout'))", "value":0,},
        "darkhole" : {"txt":"Discard your whole hand, -5 Lust for each Space Out discarded.", "eff":"renpy.call('label_card_darkhole')", "value":2,},
        "spaceout" : {"txt":"does nothing", "eff":"", "value":0,},

        "listen": {"txt":"This turn: double Trust gains.", "eff":"date.trustMultiplier *= 2",},

        "talk": {"txt":"+1 trust", "eff":"date.increment('trust',1)",},
        "talk2": {"txt":"+2 trust", "eff":"date.increment('trust',2)",},

        # "joke": {"txt":"+4 trust", "eff":"date.increment('trust',4)",},
        
        "peek": {"txt":"you peek..\n-1 trust +1 lust", "eff":"date.increment('trust',-1,False); date.increment('lust',1)", },
        "peek2": {"txt":"you peek.. -3 trust +3 lust", "eff":"date.increment('trust',-3,False); date.increment('lust',3)", },
        "peek3": {"txt":"get +5 lust", "eff":"date.increment('lust',5)", "value":-1,},
        "peek4": {"txt":"get +10 lust", "eff":"date.increment('lust',10)", "value":-2,},

        "eyecontact": {"txt":"+1 attraction, +1 lust", "eff":"date.increment('attraction',1,False); date.increment('lust',1)",},
        "flirt": {"txt":"+2 attraction +2 lust", "eff":"date.increment('attraction',2,False); date.increment('lust',2)",},
        "kiss" : {"txt":"+4 attraction +4 lust", "eff":"date.increment('attraction',4,False); date.increment('lust',4)",},
        "touchy" : {"txt":"This turn, Attraction gains are doubled.", "eff":"date.attractionMultiplier *= 2",},

        "drink" : {"txt":"Fully refill your glass.", "eff":"renpy.call('label_card_drink')", "value":2,},

        "reload": {"txt":"The top card in the discard pile is played again.", "cond":"len(deck.discard_pile)>0", "eff":"renpy.call('label_card_reload')", "value":3,},

    }




default done_flag = {}


label label_reaction(what = game.lastPlayed.name):

    
    if what == "talk2":
        call label_reaction("talk")
        return

    if what not in done_flag:
        $ done_flag[what] = 0

    $ value = done_flag[what]

    if value > game.progress[0] :
        return
    
    if what == "talk" :
        if value == 0:
            j "These days I have picked sudoku again."
            j "I play it during my offtime."
            j "What about you?"
        if value == 1:
            j "Oh you like playing games too?"
            j "What kind of games do you play?"
        elif value == 2:
            j "So you play dating sims."
            j "That's a little funny, I didn't expect it."
            j "I used to play some on the Nintendo DS too."
            j "What are you playing these days?"
        elif value == 3:
            j "Come on tell me what game you're playing."
            j "Ok at least next date tell me."
        elif value == 4:
            j "Wow you play erotic games?"
            j "Nah I get it, I've played some crazy stuff too."
            j "..."
            j "But I like it more in real life."
        elif value == 5:
            j "Maybe you can show me what kind of erotic games you like."
            j "And show me what you do while you play with it"
            j "Oops I said too much."

        elif value == 1:
            j "I loves cats sooo much"
            j "I'm kinda wondering if I should get one"
            j "But it's a big responsability still."
        elif value == 3:
            j "I'm not such a fan of summer to be honest."
            j "I easily get sunburns because my skin is too thin."
        elif value == 4:
            j "Cats are also so useful for pests."
            j "I could get some help getting rid of rats."
            j "My place has a pretty big basement, I could show you!"
        elif value == 5:
            j "How often do you meet girls like that?"
            j "I'm trying to look for the one."
            j "But I have pretty strange tastes"
            j "Will you pass the tests? I wonder heehee."

        elif value == 2:
            j "It's getting pretty warm these days!"
            j "That's why I enjoy coming here to get a drink."
            if game.progress[0] < 4: # in case we trigger it on a second date
                j "Though I regret wearing so many layers today."


    elif what == "eyecontact":
        
        show layer master:
            zoom 2.0 xalign 0.5 yalign 0.1
        with dissolve
        pause

        if value == 0:
            j "..."
            if any("dream" in tag for tag in renpy.get_attributes("joyce")) or game.progress[0]>7:
                j "hey"
            else:
                j eyesside blush "hey"
        elif value == 1:
            j "Why do you stare at me so often?"
            j "I feel so shy."
        elif value == 2:
            j "You enjoy what you're seeing?"
            j "I bet you wanna see more"

        show layer master:
            zoom 1.0 xalign 0.5 yalign 0.5
        with dissolve

    $ done_flag[what] += 1
        
    return