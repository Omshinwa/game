init python:
    def play_sexsound(trans, st, at, filename):
        renpy.play(filename, channel='sexsfx')
        return None

init python:
    class Moaning_bubble:
        def __init__(self):
            self.xpos = 500
            self.ypos = 500
            self.last_cycle = 0
            self.cycle = 0
        
        def rand_pos(self):
            self.ypos = renpy.random.randint(300, 800)
            self.xpos = renpy.random.randint(300, 1600)

        def __call__(self, st, at):
            if self.cycle%2:
                img_path = "ui/bubble_01.png"
            else:
                img_path = "ui/bubble_02.png"

            if st > (2/date.animation_speed_hash[date.animation_speed])-0.1 :
                self.cycle += 1
                self.rand_pos()

            d = Transform(img_path, ypos=self.ypos, xpos=self.xpos)
            return d, 0.1
    
    def generate_anim3(img_path, frames, speed=0.1):
        txt = "Animation("
        for frame in range(frames):
            txt += "'"+ img_path + str(frame+1) + ").png', "+str(speed)+","
        
        txt += "'#0000', 2.0)"
        return eval(txt)


image moan_bubble:
    DynamicDisplayable(Moaning_bubble()) ## in a ATL image, the st resets after every repeat #remove the () ?
    alpha 0.0
    linear 0.5/date.animation_speed_hash[date.animation_speed] alpha 1.0
    pause 1.0/date.animation_speed_hash[date.animation_speed]
    linear 0.5/date.animation_speed_hash[date.animation_speed] alpha 0.0
    # pause 1.0/date.animation_speed_hash[date.animation_speed]**2
    repeat


init python:
    def joyce_adjuster(names):
        atts = set(names[1:])
        if "null" in atts:
            atts.remove("null")
            atts.add("null_skin")
            atts.add("null_eyes")
            atts.add("null_mouth")
            if "defend" in atts:
                atts.remove("defend")
            if "armscrossed" in atts:
                atts.remove("armscrossed")

        if "armscrossed" in atts:
            if "outfit1" not in renpy.get_attributes("joyce") and "outfit2" not in renpy.get_attributes("joyce"):
                atts.remove("armscrossed")

        return names[0], *atts

define config.adjust_attributes["joyce"] = joyce_adjuster

define normal_face = ["outfit1", "outfit2", "outfitsm", "outfitred", "outfitblue"]

layeredimage joyce:

    attribute outfit1 null
    attribute outfit2 null
    attribute outfitred null
    attribute outfitblue null
    attribute outfitsm null
    attribute outfitdream null
    attribute outfitdream2 null
    attribute outfitdream3 null

    group base:
        attribute base default:
            null
        attribute base if_any "outfit1":
            "joyce_1"
        attribute base if_any "outfit2":
            "joyce_2"
        attribute base if_any "outfitsm":
            "joyce_sm"
        attribute base if_any "outfitdream":
            "joyce_dream"
        attribute base if_any "outfitdream2":
            "joyce_dream2"
        attribute base if_any "outfitdream3":
            "joyce_dream3"
        attribute base if_any "outfitred":
            "joyce_red"
        attribute base if_any "outfitblue":
            "joyce_blue"


        attribute armscrossed:
            "joyce_armscrossed"
        attribute armscrossed if_any "outfit1":
            "joyce_armscrossed"
        attribute armscrossed if_any "outfit2":
            "joyce_2armscrossed"

        attribute whip:
            "joyce_sm_whip"
        attribute key:
            "joyce_sm_key"
        attribute push:
            "joyce_sm_push"

        attribute defend:
            "joyce_2_defend"
        attribute defend if_any "outfitred":
            "joyce_red_defend"
        attribute defend if_any "outfitblue":
            "joyce_blue_defend"
    
    group skin:
        attribute null_skin if_any "null":
            null
        attribute blush if_any normal_face

    group eyes:
        attribute blink default:
            "img_blink"
        attribute null_eyes if_any "null":
            null
        attribute upset if_any normal_face
        attribute worried if_any normal_face
        attribute eyesside if_any normal_face
        attribute foxy if_any normal_face
        attribute foxy if_any "outfitsm":
            "joyce_sm_foxy"

    group mouth if_not "null":
        attribute null_mouth if_any "null":
            null
        attribute smile if_any normal_face
        attribute smirk if_any normal_face

image img_blink:
    "Joyce/joyce_blink.png"
    alpha 0.0
    pause(3.0)
    alpha 1.0
    pause(0.1)
    alpha 0.0
    pause(3.0)
    alpha 1.0
    pause(0.1)
    alpha 0.0
    pause(0.1)
    alpha 1.0
    pause(0.1)
    repeat

image joyce cowgirl:
    "Joyce/sex/cowgirl/cowgirl (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])

    function renpy.curry(play_sexsound)(filename="sex/slap.wav") #hacky

    "Joyce/sex/cowgirl/cowgirl (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/cowgirl/cowgirl (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/cowgirl/cowgirl (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/cowgirl/cowgirl (5).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/cowgirl/cowgirl (6).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image joyce footjob:
    "Joyce/sex/footjob/footjob (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])

    "Joyce/sex/footjob/footjob (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])

    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/footjob/footjob (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image joyce footjob v2:
    "Joyce/sex/footjob/footjob v2 (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob v2 (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob v2 (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])

    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/footjob/footjob v2 (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob v2 (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/footjob/footjob v2 (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image joyce handjob:
    "Joyce/sex/handjob/handjob (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/handjob/handjob (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image joyce handjob v2:
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/handjob/handjob v2 (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob v2 (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob v2 (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob v2 (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob v2 (5).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/handjob/handjob v2 (6).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image joyce blowjob:
    function renpy.curry(play_sexsound)(filename="sex/slurp.wav") #hacky
    "Joyce/sex/blowjob/blowjob (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob (5).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob (6).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image joyce blowjob v2:
    function renpy.curry(play_sexsound)(filename="sex/slurp.wav") #hacky
    "Joyce/sex/blowjob/blowjob v2 (1).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob v2 (2).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob v2 (3).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob v2 (4).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob v2 (5).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    "Joyce/sex/blowjob/blowjob v2 (6).png"
    pause(0.1 / date.animation_speed_hash[date.animation_speed])
    repeat

image card_zone_bg:
    xalign 1.0 
    "ui/card_zone_bg.png"
    linear 3.0 xalign 0.0
    repeat

image img_toilet-static:
    "prison/toilet-static.png"
    zoom 3.0

image img_toilet-flush = Movie(play="images/prison/input.avi")

image joyce cowgirl-orgasm:
    "Joyce/sex/cowgirl/cowgirl-orgasm (1).png"
    pause(0.1)
    "Joyce/sex/cowgirl/cowgirl-orgasm (2).png"
    pause(0.1)
    repeat

image img_hand_caress:
    "Joyce/anim/hand-caress.png"
    alpha 0.8
    xpos 301
    ypos 177