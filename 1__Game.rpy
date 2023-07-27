init python:
    def debugmode():
        game.debug_flag = 1 - game.debug_flag

    renpy.music.register_channel("sexsfx", "sfx")
    renpy.music.register_channel("drawcard", "sfx")
    renpy.music.register_channel("activatecard", "sfx")

    class Game():
        def __init__(self):
            self.jeu_sensitive = False
            self.card_xsize = 230
            self.card_ysize = 330

            self.turnLeft = 0
            
            self.lustMax = 10
            self.lust = 0

            self.trust = 0

            self.attraction = 0

            self.trustMultiplier = 2
            self.attractionMultiplier= 1

            self.allMultiplierOnce= 1

            self.orgasmMax = 20
            self.orgasm = 0

            self.animation_speed = 3
            self.animation_speed_hash = { 1:0.5, 2:0.75, 3:1.0, 4:1.3, 5:1.6,}

            self.state = ""

            self.isHoverHand = True

        def add(self, which, value):
            if which = "trust":
                self.trust += value * self.trustMultiplier * self.allMultiplier
                self.allMultiplierOnce = 1
            elif which = "attraction":
                self.attraction += value * self.attractionMultiplier * self.allMultiplier
                self.allMultiplierOnce = 1
            else:
                raise Error "no specified which"

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

style default:
    font FontGroup().add("FRABK.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)

style outline_text:
    color "#000000"
    outlines [ (absolute(5), "#ffffff", absolute(0), absolute(0)) ]
    font "ui"

define config.font_name_map["ui"] = FontGroup().add("FRADMIT.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
