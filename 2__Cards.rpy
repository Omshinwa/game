style style_card_effect:
    xalign 0.5
    line_spacing -5
    textalign 0.5

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
                text_effect =  Text(self.txt, style="style_card_effect", size=30 - (len(self.txt)/15) ) 

            textbox = Window(text_effect, style="empty", xalign=0.5, xsize=200, ysize=130)
                        
            self.img = Composite((230, 330), (0, 0), "cards/card_bg.png", (15,15), self.img_path, (15,180), textbox)
            self.img_hover =  Composite((230, 330), (0, 0), "cards/card_bg-hover.png", (15,15), self.img_path, (15,180), textbox)

            if "cond" in cardList[hash]:
                self.condition = cardList[hash]["cond"]
            else:
                self.condition = "True"

            self.id = hash

            self.eff = cardList[hash]["eff"]

            # self.x = 0
            # self.y = 0
        def __lt__(self,other): #this makes operation with '<' possible, and so sorting cards are by names.
            return self.id<other.id
        def __repr__(self):
            return self.id

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

        "slowsteady": {"txt":"Can only be played when it's your leftmost card, go much slower.", "cond":"index == 0", "eff":"game.speedDown(); game.speedDown()",},

        "draw2": {"txt":"draw 2 cards", "eff":"deck.draw(2)",},

        "devil": {"txt":"Draw 2 cards, Double your current lust.", "eff":"deck.draw(2); date.lust *= 2",},

        "newday": {"txt":"Divide your lust by 2", "eff":"date.lust = int(date.lust/2)",},

        "calm": {"txt":"-2 lust", "eff":"date.lust -= 2",},

        "maxcalm":{"txt":"-8 lust, can only be played if this card is your rightmost card.", 
        "cond":"index == len(deck.hand)-1", "eff":"date.lust -= 8",},#card also work if you have multiple

        "pair": {"txt":"if you have a pair in your hand: draw 2 cards", "cond":"deck.hasPair()>1", "eff":"deck.draw(2)"},
        "threeof": {"txt":"if you have three of a kind in your hand: draw 3 cards", "cond":"deck.hasPair()>2", "eff":"deck.draw(3)"},

        "change": {"txt":"Change all the cards in your hand with a random cards.", "eff":"renpy.call('label_card_change')"},

        "drawmax": {"txt":"Draw 1 card for each 5 points of lust.", "eff":"deck.draw( int(date.lust/5) )",},
        
        "discard": {"txt":"Discard the whole hand and draw as many.", "eff":"renpy.call('label_card_discardAll')",},
        
        "sisyphus": {"txt":"Shuffle back all the cards played into the deck.", "eff":"renpy.call('label_card_sisyphus')",},
        "ouroboros": {"txt":"", "eff":""},

        "angel's gift": {"txt":"If you have no cards left in your deck, -40 lust, go the slowest, shuffle back the discard pile into the deck", "eff":"renpy.call('label_card_ouroboros')",},
        
        "future vision": {"txt":"You can see the next card in your deck (click on the deck). This effect stacks.", "eff":"renpy.call('label_card_ouroboros')",},

        "reload": {"txt":"Put all your cards at the bottom of your deck, then draw as many from the top.", "eff":"renpy.call('label_card_reload')",},
        
        "recovery" : {"txt":"Discard the whole hand, -1 lust for each card discarded.", "eff":"deck.draw( int(date.lust/5) )",},

        "draw5": {"txt":"Halve your dick size this date. Draw until you have 5 cards in hand.", "eff":"game.animation_speed = 5; deck.draw(5-len(deck.hand))",},

        "stop": {"txt":"Can't be played", "cond":"False", "eff":"",},

        # "double": {"txt":"Next card is played twice.", "eff":"deck.add_to_hand( Card(11) )",},
        
        # "block": {"txt":"You cant gain lust from cards this turn.", "eff":"deck.add_to_hand( Card(11) )",},
        
        # "exodia" : {"txt":"When you have 5 in your hand, you win.", "eff":"date.lust += 5",},

        "universeout" : {"txt":"Add 2 Space Out cards in your hand.", "eff":"deck.add_to_hand(Card('spaceout')); deck.add_to_hand(Card('spaceout'))",},
        
        # "play": {"txt":"+1 trust", "eff":"date.lust += 5",},

        "listen": {"txt":"This turn: double Trust gains.", "eff":"date.trustMultiplier *= 2",},

        "smalltalk": {"txt":"+1 trust", "eff":"game.increment('trust',1)",},
        "hobbies": {"txt":"+2 trust", "eff":"game.increment('trust',2)",},
        "joke": {"txt":"+4 trust", "eff":"game.increment('trust',4)",},
        
        "peek": {"txt":"you peek..\n-1 trust +1 lust", "eff":"game.increment('trust',-1,False); game.increment('lust',1)",},
        "peek2": {"txt":"you peek.. -3 trust +3 lust", "eff":"game.increment('trust',-3,False); game.increment('lust',3)",},
        "peek3": {"txt":"get +5 lust", "eff":"game.increment('lust',5)",},

        "eyecontact": {"txt":"+1 attraction, +1 lust", "eff":"game.increment('attraction',1,False); game.increment('lust',1)",},
        "flirt": {"txt":"+2 attraction +2 lust", "eff":"game.increment('attraction',2,False); game.increment('lust',2)",},
        "kiss" : {"txt":"+4 attraction +4 lust", "eff":"game.increment('attraction',4,False); game.increment('lust',4)",},

        "touchy" : {"txt":"This turn, Attraction gains are doubled.", "eff":"date.attractionMultiplier *= 2",},

        "drink" : {"txt":"Double the next gain or loss.", "eff":"game.allMultiplierOnce *= 2",},

        "spaceout" : {"txt":"does nothing", "eff":"",},
    }


    class Deck:
        def __init__(self):
            self.hand = []
            self.deck = [] # the deck during a game

            self.list = []
            self.discard_pile = []

        # def start(self):
        #     self.deck = self.list
        #     self.shuffle()
        #     self.discard_pile = []
        #     self.draw(5)
        
        def add_to_hand(self, *cards):
            for card in cards:
                renpy.play("draw.mp3", channel='drawcard')
                self.hand.append(card)

        def draw(self, number, delay=0.2):
            global ydisplace
            ydisplace = 0
            for i in range(0,number):
                if len(self.deck)>0: #si y a une carte dans le deck
                    self.add_to_hand( self.deck.pop(0) )
                    renpy.pause(delay)

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
            renpy.pause(delay)

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
        $ renpy.pause(0.2)
    # $ game.isHoverHand = True
    $ game.lastPlayed = card.name
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
    
    call label_reaction
    
    $ game.jeu_sensitive = True

    if len(deck.hand) == 0:
        call expression date.endTurn

default done_flag = {}

label label_reaction:

    if game.lastPlayed not in done_flag:
        $ done_flag[game.lastPlayed] = 0

    $ value = done_flag[game.lastPlayed]

    if game.progress[0] < value:
        return

    if game.lastPlayed == "smalltalk":
        if value == 0:
            j "It's getting pretty warm these days!"
            if game.progress[0] == 0:
                j "I regret wearing so many layers."
        elif value == 1:
            j "I'm not such a fan of summer to be honest."
            j "I easily get sunburns"
        elif value == 2:
            j "How often do you meet girls like that?"
            j "I'm trying to look for the one."
            j "But I have pretty harsh requierements."
            j "You'll see, hehe."
    
    elif game.lastPlayed == "hobbies":
        if value == 0:
            j "Oh you like playing games?"
            j "What kind of games?"
        elif value == 1:
            j "Oh yea dating sims are cool."
            j "What are you playing now?"
        elif value == 2:
            j "Come on tell me what game you're playing."
            j "Ok at least next date tell me."
        elif value == 3:
            j "Wow you play erotic games?"
            j "Nah I get it, I've played some crazy stuff too."
            j "..."
            j "But I like it more in real life."
    
    elif game.lastPlayed == "eyecontact":
        if value == 0:
            j "..."
            j "*blush*"
        elif value == 1:
            j "Why do you stare at me so often?"
            j "I feel so shy."
        elif value == 2:
            j "You enjoy what you're seeing?"
            j "I bet you wanna see more"

    $ done_flag[game.lastPlayed] += 1
        
