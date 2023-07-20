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

            self.pleasureMax = 10
            self.pleasure = 0

            self.orgasmMax = 20
            self.orgasm = 0

            self.animation_speed = 3
            self.animation_speed_hash = { 1:0.5, 2:0.75, 3:1.0, 4:1.3, 5:1.6,}

            self.state = ""

            self.isHoverHand = True

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