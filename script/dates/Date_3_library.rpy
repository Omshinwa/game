image library-table-shadow =  ConditionSwitch(
    "'holdbook' in renpy.get_attributes('joyce')","fg2 library-table-shadow-all",
    "'whisper' in renpy.get_attributes('joyce')","fg2 library-table-shadow-right",
    True,"fg2 library-table-shadow-null")

label label_library:
    scene bg library-entrance at trs_bg_blur
    show joyce smile outfit3 at trs_depied
    j "Hey [povname], I'm here!"
    j "Did you recognize me?"
    j "I had to bring out my glasses."
    menu:
        "You wear glasses?":
            j "Yea, I usually wear contact lenses."
            j "But I was short on time today."
            j "Let's get inside!"
    hide joyce with dissolve
    play sound "day/walk in.wav"
    show bg library-1 at trs_bg_blur
    show joyce outfit3 at trs_depied
    with Fade(0.5, 1.0, 0.5)
    j eyeside -smile "Oh there's quite a few people here actually."
    j -eyeside smirk "The book I want to read is in the opposite corner."
    j "Be right back."
    hide joyce with dissolve
    play sound "day/walk out.wav"
    "Joyce is going through the aisles."
    "What subject do you want to read?"
    menu:
        "What subject do you want to read?"
        "Physics":
            $ temp = "Physics"
        "Environ\nmental":
            $ temp = "Environmental"
        "Mythology":
            $ temp = "Mythology"
    "You search for a book on [temp]."
    "..."
    "You find one that seems interesting enough."
    $ del temp
    show joyce smirk outfit3 at trs_depied with dissolve
    j "Are you good?"
    j "Let's go downstairs to read."
    
    show black onlayer master zorder 3 with dissolve 
    play sound "day/walk.wav"
    hide joyce
    pause 1.0

    show bg library at trs_bg_blur
    show fg library-table
    # show joyce smile outfit3 holdbook at trs_sitting
    show joyce outfit3 at trs_standing
    show library-table-shadow onlayer master zorder 2

    
    # show stranger_library with dissolve


    hide black onlayer master zorder 3 with dissolve
    pause 0.3
    play sound "day/chair_sit_down.wav"
    show joyce at trs_sitting
    pause
    j "Did you bring a water bottle?"
    j smirk "I brought one in case."
    play sound "day/put_on_table.wav"
    show screen screen_glass("library") onlayer master zorder 2
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

        show joyce eyesdown null_skin null_mouth holdbook with dissolve
        if len(deck.hand) == 0:
            call expression date.endTurn

        $ game.jeu_sensitive = True
        call screen screen_gameloop()
        
    jump .gameLoop
    return

    
    call label_newDay("label_home")

label label_library_endTurn:
    call label_date_isLost_common

label label_library_talk:
    menu:
        "What are you reading?":
            j -eyedown "Oh, this?"
    j "It's an ancient Indian book on the philosophy and theory of love"
    menu:
        "Is it good?":
            j "Oh yea it's pretty interesting."
            j "I might borrow it."
        "What is it called?":
            j blush "Em, you wouldn't know it."