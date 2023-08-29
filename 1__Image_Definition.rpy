init python:
    def play_sexsound(trans, st, at, filename):
        # renpy.play(filename, channel='sexsfx')
        renpy.sound.queue(filename, channel='sexsfx')
        return None

init python:
    
    #create an animation
    def generate_anim3(img_path, frames, speed=0.1):
        txt = "Animation("
        for frame in range(frames):
            txt += "'"+ img_path + str(frame+1) + ").png', "+str(speed)+","
        
        txt += "'#0000', 2.0)"
        return eval(txt)


image moan_bubble:
    # DynamicDisplayable(Moaning_bubble()) ## in a ATL image, the st resets after every repeat #remove the () ?
    parallel:
        # xalign 0.8 yalign 0.5
        # pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        xalign renpy.random.random()/2+0.25 yalign renpy.random.random()/1.1
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        repeat

    parallel:
        linear 0.25/date.animation_speed_hash[date.animation_speed] alpha 1.0
        pause 1.0/date.animation_speed_hash[date.animation_speed]
        linear 0.25/date.animation_speed_hash[date.animation_speed] alpha 0.0
        linear 0.25/date.animation_speed_hash[date.animation_speed] alpha 1.0
        pause 1.0/date.animation_speed_hash[date.animation_speed]
        linear 0.25/date.animation_speed_hash[date.animation_speed] alpha 0.0
        repeat
    
    parallel:
        "ui/bubble_01.png"
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        "ui/bubble_02.png"
        pause 1.5/date.animation_speed_hash[date.animation_speed]
        repeat
    # block:
    #     xalign 0.3
    #     pause 1.5/date.animation_speed_hash[date.animation_speed]
    #     xalign 0.8
    #     pause 0.5/date.animation_speed_hash[date.animation_speed] alpha 0.0
    #     repeat



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

        # if "armscrossed" in atts:
        #     if "outfit1" not in renpy.get_attributes("joyce") and "outfit2" not in renpy.get_attributes("joyce"):
        #         atts.remove("armscrossed")

        return names[0], *atts

define config.adjust_attributes["joyce"] = joyce_adjuster


label test_sprites:
    scene bg terrasse
    $ i = 0
    $ outfits = ["outfit1", "outfit2", "outfitsm", "outfitred", "outfitblue", "night", "night2", "night3", "night4","outfitsm"]
    $ attr = ["", "push", "key", "whip", "armscrossed", "reveal-1", "reveal-2", "defend"]

    while i<len(outfits):
        $ m = 0
        while m < len(attr):
            $ current = outfits[i] + " " + attr[m]
            show expression "joyce " + outfits[i] + " " + attr[m] at depied
            j "[current]"
            hide expression "joyce " + outfits[i]
            $ m += 1
        $ i += 1

define normal_face = ["outfit1", "outfit2", "outfitsm", "outfitred", "outfitblue", "night", "night2", "night3", "night4","night5"]

layeredimage joyce:

    group outfits:
        attribute outfit1 null
        attribute outfit2 null
        attribute outfitred null
        attribute outfitblue null
        attribute outfitsm null
        attribute outfitdream null
        attribute outfitdream2 null
        attribute outfitdream3 null
        attribute night null
        attribute night2 null
        attribute night3 null
        attribute night4 null
        attribute night5 null


    group arm variant "back":
        attribute arm default if_not "night4":
            "joyce_arm"
        attribute arm if_any "night4":
            "joyce_arm_hide_back"

        attribute arm if_any "outfit1":
            "joyce_arm_1"
        attribute arm if_any "night":
            "joyce_arm_night"
            
        attribute reveal-1 if_not "night":
            "joyce_arm_left_back"
        attribute reveal-1 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_not ["night","night3", "night4"]:
            "joyce_arm_left_back"
        attribute reveal-2 if_any "night":
            "joyce_arm_left_back_night"
        attribute push:
            "joyce_arm_right_back"

        attribute whip:
            "joyce_arm_whip_back"
        attribute key:
            "joyce_arm_key"
        attribute key:
            "joyce_arm_right_back"

        attribute armscrossed:
            "joyce_arm_crossed_back"
        attribute defend:
            "joyce_arm_crossed_back"
        
        # attribute hideboobs:
        #     "joyce_arm_hide_back"


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
        attribute base if_any "outfitred" if_not "reveal-2":
            "joyce_red"
        attribute base if_any "outfitblue":
            "joyce_blue"
        attribute base if_any "night":
            "joyce_night"
        attribute base if_any "night2":
            "joyce_night2"
        attribute base if_any "night3" if_not "reveal-2":
            "joyce_night3"
        attribute base if_any "night4" if_not "reveal-2":
            "joyce_night4"
        attribute base if_any "night5":
            "joyce_night4"

        
        attribute base if_all ["outfitred", "reveal-2"]:
            "joyce_red_reveal"
        attribute base if_all ["night", "reveal-2"]:
            "joyce_night_reveal"
        attribute base if_all ["night2", "reveal-2"]:
            "joyce_night2_reveal"
        attribute base if_all ["night3", "reveal-2"]:
            "joyce_night3_reveal"
        attribute base if_all ["night4", "reveal-2"]:
            "joyce_night4_reveal"

        # attribute armscrossed if_any "outfit2":
        #     "joyce_2_armscrossed"

        # attribute whip:
        #     "joyce_sm_whip"
        # attribute key:
        #     "joyce_sm_key"
        # attribute push:
        #     "joyce_sm_push"

    
    
    group arm:
        attribute reveal-1 if_not ["night"]:
            "joyce_arm_right_reveal (1)"
        attribute reveal-1 if_any ["night"]:
            "joyce_arm_right_reveal (1)_night"
        attribute reveal-2 if_not ["night","night3", "night4"]:
            "joyce_arm_right_reveal (2)"
        attribute reveal-2 if_any "outfitblue":
            "joyce_blue_reveal (2)"

        attribute armscrossed if_not ["outfit1", "outfit2", "outfitdream", "outfitdream2", "outfitdream3","outfitblue","outfitred"]:
            "joyce_arm_crossed"        
        attribute armscrossed if_any ["outfit1", "outfitdream", "outfitdream2", "outfitdream3"]:
            "joyce_arm_crossed_1"
        attribute armscrossed if_any "outfit2":
            "joyce_2_armscrossed"
        attribute armscrossed if_any "outfitblue":
            "joyce_arm_crossed_blue"
        attribute armscrossed if_any "outfitred":
            "joyce_arm_crossed_red"
        attribute armscrossed if_any "night":
            "joyce_arm_crossed_night"
        attribute defend:
            "joyce_arm_defend"
        attribute defend if_any "outfitred":
            "joyce_red_defend"
        attribute defend if_any "outfitblue":
            "joyce_blue_defend"
        attribute defend if_any "night":
            "joyce_arm_defend_night"

        attribute arm if_any "night4":
            "joyce_arm_hide_front"

            
        attribute whip:
            "joyce_arm_whip_front"
        attribute push:
            "joyce_arm_push"

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
        attribute eyeside if_any normal_face
        attribute foxy if_any normal_face
        attribute foxy if_any "outfitsm":
            "joyce_sm_foxy"
        attribute wink
        attribute happy

    group mouth if_not "null":
        attribute null_mouth if_any "null":
            null
        attribute smile if_any normal_face
        attribute smirk if_any normal_face
        attribute tongue
        attribute bite
    attribute green_hair:
        "green_hair"


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