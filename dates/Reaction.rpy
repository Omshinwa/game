label label_reaction():

    if "script" not in done_flag:
        $ done_flag["script"] = 0

    $ value = done_flag["script"]
    
    $ print( str((game.progress[0]+1)*2))
    $ print( str(done_flag["script"]))

    if (game.progress[0]+1) <= value:
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
        j smile "I loves cats sooo much"
        j "Petting one is soo soothing"
        j "I'm kinda wondering if I should get one"
        j null "But it's a big responsability still."
    elif value == 3:
        j "How often do you meet girls like that?"
        j "I'm trying to look for the one."
        j "But I have pretty high requierements"
        j "Will you pass the tests? I wonder heehee."
    elif value == 4:
        j "So you play dating sims."
        j "That's a little funny, I didn't expect it."
        j "I used to play some on the Nintendo DS too."
        j "What are you playing these days?"
        j "What are you getting so shy about?"
        j "Come on tell me!"
    elif value == 5:
        j "Cats are also useful for pests."
        j "I've seen some rats in my basement. A cat would be a good help"
        j "My place has a pretty big basement, I could show you!"
    elif value == 6:
        j "Wow you play erotic games?"
        j "Nah I get it, I've played some crazy stuff too."
        j "..."
        j "But I like it more in real life."
    elif value == 7:
        j "I feel like I want a cat because I'm so lonely at home."
        j "But with you, maybe I won't need a cat anymore."
        j "Will you cure my loneliness?"
    elif value == 8:
        j "Maybe you can show me what kind of erotic games you like."
        j "Show me what you like."

    show screen screen_date_ui with dissolve
    $ done_flag["script"] += 1

return


default done_flag = {"script":0}

label label_card_reaction(what = game.lastPlayed.name):
    
    if what == "talk2":
        call label_card_reaction("talk")
        return

    if what not in done_flag:
        $ done_flag[what] = 0

    $ value = done_flag[what]

    if value > game.progress[0] :
        return
    
    if game.state == "sexing":
        if what == "eyecontact" or what == "touchy" or what == "flirt" or what == "smalltalk" or what == "talk" or what == "listen":
            if done_flag[what] == 99:
                return
            $ done_flag[what] = 99
            j "What are you trying to do?"
            j "Building more trust and attraction?"
            j "How is that going to help now?"
            j "Those cards are all useless now"
            j "Hahaha"
        
    elif what == "eyecontact":
        
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
                zoom 2.0 xalign 0.5 yalign 0.1
            with dissolve
            pause 0.4
            j blush "..."
            j "Why do you stare at me so often?"
            j "I feel so shy. I'm so bad with keeping eyecontact."
            j "Can you look elsewhere besides my eyes at least?"
            show layer master:
                zoom 4.0 xalign 0.5 yalign 0.3
            with dissolve
            j "..."

        elif value == 3:
            show layer master:
                zoom 4.0 xalign 0.5 yalign 0.3
            with dissolve
            pause 0.5
            show layer master:
                zoom 3.0 xalign 0.5 yalign 0.65
            with dissolve
            pause
            j eyeside blush "..."
            j "Do you enjoy looking at me that much?"

        elif value == 4:
            show layer master:
                zoom 3.0 xalign 0.5 yalign 0.65
            with dissolve
            pause 0.4
            j smirk foxy "You enjoy what you're seeing?"
            show layer master:
                zoom 1.0 xalign 0.5 yalign 0.5
            with dissolve
            j "I bet you wanna see more.."

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
            show joyce -eyeside -blush with dissolve

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
                j "Not in public.."
            else:
                j "Not yet.."
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
                "I love your smile":
                    j eyeside blush "..."
                    j -blush foxy smile "Like this?"
                    j "What do you like about it?"
                    menu:
                        "Your lips":
                            pass
                        "You teeth":
                            pass
                    j "Oh I see"
                    j "What about my tongue?"
                    j tongue "..."
                    j -foxy smile "haha"
        elif value == 3:
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
                        j wink reveal-1 "That's it"
                        show joyce -wink -reveal-1 with dissolve
                    else:
                        show joyce reveal-2 with dissolve
                        j "You wanna lick them?"
                        j wink tongue "Slurp slurp"
                        j -wink -reveal-2 -tongue smile "Not yet hehe."
                        show joyce -reveal-2 -smile with dissolve
            $ done_flag[what] -= 1




    $ done_flag[what] += 1
        
    return