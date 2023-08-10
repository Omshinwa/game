label label_tutorial:
    $ game.state = "dating"
    $ date = Date(objectif_trust = 5, isWin = "date.trust >= 5", turnLeft = 5, endTurn = "label_firstDate_tutorial")
    $ povname = "William"

    show joyce stand stare 
    
    # j "Hello, you're [povname] right?"
    # j "I'm Joyce."

    if game.progress[1] == 0:
        show joyce base smile
        j "This is your first date no?"
        menu:
            "Yes":
                j "I'll tell you how a date works."
                $ tutorial = True
            "No":
                show joyce smile 
                j "Oh you're experienced"
                j "Then let the date begin!"
                $ tutorial = False

        show joyce 
    else:
        $ tutorial = False
        show joyce base
        j "hi again"
        j "I hope this date goes better than the last"
    
    call label_beginDuel_common()

    if tutorial:
        $ game.jeu_sensitive = False
        show joyce neutral
        show screen screen_tutorial("misc/tutorial-cards.png") with dissolve
        j "During a date, you play cards from your hand that have various effects."
        show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
        j "The aim of a date is to build {b}{color=#55f}{u}trust{/u}{/color}{/b} and {b}{color=#f3a}{u}attraction{/u}{/color}{/b}."
        j "{b}{color=#cc3}{u}Lust{/u}{/color}{/b} is a negative trait."
        j "If you have {b}more lust than trust{/b}, the girl will notive you're being too pervy."
        j "They will be upset and the date will be over."
        j "So don't act too horny. At least not on your first dates!"
        j "This date, you only need to build 8 trust for it to be successful."
        show screen screen_tutorial("misc/tutorial-end-turn.png") with dissolve
        j "The date is also over when you {b}run out of card{/b}."
        j "After every turn, you draw until you have 5 cards in hand."
        hide screen screen_tutorial with dissolve
        show joyce smile 
        j "Got it?\nLet's start the date!"
    
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
                hide joyce with dissolve
                "When a date is successful, you will keep the Lust, Trust and Attraction you built."
                call label_after_successful_Date_common
                jump label_home
            
            show joyce 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop


label label_tutorial_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

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

            hide joyce with dissolve
            $ game.progress[1] += 1
            $ game.nextDay("label_home")

        else:
            if date.turnLeft == 4:
                j "So youre [povname], you often do blind dates like that?"
            if date.turnLeft == 3:
                j "I often come to this bubble tea place."
            if date.turnLeft == 2:
                j "I have a cat, do you have any pet?"
            if date.turnLeft == 1:
                j "I eat too much sugar lately"

    call label_endTurn_common
    return


label label_firstDate:
    $ game.state = "dating"
    $ date = Date(objectif_trust = 8, isWin = "date.trust >= 8", turnLeft = 5, endTurn = "label_firstDate_endTurn")

    define pov = Character("[povname]")
    
    # python:
    #     povname = renpy.input("What is your name?", length=32)
    #     povname = povname.strip()

        # if not povname:
        #     povname = "William"


    scene bg bbt
    show joyce 
    show fg bbt-table onlayer master zorder 2
    
    show joyce stand stare
    j "boop"
    show joyce 2nd-stand stare as joyce
    j "Hey how have you been?"
    hide joyce
    show joyce base
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


label label_firstDate_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

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

            
            elif date.turnLeft == 2:
                show joyce sm at default
                
            else:
                if flag_peek:
                    call label_add_card_to_deck("deck", Card("peek"),pauseTime=1.0)
                    # pause 0.5
            
            show screen screen_date_ui with dissolve
            

    call label_endTurn_common
    return

label label_secondDate:
    $ date = Date(objectif_trust = 10, objectif_attraction = 5, isWin = "date.trust >= 10 and date.attraction >= 5", turnLeft = 6, endTurn = "label_secondDate_endTurn")
    scene bg terrasse
    hide joyce
    show joyce smile 
    show fg terrasse-table onlayer master zorder 2
    show screen screen_glass("terrasse") onlayer master zorder 2
    j "Hello again"
    j "These days it's getting hotter and hotter huh?"

    call label_beginDuel_common()

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                hide screen screen_date_ui with dissolve

                show date-nice at truecenter with blinds
                hide date-nice with moveoutbottom

                j "t'es trop forte bewbew"

                call label_after_successful_Date_common
                jump label_prison
            
            show joyce 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_secondDate_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turnLeft -= 1

    label .loseCondition:
        if date.lust > date.trust or date.turnLeft == 0 or len(deck.deck) == 0:

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
                
    if date.turnLeft == 5:
        hide screen screen_date_ui with dissolve
        j "Oh man it's really too hot"
        j "Hold on I'll go to the bathroom."
        hide joyce
        show joyce stand 
        pause
        hide joyce with dissolve
        pause
        show joyce_2nd_stand as joyce with dissolve
        j "hey" 
        j "sorry it was just too hot"
        show joyce 2nd
        j "I had to remove a few layers"
        # show boob-shoot at truecenter with moveinright
        show layer master:
            zoom 2.0 xalign 0.5 yalign 0.5
        with dissolve
        pause
        j "what's wrong?"
        "n-nothing"
        j "hm okay"
        j "Let's keep going shall we?"
        show layer master:
            zoom 1.0
        with dissolve
        show joyce smile
        j "So where were we at?"
        call label_add_card_to_deck("deck", Card("peek2"))
        "(a Peek card was added to your deck)"
        window hide
        show screen screen_date_ui with dissolve
        pause 0.5

    elif date.turnLeft < 5:
        call label_add_card_to_deck("deck", Card("peek2"))
        pause 0.5

    call label_endTurn_common

    return
