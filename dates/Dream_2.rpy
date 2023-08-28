label label_dream_2:
    show black
    with fade
    pause 0.5
    scene bg dream
    show black
    hide black with Dissolve(1.0)
    pause
    show joyce outfitdream3 null at depied onlayer master zorder 2
    with Dissolve(0.5)
    pause
    
    if g.dreamProgress == 4:
        j "Hey sweety"
        j "What's wrong? Something different about me?"
        j "Did you think I didn't notice during the date?"
        j "You were oogling at those tits, did you think I didn't notice?"
    else:
        j "Did you miss me?"
        j "Or you missed those huge tits?"

    "You can transform an Eye Contact card."
    menu:
        "flirt":
            call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?")
        "be touchy":
            call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?")
        "drink":
            call label_transform_card("eyecontact", "drink", "Transform 1 Eye Contact card into Drink?")
    
    if g.dreamProgress == 1:
        j "Maybe you'll get to suck on these tits"
        j "In real life that is."
    play sound "day/alarm.wav"
    pause 1.0
    j "Have a good day"
    $ g.dreamProgress += 1
    call label_newDay("label_home_weirdDream")
    
    

