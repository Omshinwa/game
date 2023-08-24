label label_bubbleTea:
    $ game.state = "dating"
    $ date = Date(objectif_trust = 8, objectif_attraction = 3, turnLeft = 5, endTurn = "label_bubbleTea_endTurn")

    scene bg bbt
    show fg bbt-table onlayer master zorder 2

    if game.progress[1]>=1:
        show screen screen_glass("bbt") onlayer master zorder 2

    show joyce outfit1 smile at sitting

    with dissolve

    show expression generate_anim3("Joyce/anim/touch-hair/touch-hair (",9,0.15) at sitting as anim
    pause 0.15*9
    hide anim

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
                hide screen screen_date_ui with dissolve

                play sound "rpg/Holy5.wav"
                show date-nice at truecenter with blinds
                pause 0.3
                hide date-nice with moveoutbottom

                j "So did you like the drink?"
                j "I think we should get a drink every time we hang out now haha"
                j "It is getting pretty hot!"
                call label_after_successful_Date_common
                call label_newDay("label_home")
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop


label label_bubbleTea_endTurn:
    call label_date_endTurn

    if game.progress[1]<=date.turn:
        if date.turn == 0:
            hide screen screen_date_ui with dissolve
            j "I'm gonna grab a drink, I'll take you something too!"
            show joyce at standing with dissolve
            pause 0.5
            hide joyce with dissolve
            pause 3.0
            show joyce outfit1 smile at standing with dissolve
            pause 2.0
            show joyce at sitting with dissolve
            j "here"
            show screen screen_glass("bbt") onlayer master zorder 2 with Dissolve(0.2)
            pause
            show joyce smile
            j "Isn't it nice to be able to drink something sweet?"
            show screen screen_tutorial("misc/tutorial-drink.png") with dissolve
            j "When you take a sip, you'll shuffle back all your cards in hand into the deck"
            j "Then you'll redraw as many! Do this when you feel like you're stuck"
            j "You can drink it 3 times until it's empty"
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
                    j "Is there something on my face?"
                    pause
                    show layer master:
                        zoom 1.0 xalign 0.5 yalign 0.5
                    hide screen screen_tutorial onlayer master
                    if date.drink>0:
                        $ date.drink-=1
                    with dissolve
                    "You feel a little weird.."
                    "You feel like you want to look at her lips closer..."
                    show screen screen_date_ui with dissolve
                    "(a Peek card was added to your hand)"
                "no":
                    j "oh, ok.."
                    $ date.attraction -= 2
                    $ date.trust -= 4
                    "-2 attraction -4 trust."
    else:
        call label_reaction
        
    show screen screen_date_ui with dissolve
            

    call label_endTurn_common
    
    if date.turn>=2 or game.progress[1]>=2:
        call label_add_card_to_deck("hand", Card("peek"),pauseTime=1.0)

    return