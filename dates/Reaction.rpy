label label_reaction():

    if "script" not in done_flag:
        $ done_flag["script"] = 0

    $ value = done_flag["script"]
    
    $ print( str((game.progress[0]+1)*2))
    $ print( str(done_flag["script"]))

    if (game.progress[0]+1)*2 <= value:
        return

    hide screen screen_date_ui with dissolve

    show joyce null with dissolve

    if value == 0:
        j eyesside armscrossed "It's getting pretty warm these days."
        j "I'm not such a fan of summer to be honest."
        j "I easily get sunburns because my skin is too thin."
        show joyce null
        j -eyesside smile "Oh well"
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
            if any("dream" in tag for tag in renpy.get_attributes("joyce")) or game.progress[0]>7:
                pass
            else:
                show joyce eyesside blush with dissolve
            pause
            j "..."
            j eyesside "Is there something on my face?"

        elif value == 1:
            show layer master:
                zoom 2.0 xalign 0.5 yalign 0.1
            with dissolve
            pause 0.4
            j blush "..."
            j "Why do you stare at me so often?"
            j "I feel so shy. I'm so bad with keeping eyecontact."

        elif value == 2:
            show layer master:
                zoom 2.0 xalign 0.5 yalign 0.1
            with dissolve
            pause 0.4
            j blush "..."
            j "Do you enjoy looking at me that much?"
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
            j eyesside blush "..."

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

        if value == 0: #touch hair
            
            show expression generate_anim3("Joyce/anim/touch-hair/touch-hair (",9, 0.15) at sitting as anim
            play sound "date/touch.wav"
            pause 0.15*9
            hide anim
            j eyesside blush "..."
            show joyce -eyesside -blush with dissolve
                
        elif value == 1:
            # show layer master:
            #     zoom 1.5 xalign 0.5 yalign 0.3
            # with dissolve
            show expression generate_anim3("Joyce/anim/touch-shoulder/touch-shoulder (",4, 0.15) at sitting as anim
            play sound "date/caress.wav"
            pause 0.15*4
            hide anim
            show expression generate_anim3("Joyce/anim/touch-shoulder/touch-shoulder (",4, 0.15) at sitting as anim
            pause 0.15*4
            hide anim
            j eyesside blush "..."
            show joyce -eyesside -blush with dissolve

            # show layer master:
            #     zoom 1.0 xalign 0.5 yalign 0.5
            # with dissolve

        elif value == 2:
            # show layer master:
            #     zoom 1.5 xalign 0.5 yalign 0.3
            # with dissolve
            show expression generate_anim3("Joyce/anim/touch-face/touch-face (",4, 0.15) at sitting as anim
            play sound "date/caress.wav"
            pause 0.15*4
            hide anim
            show expression generate_anim3("Joyce/anim/touch-face/touch-face (",4, 0.15) at sitting as anim
            pause 0.15*4
            hide anim
            j eyesside blush "..."
            show joyce -eyesside -blush with dissolve

            # show layer master:
            #     zoom 1.0 xalign 0.5 yalign 0.5
            # with dissolve

        elif value == 3 or value == 4:
            # show layer master:
            #     zoom 1.5 xalign 0.5 yalign 0.3
            # with dissolve
            show expression generate_anim3("Joyce/anim/touch-boobs/touch-boobs (",10, 0.15) at sitting as anim
            pause 0.15*4
            play sound "date/caress2.wav"
            pause 0.15*4
            show joyce at shock
            pause 0.15*2
            hide anim
            j blush defend "hey"
            if game.progress[0]<4:
                j "Not in public.."
            else:
                j "Not yet.."
            show joyce -blush -defend with dissolve

    elif what == "flirt":
        if value == 0 1:
            menu:
                "You have beautiful eyes":
                    j "oh"
                "I love your smile":
                    j "oh"
        elif value == 2 3:
            menu:
                "You have huge boobs":
                    j "oh"
                "I love your smile":
                    j "oh"




    $ done_flag[what] += 1
        
    return