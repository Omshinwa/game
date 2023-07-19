init python:

    class Card:
        def __init__(self, hash):
            self.name = hash

            chemin = "cards/" + str(self.name) + ".png"
            if renpy.exists("images/" + chemin):
                self.img_path = chemin
            else:
                self.img_path = "cards/default.png"
            self.txt = cardList[hash]["txt"]
            
            self.img = Composite((230, 330), (0, 0), "cards/card_bg.png", (15,15), self.img_path)
            self.img_hover = Composite((230, 330), (0, 0), "cards/card_bg-hover.png", (15,15), self.img_path)

            if "cond" in cardList[hash]:
                self.cond = cardList[hash]["cond"]
            else:
                self.cond = "True"

            self.id = hash

            self.eff = cardList[hash]["eff"]

            # self.x = 0
            # self.y = 0

        # #this is a getter 
        # def update_x_in_hand(self, index, cards_in_hand):
        #     self.x = int((index)* 230 + getCardPadding(cards_in_hand)*index)
           

    cardList = { 
        # get preview of next cards to come?

        "faster": {"txt":"go faster", "eff":"game.speedUp()",},
        "slower": {"txt":"go slower", "eff":"game.speedDown()",},
        "distract": {"txt":"you peek.. get distracted (+5 pleasure)", "eff":"game.pleasure += 5",},
        "excite": {"txt":"get +3 pleasure", "eff":"game.pleasure += 3",},
        "draw2": {"txt":"draw 2 cards", "eff":"deck.draw(2)",},
        "emptymind": {"txt":"Divide your pleasure by 2", "eff":"game.pleasure = int(game.pleasure/2)",},
        "calm": {"txt":"-2 pleasure", "eff":"game.pleasure -= 5",},
        "ultracalm":{"txt":"-4 pleasure", "eff":"game.pleasure -= 5",},

        "shuang": {"txt":"if you have a pair in your hand: draw 3 cards", "cond":"deck.hasPair()>1", "eff":"deck.draw(3)"},

        "change": {"txt":"Change all the cards in your hand with a random cards.", "eff":"for i in range(len(deck.hand)): @deck.hand[i] = Card( renpy.random.choice( list(cardList.keys()) ) )"},

        "drawmax": {"txt":"Draw 1 card for each 5 points of pleasure.", "eff":"deck.draw( int(game.pleasure/5) )",},
        
        "discardAll": {"txt":"Discard the whole hand and draw as many.", "eff":"deck.draw( int(game.pleasure/5) )",},
        
        "recycle": {"txt":"Shuffle back all the cards played into the deck.", "eff":"deck.draw( int(game.pleasure/5) )",},

        "shuffle": {"txt":"Shuffle back the whole hand and draw as many.", "eff":"deck.draw( int(game.pleasure/5) )",},
        
        "recovery" : {"txt":"Discard the whole hand, -1 pleasure for each card discarded.", "eff":"deck.draw( int(game.pleasure/5) )",},

        "draw5": {"txt":"Get to max speed. Draw until you have 5 cards in hand.", "eff":"game.animation_speed = 5, deck.draw(5-len(deck.hand))",},

        "stop": {"txt":"Can't be played", "cond":"False", "eff":"",},

        "double": {"txt":"Next card is played twice.", "eff":"deck.add_to_hand( Card(11) )",},
        
        "block": {"txt":"You cant gain pleasure from cards this turn.", "eff":"deck.add_to_hand( Card(11) )",},

        
        "exodia" : {"txt":"When you have 5 in your hand, you win.", "eff":"game.pleasure += 5",},

        "smalltalk": {"txt":"+1 trust", "eff":"game.pleasure += 5",},
        "big talk": {"txt":"+2 trust", "eff":"game.pleasure += 5",},
        "peek": {"txt":"you peek.. (-2 pleasure)", "eff":"game.pleasure += 5",},

        "eyecontact": {"txt":"+1 flirt -1 trust", "eff":"",},
        "flirt": {"txt":"+2 flirt -2 trust", "eff":"",},
        "touch" : {"txt":"+4 flirt -4 trust", "eff":"",},

        "nothing" : {"txt":"does nothing", "eff":"",},
    }


    class Deck:
        def __init__(self):
            self.hand = []
            self.deck = [] # the deck during a game

            self.list = []
        
        def add_to_hand(self, *cards):
            for card in cards:
                renpy.sound.play("draw.mp3")
                self.hand.append(card)

        def draw(self, number):
            global ydisplace
            ydisplace = 0
            for i in range(0,number):
                if len(self.deck)>0: #si y a une carte dans le deck
                    self.add_to_hand( self.deck[0] )
                    self.deck.pop(0)
                    renpy.pause(0.2, hard=True)

        def __str__(self):
            txt = []
            for card in self.hand:
                txt.append(str(card.id) + card.name)

            return ", ".join(txt)
        
        # return the number of cards in the hand that are the same.
        def hasPair(self):
            highest = 0
            for i in self.hand:
                current = 1
                for j in self.hand:
                    if i != j:
                        if i.name == j.name:
                            current+=1
                if current > highest:
                    highest = current
            return highest
                

    def for_in(i, list, callback):
        for i in list:
            callback

label playCard(card):
    $ commands = card.eff.replace("@", "\n    ")
    $ commands = commands.split(";")
    $ i = 0
    while i < len(commands):
        # j " [commands[0]] "
        $ print(commands[i])
        $ exec(commands[i])
        $ i+=1
    $ game.jeu_sensitive = True
    $ game.isHoverHand = True
    return

label playCardfromHand(index):
    if eval(deck.hand[index].cond):
        $ game.jeu_sensitive = False
        $ ydisplace = 0
        
        
        $ print (deck.hand[index].img_path)

        play sound "activate.mp3"
        $ card = Card( deck.hand[index].id )
        $ deck.hand.pop(index)

        # animation:
        $ renpy.show('cardPlayed', what=card.img, at_list=[trans_card_played], zorder=2, layer="screens")
        $ renpy.pause(1.0, hard=True)
        $ renpy.hide('cardPlayed', layer="screens")

        call playCard(card)
    else:
        $ print("invalid")
