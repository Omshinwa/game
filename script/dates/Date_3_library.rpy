image library-table-shadow =  ShowingSwitch(
    "joyce holdbook","fg2 library-table-shadow-all",
    "joyce whisper","fg2 library-table-shadow-right",
    None,"fg2 library-table-shadow-null")

label label_library_intro_first_time:
    j "Hey [povname], I'm here!"
    j "Did you recognize me?"
    j happy "Notice anything different about me?"
    menu:
        "You wear glasses?":
            j -happy "Yea, I usually wear contact lenses."
            j "But I was short on time today."
        "Cute dress.":
            show joyce -smile blush -happy with dissolve
            j "Oh."
            j smirk "I was more thinking about the glasses."
            j smirk "But thanks!"
    j "Wanna get inside?"
    return

label label_library_intro_again:
    j "..."
    j squint "?"
    j happy smile "Oh! [povname]."
    j wave -happy "Sorry I didn't recognize you!"
    menu:
        "After 4 dates with me you still can't recognize me?":
            j -wave -happy "Hahaha"
            j "Hey it's tough without my lenses alright?"
    j "You ready for round 2?"
    j "I'm still not done with my book!"
    j "Let's get inside!"
    return

label label_library:
    scene bg library-entrance at trs_bg_blur
    if game.progress[1]==-1:
        show joyce smile outfit4 glasses at trs_depied
    else:
        show joyce outfit4 at trs_depied

    with dissolve
    pause

    if game.progress[1]==-1:
        call label_library_intro_first_time
    else:
        call label_library_intro_again
    
    hide joyce with dissolve
    play sound "day/walk in.wav"
    show bg library-1 at trs_bg_blur
    if game.progress[1]==-1:
        show joyce outfit4 glasses at trs_depied
    else:
        show joyce outfit4 at trs_depied
    with Fade(0.5, 1.0, 0.5)
    j -smile "Oh there's quite a few people."
    j eyeside "Mhhh..."
    j -eyeside smirk "The book I want to read is in the opposite corner."
    j wave "I'll go pick it up."
    hide joyce with dissolve
    play sound "day/walk out.wav"
    "Joyce is going through the aisles."
    "While she does it, you think about what you'd want to read."
    menu:
        "What do you want to read?"
        "Physics":
            $ temp = "Physics"
        "Environ\nment":
            $ temp = "the Environment"
        "Mythology":
            $ temp = "Mythology"
    "You search for a book on [temp]."
    "..."
    $ del temp
    if game.progress[1]==-1:
        show joyce smirk outfit4 glasses at trs_depied
    else:
        show joyce smirk outfit4 at trs_depied
    with dissolve
    j "Are you good?"
    j "Let's go downstairs to read."
    
    show black onlayer master zorder 3 with dissolve 
    play sound "day/walk.wav"
    hide joyce
    pause 1.0

    show bg library at trs_bg_blur
    show fg library-table
    # show joyce smile outfit4 holdbook at trs_sitting
    if game.progress[1]==-1:
        show joyce outfit4 glasses at trs_standing
    else:
        show joyce outfit4 at trs_standing
    with dissolve
    show library-table-shadow onlayer master zorder 2

    
    # show stranger_library with dissolve


    hide black onlayer master zorder 3 with dissolve
    pause 0.3
    play sound "day/chair_sit_down.wav"
    show joyce at trs_sitting
    pause
    j "Did you bring a water bottle?"
    j smirk "I brought one."
    $ date.drink = 3
    play sound "day/put_on_table.wav"
    show screen screen_glass("library", (600,600)) onlayer master zorder 2
    with dissolve
    pause
    j happy blush "You can drink from it if you're thirsty."

    show joyce eyeside whisper with dissolve
    pause
    j -eyeside "(Let's not be too loud.)"
    j breath holdbook "(Lots of people are reading here.)"
    j -whisper "(Lots of people are reading here.)"

    
    $ date = Date("date", objectif_trust = 22, objectif_attraction = 20, turnLeft = 6, endTurn = "label_library_endTurn")

    call label_beginDuel_common()
    
    label .gameLoop:
        $ game.jeu_sensitive = False

        label .winCondition:
            if date.isWin():
                call label_after_successful_Date_common
                call label_newDay("label_home")
        pause 0.0
        show joyce eyesdown null_skin null_mouth holdbook with Dissolve(.5)
        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return

    
    call label_newDay("label_home")

label label_library_endTurn:
    call label_endTurn_common
    call label_date_isLost_common

label label_library_talk:
    # menu:
    #     "What are you reading?":
    #         j -eyedown "Oh, this?"
    # j "It's an ancient Indian book on the philosophy and theory of love"
    # menu:
    #     "Is it good?":
    #         j "Oh yea it's pretty interesting."
    #         j "I might borrow it."
    #     "What is it called?":
    #         j blush "Em, you wouldn't know it."