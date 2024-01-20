"""
A bunch of script labels where Joyce talks with you, they are naturally triggered after each turn if theres no dialogue left
"""
default done_flag = {"script":0}
label label_reaction():

    if "script" not in done_flag:
        $ done_flag["script"] = 0

    $ value = done_flag["script"]
    
    if (game.progress[0]+1)*2 <= value:
        return
    elif value>10:
        return

    hide screen screen_date_ui with dissolve

    show joyce null

    if value == 0:
        j eyeside armscrossed "It's getting pretty warm these days."
        j "I'm not such a fan of summer to be honest."
        j "I don't really tan... I get more like sunburns..."
        j "I heard it's because my skin is too thin."
        show joyce null
        j -eyeside smile "Oh well"
        if game.progress[0] < 1:
            j "Nothing like a day at the park to stay fresh."
        elif game.progress[0] < 4: # in case we trigger it on a second date
            j "That's why I like to come here for an afternoon drink."
        j eyes_closed -armscrossed "Though I regret wearing so many layers today."

    if value == 1:
        j "These days I've picked up sudoku again."
        j "I solve puzzle books to pass the time on my morning commute."
        j "That sounds like such a boring hobby, doesn't it?"
        j "What about you, do you like playing games?"
        menu:
            "yes":
                j smile "Oh, you do? That's nice!"
                j "What kind of games do you play?"
            "no":
                j "..."
                j upset "really"
                show joyce -upset
    
    elif value == 2:
        j "So you play dating sims…"
        j "I used to play those on the Nintendo DS too."
        j "What are you playing these days?"
        "..."
        j "What are you getting so shy about?"
        j smile "Come, on tell me!"
        j smile "Alright, but you have to tell me on our next date!"

    elif value == 3:
        j "How often do you meet girls like this?"
        j "I'm just wondering if you're a playboy type."
        j smile "Though you don't seem like one, haha."
        j -smile "I'm personally looking for the one..."
        j "But I have pretty high requirements."
        j foxy smile "Will you pass the test? Hehe, just kidding."

    elif value == 4:
        j smile "I love cats sooo much"
        j "Petting one is soo soothing"
        j "I'm kinda wondering if I should get one"
        j null "But it's a huge responsibility."
    
    elif value == 5:
        j "Cats are also useful against pests."
        j "I've seen some rats in my basement. A cat would be helpful…"
        j smile "Oh yeah, my place has a really huge basement, I'll show you next time!"

    elif value == 6:
        play sound "day/gulp.wav"
        j smile "*slurp*"
        j "Ah! Nothing like alcohol after a rough day!"
        j "I drink occasionally."
        j "And when I mean occasionally, I mean you're my excuse to drink!"

    elif value == 7:
        j "I feel like I want a cat because I'm so lonely at home."
        j happy smile "But with you, maybe I won't need a cat anymore."
        j "Will you cure my loneliness?"
        show joyce -happy -smile with dissolve

    elif value == 8:
        j blush smile "Come on, drink!"
        j "*hic*"
        j "My friends say I'm bad with alcohol."
        j "Fudge them! I can totally drink my own!"
        j "Cheeeers!"
        menu:
            "Drink with her":
                if date.drink>0:
                    play sound "day/gulp.wav"
                    $ date.drink -= 1
                    j "Nice, NICE!"
                    j "You're a jolly fellow!"
                    "+4 attraction"
                    $ date.attraction += 4
                    with dissolve
                else:
                    j "HEY WAIT A MINUTE"
                    j "Your glass is empty!"
                    j "GARCON! BRING THE BOY ANOTHER!"
                    play sound "day/pour-drink.wav"
                    while date.drink<3:
                        $ date.drink += 1
                        with wipeup
                    j "Much better!"
                    j "BOTTOMS UP!!"
            "Maybe you should calm down":
                j "Booo"
                j "You're such a *hic* Joy killer"
                j "Joyce killer?"
                j "HAHAHA"

    elif value == 9:
        j "Wow you play porn games?"
        j "Oh, I'm not judging."
        j smirk "I'm not so innocent either, hehe."
        j "Erotic video games are fun."
        j -smirk "..."
        j foxy blush "But I like more human contact."
        show joyce -foxy -blush with dissolve

    elif value == 10:
        j "*hic* You know."
        j "I'm a *hic* pretty dangerous person."
        j "I may seem frail, or weak."
        j "But don't underestimate me!"
        j "*hic*"

    show screen screen_date_ui with dissolve
    $ done_flag["script"] += 1

return




"""
These scripts are reacting to a card being played
"""

label label_card_reaction(what = None):

    if what == None:
        if hasattr(game.lastPlayed, "name"):
            $ what = game.lastPlayed.name

    if what == "talk2":
        call label_card_reaction("talk") from _call_label_card_reaction_1
        return

    if what not in done_flag:
        $ done_flag[what] = 0

    $ value = done_flag[what]

    if value > game.progress[0]:
        return
    
    if game.state == "sexing":
        $ i = ["eyecontact", "touchy", "flirt", "smalltalk", "talk", "listen"]
        if what in i:
            if done_flag[what] == 99:
                return
            $ i2 = 0 
            while i2<len(i):
                $ done_flag[i[i2]] = 99
                $ i2 += 1
            j "What are you trying to do?"
            j "Building more trust and attraction?"
            j "How is that going to help now?"
            j "I'm playing with your dick and that's the only thing you can think of?"
            j "Hahaha, change the way you play."

        return

    elif game.state == "dating":
        show joyce null with {"master": dissolve}

    if what == "eyecontact":

        if value <= 4:
            hide screen screen_date_ui with dissolve

        if value == 0:
            show layer master:
                zoom 1.5 xalign 0.5 yalign 0.1
            with dissolve
            pause 0.4
            j "..."
            j eyeside blush "..."

        elif value == 1:
            show layer master:
                zoom 2.0 xalign 0.5 yalign 0.1
            with dissolve
            pause 0.4
            j blush "..."
            j eyeside "Is there something on my face?"

        elif value == 2:
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

        elif value == 3:
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

        elif value == 4:
            show layer master:
                zoom 3.0 xalign 0.5 yalign 0.55
            with dissolve
            pause 0.4
            j smirk foxy "You like what you see?"
            show layer master:
                zoom 1.0 xalign 0.5 yalign 0.5
            with dissolve
            j bite "I bet you wanna see more.."
            show joyce -bite with dissolve
        show layer master:
            zoom 1.0 xalign 0.5 yalign 0.5
        with dissolve

    elif what == "touchy":
        if value <= 4:
            hide screen screen_date_ui with dissolve

        if renpy.get_image_bounds("joyce")[1]<55:
            $ i = trs_depied
        else:
            $ i = sitting
        show joyce
        
        if value == 0: #touch hair
            show expression generate_anim3("Joyce/anim/touch-hair/touch-hair (",9, 0.15) at i as anim
            play sound "date/touch.wav"
            pause 0.15*9
            hide anim
            j eyeside blush "..."
            show joyce -eyeside -blush with dissolve
                
        elif value == 1:
            # show layer master:
            #     zoom 1.5 xalign 0.5 yalign 0.3
            # with dissolve
            show expression generate_anim3("Joyce/anim/touch-shoulder/touch-shoulder (",4, 0.15) at i as anim
            play sound "date/caress.wav"
            pause 0.15*4
            hide anim
            show expression generate_anim3("Joyce/anim/touch-shoulder/touch-shoulder (",4, 0.15) at i as anim
            pause 0.15*4
            hide anim
            j eyeside blush "..."
            j foxy blush "Stop, I'm ticklish…!"
            show joyce -foxy -blush with dissolve

            # show layer master:
            #     zoom 1.0 xalign 0.5 yalign 0.5
            # with dissolve

        elif value == 2:
            # show layer master:
            #     zoom 1.5 xalign 0.5 yalign 0.3
            # with dissolve
            show expression generate_anim3("Joyce/anim/touch-face/touch-face (",4, 0.15) at i as anim
            play sound "date/caress.wav"
            pause 0.15*4
            hide anim
            show expression generate_anim3("Joyce/anim/touch-face/touch-face (",4, 0.15) at i as anim
            pause 0.15*4
            hide anim
            j eyeside blush "..."
            j "You have such warm hands."
            show joyce bite with dissolve
            pause
            show joyce -eyeside -blush with dissolve

            # show layer master:
            #     zoom 1.0 xalign 0.5 yalign 0.5
            # with dissolve

        elif value == 3 or value == 4:
            # show layer master:
            #     zoom 1.5 xalign 0.5 yalign 0.3
            # with dissolve
            show expression generate_anim3("Joyce/anim/touch-boobs/touch-boobs (",10, 0.15) at i as anim
            pause 0.15*4
            play sound "date/caress2.wav"
            pause 0.15*4
            show joyce at shock(renpy.get_image_bounds("joyce")[3] / 1140)
            pause 0.15*2
            hide anim
            j blush defend "hey"
            if game.progress[0]<4:
                j foxy smirk "Not in public…"
            else:
                j foxy smirk "Not yet…"
            show joyce -blush -defend with dissolve

    elif what == "flirt":

        if value == 0 or value == 1:
            hide screen screen_date_ui with dissolve
            menu:
                "I like your dress":
                    if game.progress[0] != 3:
                        j blush "..."
                        j "Thanks, I wasn't sure what to wear."
                        j smile "I thought maybe I should wear something more elegant…"
                        j "Then I realized I was running late, so I just put on whatever."
                        j "haha"
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
                        "oh yea big time":
                            j "Green?"
                            j "Really?"
                            j "No way! That's so bold. I could never."
                            j "I kinda admire her for that."
                        "hmm no":
                            j "Yeah, I didn't think so either."
                            j "haha."
                            j "But I kinda admire my friend."
                            j "Would you bleach your hair green?"
                    show joyce -green_hair with dissolve
        elif value == 2:
            hide screen screen_date_ui with dissolve
            menu:
                "I think you're beautiful":
                    j eyeside blush "..."
                    j "Don't say that…"
                    j "You're making me shy"
                    j -eyeside "..."
                    j eyeside bite "You're not bad looking either"
                    show joyce -eyeside -bite with dissolve
                "I love being with you":
                    j eyeside blush "..."
                    j "You're so bold"
                    j "..."
                    j -blush happy smile "But I also do enjoy our dates together."
                    j -eyeside "I hope this will last"
                    j tongue -happy  "teehee ~"
                    show joyce -tongue with dissolve

        elif value == 3:
            python:
                if "flirt_done" not in done_flag:
                    done_flag["flirt_done"] = set()
                outfits = ["outfitred","outfitblue","night","night2","night3","night4"]
                for i in outfits:
                    if i in renpy.get_attributes("joyce"):
                        if i in done_flag["flirt_done"]:
                            renpy.show_screen("screen_date_ui")
                            renpy.with_statement(dissolve)
                            renpy.return_statement()
                        done_flag["flirt_done"].add(i)
            
            hide screen screen_date_ui with dissolve
            menu:
                "You have nice boobs":
                    j foxy smirk "You like them?"
                    j "They're pretty big, right?"
                    if "night3" not in renpy.get_attributes("joyce") and "night4" not in renpy.get_attributes("joyce"):
                        j "Here's a peek…"
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
                        j -wink -reveal-2 -tongue smile "Not yet, hehe…"
                        show joyce -reveal-2 -smile with dissolve
            $ done_flag[what] -= 1

    show screen screen_date_ui with dissolve
    $ done_flag[what] += 1
        
    return