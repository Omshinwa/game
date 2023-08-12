label label_bubbleTea:
    $ game.state = "dating"
    $ date = Date(objectif_trust = 8, isWin = "date.trust >= 8", turnLeft = 5, endTurn = "label_bubbleTea_endTurn")

    
    # python:
    #     povname = renpy.input("What is your name?", length=32)
    #     povname = povname.strip()

        # if not povname:
        #     povname = "William"


    scene bg bbt
    show joyce 
    show fg bbt-table onlayer master zorder 2
    
    show joyce at standing
    j "Hey how have you been?"
    show joyce base at sitting
    j "I really like this place."
    j "I hope you like it too."
    
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

                j "haha"
                j "That was a nice first date. I feel like I can trust you."
                j "Hey... Here's my number"
                j "Do you want to meet again in the week?"
                j "I'll text you."
                j "See ya."
                call label_after_successful_Date_common
                jump label_home
            
            show joyce at default
            ""
            show joyce 2nd 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop


label label_bubbleTea_endTurn:
    $ game.jeu_sensitive = False;

    label .loseCondition:
        if date.lust > date.trust or date.turnLeft == 0 or len(deck.deck) == 0:

            play sound "rpg/Fall1.wav"
            show date-fail at truecenter with blinds
            pause 0.3
            hide date-fail with moveoutbottom

            show joyce neutral
            show joyce armscrossed upset

            if date.lust > date.trust:
                hide screen screen_date_ui with dissolve
                j "um.. don't you think I can notice?"
                j "Sorry but gotta go"
                j "Maybe we can do this another day?"

            elif date.turnLeft == 0 or len(deck.deck) == 0:
                hide screen screen_date_ui with dissolve
                j "OH look at the time."
                j "Sorry but I gotta go."
                j "That kinda dragged on no?"
                j "Maybe we can do this another day? See ya."
            
            $ game.progress[1] += 1
            $ game.nextDay("label_home")

        else:
            if date.turnLeft == 4:
                hide screen screen_date_ui with dissolve
                j "I'm gonna grab a drink, I'll take you something too!"
                show joyce stand  with dissolve
                pause 0.5
                hide joyce with dissolve
                pause 3.0
                show joyce stand  with dissolve 
                pause 2.0
                show joyce base with dissolve
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

            elif date.turnLeft == 3:
                hide screen screen_date_ui with dissolve
                j "Does it taste good?"
                show joyce neutral worried
                j "Em"
                j "Can I take a taste it?"
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
                        "You feel like you want to look at her mouth again..."
                        show screen screen_date_ui with dissolve
                        call label_add_card_to_deck("deck", Card("peek"),pauseTime=2.0)
                        "(a Peek card was added to your deck)"
                        $ flag_peek = True
                    "no":
                        j "oh, ok.."
                        $ date.attraction -= 2
                        $ date.trust -= 4
                        "-2 attraction -4 trust."
                
            else:
                if flag_peek:
                    call label_add_card_to_deck("deck", Card("peek"),pauseTime=1.0)
                    # pause 0.5
            
            show screen screen_date_ui with dissolve
            

    call label_endTurn_common
    return