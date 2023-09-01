
label label_barDate:
    $ date = Date("date", objectif_trust = 32, objectif_attraction = 32, turnLeft = 7, endTurn = "label_barDate_endTurn")
    scene bg bar
    show fg bar-table onlayer master zorder 2

    
    if game.progress[1]<0:
        if whichDress == "red":
            show joyce outfitred at depied onlayer master zorder 2
        else:
            show joyce outfitblue at depied onlayer master zorder 2
            $ g.phoneLogs[7][0] = [1, "pic5-blue.png"]
        with dissolve
    
        j smile "Heey [povname]"
        j eyeside "Wow what a nice place"
        j -eyeside "Come on, let's get some seats and drinks haha!"

        if whichDress == "red":
            show joyce outfitred at sitting onlayer master zorder 0 
        else:
            show joyce outfitblue at sitting onlayer master zorder 0 
        with dissolve
        
        show screen screen_glass("bar") onlayer master zorder 2
        play sound "day/put_on_table.wav"
        j "A nice gin tonic"
        with dissolve
    else:
        show screen screen_glass("bar") onlayer master zorder 2

        if whichDress == "red":
            show joyce outfitred at sitting onlayer master zorder 0 
        else:
            show joyce outfitblue at sitting onlayer master zorder 0 
        with dissolve
        j smile "Hurry! Let's party!"
        j smile "haha"

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
                call label_after_successful_Date_common from _call_label_after_successful_Date_common_3

                j smile "That was a beautiful evening"
                j "I'll think about you tonight."
                j "See you soon."
                call label_newDay("label_home") from _call_label_newDay_11
            
            show joyce 
    
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_4

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_barDate_endTurn:
    call label_date_isLost_common from _call_label_date_isLost_common_3
    
    if date.turn == 1 and game.progress[1]<=1:
        hide screen screen_date_ui with dissolve
        j "I'll go to the bathroom a bit"
        show joyce at standing with dissolve
        pause 0.5
        hide joyce with dissolve
        pause 
        play sound "day/newmsg.wav"
        pause
        "?"
        show screen screen_home_phone(False) onlayer master zorder 2
        $ g.phoneProgress[0] += 1
        $ g.phoneProgress[1] = 0
        
        $ game.jeu_sensitive = True
        label .gameLoop:
            call screen screen_gameloop()
        if g.phoneProgress[1]<2:
            jump .gameLoop

        pause
        pause

        if whichDress == "red":
            show joyce outfitred at standing onlayer master zorder 0 
        else:
            show joyce outfitblue at standing onlayer master zorder 0 
        with dissolve

        j smile "Hello I'm back."
        show joyce at sitting with dissolve
        j foxy "Did you receive my photo?"
        j "No peeking under the table hehe!"
        show screen screen_date_ui with dissolve
    else:
        call label_reaction from _call_label_reaction_3

    call label_endTurn_common from _call_label_endTurn_common_3

    call label_add_card_to_deck("hand", Card("peek"+whichDress),pauseTime = 0.5) from _call_label_add_card_to_deck_7

    return

label label_pic5_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a" onlayer master zorder 2
    show expression "Joyce/selfie/pic5-"+whichDress+".png"  at truecenter onlayer master zorder 2
    with dissolve
    pause
    "this picture has some effect on you.."
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