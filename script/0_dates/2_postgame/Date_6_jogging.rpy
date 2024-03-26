#hey
# is it ok if we talk?

#im sorry

#wanna meet again?

label label_jogging:
    scene bg chemin-0 at trs_bg_blur(2, "soft")
    show joyce outfitsport smile at trs_depied
    j wave "Heey [povname]!"
    j -wave "It's been a while!"
    j happy "Did you miss me?"
    menu:
        "Yes":
            j -happy foxy "Hehe."
            j -foxy smirk "Sorry, I've been busy with work."
            j "But we'll spend a lot of time together again."
            j happy "I hope you're excited!"
        "No":
            j moue surprised "..."
            j "Oh no, I'm so sad."
            j -moue smile foxy "Kidding."
            j "I know you ran over here boy."
            j -foxy "It's ok, we'll spend lot of time together again."
    j null "Come on, let's do some sport for once!"
    j running smile "Let's run to the lake!"
    j "I know a nice running trail."
    play sound "day/run.wav"
    pause 0.3
    show bg chemin-1 at trs_bg_blur() with Dissolve(1.0)
    j upset smirk "The first to arrive can order the other around!"
    show joyce breath with dissolve
    $ objectif_trust = game.trust + 10
    $ objectif_attraction = game.attraction + 10
    $ date = Date("date", name="jogging", objectif_trust = objectif_trust, objectif_attraction = objectif_attraction, turnLeft = 8, isWin="date.turnLeft == 0", isLost="len(deck.deck) == 0 or (date.lust > date.trust and date.lust > date.attraction)", neutralJoyce = "joyce null_eyes breath running")
    call label_beginDuel_common() 

    # hide screen screen_date_ui with dissolve
    # call label_add_card_to_deck("hand", Card("peek"+whichDress),pauseTime = 0.5)

    call label_gameLoop()

label label_jogging_endTurn:
    
    play sound "day/run.wav"
    pause 0.3
    if date.turn >= 1:
        show expression "bg chemin-"+str(date.turn+1) as bg at trs_bg_blur(2) with Dissolve(1.0)

    call label_add_card_to_deck("hand", Card("tired"),pauseTime = 0.5)
    python:
        i = 0
        for card in deck.hand:
            if card.name == "tired":
                i+=1
    if i >= 5:
        jump label_Lost_common

    
    if date.turn == 2:
        j sweaty "You holding up?"
        j smile "There's still a long way to go!"
        $ date.neutralJoyce = "joyce sweaty null_eyes breath running"
    elif date.turn == 4:
        j bored mouthopen sweaty2 "Phew, I'm so sweaty!"
        show joyce foxy with dissolve
        j "Hold on."
        play sound "sex/undress2.wav"
        show joyce undress with dissolve
        pause 1.0
        show joyce outfitsport2 -undress with dissolve
        j smile null_eyes "Ah! Much better."
        "..."
        "You get a bit excited"
        "Lust +15"
        $ date.increment("lust", 15)
        j running "Let's keep going."
        $ date._isLost = "date.turn > 4 and (len(deck.deck) == 0 or (date.lust > date.trust and date.lust > date.attraction))"
    return

label label_jogging_Lost:    
    python:
        i = 0
        for card in deck.hand:
            if card.name == "tired":
                i+=1
    pause
    if i >= 5:
        call label_jogging_Lost_tired
    else:
        call label_reaction_default_Lost
    return

label label_jogging_Win:
    if date.trust >= objectif_trust and date.attraction >= objectif_attraction:
        j "Oh it's just ahead."
        j smile "You're not getting there before me!"
        play sound "day/run.wav"
        pause 0.3
        hide joyce with dissolve
        pause
        play sound "day/run.wav"
        pause 0.3
        show bg chemin-10 at trs_bg_blur(2) with dissolve
        pause
        play sound "day/run.wav"
        pause 0.3
        show bg chemin-11 at trs_bg_blur(2) with dissolve
        pause
        "Joyce is looking at the lake."
        show joyce outfitsport3 smile at trs_depied with dissolve
        pause
        "!"
        j armhip "Phew! Finally here."
        j happy "Isn't the view great?"
        j -happy "?"
        j blush smirk "..."
        j -armhip foxy "Are you even looking at the lake?"
        j eyesdown showboobs "Oh yea these?"
        j -eyesdown "I was still hot, so I removed an extra layer."
        j foxy "You don't mind right?"
        j -showboobs "It's fine, there's no one around."
        j "Just us."
        j wink tongue "By the way, remember the bet we did?"
        j "The one to arrive last has to listen to the other."
        j -wink -tongue "And I just have the idea what I want you to do."
        j foxy smirk "[povname], lie down."

        call label_cowgirl2
    else:
        j "We're here!"
        j "Isn't it pretty?"
        "..."
        "(It's pretty awkward.)"
        "(You feel like there's still a distance between you two.)"
        "(Maybe you should have built trust and attraction more this date?)"
        j smile "Let's head back?"
        hide joyce with dissolve
    return

label label_jogging_Lost_tired:
    j surprised wave "Hey, are you ok?"
    mc "*Huff* *Huff*"
    mc "Yea... I'm..."
    mc "Fine..."
    j worried smirk "Maybe let's stop there."
    j "We can always do that next time."
    hide joyce with dissolve
    return
    