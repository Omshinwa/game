label label_dream_1:
    if g.dreamProgress >= 3:
        jump label_dream_2
    show black
    with fade
    if g.dreamProgress == 1:
        pause 0.5
    scene bg dream
    show black
    hide black with Dissolve(1.0)
    show joyce outfitdream2 null at depied onlayer master zorder 2
    with Dissolve(0.5)
    pause 0.5
    
    if g.dreamProgress == 1:
        j "Hey sweety"
        j "What's wrong? Something different about me?"
        j "Did you think I didn't notice during the date?"
        j "You were oogling at those tits."
    else:
        j "Did you miss me?"
        j "Or you missed those huge tits?"

    "You can transform an Eye Contact card."
    menu:
        "flirt":
            call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?")
        "be touchy":
            call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?")
        "devil":
            call label_transform_card("eyecontact", "devil", "Transform 1 Eye Contact card into DevilPact?")
    
    if g.dreamProgress == 1:
        j "Maybe you'll get to suck on these tits"
        j "In real life that is."
    play sound "day/alarm.wav"
    pause 1.0
    j "Goodbye"
    $ g.dreamProgress += 1
    call label_newDay("label_home_weirdDream")
    
    

