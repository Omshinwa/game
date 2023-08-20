label label_dream_2:
    show black
    with fade
    pause 2.0

    $ date = Date(objectif_attraction = 10, isWin = "date.attraction >= 10", turnLeft = 7, isLost= "len(deck.deck)==0", endTurn = "label_dream_0_endTurn")
    scene bg dream
    show black
    hide black with Dissolve(1.0)
    pause
    "?"
    show joyce dream3 stare at depied onlayer master zorder 2
    with Dissolve(1.0)
    pause
    j "Hello [povname]"
    j "Did you miss me that much?"
    j "You just can't wait for our next date huh.."
    j "I'll entertain you. Let's play a shadow game.."

    call label_beginDuel_common()
    $ date.lust = 0
    $ date.attraction = 0
    $ date.trust = 0
    with dissolve
    
    j "Don't be scared baby"
    j "This is just you and me"


    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                hide screen screen_date_ui with dissolve

                show date-nice at truecenter with blinds
                hide date-nice with moveoutbottom

                j "nicely done"
                j "So that's what your perfect date would look like huh"
                j "Does this give you any new ideas?"
                "You can transform up to two Eye Contact cards."
                
                menu:
                    "drink!":
                        call label_transform_card("eyecontact", "drink", "Transform 1 Eye Contact card into Flirt?")
                    "flirt":
                        call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?")
                    "touchy":
                        call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?")
                pause
                
                j "I hope you use those ideas for the next date.."
                play sound "day/alarm.wav"
                pause 1.0
                j "Oh"
                j "We had fun together, but it seems like our time is up."
                j "See you soon cowboy."

                $ global_var.dreamProgress += 1

                # modified new day
                window hide
                $ game.day += 1
                $ game.state = "living"
                show black onlayer screens
                with Dissolve(2.0)
                play sound "day/alarm.wav"
                pause 2.0
                $ game.state = "living"
                window auto

                show black onlayer screens with dissolve
                jump label_home_weirdDream
            
            show joyce 
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return

label label_dream_2_endTurn:
    $ game.jeu_sensitive = False;
    $ date.turn += 1

    label .loseCondition:
        if len(deck.deck) == 0:

            show date-fail at truecenter with blinds
            pause 0.3
            hide date-fail with moveoutbottom

            show joyce null
            show joyce armscrossed upset


            if date.turnLeft == 0 or len(deck.deck) == 0:
                hide screen screen_date_ui with dissolve
                play sound "day/alarm.wav"
                pause 1.5
                j "Seems like our time is up."
                j "You didn't satisfy me yet.."
                j "Come back next time."
                j "Please try harder next time baby."
            
                call label_newDay("label_home")
                
    if date.turn == 1:
        hide screen screen_date_ui with dissolve

        if date.turn == 1:
            j "Stop being so shy."
            j "You can be as horny as you want here.."
            j "You'll forget everything when you wake up.'"

        show screen screen_date_ui with dissolve
        pause 0.5

    call label_endTurn_common

    return