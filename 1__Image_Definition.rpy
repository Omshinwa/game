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
    
image moan_bubble:
    DynamicDisplayable(Moaning_bubble()) ## in a ATL image, the st resets after every repeat
    alpha 0.0
    linear 0.5/date.animation_speed_hash[date.animation_speed] alpha 1.0
    pause 1.0/date.animation_speed_hash[date.animation_speed]
    linear 0.5/date.animation_speed_hash[date.animation_speed] alpha 0.0
    # pause 1.0/date.animation_speed_hash[date.animation_speed]**2
    repeat

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
            "joyce_2"
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
    
    group skin:
        attribute neutral default:
            null
        attribute blush

    group eyes:
        attribute blink default:
            "img_blink"
        attribute stare:
            null
        attribute upset
        attribute worried
        attribute eyesside
    group mouth:
        attribute smile
        attribute neutral:
            null

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

image joyce footjobv2:
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