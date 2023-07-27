init python:
    def debugmode():
        game.debug_flag = 1 - game.debug_flag

    def nullfunction(*args):
        return

    renpy.music.register_channel("sexsfx", "sfx")
    renpy.music.register_channel("drawcard", "sfx")
    renpy.music.register_channel("activatecard", "sfx")


    class Game():
        def __init__(self):
            self.jeu_sensitive = False
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

            self.orgasmMax = 20
            self.orgasm = 0

            self.animation_speed = 3
            self.animation_speed_hash = { 1:0.5, 2:0.75, 3:1.0, 4:1.3, 5:1.6,}

            self.state = ""

            self.isHoverHand = True

            self.story = ["firstDate", "secondDate", "thirdDate", "fourthDate", "stripPoker", "footjob", "handjob", "blowjob", "cowgirl"]
            self.progress = 0

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
    
    
    game = Game()
    game.debug_flag = 0

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
                self.config["isGameOver"] = "len(deck.deck) == 0 or game.lust > game.trust or game.turnLeft == 0"

            if "isWin" in kwargs:
                self.config["isWin"] = kwargs["isWin"]
            else:
                self.config["isWin"] = "game.lust >= self.config['objectif_lust'] and game.attraction >= self.config['objectif_attraction'] and game.trust >= self.config['objectif_trust']"
        
        def isGameOver(self):
            return eval(self.config["isGameOver"])
        def isWin(self):
            return eval(self.config["isWin"])


label label_null(*args):
    return

style default:
    font FontGroup().add("FRABK.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)

style outline_text:
    color "#000000"
    outlines [ (absolute(5), "#ffffff", absolute(0), absolute(0)) ]
    font "ui"

define config.font_name_map["ui"] = FontGroup().add("FRADMIT.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
