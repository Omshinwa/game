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
            
            self.updateArt()

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
        def get_random_card(customList=None):
            if customList == None or len(customList)==0:
                return Card( renpy.random.choice( list(cardList.keys()) ) )
            else:
                return Card( renpy.random.choice( list(customList.keys()) ) )
                

        def updateArt(self):
            if len(self.txt)<30:
                text_effect = Text(self.txt, style="style_card_effect", size=30) 
            else:
                text_effect =  Text(self.txt, style="style_card_effect", size=33 - (len(self.txt)/10) ) 
            textbox = Window(text_effect, style="empty", xalign=0.5, xsize=200, ysize=130)
            self.img = Composite((230, 330), (0, 0), "cards/card_bg.png", (15,15), self.img_path, (15,175), textbox)
            self.img_hover =  Composite((230, 330), (0, 0), "cards/card_bg-hover.png", (15,15), self.img_path, (15,175), textbox)

        # #this is a getter 
        # def update_x_in_hand(self, index, cards_in_hand):
        #     self.x = int((index)* 230 + getCardPadding(cards_in_hand)*index)
         
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
                renpy.play("card/draw.mp3", channel='drawcard')
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
    $ i = 0
    while i < len(commands):
        $ print(commands[i])
        $ exec(commands[i])
        $ i+=1
        $ renpy.pause(0.2)
    $ game.lastPlayed = card
    $ game.cardPlaying = None
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
        $ renpy.pause(0.8)
        $ renpy.hide('cardPlayed', layer="screens")

        call playCard(card, index)
    else:
        $ print("invalid")
    
    call label_reaction
    
    $ game.jeu_sensitive = True

    if len(deck.hand) == 0:
        call expression date.endTurn

    return








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