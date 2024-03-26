"""
A bunch of script labels where Joyce talks with you, they are naturally triggered after each turn if theres no dialogue left
"""
default done_flag = {"buttons":Set(),"seen_labels":Set(),"oncePerDate":Set(),"ask":[0,1,2]}


label label_reaction_check_if_sex(card = None):

    if game.state == "sexing" and "label_reaction_check_if_sex" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("label_reaction_check_if_sex")
        j "What are you trying to do?"
        j "Building more trust and attraction?"
        j "How is that going to help now?"
        j "I'm playing with your dick and that's the only thing you can think of?"
        j "Hahaha, change the way you think."
    return


"""
label_reaction_common is played before each cutscene
"""

label label_reaction_common(what = None):
    if what == None:
        if hasattr(date.lastPlayed, "name"):
            $ what = date.lastPlayed.name
    hide screen screen_date_ui with dissolve
    
    call label_reaction_check_if_sex()
    
    if game.state == "sexing":
        # ugly double jump lol???
        $ renpy.pop_call()
        # $ renpy.pop_return()
        return
    
    if what not in done_flag:
        $ done_flag[what] = 0

    $ value = done_flag[what]
    
    show joyce null with {"master": dissolve}
    return

label label_reaction_commonEND(what):
    show screen screen_date_ui with dissolve
    $ done_flag[what] += 1
    return

init python:
    def get_ask_question():
        global i 
        i+=1
        if i in done_flag["ask"]:
            return True
        else:
            return False

    def update_ask_question(index):
        # change the index of the bubble that contains question INDEX with max +1 
        done_flag["ask"][done_flag["ask"].index(index)] = max(done_flag["ask"]) + 1

label label_reaction_undress():
    show joyce 1 with dissolve
    j "You want to see my body?"
    j "I'm a bit shy, how about you close your eyes?"

    show black onlayer screens with dissolve
    $ date.naked = True
    
    show joyce naked
    pause 0.2
    play sound "sex/undress.wav"
    pause 1.0
    hide black onlayer screens with dissolve
    j "How do you like it?"
    show joyce -1
    return

label label_date_Lost_lust:
    $ what = "isLost_lust"
    if what not in done_flag:
        $ done_flag[what] = 0
    $ what = done_flag[what]
    if date.name == "stripPoker":
        if game.progress[1]<3:
            j foxy armscrossed "You're getting a bit too horny, aren't you?"
            j smile "Seems like today's not your day."
            j tongue "Hehe, try next time. "
            j smirk "My door is always open for you."
        else:
            j foxy armscrossed "Ooh bad play."
            j smile "You should take your time."
            j "You don't need to burst everything in one go."
            j "Just focus on each step, one at a time."
            j wink tongue "Big boy."

    if what == 0:
        j armscrossed upset "Um... don't you think I can notice?"
        j "Sorry but I'm gonna go. I'm really not in the mood today."
        j "Let's do this another day."
    elif what == 1:
        j "Em.."
        j "The way you're looking at me... with those eyes..."
        j "You thought I didn't notice?"
        j "Let's do this another time when you have cooled off?"
    elif what == 2:
        j "Where are you looking?"
        j "You've just been staring at my body..."
        j "It's flattering but..."
        j "Let's end it there for today, okay?"
    elif what == 3:
        j eyesdown "..."
        j -eyedown "..."
        j eyesdown blush "..."
        j -eyedown "..."
        j "[povname].."
        j "Your pants..."
        j "There's a bulge in your pants."
        j "Maybe we should, um.."
        j "Do this another day? Even I can't focus..."
    elif what == 3:
        j blush "Oh my god, are you getting hard again?"
        j "How are you getting hard just from talking with me?"
        j "Do you want to go to the bathroom?"
        j "Release your tension, or something..."
        j "Masturbate."
        j "Em forget what I said..."
        j "I said too much."
        j "Let's stop here? I need some air..."
    
    elif what == 4:
        j "[povname] you look like you're trying so hard."
        j "I can see it in your eyes."
        j "You want to jump me so bad."
        j "You're going to devour me."
        j "Kyaa I'm so scared, I want to run awaaay."
        j "Heehee, [povname], you should be more gentleman-ly."
        j "Let's stop here for now shall we?"
        j "We can try again another time... [povname]..."

    elif what == 5:
        j "What's in your mind?"
        j "What have you been thinking?"
        j "Hmm let me guess..."
        j "You just wanna rip off my clothes and see what's under, right?"
        j "Heehee, you're so transparent [povname]."
        j "But not yet... you're not there yet."
        j "I'll need you to try just a little bit harder."

    elif what >= 6:
        j "You're being a bit... too pushy [povname]."
        j "I love dating you [povname]."
        j "But it's not fun if it's too easy."
        j "Bear it a little more, I know you can do it."
        j "You'll get your reward eventually."
        "(zoom master layer)"
        j "whisper (you'll get to fuck my body)"
        j "See you next time."


label label_reaction_default_Lost():
    if date.lust > date.trust and date.lust > date.attraction:
        jump label_date_Lost_lust

    if len(deck.deck) == 0:
                j eyeside armscrossed "..."
                j "Seems like you've run out of things to say."
                j "I guess the date's over then..."
                j "Next time, think about other topics to talk about."
                    
    elif date.turnLeft <= 1:
        if game.progress[0]<4:
            j eyeside armscrossed "Oh, look at the time!"
            j "Sorry, I gotta go."
            j "That kinda dragged on anyway, right?"
            j "Maybe we can do this another day? See ya."
        else:
            if game.progress[1]<3:
                j foxy armscrossed "Oh, look at the time!"
                j smile "Seems like today's not your day."
                j tongue "Hehe, try next time."
                j smirk "My door is always open for you."
            else:
                j foxy armscrossed "Ooh time's up."
                j smile "You should take your time."
                j "You don't need to burst everything in one go."
                j "Just focus on each step, one at a time."
                j wink tongue "Big boy."

    hide joyce with dissolve
    
    return