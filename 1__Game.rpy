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
            self.jeu_sensitive = False
            self.card_xsize = 230
            self.card_ysize = 330
            
            self.score = 0

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

            self.state = "" #either "dating" or "deckbuilding"

            self.isHoverHand = False

            self.story = ["firstDate", "secondDate", "thirdDate", "fourthDate", "stripPoker", "footjob", "handjob", "blowjob", "cowgirl"]
            self.progress = [0,0] # left is progress, right is number of passing days spend on that step

            self.day = 0

            self.lastPlayed = ""

            self.debug_flag = 0

        def nextDay(self, label_callback):
            renpy.play("newday.wav", channel='sound') 
            self.day += 1
            renpy.with_statement(fade)
            renpy.jump(label_callback)

        def increment(self, which, value, resetAllMultiplier = True):
            if which == "trust":
                self.trust += value * self.trustMultiplier * self.allMultiplierOnce
            elif which == "attraction":
                self.attraction += value * self.attractionMultiplier * self.allMultiplierOnce
            elif which == "lust":
                self.lust += value * self.lustMultiplier * self.allMultiplierOnce
            else:
                raise ValueError("no valid specified argument: + which : "+ which) 
            
            if resetAllMultiplier:
                self.allMultiplierOnce = 1


        def speedUp(self):
            if self.animation_speed < 5:
                self.animation_speed += 1
                # renpy.show("joyce cowgirl")

        def speedDown(self):
            if self.animation_speed > 1:
                self.animation_speed -= 1
                # renpy.show("joyce cowgirl")

    class Date():
        def __init__(self, **kwargs):
            
            if "turnLeft" in kwargs:
                self.turnLeft = kwargs["turnLeft"]
            else:
                self.turnLeft = 0

            self.config = { "objectives":{} }
            if "objectif_trust" in kwargs:
                self.config["objectives"]["trust"] = kwargs["objectif_trust"]
            else:
                self.config["objectives"]["trust"] = 0
            
            if "objectif_attraction" in kwargs:
                self.config["objectives"]["attraction"] = kwargs["objectif_attraction"]
            else:
                self.config["objectives"]["attraction"] = 0
            
            if "objectif_lust" in kwargs:
                self.config["objectives"]["lust"] = kwargs["objectif_lust"]
            else:
                self.config["objectives"]["lust"] = 0

            if "isGameOver" in kwargs:
                self.config["isGameOver"] = kwargs["isGameOver"]
            else:
                self.config["isGameOver"] = "len(deck.deck) == 0 or date.lust > date.trust or game.turnLeft == 0"

            if "isWin" in kwargs:
                self.config["isWin"] = kwargs["isWin"]
            else:
                self.config["isWin"] = "date.lust >= self.config['objectif_lust'] and date.attraction >= self.config['objectif_attraction'] and date.trust >= self.config['objectif_trust']"

            # label to call at the end of every turn
            if "endTurn" in kwargs:
                self.endTurn = kwargs["endTurn"]
            else:
                self.endTurn = ""

            self.ydisplace = Transform( ypos=1080 )

            self.lustMax = 10
            self.lust = 0

            self.trust = 0
            self.attraction = 0

            self.trustMultiplier = 1
            self.attractionMultiplier= 1
            self.lustMultiplier = 1

        def isGameOver(self):
            return eval(self.config["isGameOver"])
        def isWin(self):
            return eval(self.config["isWin"])

        def updateYdisplace(self):
            if not game.jeu_sensitive:
                pass
            elif game.isHoverHand:
                self.ydisplace = trsfm_cards_go_up
            else:
                self.ydisplace = trsfm_cards_go_down
            
            return self.ydisplace

transform trsfm_cards_go_down:
    ypos 1080
    ease 0.2 ypos 1210

transform trsfm_cards_go_up:
    ypos 1210
    ease 0.2 ypos 1080

label label_null(*args):
    return

style default:
    font FontGroup().add("FRABK.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)

style outline_text:
    color "#000000"
    outlines [ (absolute(5), "#ffffff", absolute(0), absolute(0)) ]
    font "ui"

define config.font_name_map["ui"] = FontGroup().add("FRADMIT.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
