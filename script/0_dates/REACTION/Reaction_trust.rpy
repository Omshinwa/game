# postgame
# isnt it weird seeing each others like that now?
# i mean, in a normal setting?
# i just cant stop imagining you naked
# fucking me again
# hehe


#############################################################################
##
##
#           :::      ::::::::  :::    ::: 
#         :+: :+:   :+:    :+: :+:   :+:  
#        +:+   +:+  +:+        +:+  +:+   
#       +#++:++#++: +#++:++#++ +#++:++    
#       +#+     +#+        +#+ +#+  +#+   
#       #+#     #+# #+#    #+# #+#   #+#  
#       ###     ###  ########  ###    ### 
##
##
#############################################################################

label label_reaction_ask(): #ASK
    call label_reaction_common("ask")
    $ i = -1 #track the number of questions youre asking
    menu:
        "Do you often go on dates?" if get_ask_question():
            $ update_ask_question(0)
            j "Mhhh..."
            j blush "I'm embarassed to say it."
            j happy smirk "I'm personally looking for my soulmate."
            j -happy smile "Is it cheesy to say that?"
            j "But I have pretty high requirements."
            j happy "Or more like weird tastes, haha."
            j foxy "Will you pass the test? Hehe, just kidding."

        "What do you do in your free time?" if get_ask_question():
            $ update_ask_question(1)
            j "I told you I've been a real sudoku fanatic right?"
            j "Besides that, I'm working part-time."
            j "It's at a casino."
        "What else do you do during your free time?" if get_ask_question():
            $ update_ask_question(1)
            j "Well my work is taking quite some time"
            j "On my days off... I just meet you."
        "What is your favorite sex position?" if get_ask_question():
            j blush "..."
            j "I like being on top."
            j "but i think my tastes are changing"
            j "maybe i wanna be dominated now"
            $ update_ask_question(2)
            j "I'm embarassed to say it."
            j "But let's say I've been looking for the one."
        "What is your favorite fromage?" if get_ask_question():
            $ update_ask_question(3)
            j "Mhhh..."
            j "I'm embarassed to say it."
            j "But let's say I've been looking for the one."
        "So, are we a couple now?" if get_ask_question():
            $ update_ask_question(4)
            j "Do i scare you?"
            j "You gotta love all of me."
            j "I'll tell you about our situation at the end of the date."
        "5" if get_ask_question():
            $ update_ask_question(5)
        "6" if get_ask_question():
            $ update_ask_question(6)
        "7" if get_ask_question():
            $ update_ask_question(7)
        "X":
            pass

    show screen screen_date_ui with dissolve
    return



label label_reaction_listen():
    jump label_reaction_chat

label label_reaction_chat():
    call label_reaction_common("chat")

    if (game.progress[0]+1)*2 <= value:
        return

    hide screen screen_date_ui with dissolve
    show joyce null with {"master": dissolve}
    if value == 0:
        j smile "It's getting pretty warm these days."
        j eyeside armscrossed -smile "But to be honest I don't like summer too much."
        j "When I try to tan, I just get sunburns..."
        j -armscrossed smile happy "I think it's because my skin is too thin."
    if value == 10:
        j "Another reason I don't like summer."
        j "It just gets so hot you know?"
        j "I regret wearing so many layers today."
        j -eyeside smile "Oh well."
        if game.progress[0] < 1:
            j "Nothing like a day at the park to stay fresh."
    elif value == 1:
        j "These days I've picked up sudoku again."
        j smile "I used to only play it to pass the time on my morning commute."
        j happy "But now I've realized I do it even when I'm home."
        j -happy "That sounds like such a boring hobby, doesn't it?"
        
    elif value == 2:
        j "What about you, do you like playing games?"
        menu:
            "Yes":
                j smile "Oh, you do? That's nice!"
                j "What kind of games do you play?"
            "No":
                j "Oh."
                j upset "That's disappointing."
                show joyce -upset
    
    elif value == 2:
        j "So you play dating sims..."
        j "I used to play those on the Nintendo DS too."
        j "What are you playing these days?"
        "..."
        j smile "What are you getting so shy about?"
        j smile "Come, on tell me!"
        menu:
            "I will tell you next time...":
                j upset -smile "Oh what? Come on."
                j -upset "Alright."
                j smile "But you have to tell me on our next date!"
            "I play adult dating sims":
                j -smile  "Adult...?"
                j worried blush "Like, with naked people?"

    elif value == 3:
        j "How often do you meet girls like this?"
        j "I'm just wondering if you're a playboy type."
        j smile "Though you don't seem like one, haha."

    elif value == 4:
        j smile "I love cats sooo much"
        j "Petting one is soo soothing"
        j "I'm kinda wondering if I should get one"
        j null "But it's a huge responsibility."
    
    elif value == 5:
        j "Cats are also useful against pests."
        j "I've seen some rats in my basement. A cat would be helpful."
        j smile "Oh yeah, my place has a really huge basement, I'll show you next time!"

    elif value == 6:
        pass

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
        j "So you play porn games?"
        j "Oh, I'm not judging."
        j smirk "I'm not so innocent either, hehe."
        j happy smile "I actually think I played some..."
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

    call label_reaction_commonEND("chat")

    return

