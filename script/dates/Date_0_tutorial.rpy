label label_tutorial:
    $ date = Date("date", objectif_trust = 5, turnLeft = 4, endTurn = "label_tutorial_endTurn")

    scene bg park
    show joyce outfit1 at trs_depied
    with dissolve

    if game.progress[1] < 0:
    
        j smile "Hello! You're [povname] right?"
        j "I'm Joyce."
        j "This is your first date, right?"
        menu:
            "Yes":
                j "I'll tell you how a date works."
                $ tutorial = True
            "No":
                show joyce smile 
                j "Oh, you already have experience!"
                j "Then let the date begin!"
                $ tutorial = False

        show joyce 
    else:
        $ tutorial = False
        show joyce outfit1 null
        j "Hi again"
        j "I hope this date goes better than last time..."
    
    call label_beginDuel_common() from _call_label_beginDuel_common

    if tutorial:
        $ game.jeu_sensitive = False
        show screen screen_tutorial("misc/tutorial-cards.png") with dissolve
        play sound "rpg/Item1.wav"
        j null armscrossed "During a date, you play cards from your hand that have various effects."
        show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
        j "The aim of a date is to build {color=#55f}{b}trust{/b}{/color} and {color=#f3a}{b}attraction{/b}{/color}."
        j "{b}{color=#cc3}Lust{/color}{/b} is a negative trait."
        j "If {color=#f00}Lust is your highest stat{/color}, the girl will notice you're being too horny."
        j "She will be upset and the date will end early."
        j "So don't act too horny. At least not on your first dates!"
        j "This date, you need to build 5 Trust to be successful."
        show screen screen_tutorial("misc/tutorial-end-turn.png") with dissolve
        j "After every turn, you draw until you have 5 cards in hand."
        j "You can end your turn early to keep some cards for future turns."
        j "Click on the card icon to see what cards are left in your deck!"
        show screen screen_tutorial("misc/tutorial-turn-limit.png") with dissolve
        j "There's a turn limit after which the date will be over."
        hide screen screen_tutorial with dissolve
        j smile base "Got it?\nLet's start the date!"
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():

                call label_after_successful_Date_common from _call_label_after_successful_Date_common
                j smile "I had a good time."
                j "I feel like I can trust you."
                j "Do you want to meet again later this week?"
                j "Hey... Here's my number"
                j "I'll text you."
                j "See ya."
                hide joyce with dissolve
                
                call label_newDay("label_home_tutorial")

        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        # pause
        
    jump .gameLoop


label label_tutorial_endTurn:
    call label_date_isLost_common("label_home_tutorial")
    call label_endTurn_common
    return

label label_tutorial_talk:
    if "label_tutorial_talk" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("label_tutorial_talk")
        hide screen screen_date_ui with dissolve
        show joyce null
        j smile "So you're [povname]! Nice to meet you."
        j "I was a bit worried before coming here, but you seem nice."
        j "Do you often meet girls like this?"
        show screen screen_date_ui with dissolve
    else:
        call label_reaction_talk
