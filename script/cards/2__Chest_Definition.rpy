init python:

    class Chest:
        def __init__(self):
            self.box = []
            self.date = [] # the deck during a game
            self.sex = []

            #[nombre de cartes dans le coffre, nb de cartes dans le deck ]
        
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
        