label label_terrasse:
    $ date = Date("date", objectif_trust = 20, objectif_attraction = 16, turnLeft = 6, endTurn = "label_terrasse_endTurn")
    scene bg terrasse
    show fg terrasse-table onlayer master zorder 2

    if game.progress[1]>=1:
        show screen screen_glass("terrasse") onlayer master zorder 2
        show joyce outfit2 smile at trs_sitting
        with dissolve
        j "I remembered to dress lighter this time."
    else:
        show joyce outfit1 smile at trs_sitting
        with dissolve
        j "Hey!"
        j "You found me! Come sit there."
        show screen screen_glass("terrasse") onlayer master zorder 2
        play sound "day/put_on_table.wav"
        j "Ahhh... Nothing beats a cold beer on a terrace."

    call label_beginDuel_common() from _call_label_beginDuel_common_2

    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                call label_after_successful_Date_common from _call_label_after_successful_Date_common_2

                j smile "Phew! I'm getting a bit tipsy."
                j "I think I'll go home now. This was nice."
                j "We should go somewhere special next time"
                j "I'll think about something."
                j "See ya!"
                call label_newDay("label_home") from _call_label_newDay_10

        show joyce null with Dissolve(0.1)
        if len(deck.hand) == 0:
            call expression date.endTurn from _call_expression_3

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return


label label_terrasse_endTurn:
    
    call label_endTurn_common
    call label_date_isLost_common from _call_label_date_isLost_common_2
    
    if game.progress[1]<=0:            
        if date.turn == 0:
            hide screen screen_date_ui with dissolve
            show joyce null
            j blush bored opened "Geez, it's so hot today."
            j "Hold on, I'm gonna go to the bathroom."
            j "Be right back."
            show joyce at trs_standing with dissolve
            pause 0.5
            hide joyce with dissolve
            pause 3.0
            show joyce outfit2 at trs_standing as joyce with dissolve
            j smile "Hey" 
            j "Sorry, it was just too hot."
            show joyce outfit2
            j "I had to remove a few layers."
            show layer master:
                zoom 2.0 xalign 0.5 yalign 0.5
            with dissolve
            pause 3.0
            j "What's wrong?"
            menu:
                "N-nothing":
                    j "Hmm okay."
            show layer master:
                zoom 1.0
            with dissolve
            show joyce smile at trs_sitting with dissolve
            j "So where were we at?" 
            show screen screen_date_ui with dissolve
            pause 0.5

    if has_attribute("outfit2"):
        call label_add_card_to_deck("hand", Card("peek2"), pauseTime = 0.5) from _call_label_add_card_to_deck_6

    return

label label_terrase_talk:
    if "terrase_talk-1" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("terrase_talk-1")
        hide screen screen_date_ui with dissolve
        show joyce null

        play sound "day/gulp.wav"
        j smile "*slurp*"
        j "Ah! Nothing like alcohol after a rough day!"
        j "I drink occasionally."
        j "And when I mean occasionally, I mean you're my excuse to drink!"
        
        show screen screen_date_ui with dissolve
    
    elif "terrase_talk-2" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("terrase_talk-2")
        hide screen screen_date_ui with dissolve
        show joyce null

        j smile "Do you drink alcohol?"
        menu:
            "Sometimes":
                j "Hehe, let's enjoy ourselves."
            "Never":
                j worried -smile "Oh really?"
                j "Please don't force yourself for me."
                j "Next time let's do something without alcohol then."
        
        show screen screen_date_ui with dissolve
        return
    else:
        call label_reaction_talk


label label_terrase_flirt:    
    if "terrase_flirt" not in done_flag["seen_labels"] and "terrase_talk-2" not in done_flag["seen_labels"]:
        $ done_flag["seen_labels"].add("terrase_flirt")
        hide screen screen_date_ui with dissolve
        show joyce null

        j smile "Do you drink alcohol?"
        menu:
            "Only for you":
                j -smile blush "..."
                j "You're the type to say cheesy lines heh?"
                j "Hahaha."
        
        show screen screen_date_ui with dissolve
    else:
        call label_reaction_flirt
    return