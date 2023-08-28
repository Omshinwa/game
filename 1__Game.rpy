init python:
    def debugmode():
        game.debug_flag = 1 - game.debug_flag

    def nullfunction(*args):
        return

    renpy.music.register_channel("sexsfx", "voice")
    renpy.music.register_channel("sexvoice", "voice")

    renpy.music.register_channel("drawcard", "sfx")
    renpy.music.register_channel("activatecard", "sfx")


    class Game():
        def __init__(self):
            self.jeu_sensitive = True
            self.card_xsize = 230
            self.card_ysize = 330

            self.lustMax = 10
            self.lust = 0

            self.trust = 0
            self.attraction = 0

            self.trustMultiplier = 1
            self.attractionMultiplier= 1
            self.lustMultiplier = 1

            self.allMultiplierOnce= 1

            self.state = "" #either "dating" or "deckbuilding"

            self.isHoverHand = False

            self.story = ["tutorial", "bubbleTea", "terrasse", "barDate", "stripPoker", "footjob", "handjob", "blowjob", "cowgirl", "start"]
            self.progress = [0,-1] # left is progress, right is numbers of turns 

            self.day = 3

            self.lastPlayed = None
            self.cardPlaying = None

            self.debug_flag = 1

            self.dateEvery = 4

            self.lustPerDay = "game.progress[0]"

        @staticmethod
        def hasNewMessage():
            if g.phoneProgress[0] not in g.phoneLogs:
                return False
            return g.phoneProgress[1]<len(g.phoneLogs[g.phoneProgress[0]])-1

    class Date():
        def __init__(self, dateOrSex, **kwargs):
            game.jeu_sensitive = False;

            if dateOrSex == "date":
                game.state = "dating"
            elif dateOrSex == "sex":
                game.state = "sexing"
            else:
                raise Exception

            if "turnLeft" in kwargs:
                self._turnLeft = kwargs["turnLeft"]
            else:
                self._turnLeft = 0

            self.turn = 0

            self.config = {}

            self.objectives = {}
            if "objectif_trust" in kwargs:
                self.objectives["trust"] = kwargs["objectif_trust"]
            else:
                self.objectives["trust"] = -999
            
            if "objectif_attraction" in kwargs:
                self.objectives["attraction"] = kwargs["objectif_attraction"]
            else:
                self.objectives["attraction"] = -999
            
            if "objectif_lust" in kwargs:
                self.objectives["lust"] = kwargs["objectif_lust"]
            else:
                self.objectives["lust"] = -999

            if "isLost" in kwargs:
                self.config["isLost"] = kwargs["isLost"]
            else:
                if game.state == "dating":
                    self.config["isLost"] = "len(deck.deck) == 0 or (date.lust > date.trust and date.lust > date.attraction) or date.turnLeft == 0"
                else:
                    self.config["isLost"] = "len(deck.deck) == 0 or date.lust >= date.lustMax"

            if "isWin" in kwargs:
                self.config["isWin"] = kwargs["isWin"]
            else:
                self.config["isWin"] = "date.lust >= date.objectives['lust'] and date.attraction >= date.objectives['attraction'] and date.trust >= date.objectives['trust']"

            # label to call at the end of every turn
            if "endTurn" in kwargs:
                self.endTurn = kwargs["endTurn"]
            else:
                self.endTurn = ""

            self.ydisplace = Transform( ypos=1080 )

            self.drink = 3

            self.lustMax = 10
            self.lust = 0

            self.trust = 0
            self.attraction = 0

            self.trustMultiplier = 1
            self.attractionMultiplier= 1
            self.lustMultiplier = 1

            self.allMultiplierOnce= 1

            self.orgasmMax = 20
            self.orgasm = 0

            self.animation_speed = 3
            self.animation_speed_hash = { 1:0.5, 2:0.75, 3:1.0, 4:1.3, 5:1.6,}

        @property
        def turnLeft(self):
            return self._turnLeft - self.turn

        def speedUp(self, useMultiplier=False):            
            if useMultiplier:
                i = 1
                while date.lustMultiplier >= i:
                    if self.animation_speed < 5:
                        self.animation_speed += 1
                        if self.animation_speed < 5:
                            renpy.pause(0.3)
                    i += 1
            else:
                if self.animation_speed < 5:
                    self.animation_speed += 1

        def speedDown(self, useMultiplier=False):
            if useMultiplier:
                i = 1
                while date.lustMultiplier >= i:
                    if self.animation_speed > 1:
                        self.animation_speed -= 1
                        if self.animation_speed > 1:
                            renpy.pause(0.3)
                    i += 1
            else:
                if self.animation_speed > 1:
                    self.animation_speed -= 1

        def isLost(self):
            return eval(self.config["isLost"])
        def isWin(self):
            return eval(self.config["isWin"])

        def updateYdisplace(self):
            # game.jeu_sensitive and 
            if game.isHoverHand:
                self.ydisplace = trsfm_cards_go_up
            else:
                self.ydisplace = trsfm_cards_go_down
            
            return self.ydisplace

        def increment(self, which, value, resetAllMultiplier = True, allowNegative=True): #allowNegative=False
            if which == "trust":
                if not allowNegative:
                    temp = self.trust + value * self.trustMultiplier * self.allMultiplierOnce
                    self.trust = max(0, temp)
                else:
                    self.trust += value * self.trustMultiplier * self.allMultiplierOnce
            elif which == "attraction":
                if not allowNegative:
                    temp = self.attraction + value * self.attractionMultiplier * self.allMultiplierOnce
                    self.attraction = max(0, temp)
                else:
                    self.attraction += value * self.attractionMultiplier * self.allMultiplierOnce
            elif which == "lust":
                if not allowNegative:
                    temp = self.lust + value * self.lustMultiplier * self.allMultiplierOnce
                    self.lust = max(0, temp)
                else:
                    self.lust += value * self.lustMultiplier * self.allMultiplierOnce
            else:
                raise Exception("no valid specified argument: which") 
            
            if resetAllMultiplier:
                self.allMultiplierOnce = 1

label label_null(*args):
    return

default g.page = 0
default g.card_per_line = 7
default g.phoneLogs = {
    1:[
        [0, "heloo~ it's joyce"],[0, "are you free in 3 days?"],[0, "let's meet up again!"],
    ],
    2:[
        [0, "heeey"],[0, "wanna get some drinks tmr?"],[0, "There's a bubble tea place I like."],[2, "Okay see you there."]
    ],
    3:[
        [0, "today was so fun!"],[0, "I hope to see you next time too!"],[0, "right now i'm stuck on a sudoku haha"],[1, "pic1.png"], ["exe", "renpy.call('label_pic1_reaction')"]
    ],
    4:[
        [0, "hey look at this kitty"], [0, "she followed me around"], [0,"such a cutie! I wished I had a cat."], [1, "pic2.png"], ["exe", "renpy.call('label_pic2_reaction')"]
    ],
    5:[
        [0, "next time, let's go to a fancy bar!"], [0, "im so tiired now"],[0, "im gonna go to sleep now"],[0, "good niight"],[1, "pic3.png"], ["exe", "renpy.call('label_pic3_reaction')", [2, "goodnight"]]
    ],
    6:[
        [0, "about the fancy bar"],[0, "I don't know what to wear for tomorrow"],[0, "which dress do you think looks better?"],[1, "pic4.png"], ["exe", "renpy.call('label_pic4_reaction')"]
    ],
    # 0:[
    #     [0, "hello~"],[0, "today was so fun"],[0, "I hope to see you tmr"],[0, "goodnight!"], [1, "pic1.png"], ["exe", "renpy.call('label_pic1_reaction')"]
    # ],
    }
default g.phoneProgress = [0,0]
default g.prison_cards = []
default g.dreamProgress = 0
default g.trashbin = []

default phone_Scroll = ui.adjustment(range=0, value=0, step=None, page=1, changed=None, adjustable=None, ranged=None, force_step=False)
