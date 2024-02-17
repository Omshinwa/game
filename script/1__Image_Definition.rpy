init python:
    def play_sexsound(trans, st, at, filename):
        renpy.sound.play(filename, channel='sexsfx', relative_volume=1.0-animation_speed*3)
        return None


init python:
    
    #create an animation
    def generate_anim3(img_path, frames, speed=0.1):
        txt = "Animation("
        for frame in range(frames):
            txt += "'"+ img_path + str(frame+1) + ").png', "+str(speed)+","
        
        txt += "'#0000', 2.0)"
        return eval(txt)

# image test:
#     contains:
#         "cut-in_drink"
#         shaking

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

        return names[0], *atts

define config.adjust_attributes["joyce"] = joyce_adjuster


label test_sprites:
    scene bg terrasse
    $ i = 0
    $ outfits = ["outfitsport", "outfit1", "outfit2", "outfitsm", "outfitred", "outfitblue", "night", "night2", "night3", "night4","outfitsm"]
    $ attr = ["", "push", "key", "whip", "armscrossed", "reveal-1", "reveal-2", "defend"]
    # $ attr = ["", "foxy", "happy", "upset", "wink", "worried", "bite", "smile", "smirk", "tongue", "blush", "eyeside"]
    # $ third_switch = ["", "hair_braids"]
    $ third_switch = [""]

    while i<len(outfits):
        $ m = 0
        while m < len(attr):
            $ n = 0
            while n < len(third_switch):
                $ current = outfits[i] + " " + attr[m] + " " + third_switch[n]
                $ renpy.show("joyce " + outfits[i] + " " + attr[m] + " " + third_switch[n], at_list=[trs_depied])
                j "[current]"
                hide joyce
                $ n += 1
            $ m += 1
        $ i += 1

# define all the outfits that doesnt have the face tilted, useful to check for blushes etc
define normal_face = ["outfitsport", "outfit1", "outfit2", "outfitsm", "outfitred", "outfitblue", "night", "night2", "night3", "night4","night5","outfitcasino", "outfit3"]

layeredimage joyce:

    group outfits: #make sure you cant have two different outfit at the same time
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

        attribute outfit3 null
        attribute outfitcasino null
        attribute outfitsport null

    group hair variant "back":
        attribute hair default: 
            "joyce_hair_back" 
        attribute hair_braids
        attribute outfitsport
        attribute outfitsm:
            "joyce_hair_back" 

    group arm variant "back":

        attribute arm default: #the default argument means we're always including the attribute "arm"
            null

        # if "outfitpoker" in renpy.get_attributes("joyce"):
        #     "joyce_arm_poker"
        # else:
        #     if not "night4":
        #         "joyce_arm"

        attribute arm if_not ["night4", "outfitcasino"]:
            "joyce_arm"
        attribute arm if_any "night4":
            "joyce_arm_hide_back"
        attribute arm if_any "outfit1":
            "joyce_arm_1"
        attribute arm if_any "night":
            "joyce_arm_night"
        attribute arm if_any "outfitcasino":
            "joyce_arm_casino"
        attribute arm if_any "outfitsport":
            "joyce_arm_sport"
        attribute arm if_any "outfitsm":
            "joyce_arm_sm"
            
        attribute reveal-1 if_not "night":
            "joyce_arm_left_back"
        attribute reveal-1 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_not ["night","night3", "night4"]:
            "joyce_arm_left_back"
        attribute push if_not "outfitsm":
            "joyce_arm_right_back"
        attribute push if_any "outfitsm":
            "joyce_arm_right_back_sm"

        attribute whip:
            "joyce_arm_whip_back_sm"
        attribute key if_not "outfitsm":
            "joyce_arm_key"
        attribute key if_not "outfitsm":
            "joyce_arm_right_back"
        attribute key if_any "outfitsm":
            "joyce_arm_key_sm"
        attribute key if_any "outfitsm":
            "joyce_arm_right_back_sm"

        attribute armscrossed:
            "joyce_arm_armscrossed_back"
        # attribute defend:
            # "joyce_arm_crossed_back"
        
        # attribute hideboobs:
        #     "joyce_arm_hide_back"
        attribute holdbook:
            "joyce_arm_holdbook_back"

    group base:
        attribute base default:
            null
        attribute base if_any "outfit1":
            "joyce_1"
        attribute base if_any "outfit2":
            "joyce_2"
        attribute base if_any "outfit3":
            "joyce_3"
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
        attribute base if_all ["outfitred","defend"]:
            "joyce_red_defend"
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
        
        attribute base if_any "outfitcasino":
            "joyce_casino"
        attribute base if_any "outfitsport":
            "joyce_sport"
        
        attribute base if_all ["outfitred", "reveal-2"]:
            "joyce_red_reveal"
        attribute base if_all ["outfitblue", "reveal-2"]:
            "joyce_blue_reveal"
        attribute base if_all ["night", "reveal-2"]:
            "joyce_night_reveal"
        attribute base if_all ["night2", "reveal-2"]:
            "joyce_night2_reveal"
        attribute base if_all ["night3", "reveal-2"]:
            "joyce_night3_reveal"
        attribute base if_all ["night4", "reveal-2"]:
            "joyce_night4_reveal"
    

    group face:
        attribute face default:
            "joyce_face"

    group skin:
        attribute null_skin if_any "null":
            null
        attribute blush if_any normal_face

    group eyes:
        attribute null_eyes default:
            "img_blink" #null
        attribute upset if_any normal_face
        attribute worried if_any normal_face
        attribute eyeside if_any normal_face
        attribute foxy if_any normal_face
        attribute foxy if_any "outfitsm":
            "joyce_sm_foxy"
        attribute wink
        attribute happy
        attribute eyes_closed:
            "joyce_eyes_closed"
        attribute eyesdown

    group mouth if_not "null":
        attribute null_mouth default:
            "joyce_mouth_normal"
        attribute smile if_any normal_face
        attribute smirk if_any normal_face
        attribute tongue
        attribute bite

    group arm: #frontarm
        attribute reveal-1 if_not ["night"]:
            "joyce_arm_right_reveal (1)"
        attribute reveal-1 if_any ["night"]:
            "joyce_arm_right_reveal (1)_night"
        attribute reveal-2 if_not ["night","night3", "night4"]:
            "joyce_arm_right_reveal (2)"
        attribute reveal-2 if_any ["night"]:
            "joyce_arm_right_reveal (2)_night"

        attribute armscrossed if_not ["outfit1", "outfit2","outfitdream", "outfitdream2", "outfitdream3"]:
            "joyce_arm_armscrossed_front"        
        attribute armscrossed if_any ["outfit1", "outfitdream", "outfitdream2", "outfitdream3"]:
            "joyce_arm_crossed_1"

        attribute armscrossed if_any ["outfit2"]:
            "joyce_2_armscrossed"
        attribute armscrossed if_any "night":
            "joyce_arm_crossed_night"
        attribute arm if_any "night4":
            "joyce_arm_hide_front"

        attribute holdbook
            

    group hair variant "front":
        attribute hair: 
            "joyce_hair_front" 
        attribute hair_braids
        attribute green_hair:
            "green_hair"
        attribute outfitsport
        attribute outfitsm:
            "joyce_hair_front_sm" 
    
    group accessories:
        attribute outfit3:
            "joyce_glasses"

    group arm variant "in front of hair":
    
        attribute whip:
            "joyce_arm_whip_front_sm"
        attribute push:
            "joyce_arm_push"
        attribute push if_any "outfitsm":
            "joyce_arm_push_sm"


        attribute defend:
            "joyce_arm_defend"
        # attribute defend if_any "outfitblue":
        #     "joyce_blue_defend"
        attribute defend if_any "night":
            "joyce_arm_defend_night"
        

image img_blink:
    "joyce_eyes_normal"
    pause(3.0)
    "joyce_eyes_half"
    pause(0.1)
    "joyce_eyes_closed"
    pause(0.1)
    "joyce_eyes_half"
    pause(0.1)
    "joyce_eyes_normal"
    pause(2.0)
    repeat

default animation_speed = 0.9

init python:
    def update_animationSpeed(speed:float = None) :
        """
        whenever the speed changes, we need to show the img again. also it automatically put "v2" again 
        """
        global animation_speed
        if speed is None:
            speed = date.animation_speed_hash[date.animation_speed]
        animation_speed = speed

        # if joyce isnt in animation mode, this remake her animated by removing superfluous tags
        keywords = [renpy.get_attributes("joyce")[0], "naked", "v2"]
        temp = tuple(element for element in renpy.get_attributes("joyce") if element not in keywords)
        renpy.show("joyce -" + " -".join(temp))
        # renpy.show("joyce")
        return


init python:
    #those are functions used to make writing SEX animations easier/more dynamic

    def img_if_naked(filename, skipIfSlow=False, frameToShowIfSlow = None):
        """
        add 'naked' if the variable naked is on
        """
        if "naked" in renpy.get_attributes("joyce"):
            return "Joyce/sex/" + filename + " naked.png"
        else:
            return "Joyce/sex/" + filename + ".png"



    def skip_frame_if_slow(minimum = 2):
        if animation_speed < date.animation_speed_hash[minimum]:
            # return "pause(animation_speed)"
            return animation_speed
        else:
            return "this_will_skip_the_frame"

    def alt_img_if_slow(minimum, normal_img, slow_img):
        if animation_speed < date.animation_speed_hash[minimum]:
            return normal_img
        else:
            return slow_img

image img_joyce_cowgirl:
    img_if_naked("cowgirl/joyce cowgirl 1")
    pause(animation_speed)
    function renpy.curry(play_sexsound)(filename="sex/slap.wav") #hacky
    img_if_naked("cowgirl/joyce cowgirl 2")
    pause(animation_speed)
    img_if_naked("cowgirl/joyce cowgirl 3")
    pause(animation_speed)
    img_if_naked("cowgirl/joyce cowgirl 4")
    pause(animation_speed)
    img_if_naked("cowgirl/joyce cowgirl 5")
    pause(animation_speed)
    img_if_naked("cowgirl/joyce cowgirl 6")
    pause(animation_speed)
    repeat

layeredimage joyce cowgirl:
    group cowgirl:
        attribute v1 default:
            "img_joyce_cowgirl"
        attribute naked if_not "v2":
            "img_joyce_cowgirl"
        attribute v2:
            "img_joyce_cowgirl"

image img_joyce_footjob:
    "Joyce/sex/footjob/joyce footjob 1.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 2.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 3.png"
    pause(animation_speed)
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/footjob/joyce footjob 4.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 3.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 2.png"
    pause(animation_speed)
    repeat
image img_joyce_footjob_naked:
    "Joyce/sex/footjob/joyce footjob 1 naked.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 3 naked.png"
    pause(animation_speed)
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/footjob/joyce footjob 4 naked.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 3 naked.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 2 naked.png"
    pause(animation_speed)
    repeat
image img_joyce_footjob_v2:
    img_if_naked("footjob/joyce footjob v2 1")
    skip_frame_if_slow(1)
    img_if_naked("footjob/joyce footjob v2 2")
    skip_frame_if_slow(1)
    img_if_naked("footjob/joyce footjob v2 3")
    skip_frame_if_slow(1)
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    img_if_naked("footjob/joyce footjob v2 4")
    pause(animation_speed)
    img_if_naked("footjob/joyce footjob v2 5")
    pause(animation_speed)
    img_if_naked("footjob/joyce footjob v2 6")
    skip_frame_if_slow(2)
    img_if_naked("footjob/joyce footjob v2 7")
    skip_frame_if_slow(2)
    img_if_naked("footjob/joyce footjob v2 6")
    skip_frame_if_slow(2)
    img_if_naked("footjob/joyce footjob v2 5")
    skip_frame_if_slow(2)
    img_if_naked("footjob/joyce footjob v2 4")
    pause(animation_speed)
    img_if_naked("footjob/joyce footjob v2 3")
    pause(animation_speed)
    img_if_naked("footjob/joyce footjob v2 2")
    skip_frame_if_slow(1)
    repeat

layeredimage joyce footjob:
    group footjob:
        attribute v1 default:
            "img_joyce_footjob"
        attribute naked if_not "v2":
            "img_joyce_footjob_naked"
        attribute v2:
            "img_joyce_footjob_v2"

image img_joyce_handjob:
    "Joyce/sex/handjob/joyce handjob 3.png"
    skip_frame_if_slow(2)
    "Joyce/sex/handjob/joyce handjob 2.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob 1.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob 2.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob 3.png"
    pause(animation_speed)
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/handjob/joyce handjob 4.png"
    skip_frame_if_slow(2)
    repeat
image img_joyce_handjob_naked:
    "Joyce/sex/handjob/joyce handjob 3 naked.png"
    skip_frame_if_slow(2)
    "Joyce/sex/handjob/joyce handjob 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob 1 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob 3 naked.png"
    pause(animation_speed)
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/handjob/joyce handjob 4 naked.png"
    skip_frame_if_slow(2)
    repeat
image img_joyce_handjob_v2:
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/handjob/joyce handjob v2 1.png"
    skip_frame_if_slow(2)
    "Joyce/sex/handjob/joyce handjob v2 2.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 3.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 4.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 5.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 6.png"
    pause(animation_speed)
    repeat
image img_joyce_handjob_v2_naked:
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    "Joyce/sex/handjob/joyce handjob v2 1 naked.png"
    skip_frame_if_slow(2)
    "Joyce/sex/handjob/joyce handjob v2 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 3 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 4 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 5 naked.png"
    pause(animation_speed)
    "Joyce/sex/handjob/joyce handjob v2 6 naked.png"
    pause(animation_speed)
    repeat

layeredimage joyce handjob:
    group handjob:
        attribute v1 default:
            "img_joyce_handjob"
        attribute naked if_not "v2":
            "img_joyce_handjob_naked"
        attribute v2 if_not "naked":
            "img_joyce_handjob_v2"
        attribute v2 if_all "naked":
            "img_joyce_handjob_v2_naked"

image img_joyce_titjob:
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    img_if_naked("titjob/joyce titjob 1")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob 2")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob 3")
    skip_frame_if_slow(2)
    img_if_naked("titjob/joyce titjob 4")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob 5")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob 6")
    skip_frame_if_slow(1)
    repeat
image img_joyce_titjob_v2:
    function renpy.curry(play_sexsound)(filename="sex/sloppy.wav") #hacky
    img_if_naked("titjob/joyce titjob v2 1")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob v2 2")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob v2 3")
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob v2 4")
    pause(animation_speed)
    alt_img_if_slow(2,img_if_naked("titjob/joyce titjob v2 5"), img_if_naked("titjob/joyce titjob v2 3"))
    pause(animation_speed)
    alt_img_if_slow(2,img_if_naked("titjob/joyce titjob v2 6"), img_if_naked("titjob/joyce titjob v2 2"))
    pause(animation_speed)
    img_if_naked("titjob/joyce titjob v2 7")
    skip_frame_if_slow(2)
    repeat

layeredimage joyce titjob:
    group titjob:
        attribute v1 default:
            "img_joyce_titjob"
        attribute naked if_not "v2":
            "img_joyce_titjob"
        attribute v2 if_not "naked":
            "img_joyce_titjob_v2"
        attribute v2 if_all "naked":
            "img_joyce_titjob_v2"

image img_joyce_blowjob:
    function renpy.curry(play_sexsound)(filename="sex/slurp.wav") #hacky
    "Joyce/sex/blowjob/joyce blowjob 1.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob 2.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob 3.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob 4.png"
    skip_frame_if_slow(2)
    "Joyce/sex/blowjob/joyce blowjob 5.png"
    skip_frame_if_slow(2)
    "Joyce/sex/blowjob/joyce blowjob 6.png"
    pause(animation_speed)
    repeat
image img_joyce_blowjob_naked:
    function renpy.curry(play_sexsound)(filename="sex/slurp.wav") #hacky
    "Joyce/sex/blowjob/joyce blowjob 1 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob 3 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob 4 naked.png"
    skip_frame_if_slow(2)
    "Joyce/sex/blowjob/joyce blowjob 5 naked.png"
    skip_frame_if_slow(2)
    "Joyce/sex/blowjob/joyce blowjob 6 naked.png"
    pause(animation_speed)
    repeat
image img_joyce_blowjob_v2:
    function renpy.curry(play_sexsound)(filename="sex/slurp.wav") #hacky
    "Joyce/sex/blowjob/joyce blowjob v2 1.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 2.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 3.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 4.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 5.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 6.png"
    pause(animation_speed)
    repeat
image img_joyce_blowjob_v2_naked:
    function renpy.curry(play_sexsound)(filename="sex/slurp.wav") #hacky
    "Joyce/sex/blowjob/joyce blowjob v2 1 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 3 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 4 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 5 naked.png"
    pause(animation_speed)
    "Joyce/sex/blowjob/joyce blowjob v2 6 naked.png"
    pause(animation_speed)
    repeat


layeredimage joyce blowjob:
    group blowjob:
        attribute v1 default:
            "img_joyce_blowjob"
        attribute naked if_not "v2":
            "img_joyce_blowjob_naked"
        attribute v2 if_not "naked":
            "img_joyce_blowjob_v2"
        attribute v2 if_all "naked":
            "img_joyce_blowjob_v2_naked"

image card_zone_bg:
    xalign 1.0 
    "ui/card_zone_bg.png"
    linear 3.0 xalign 0.0
    repeat

image img_toilet-static:
    "prison/toilet-static.png"
    zoom 3.0

image img_toilet-flush = Movie(play="images/prison/flush.avi")

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