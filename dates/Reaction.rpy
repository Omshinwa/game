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
        j "But I have pretty strange tastes"
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

    elif what == "eyecontact":
        
        show layer master:
            zoom 2.0 xalign 0.5 yalign 0.1
        with dissolve
        pause

        if value == 0:
            j "..."
            if any("dream" in tag for tag in renpy.get_attributes("joyce")) or game.progress[0]>7:
                j "hey"
            else:
                j eyesside blush "hey"
        elif value == 1:
            j "Why do you stare at me so often?"
            j "I feel so shy."
        elif value == 2:
            j "You enjoy what you're seeing?"
            j "I bet you wanna see more"

        show layer master:
            zoom 1.0 xalign 0.5 yalign 0.5
        with dissolve

    $ done_flag[what] += 1
        
    return