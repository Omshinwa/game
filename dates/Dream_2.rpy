label label_dream_2:
    show black
    with fade
    scene bg dream
    show black
    hide black with Dissolve(1.0)
    show joyce outfitdream3 null at depied onlayer master zorder 2
    with Dissolve(0.5)
    pause 0.5
    
    if g.dreamProgress == 3:
        j "Hey sweety"
        j "What's wrong? Something different about me?"
        j "Oh noooo I'm wet."
        j "hahaha"
    else:
        pass
    "You can transform an Eye Contact card."
    menu:
        "flirt":
            call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?")
        "be touchy":
            call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?")
        "devil":
            call label_home_add_cards("devil", "Add a Devil's Pact to your deck?")
        "pair":
            call label_home_add_cards("pair", "Transform 1 Eye Contact card into Pair?")

    play sound "day/alarm.wav"
    pause 1.0
    j "Good luck"
    $ g.dreamProgress += 1
    call label_newDay("label_home_weirdDream")
    
    
