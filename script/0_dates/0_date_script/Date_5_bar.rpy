
label label_barDate:
    $ date = Date("date", objectif_trust = 32, objectif_attraction = 32, turnLeft = 7, endTurn = "label_barDate_endTurn")
    scene bg bar
    show fg bar-table onlayer master zorder 2

    
    if game.progress[1]<0:
        if whichDress == "red":
            show joyce outfitred at trs_depied onlayer master zorder 2
        else:
            show joyce outfitblue at trs_depied onlayer master zorder 2
            $ g.phoneLogs[7][0] = [1, "pic5-blue.png"]
        with dissolve
    
        j smile "Heey [povname]~"
        j eyeside "Wow… This place is so nice!"
        j -eyeside "Come on, let's get some seats and something to drink haha!"

        if whichDress == "red":
            show joyce outfitred at trs_sitting onlayer master zorder 0 
        else:
            show joyce outfitblue at trs_sitting onlayer master zorder 0 
        with dissolve
        
        pause
        show screen screen_glass("bar") onlayer master zorder 2
        play sound "day/put_on_table.wav"
        pause
        j "Ah, a nice gin tonic."
        with dissolve
    else:
        show screen screen_glass("bar") onlayer master zorder 2

        if whichDress == "red":
            show joyce outfitred at trs_sitting onlayer master zorder 0 
        else:
            show joyce outfitblue at trs_sitting onlayer master zorder 0 
        with dissolve
        j smile "Hurry! Let's party!"
        show joyce foxy

    show layer master:
        zoom 1.5 xalign 0.5 yalign 0.65
    with dissolve
    pause 0.4
    j smirk foxy "Hey, my eyes are up there."
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0.5
    with dissolve

    call label_beginDuel_common() from _call_label_beginDuel_common_3

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                
                if game.progress[1]<=2:
                    call label_barDate_event

                call label_after_successful_Date_common from _call_label_after_successful_Date_common_3

                j smile "That was a beautiful evening"
                j "I'll be thinking about you tonight."
                j "See you soon."
                call label_newDay("label_home")
    
        show joyce null with Dissolve(0.1)
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_4

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_barDate_endTurn:
    call label_endTurn_common
    call label_date_isLost_common from _call_label_date_isLost_common_3
    if date.turn == 2 and game.progress[1]<=2:
        call label_barDate_event

    call label_add_card_to_deck("hand", Card("peek"+whichDress),pauseTime = 0.5) from _call_label_add_card_to_deck_7

    return

label label_barDate_event:
    hide screen screen_date_ui with dissolve
    j "Sorry, I have to use the restroom…"
    show joyce at trs_standing with dissolve
    pause 0.5
    hide joyce with dissolve
    pause 
    play sound "day/newmsg.wav"
    pause
    "?"
    show screen screen_home_phone onlayer master zorder 2
    $ g.phoneProgress[0] += 1
    $ g.phoneProgress[1] = 0
    
    $ game.jeu_sensitive = True
    label .gameLoop:
        call screen screen_gameloop()
    if g.phoneProgress[1]<2:
        jump .gameLoop

    pause
    hide screen screen_home_phone onlayer master
    $ game.jeu_sensitive = False
    pause 1.0

    if whichDress == "red":
        show joyce outfitred at trs_standing onlayer master zorder 0 
    else:
        show joyce outfitblue at trs_standing onlayer master zorder 0 
    with dissolve

    j smile "Hey! Hope I didn't keep you waiting."
    show joyce at trs_sitting with dissolve
    j foxy "Did you get my picture?"
    j "No peeking under the table hehe!"
    show screen screen_date_ui with dissolve
    return

label label_pic5_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a" onlayer master zorder 2
    show expression "Joyce/selfie/pic5-"+whichDress+".png"  at truecenter onlayer master zorder 2
    with dissolve
    $ renpy.mark_image_seen("Joyce/selfie/pic5-"+whichDress+".png")
    pause
    "This picture is turning you on…"
    "Lust +10"
    $ date.lust += 10
    play sound "rpg/Lust.wav"
    window hide 
    pause
    window auto
    hide expression "Joyce/selfie/pic5-"+whichDress+".png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone from _call_label_home_phone_5
    return

label label_bar_talk:
    if "bar_talk" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("bar_talk")
        hide screen screen_date_ui with dissolve
        show joyce null
        j smile "So?"
        j "What do you think of the dress?"
        menu:
            "It looks great on you!":
                j "Hehe."
                j "I agree, I don't look half bad in it."
            "I think you look better without wearing it.":
                j "Huh? What do you..."
                j foxy "Oh."
                j "You naughty boy."
                j "You don't even know what I look like under."
        show screen screen_date_ui with dissolve
    else:
        call label_reaction_talk
    return


label label_bar_flirt:
    if "bar_talk" in done_flag["seen_labels"] and "bar_flirt" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("bar_flirt")
        hide screen screen_date_ui with dissolve
        show joyce null
        menu:
            "I think you look better without wearing it.":
                j foxy "You don't even know what I look like under."
        menu:
            "Oh but I can imagine.":
                j "Oh yea?"
                j "This dress doesn't leave much room for imagination though."
                j "My tits are almost overflowing."
            "Soon enough I'll know.":
                j "Aren't you cocky?"
                j "You might end up disappointed."
                j "Or I might be disappointed."
                j "You're setting my expectactions pretty high."
