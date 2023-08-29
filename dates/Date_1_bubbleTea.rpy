label label_bubbleTea:
    $ date = Date("date", objectif_trust = 10, objectif_attraction = 5, turnLeft = 4, endTurn = "label_bubbleTea_endTurn")

    scene bg bbt
    show fg bbt-table onlayer master zorder 2

    if game.progress[1]>=1:
        show screen screen_glass("bbt") onlayer master zorder 2

    show joyce outfit1 smile at sitting

    with dissolve

    if game.progress[1] == -1:
        j "Hey how have you been?"
        j "I really like this cafe."
        j "I hope you like it too."
    else:
        j "Hello again"
        if game.progress[1]>=1:
            j "I got us drinks already."
    
    call label_beginDuel_common()
    
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                call label_after_successful_Date_common

                j smile "So did you like the cafe?"
                j "I think we should hang out outside again."
                j worried "It is getting pretty hot! Let's drink outside next time."
                call label_newDay("label_home")
                
        if len(deck.hand) == 0:
            call expression date.endTurn
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop


label label_bubbleTea_endTurn:
    call label_date_isLost_common

    if game.progress[1]<=1:
        if date.turn == 0:
            hide screen screen_date_ui with dissolve
            j "I'm gonna grab a drink, I'll take you something too!"
            show joyce at standing with dissolve
            pause 0.5
            hide joyce with dissolve
            pause 2.0
            show joyce outfit1 smile at standing with dissolve
            show joyce at sitting with dissolve
            j "here"
            play sound "day/put_on_table.wav"
            show screen screen_glass("bbt") onlayer master zorder 2 with Dissolve(0.2)
            pause
            show joyce smile
            j "Isn't it nice to be able to drink something sweet?"
            show screen screen_tutorial("misc/tutorial-drink.png") with dissolve
            j "When you take a sip, you'll shuffle back all your cards in hand into the deck"
            j "Then you'll redraw as many! Do this when you feel like you're stuck."
            j "Here, try it:"
            hide screen screen_tutorial with dissolve 

        elif date.turn == 1:
            hide screen screen_date_ui with dissolve
            j "Does it taste good?"
            show joyce null
            j worried "Em"
            j "Can I taste it?"
            menu:
                "yes":
                    show joyce blink smile
                    j "Thanks!"
                    show screen screen_tutorial("Joyce/cut-in_drink.png", {"xalign":0.5, "yalign":0.3, "zoom":1.5}) onlayer master zorder 5 with moveinleft
                    
                    play sound "day/gulp.wav"
                    j "mhh it tastes so good"
                    j "Maybe I drink too much bubble teas though haha"
                    play sound "day/gulp.wav"
                    show layer master:
                        zoom 2.0 xalign 0.5 yalign 0.4
                    with dissolve
                    pause
                    j "huh, what's wrong?"
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
                    "(a Peek card was added to your hand)"
                    $ g.bubbleTea_share_drink = True
                    window hide
                    window auto
                "no":
                    j "oh, ok.."
                    $ date.attraction -= 2
                    $ date.trust -= 2
                    $ game.attraction -= 2
                    $ game.trust -= 2
                    "-2 attraction -2 trust."
                    window hide
                    window auto
    else:
        call label_reaction
        
    show screen screen_date_ui with dissolve
            

    call label_endTurn_common
    
    if game.progress[1]>=2 and g.bubbleTea_share_drink:
        call label_add_card_to_deck("hand", Card("peek"),pauseTime=0.5)

    return