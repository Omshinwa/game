label label_bubbleTea:
    $ date = Date("date", objectif_trust = 10, objectif_attraction = 5, turnLeft = 5, endTurn = "label_bubbleTea_endTurn")

    scene bg bbt
    show fg bbt-table onlayer master zorder 2

    if game.progress[1]>=1:
        show screen screen_glass("bbt") onlayer master zorder 2

    show joyce outfit1 smile at trs_sitting

    with dissolve

    if game.progress[1] == -1:
        j "Hey! How have you been?"
        j "I really like this cafe."
        j "I hope you'll like it too."
    else:
        j "Hello again!"
        if game.progress[1]>=1:
            j "I got us drinks already."
    
    call label_beginDuel_common() from _call_label_beginDuel_common_1
    
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                call label_after_successful_Date_common from _call_label_after_successful_Date_common_1

                j smile "So, did you like the cafe?"
                j "I think we should hang out outside again."
                j worried "It's getting quite warm! How about we enjoy our drinks outdoors next time?"
                call label_newDay("label_home") from _call_label_newDay_9
                
        show joyce null with dissolve
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_2
        $ game.jeu_sensitive = True
        
        call screen screen_gameloop()
        
    jump .gameLoop


label label_bubbleTea_endTurn:
    call label_endTurn_common
    call label_date_isLost_common from _call_label_date_isLost_common_1
    if game.progress[1]<=1:
        if date.turn == 1:
            hide screen screen_date_ui with dissolve
            j smirk "I'm gonna grab a drink, I'll get something for you too!"
            show joyce at trs_standing with dissolve
            pause 0.5
            hide joyce with dissolve
            pause 2.0
            show joyce outfit1 smile at trs_standing with dissolve
            show joyce at trs_sitting, trs_lighting_bbt with dissolve 
            j "Here."
            play sound "day/put_on_table.wav"
            show screen screen_glass("bbt", (380,550)) onlayer master zorder 2 with Dissolve(0.2)
            pause
            show joyce smile
            j "Isn't it nice to have something sweet to drink?"
            show screen screen_tutorial("misc/tutorial-drink.png") with dissolve
            play sound "rpg/Item1.mp3"
            j "When you take a sip, you'll shuffle back all the cards in your hand into the deck."
            j "Then you'll redraw as many! Try this when you feel stuck."
            j "Here, try it:"
            hide screen screen_tutorial with dissolve 

        elif date.turn == 2:
            hide screen screen_date_ui with dissolve
            j "Does it taste good?"
            j null "Em..."
            j worried "Can I taste it?"
            menu:
                "Yes":
                    j -worried smile "Thanks!"
                    show screen screen_tutorial("Joyce/cut-in_drink.png", {"xalign":0.5, "yalign":0.3, "zoom":1.5}) onlayer master zorder 5 with moveinleft
                    
                    play sound "day/gulp.wav"
                    j "Mhh, it tastes so good."
                    j "Maybe I drink too much bubble tea though haha."
                    play sound "day/gulp.wav"
                    show layer master:
                        zoom 2.0 xalign 0.5 yalign 0.4
                    with dissolve
                    pause
                    j "Huh, what's wrong?"
                    j "Is there something wrong with my face?"
                    pause
                    show layer master:
                        zoom 1.0 xalign 0.5 yalign 0.5
                    hide screen screen_tutorial onlayer master
                    if date.drink>0:
                        $ date.drink-=1
                    with dissolve
                    "You feel like you want to look at her lips closer..."
                    show screen screen_date_ui with dissolve
                    "(a Peek card is added to your hand)"
                    $ g.bubbleTea_share_drink = True
                    window hide
                    window auto
                "No":
                    j "Oh, ok..."
                    $ date.attraction -= 2
                    $ date.trust -= 2
                    $ game.attraction -= 2
                    $ game.trust -= 2
                    "-2 attraction -2 trust."
                    window hide
                    window auto
        
    show screen screen_date_ui with dissolve
            
    if game.progress[1]>=2 and g.bubbleTea_share_drink:
        call label_add_card_to_deck("hand", Card("peek"),pauseTime=0.5) from _call_label_add_card_to_deck_5

    return

label label_bubbleTea_talk:
    if "bubbleTea_talk" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("bubbleTea_talk")
        hide screen screen_date_ui with dissolve
        show joyce null
        j smile "You like drinking milk tea?"
        j "I like this place, but I've been coming here too often lately."
        j "Haha."
        show screen screen_date_ui with dissolve
    else:
        call label_reaction_talk
    return