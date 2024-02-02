init python:

    class Card:
        def __init__(self, hash):

            self.name = hash

            self.illustration = CARD_IMG_DICT[hash]

            self.txt = cardList[hash]["txt"]
            
            self.updateArt()

            if "cond" in cardList[hash]:
                self.condition = cardList[hash]["cond"]
            else:
                self.condition = "True"

            if "eff" in cardList[hash]:
                self.eff = cardList[hash]["eff"]
            else:
                self.eff = "renpy.call('label_card_" + hash +"')"


        def __lt__(self,other): #this makes operation with '<' possible, and so sorting cards are by names.
            if "sort" in cardList[self.name]:
                i = cardList[self.name]["sort"]
            else:
                i = self.name
            if "sort" in cardList[other.name]:
                j = cardList[other.name]["sort"]
            else:
                j = other.name
            return i<j
        
        def __repr__(self):
            return self.name

        def cond(self, index):
            return eval(self.condition.replace( "index" , str(index)))

        @staticmethod
        def get_random_card(customList=None):
            if customList == None or len(customList)==0:
                return Card( renpy.random.choice( list(cardList.keys()) ) )
            else:
                return Card( renpy.random.choice( list(customList.keys()) ) )
                

        def updateArt(self):

            if len(self.txt)<32:
                text_effect = Text(self.txt, style="style_card_effect", size=32, line_spacing=0) 
            else:
                text_effect = Text(self.txt, style="style_card_effect", size=35 - (len(self.txt)/8), line_spacing=0, layout="greedy") 

            # open dyslexic
            # if len(self.txt)<32:
            #     text_effect = Text(self.txt, style="style_card_effect", size=29, line_spacing=0) 
            # else:
            #     text_effect = Text(self.txt, style="style_card_effect", size=33 - (len(self.txt)/8), line_spacing=max((30-len(self.txt))/2,-8) ) 
            
            # line_spacing=max((30-len(self.txt))/2,-8)) 
            textbox = Window(text_effect, style="empty",  xysize=(200, 135), background=Color("#f9f5d4"), padding=(3,2))

            if "color" in cardList[self.name]:
                if cardList[self.name]["color"] == "bad":
                    text_effect.color = "#fff"

            if "color" not in cardList[self.name]:
                card_bg = Transform("cards/card_bg.png", matrixcolor=TintMatrix("#e1ddd4"))
            else:
                if cardList[self.name]["color"] == "trust":
                    card_bg = Transform("cards/card_bg.png", matrixcolor=TintMatrix("#93efff"))
                elif cardList[self.name]["color"] == "lust":
                    card_bg = Transform("cards/card_bg.png", matrixcolor=TintMatrix("#ebef73"))
                elif cardList[self.name]["color"] == "attraction":
                    card_bg = Transform("cards/card_bg.png", matrixcolor=TintMatrix("#ffa4e4"))
                elif cardList[self.name]["color"] == "bad":
                    card_bg = Transform("cards/card_bg.png", matrixcolor=ColorizeMatrix("#bdc4c9","#131513"))

            self.img = Composite((230, 330), (0, 0), card_bg, (15,15), self.illustration, (15,174), textbox)
            self.img_hover =  Transform(self.img, matrixcolor=ColorizeMatrix("#005d36","#eeffee"))

            del text_effect, card_bg

        # #this is a getter 
        # def update_x_in_hand(self, index, cards_in_hand):
        #     self.x = int((index)* 230 + getCardPadding(cards_in_hand)*index)
         
    class Deck:
        def __init__(self):
            self.hand = []
            self.deck = [] # the deck during a game

            self.list = []
            self.discard_pile = []
        
        def add_to_hand(self, *cards):
            for card in cards:
                renpy.play("card/draw.mp3", channel='drawcard')
                self.hand.append(card)

        def draw(self, number, delay=0.2):
            global ydisplace
            ydisplace = 0
            for i in range(0,number):
                if len(self.deck)>0: #si y a une carte dans le deck
                    self.add_to_hand( self.deck.pop(0) )
                    renpy.pause(delay)

        # @property
        # def handSize(self):
        #     if game.state != "living":
        #         return len(deck.hand)**2-1
        #     else:
        #         return "(number of discarded cards)²"

        def __str__(self):
            txt = []
            for card in self.hand:
                txt.append(card.name)

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
            renpy.play("card/shuffle.mp3", channel='drawcard')
            renpy.pause(0.5)

        # discard card from hand
        def discard(self, index, delay=0.2):
            renpy.play("card/draw.mp3", channel='drawcard')
            self.discard_pile.append( self.hand.pop(index) )
            renpy.pause(delay)


label playCard(card, index):
    $ game.cardPlaying = card
    $ commands = card.eff
    $ commands.replace("index", str(index))
    $ commands = commands.split("; ")
    $ playCardindex = 0
    while playCardindex < len(commands):
        $ exec(commands[playCardindex])
        $ playCardindex+=1
        # if i < len(commands):
        pause 0.2
    $ game.lastPlayed = card
    $ game.cardPlaying = None
    # $ del playCardindex 
    
    return

label playCardfromHand(index):
    if deck.hand[index].cond(index):
        $ game.jeu_sensitive = False
        $ ydisplace = 0

        $ renpy.play("card/activate.mp3", channel='activatecard')
        $ card = deck.hand[index]
        $ deck.discard(index)

        # animation:
        $ renpy.show('cardPlayed', what=card.img, at_list=[trans_card_played], zorder=2, layer="screens")
        # $ renpy.pause(0.5)
        $ renpy.hide('cardPlayed', layer="screens")

        call playCard(card, index) from _call_playCard
    else:
        $ raise Exception("playCardfromHand cond invalid")
    
    $ game.jeu_sensitive = True

    return
