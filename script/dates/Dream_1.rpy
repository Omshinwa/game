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
    show joyce outfitdream2 null at trs_depied onlayer master zorder 2
    with Dissolve(0.5)
    pause 0.5
    
    if g.dreamProgress == 1:
        j "Hey, sweetie…"
        j "What's wrong? Something different about me?"
        j "Did you think I didn't notice during our date?"
        j "You were drooling over those tits."
    else:
        j "Did you miss me…"
        j "Or did you miss those huge tits?"

    "You can transform an Eye Contact card or get a special card."
    label .chooseOption:
        menu:
            "Flirt with her":
                $ i = len([item for item in deck.list if item.name == "eyecontact"])
                call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?") from _call_label_transform_card_6
                if len([item for item in deck.list if item.name == "eyecontact"]) == i:
                    jump .chooseOption
            "Touch her":
                $ i = len([item for item in deck.list if item.name == "eyecontact"])
                call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?") from _call_label_transform_card_7
                if len([item for item in deck.list if item.name == "eyecontact"]) == i:
                    jump .chooseOption
            "Sisyphus":
                $ i = len(deck.list)
                call label_home_add_cards("sisyphus", "Add Sisyphus to your deck?", False) from _call_label_home_add_cards_9
                if len(deck.list) == i:
                    jump .chooseOption

    if g.dreamProgress == 1:
        j "Maybe you'll get to suck on these tits…"
        j "In real life that is."
    play sound "day/alarm.wav"
    pause 1.0
    j "Goodbye."
    $ g.dreamProgress += 1
    call label_newDay("label_home_weirdDream") from _call_label_newDay_14
    
    

