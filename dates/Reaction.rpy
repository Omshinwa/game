label label_reaction():

    if "script" not in done_flag:
        $ done_flag["script"] = 0

    $ value = done_flag["script"]
    
    if (game.progress[0]+1)*2 <= value:
        return
    elif value>8:
        return

    hide screen screen_date_ui with dissolve

    show joyce null with dissolve

    if value == 0:
        j eyeside armscrossed "It's getting pretty warm these days."
        j "I'm not such a fan of summer to be honest."
        j "I easily get sunburns because my skin is too thin."
        show joyce null
        j -eyeside smile "Oh well"
        if game.progress[0] < 1:
            j "Nothing like a day at the park to stay fresh."
        elif game.progress[0] < 4: # in case we trigger it on a second date
            j "That's why I enjoy coming here to get a drink."
        j -armscrossed "Though I regret wearing so many layers today."

    if value == 1:
        j "These days I have picked sudoku again."
        j "I play it during my offtime."
        j "That seems like such a boring activity no?"
        j "What about you, do you like playing games?"
        menu:
            "yes":
                j smile "Oh you do? That's nice!"
                j "What kind of games do you play?"
            "no":
                j "..."
                j upset "really"
                show joyce -upset
    
    elif value == 2:
        j "So you play dating sims."
        j "I used to play some on the Nintendo DS too."
        j "What are you playing these days?"
        "..."
        j "What are you getting so shy about?"
        j smile "Come on tell me!"
        j smile "Alright you better tell me next date!"

    elif value == 3:
        j "How often do you meet girls like that?"
        j "I'm trying to look for the one."
        j "But I have pretty high requierements"
        j foxy smile "Will you pass the tests? I wonder heehee."

    elif value == 4:
        j smile "I loves cats sooo much"
        j "Petting one is soo soothing"
        j "I'm kinda wondering if I should get one"
        j null "But it's a big responsability still."
    
    elif value == 5:
        j "Cats are also useful for pests."
        j "I've seen some rats in my basement. A cat would be a good help"
        j "My place has a pretty big basement, I could show you!"

    elif value == 6:
        j "I feel like I want a cat because I'm so lonely at home."
        j happy smile "But with you, maybe I won't need a cat anymore."
        j "Will you cure my loneliness?"
        show joyce -happy -smile with dissolve

    elif value == 7:
        j "Wow you play erotic games?"
        j "No I'm not judging."
        j smirk "I'm not too innocent either hehe."
        j "Erotic video games are fun."
        j -smirk "..."
        j foxy blush "But I like it more in real life."
        show joyce -foxy -blush with dissolve

    elif value == 8:
        j "Maybe you can show me what kind of erotic games you like."
        j "Show me what you like."

    show screen screen_date_ui with dissolve
    $ done_flag["script"] += 1

return


default done_flag = {"script":0, "thisTurn":set()}

label label_card_reaction(what = game.lastPlayed.name):


    if what == "talk2":
        call label_card_reaction("talk")
        return

    if what not in done_flag:
        $ done_flag[what] = 0

    $ value = done_flag[what]

    if value > game.progress[0]: # or what in done_flag["thisTurn"]:
        return
    
    #$ done_flag["thisTurn"].add(what) 
    
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
            j "You should get rid of those useless cards."

        return

    if game.state == "dating":
        show joyce null with dissolve

    if what == "eyecontact":
        
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
            j "I feel so shy. I'm so bad with keeping eyecontact."
            j eyeside "Can you look elsewhere at least?"
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
            j smirk foxy "You like what you're looking at?"
            show layer master:
                zoom 1.0 xalign 0.5 yalign 0.5
            with dissolve
            j bite "I bet you wanna see more.."
            show joyce -bite with dissolve
        show layer master:
            zoom 1.0 xalign 0.5 yalign 0.5
        with dissolve

    elif what == "touchy":
        if renpy.get_image_bounds("joyce")[1]<55:
            $ i = depied
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
            j foxy blush "Stop, I'm ticklish"
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
                j foxy smirk "Not in public.."
            else:
                j foxy smirk "Not yet.."
            show joyce -blush -defend with dissolve

    elif what == "flirt":
        if value == 0 or value == 1:
            menu:
                "I like your dress":
                    if game.progress[0] != 3:
                        j blush "..."
                        j "Thanks, I wasn't sure what to wear."
                        j smile "Should I wear something more casual or not."
                        j "Then I noticed there was only 30 minutes left so I just picked whatever."
                        j "haha"
                        show joyce -blush with dissolve
                    else:
                        j foxy smirk "Hehe"
                        j "I guess I did pull it off"
                "I like your hair":
                    show joyce null
                    j smile "Isn't it a bit boring?"
                    j "I have a friend that's always bleaching their hair all the time"
                    j "Nowadays she has green hair I think"
                    j "Do you think it would suit me?"
                    show joyce green_hair with dissolve
                    pause
                    menu:
                        "oh yea big time":
                            j "Green?"
                            j "Really?"
                            j "No way that's so bold. I could never."
                            j "I kinda admire my friend."
                        "hmm no":
                            j "Yea I don't think either."
                            j "haha."
                            j "But I kinda admire my friend."
                            j "Would you bleach your hair green?"
                    show joyce -green_hair with dissolve
        elif value == 2:
            menu:
                "I think you're beautiful":
                    j eyeside blush "..."
                    j "Don't say that"
                    j "You're making me shy"
                    j -eyeside "..."
                    j eyeside bite "You're not bad looking either"
                    show joyce -eyeside -bite with dissolve
                "I love being with you":
                    j eyeside blush "..."
                    j "You're so bold"
                    j "..."
                    j -blush happy smile "But I also do enjoy our dates together."
                    j -eyeside "I hope that will last"
                    j tongue -happy  "teehee"
                    show joyce -tongue with dissolve

        elif value == 3:
            python:
                if "flirt_done" not in done_flag:
                    done_flag["flirt_done"] = set()
                outfits = ["outfitred","outfitblue","night","night2","night3","night4"]
                for i in outfits:
                    if i in renpy.get_attributes("joyce"):
                        if i in done_flag["flirt_done"]:
                            renpy.return_statement()
                        done_flag["flirt_done"].add(i)
            menu:
                "You have nice boobs":
                    j foxy smirk "You like them?"
                    j "They are pretty big"
                    if "night3" not in renpy.get_attributes("joyce") and "night4" not in renpy.get_attributes("joyce"):
                        j "Here's a peek"
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
                        j -wink -reveal-2 -tongue smile "Not yet hehe."
                        show joyce -reveal-2 -smile with dissolve
            $ done_flag[what] -= 1




    $ done_flag[what] += 1
        
    return