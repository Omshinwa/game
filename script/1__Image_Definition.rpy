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

    #create an animation from AE
    def generate_anim_AE(img_path, frames, speed=0.1):
        txt = "Animation("
        for frame in range(frames):
            txt += "'"+ img_path + format(frame,'02d') + ".png', "+str(speed)+","
        
        txt += "'#0000', 0.0)"
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


#############################################################################
#                                                                                     
#
#         :::            :::   :::   ::: :::::::::: :::::::::  :::::::::: :::::::::  
#         :+:          :+: :+: :+:   :+: :+:        :+:    :+: :+:        :+:    :+: 
#         +:+         +:+   +:+ +:+ +:+  +:+        +:+    +:+ +:+        +:+    +:+ 
#         +#+        +#++:++#++: +#++:   +#++:++#   +#++:++#:  +#++:++#   +#+    +:+ 
#         +#+        +#+     +#+  +#+    +#+        +#+    +#+ +#+        +#+    +#+ 
#         #+#        #+#     #+#  #+#    #+#        #+#    #+# #+#        #+#    #+# 
#         ########## ###     ###  ###    ########## ###    ### ########## #########  
#
#
#############################################################################

init python:
    def joyce_adjuster(names):
        atts = set(names[1:])
        if "null" in atts:
            atts.remove("null")
            atts.add("null_skin")
            atts.add("null_eyes")
            atts.add("null_mouth")
            atts.add("arm")

        return names[0], *atts

define config.adjust_attributes["joyce"] = joyce_adjuster


# define all the outfits that doesnt have the face tilted, useful to check for blushes etc
define normal_face = ["outfitsport", "outfitsport2", "outfitsport3", "outfit1", "outfit2", "outfitsm", "outfitred", "outfitblue", "night", "night2", "night3", "night4","night5","night6", "outfitcasino", "outfit3"]

layeredimage joyce:

    group outfits: #make sure you cant have two different outfit at the same time
        attribute outfit1 null
        attribute outfit2 null
        attribute outfitred null
        attribute outfitblue null
        attribute outfitsm null
        attribute night null
        attribute night2 null
        attribute night3 null
        attribute night4 null
        attribute night5 null
        attribute night6 null
        attribute sitted null

        attribute outfit3 null
        attribute outfit4 null
        attribute outfitcasino null
        attribute outfitsport null
        attribute outfitsport2 null
        attribute outfitsport3 null

        attribute wet null

    group hair variant "back":
        attribute hair default: 
            "joyce_hair_back" 
        attribute wet: 
            "joyce_hair_back" 
        attribute green_hair:
            "joyce_hair_back_green" 
        attribute hair_braids
        attribute outfitsport
        attribute outfitsport2:
            "joyce_hair_back_outfitsport"
        attribute outfitsport3:
            "joyce_hair_back_outfitsport"

    group arm variant "back":

        attribute arm default: #the default argument means we're always including the attribute "arm"
            null

        attribute arm if_not ["outfitcasino", "sitted"]:
            "joyce_arm"
        attribute hide1:
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

        attribute arm if_any "sitted" "joyce_arm_back_right_half"
        attribute arm if_any "sitted" "joyce_arm_back_left_half"


        attribute posé:
            "joyce_arm_back_right_half"
        attribute posé:
            "joyce_arm_back_left_half"
        
        attribute armstraight "joyce_arm"

        attribute defend:
            "joyce_arm_defend_back"

        attribute holdglasses if_any "sitted":
            "joyce_arm_back_right_half"
        attribute holdglasses if_not "sitted" "joyce_arm_right_back"

        attribute reveal-1 if_not "night":
            "joyce_arm_left_back"
        attribute reveal-1 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_not ["night","night3", "night4", "night5"]:
            "joyce_arm_left_back"
        attribute push if_not "outfitsm":
            "joyce_arm_right_back"
        attribute push if_any "outfitsm":
            "joyce_arm_right_back_sm"


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
        attribute holdbook:
            "joyce_arm_holdbook_back"

        attribute running if_not ["outfitsport"]:
            "joyce_arm_back_diagonal"
        attribute running if_any ["outfitsport"]:
            "joyce_arm_back_diagonal_sport"

            
        attribute shh "joyce_arm_whisper_back"
        attribute shh if_not "outfit4" "joyce_arm_right_back"
        
        attribute throwWater "joyce_arm_right_back"
        attribute wave "joyce_arm_back_diagonal_right"
        attribute wave "joyce_arm_left_back"
        attribute whip "joyce_arm_whip_back_sm"
        attribute whisper "joyce_arm_whisper_back"
        attribute whisper if_not "outfit4" "joyce_arm_right_back"


    # this is the case where base changes on some arm positions:
    # group base variant "outfitred" if_all "outfitred" auto
    # group base variant "outfitblue" if_all "outfitblue" auto
    # group base variant "outfitsport" if_all "outfitsport" auto
    # group base variant "night" if_all "night" auto
    # group base variant "night2" if_all "night2" auto
    # group base variant "night3" if_all "night3" auto
    # group base variant "night4" if_all "night4" auto
    # group base variant "night5" if_all "night5" auto

    group base variant "defend" if_any "defend" auto
    group base variant "reveal-2" if_any "reveal-2" auto
    group base variant "reveal" if_any "reveal" auto

    group base auto:
        attribute night6 default
        attribute outfitred if_not "reveal-2"
        attribute outfitblue if_not "reveal-2"
        attribute night if_not "reveal-2"
        attribute night2 if_not "reveal-2"
        attribute night3 if_not "reveal-2"
        attribute night4 if_not "reveal-2"
        attribute night5 if_not "reveal-2"
        attribute outfitsport if_not "undress"
        
    group face:
        attribute face default:
            "joyce_face"
        attribute sweaty
        attribute sweaty2


    group skin:
        attribute null_skin if_any "null":
            null
        attribute blush

    group eyes auto:
        attribute null_eyes default:
            "img_blink" #null
        attribute upset
        attribute worried
        attribute eyeside
        attribute foxy
        attribute wink
        attribute happy
        attribute eyesclosed "joyce_eyes_closed"
        attribute eyesdown
        attribute squint
        attribute bored

    group mouth: #if_not "null":
        attribute null_mouth default:
            "joyce_mouth_normal"
        attribute smile 
        attribute smirk
        attribute tongue
        attribute bite
        attribute breath
        attribute opened

    group arm variant "front": #frontarm

        attribute armscrossed if_not ["outfit1"]:
            "joyce_arm_armscrossed_front"        
        attribute armscrossed if_all ["outfitsport"]:
            "joyce_arm_armscrossed_front_sport"        
        attribute armscrossed if_any ["outfit1"]:
            "joyce_arm_crossed_1"
        attribute armscrossed if_any ["outfit2"]:
            "joyce_2_armscrossed"
        attribute armscrossed if_any "night":
            "joyce_arm_crossed_night"

        attribute reveal-1 if_not ["night"]:
            "joyce_arm_right_reveal (1)"
        attribute reveal-1 if_any ["night"]:
            "joyce_arm_right_reveal (1)_night"
        attribute reveal-2 if_not ["night","night3", "night4", "night5"]:
            "joyce_arm_right_reveal (2)"
        attribute reveal-2 if_any ["night"]:
            "joyce_arm_right_reveal (2)_night"

        
        attribute arm if_any "sitted" "joyce_arm_front_sitted_right"
        attribute arm if_any "sitted" "joyce_arm_front_sitted_left"

        attribute posé:
            "joyce_arm_front_sitted_right"
        attribute posé:
            "joyce_arm_front_sitted_left"
            
        attribute hide1:
            "joyce_arm_hide_front"
        attribute hide2:
            "joyce_arm_hide2"

        attribute holdbook
        attribute holdglasses if_any "sitted" "joyce_arm_front_sitted_right"

        attribute running if_not ["outfitsport"]:
            "joyce_arm_front_running"
        attribute running if_any ["outfitsport"]:
            "joyce_arm_front_running_sport"

    group accessories:
        attribute outfitred:
            "joyce_accessories_pearls"
        attribute outfitblue:
            "joyce_accessories_pearls"
        attribute pearls

    group hair variant "front":
        attribute hair: 
            "joyce_hair_front" 
        attribute hair_braids
        attribute green_hair:
            "joyce_hair_front_green"
        attribute outfitsport
        attribute outfitsport2:
            "joyce_hair_front_outfitsport"
        attribute outfitsport3:
            "joyce_hair_front_outfitsport"
        attribute wet

    
    group accessories auto:
        attribute outfitsm:
            "joyce_glasses_sm" 
        attribute pearls null
        attribute sweaty:
            "joyce_sweaty"
        attribute sweaty2:
            "joyce_sweaty2"
        attribute sunglasses
        attribute sunglasses2

    group arm variant "in front of hair":
        attribute whip:
            "joyce_arm_whip_front_sm"
        attribute push:
            "joyce_arm_push"
        attribute push if_any "outfitsm":
            "joyce_arm_push_sm"

        attribute defend:
            "joyce_arm_defend_front"
        # attribute defend if_any "outfitblue":
        #     "joyce_blue_defend"
        attribute defend if_any "outfitsport":
            "joyce_arm_defend_front_sport"
        attribute defend if_any "night":
            "joyce_arm_defend_night"

        attribute holdglasses:
            "joyce_arm_holdglasses"

        attribute shh:
            "joyce_arm_right_shh"
        attribute shh if_all "outfit4":
            "joyce_arm_holdbook_right"

        attribute throwWater:
            "joyce_arm_throwwater"
        attribute undress if_any ["outfitsport", "outfitsport2"]:
            "joyce_arm_front_sport_undress"
        
        attribute wave:
            "joyce_arm_wave"
        attribute whisper:
            "joyce_arm_whisper_front"
        attribute whisper if_all "outfit4":
            "joyce_arm_holdbook_right"

        
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

default animation_speed = 0.999

init python:
    def update_animationSpeed(speed:float = None, * , changeSprite:bool = True) :
        """
        whenever the speed changes, we need to show the img again. also it automatically put "v2" again 
        """
        global animation_speed
        if speed is None:
            speed = date.animation_speed_hash[date.animation_speed]
        animation_speed = speed

        # if _in_replay:
            # if joyce isnt in animation mode, this remake her animated by removing superfluous tags
        
        # do we update the sprite to show the sex animation?
        if changeSprite:
            keywords = [renpy.get_attributes("joyce")[0], "naked", "v2"]
            temp = tuple(element for element in renpy.get_attributes("joyce") if element not in keywords)
            renpy.show("joyce -" + " -".join(temp))
        
        return

init python:
    #those are functions used to make writing SEX animations easier/more dynamic

    def img_if_naked(filename, skipIfSlow=False, frameToShowIfSlow = None):
        """
        add 'naked' if the variable naked is on
        """
        if renpy.get_attributes("joyce") and "naked" in renpy.get_attributes("joyce"):
            return "Joyce/sex/" + filename + " naked.png"
        else:
            return "Joyce/sex/" + filename + ".png"



    def skip_frame_if_slow(minimum = 2):
        if animation_speed < date.animation_speed_hash[minimum]:
            # return "pause(animation_speed)"
            return "pause " + animation_speed
        else:
            return "this_will_skip_the_frame"

    def skip_frame_if_fast(minimum = 2):
        if date.animation_speed > minimum:
            # return "pause(animation_speed)"
            return "pause " + animation_speed
        else:
            return "this_will_skip_the_frame"

    def alt_img_if_slow(minimum, normal_img, slow_img):
        if animation_speed < date.animation_speed_hash[minimum]:
            return normal_img
        else:
            return slow_img

# ############################################################################
#
#             ::::::::  :::::::::: :::    ::: 
#            :+:    :+: :+:        :+:    :+: 
#            +:+        +:+         +:+  +:+  
#            +#++:++#++ +#++:++#     +#++:+   
#                   +#+ +#+         +#+  +#+  
#            #+#    #+# #+#        #+#    #+# 
#             ########  ########## ###    ### 
#
# ############################################################################
image img_joyce_doggy_naked:
    "Joyce/sex/doggy/joyce doggy 1 naked.png"
    pause(animation_speed)
    "Joyce/sex/doggy/joyce doggy 2 naked.png"
    pause(animation_speed)
    "Joyce/sex/doggy/joyce doggy 3 naked.png"
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
    pause(animation_speed)
    "Joyce/sex/doggy/joyce doggy 4 naked.png"
    pause(animation_speed)
    "Joyce/sex/doggy/joyce doggy 5 naked.png"
    pause(animation_speed)
    "Joyce/sex/doggy/joyce doggy 6 naked.png"
    pause(animation_speed)
    "Joyce/sex/doggy/joyce doggy 7 naked.png"
    pause(animation_speed)
    repeat

layeredimage joyce doggy:
    group doggy:
        attribute v1 default:
            "img_joyce_doggy_naked"
        # attribute naked if_not "v2":
        #     "img_joyce_footjob_naked"
        # attribute v2:
        #     "img_joyce_footjob_v2"


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
        attribute v2 if_all "naked":
            "img_joyce_cowgirl"

image img_joyce_footjob:
    "Joyce/sex/footjob/joyce footjob 1.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 2.png"
    pause(animation_speed)
    "Joyce/sex/footjob/joyce footjob 3.png"
    pause(animation_speed)
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
    "Joyce/sex/handjob/joyce handjob 4 naked.png"
    skip_frame_if_slow(2)
    repeat
image img_joyce_handjob_v2:
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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
    function renpy.curry(play_sexsound)(filename="sex/_sloppy.wav") #hacky
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



############################################################################################################
#
#        ::::    ::::  ::::::::::: ::::::::   ::::::::  
#        +:+:+: :+:+:+     :+:    :+:    :+: :+:    :+: 
#        +:+ +:+:+ +:+     +:+    +:+        +:+        
#        +#+  +:+  +#+     +#+    +#++:++#++ +#+        
#        +#+       +#+     +#+           +#+ +#+        
#        #+#       #+#     #+#    #+#    #+# #+#    #+# 
#        ###       ### ########### ########   ########  
#
###########################################################################################################


image img_toilet-static:
    "prison/toilet-static.png"
    zoom 3.0

image img_toilet-flush = Movie(play="images/prison/flush.avi")


image img_hand_caress:
    "Joyce/anim/hand-caress.png"
    alpha 0.8
    xpos 301
    ypos 177