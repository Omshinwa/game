label label_reaction_touchy():
    call label_reaction_common("touchy")

    if renpy.get_image_bounds("joyce")[1] == -45:
        $ i = trs_depied
    else:
        $ i = trs_sitting
    
    if value == 0: #touch hair
        show expression generate_anim3("Joyce/anim/touch-hair/touch-hair (",9, 0.15) at i as anim
        play sound "date/touch_hair.wav"
        pause 0.15*9
        hide anim
        j eyeside blush "..."
        show joyce -eyeside -blush with dissolve
            
    elif value == 1:
        show expression generate_anim3("Joyce/anim/touch-shoulder/touch-shoulder (",4, 0.15) at i as anim
        play sound "date/caress.wav"
        pause 0.15*4
        hide anim
        show expression generate_anim3("Joyce/anim/touch-shoulder/touch-shoulder (",4, 0.15) at i as anim
        pause 0.15*4
        hide anim
        j eyeside blush "..."
        j happy smile blush "Stop, I'm ticklish…!"
        show joyce -happy -smile -blush with dissolve

    elif value == 2:
        show expression generate_anim3("Joyce/anim/touch-face/touch-face (",4, 0.15) at i as anim
        play sound "date/caress.wav"
        pause 0.15*4
        hide anim
        show expression generate_anim3("Joyce/anim/touch-face/touch-face (",4, 0.15) at i as anim
        pause 0.15*4
        hide anim
        j eyeside blush "..."
        j "You have such warm hands."
        show joyce worried bite with dissolve
        pause
        show joyce -eyeside -blush with dissolve

    else:
        show expression generate_anim3("Joyce/anim/touch-boobs/touch-boobs (",10, 0.15) at i as anim
        pause 0.15*4
        play sound "date/caress2.wav"
        pause 0.15*4
        show joyce at shock(renpy.get_image_bounds("joyce")[3] / 1250)
        pause 0.15*2
        hide anim
        j blush defend "Hey!"
        if game.progress[0]<4:
            j foxy smirk "Not in public…"
        else:
            j foxy smirk "Not yet…"
        show joyce -blush -defend with dissolve

    call label_reaction_commonEND("touchy")

label label_reaction_flirt():
    call label_reaction_common("flirt")
    if value == 0 or value == 1:
        menu:
            "I like your dress":
                if game.progress[0] != 3:
                    if date.name == "label_jogging":
                        j eyeside "Em..."
                        j -eyeside "What dress?"
                    else:
                        j blush "..."
                        j smirk "Thanks, I wasn't sure what to wear."
                        j smile "I thought maybe I should wear something more elegant..."
                        j "Then I realized I was running late, so I just put on whatever."
                        j "Haha."
                        show joyce -blush with dissolve
                else:
                    j foxy smirk "Hehe"
                    j "I guess I did pull it off…"
            "I like your hair":
                show joyce null
                j smile "Isn't it a bit boring?"
                j "I have a friend who's always bleaching her hair all the time"
                j "These days she's doing green hair I think"
                j "Do you think it would suit me?"
                show joyce green_hair with dissolve
                pause
                menu:
                    "I can totally see it":
                        j "Green?"
                        j happy "Really?"
                        j "No way! That's so bold. I could never."
                        j "I kinda admire her for that."
                    "Hmm no":
                        j happy "Yeah, I didn't think so either."
                        j "Haha."
                        j -happy "But I kinda admire my friend."
                        j "Would you bleach your hair green?"
                show joyce -green_hair with dissolve
    elif value == 2:
        
        menu:
            "I think you're beautiful":
                j eyeside blush "..."
                j "Don't say that…"
                j "You're making me shy."
                j -eyeside "..."
                j happy smile "You're not bad looking either."
                show joyce -eyeside -bite with dissolve
            "I love being with you":
                j eyeside blush "..."
                j "You're so bold"
                j "..."
                j -blush happy smile "But I also do enjoy our dates together."
                j -eyeside "I hope this will last."
                j tongue -happy  "teehee ~"
                show joyce -tongue with dissolve

    elif value >= 3:
        python:
            if "oncePerDate" not in done_flag:
                done_flag["oncePerDate"] = set()
            outfits = ["outfitred","outfitblue","night","night2","night3","night4"]
            for i in outfits:
                if has_attribute(i):
                    if i in done_flag["oncePerDate"]:
                        renpy.show_screen("screen_date_ui")
                        renpy.with_statement(dissolve)
                        renpy.return_statement()
                    done_flag["oncePerDate"].add(i)

        if value == 3:
            menu:
                "You have a nice figure":
                    "FYNTODO"
                "You have nice boobs":
                    j foxy smirk "Oh? You're pretty bold."
                    j "You like them?"
        else:
            j "You like my boobs?"
            
        j "They're pretty big, right?"
        if not (has_attribute("night3") and has_attribute("night4")):
            j "Here's a peek..."
            show joyce reveal-1 with dissolve
            pause 0.5
            show joyce reveal-2 with dissolve
            pause
            j wink tongue reveal-1 "That's it"
            show joyce -wink -tongue -reveal-1 with dissolve
        else:
            show joyce reveal-2 with dissolve
            j "You wanna lick them?"
            j wink tongue "Slurp slurp"
            j -wink -reveal-2 -tongue smile "Not yet, hehe..."
            show joyce -reveal-2 -smile with dissolve
    call label_reaction_commonEND("flirt")
    return

label label_reaction_eyecontact():
    call label_reaction_common("eyecontact")

    if value == 0:
        show layer master:
            zoom 1.2 xalign 0.5 yalign 0.1
        with dissolve
        pause 0.4
        j "?"
        j "..."
    
    elif value == 1:
        show layer master:
            zoom 1.5 xalign 0.5 yalign 0.1
        with dissolve
        pause 0.4
        j "?"
        j eyeside blush "..."

    elif value == 2:
        show layer master:
            zoom 2.0 xalign 0.5 yalign 0.1
        with dissolve
        pause 0.4
        j blush "..."
        j eyeside "Is there something on my face?"

    elif value == 3:
        show layer master:
            zoom 1.5 xalign 0.5 yalign 0.1
        with dissolve
        pause 0.4
        j blush "..."
        j "Why do you stare at me so often?"
        j "I feel so shy. I'm so bad at keeping eye contact."
        j eyeside "Please, can you look elsewhere?"
        show layer master:
            zoom 2.0 xalign 0.5 yalign 0.5
        with dissolve
        j -eyeside "..."

    elif value == 4:
        show layer master:
            zoom 3.0 xalign 0.5 yalign 0.4
        with dissolve
        pause 0.5
        show layer master:
            zoom 3.0 xalign 0.5 yalign 0.55
        with dissolve
        pause
        j eyeside blush "..."
        j "Do you enjoy looking at me that much?"

    elif value == 5:
        show layer master:
            zoom 3.0 xalign 0.5 yalign 0.55
        with dissolve
        pause 0.4
        j smirk foxy "You like what you see?"
        show layer master:
            zoom 1.0 xalign 0.5 yalign 0.5
        with dissolve
        j worried bite "I bet you wanna see more.."
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0.5
    with dissolve
    call label_reaction_commonEND("eyecontact")
    return