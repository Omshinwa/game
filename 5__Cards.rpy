style style_card_effect:
    xalign 0.5
    size 22
    line_spacing -5
    textalign 0.5

label game_init:
    #set up the deck and keybinds

    $ deck = Deck()
    $ deck.list = [Card("faster"),Card("slower"),Card("distract"),Card("peek"),Card("devil"),Card("newday"),Card("calm"),Card("maxcalm"),Card("pair"),Card("change"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("drawmax"),Card("devil"),Card("faster"),Card("devil"),Card("devil"),Card("devil"),Card("devil"),Card("devil"),Card("slower"),Card("slower"),Card("faster"),Card("devil"),Card("devil"),]
    show screen keybinds()
    return

init python:

    class Card:
        def __init__(self, hash):
            self.id = hash

            if "name" in cardList[hash]:
                self.name = cardList[hash]["name"]
            else:
                self.name = self.id

            chemin = "cards/" + str(self.id) + ".png"

            if renpy.exists("images/" + chemin):
                self.img_path = chemin
            else:
                self.img_path = "cards/default.png"

            self.txt = cardList[hash]["txt"]
            
            if len(self.txt)<30:
                text_effect = Text(self.txt, style="style_card_effect", size=30) 
            else:
                text_effect =  Text(self.txt, style="style_card_effect", size=25) 

            textbox = Window(text_effect, style="empty", xalign=0.5, xsize=200, ysize=130)

            card_name = Text(self.name, style="outline_text", xalign=0.5, size=30)
            card_name_box =  Window(card_name, style="empty", xsize=200, ysize=30)
                        
            self.img = Composite((230, 330), (0, 0), "cards/card_bg.png", (15,15), self.img_path, (15,180), textbox)
            # self.img = Composite((230, 330), (0, 0), "cards/card_bg.png", (5,5), card_name_box, (15,30), self.img_path, (15,195), textbox)

            # self.img_hover = Composite((230, 330), (0, 0), "cards/card_bg-hover.png", (15,15), self.img_path, (15,180), self.textbox)
            self.img_hover = Composite((230, 330), (0, 0), "cards/card_bg-hover.png", (5,5), card_name_box, (15,30), self.img_path, (15,195), textbox)

            if "cond" in cardList[hash]:
                self.condition = cardList[hash]["cond"]
            else:
                self.condition = "True"

            self.id = hash

            self.eff = cardList[hash]["eff"]

            # self.x = 0
            # self.y = 0
        def __lt__(self,other): #this makes operation with '<' possible, and so sorting cards are by names.
            return self.name<other.id

        def cond(self, index):
            return eval(self.condition.replace( "index" , str(index)))

        @staticmethod
        def get_random_card():
            return Card( renpy.random.choice( list(cardList.keys()) ) )

        # #this is a getter 
        # def update_x_in_hand(self, index, cards_in_hand):
        #     self.x = int((index)* 230 + getCardPadding(cards_in_hand)*index)
           

    cardList = { 
        # get preview of next cards to come?
        # the string 'index' is replaced with the index of the card in hand

        "faster": {"txt":"go faster", "eff":"game.speedUp()",},
        "slower": {"txt":"go slower", "eff":"game.speedDown()",},

        "draw2": {"txt":"draw 2 cards", "eff":"deck.draw(2)",},

        "devil": {"txt":"Draw 2 cards, Double your current pleasure.", "eff":"deck.draw(2); game.lust *= 2",},

        "newday": {"txt":"Divide your pleasure by 2", "eff":"game.lust = int(game.lust/2)",},

        "calm": {"txt":"-2 pleasure", "eff":"game.lust -= 2",},

        "maxcalm":{"txt":"-8 pleasure, can only be played if this card is your rightmost card.", 

        "cond":"index == len(deck.hand)-1", "eff":"game.lust -= 8",},#card also work if you have multiple

        "pair": {"txt":"if you have a pair in your hand: draw 3 cards", "cond":"deck.hasPair()>1", "eff":"deck.draw(3)"},

        "change": {"txt":"Change all the cards in your hand with a random cards.", "eff":"renpy.call('label_card_change')"},

        "drawmax": {"txt":"Draw 1 card for each 5 points of pleasure.", "eff":"deck.draw( int(game.lust/5) )",},
        
        "discard": {"txt":"Discard the whole hand and draw as many.", "eff":"renpy.call('label_card_discardAll')",},
        
        "ouroboros": {"txt":"Shuffle back all the cards played into the deck.", "eff":"renpy.call('label_card_ouroboros')",},

        "angel's gift": {"txt":"If you have no cards left in your deck, -40 pleasure, go the slowest, shuffle back the discard pile into the deck", "eff":"renpy.call('label_card_ouroboros')",},
        
        "future vision": {"txt":"You can see the next card in your deck (click on the deck). This effect stacks.", "eff":"renpy.call('label_card_ouroboros')",},

        "reload": {"txt":"Shuffle back the whole hand and draw as many.", "eff":"renpy.call('label_card_shuffle')",},
        
        "recovery" : {"txt":"Discard the whole hand, -1 pleasure for each card discarded.", "eff":"deck.draw( int(game.lust/5) )",},

        "draw5": {"txt":"Halve your dick size this date. Draw until you have 5 cards in hand.", "eff":"game.animation_speed = 5; deck.draw(5-len(deck.hand))",},

        "stop": {"txt":"Can't be played", "cond":"False", "eff":"",},

        "double": {"txt":"Next card is played twice.", "eff":"deck.add_to_hand( Card(11) )",},
        
        "block": {"txt":"You cant gain pleasure from cards this turn.", "eff":"deck.add_to_hand( Card(11) )",},

        
        "exodia" : {"txt":"When you have 5 in your hand, you win.", "eff":"game.lust += 5",},

        
        "smalltalk": {"txt":"+1 trust", "eff":"game.lust += 5",},

        "play": {"txt":"+1 trust", "eff":"game.lust += 5",},

        "listen": {"txt":"", "eff":"game.lust += 5",},

        "hobbies": {"txt":"+1 interest", "eff":"game.lust += 5",},
        
        "peek": {"txt":"you peek.. (-2 trust)", "eff":"game.lust += 5",},
        "peek2": {"txt":"you peek.. (-4 trust)", "eff":"game.lust += 3",},
        "peek3": {"txt":"get +3 pleasure", "eff":"game.lust += 3",},

        "eyecontact": {"txt":"+1 flirt -1 trust", "eff":"",},
        "flirt": {"txt":"+2 flirt -2 trust", "eff":"",},
        "kiss" : {"txt":"+10 flirt, divide trust by 2", "eff":"",},

        "touchy" : {"txt":"For the rest of the turn, Romance gains are doubled", "eff":"",},

        "spaceout" : {"txt":"does nothing", "eff":"",},
    }


    class Deck:
        def __init__(self):
            self.hand = []
            self.deck = [] # the deck during a game

            self.list = []
            self.discard_pile = []

        def start(self):
            self.deck = self.list
            self.shuffle()
            self.discard_pile = []
            self.draw(5)
        
        def add_to_hand(self, *cards):
            for card in cards:
                renpy.play("draw.mp3", channel='drawcard')
                self.hand.append(card)

        def draw(self, number, delay=0.2):
            global ydisplace
            ydisplace = 0
            for i in range(0,number):
                if len(self.deck)>0: #si y a une carte dans le deck
                    self.add_to_hand( self.deck[0] )
                    self.deck.pop(0)
                    renpy.pause(delay, hard=True)

        def __str__(self):
            txt = []
            for card in self.hand:
                txt.append(str(card.id) + card.name)

            return ", ".join(txt)
        
        # return the highest number of cards in the hand that are the same.
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

        def shuffle(self):
            renpy.random.shuffle(self.deck)
            renpy.play("shuffle.mp3", channel='drawcard')
            renpy.pause(0.5)

        # discard card from hand
        def discard(self, index, delay=0.2):
            renpy.play("draw.mp3", channel='drawcard')
            self.discard_pile.append( self.hand.pop(index) )
            renpy.pause(delay, hard=True)

                

    def for_in(i, list, callback):
        for i in list:
            callback

label playCard(card, index):
    $ commands = card.eff
    $ commands.replace("index", str(index))
    $ commands = commands.split("; ")
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
    if deck.hand[index].cond(index):
        $ game.jeu_sensitive = False
        $ ydisplace = 0

        $ renpy.play("activate.mp3", channel='activatecard')
        $ card = Card( deck.hand[index].id )
        $ deck.discard(index)

        # animation:
        $ renpy.show('cardPlayed', what=card.img, at_list=[trans_card_played], zorder=2, layer="screens")
        $ renpy.pause(0.8)
        $ renpy.hide('cardPlayed', layer="screens")

        call playCard(card, index)
    else:
        $ print("invalid")
