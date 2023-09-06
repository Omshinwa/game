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
        j "Oh no, I'm wet!"
        j "What will I do?..."
    else:
        pass
    "You can transform an Eye Contact card or get a special card."
    label .chooseOption:
        menu:
            "flirt":
                $ i = len([item for item in deck.list if item.name == "eyecontact"])
                call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?") from _call_label_transform_card_9
                if len([item for item in deck.list if item.name == "eyecontact"]) == i:
                    jump .chooseOption
            "be touchy":
                $ i = len([item for item in deck.list if item.name == "eyecontact"])
                call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?") from _call_label_transform_card_10
                if len([item for item in deck.list if item.name == "eyecontact"]) == i:
                    jump .chooseOption
            "sisyphus":
                $ i = len(deck.list)
                call label_home_add_cards("sisyphus", "Add Sisyphus to your deck?", False) from _call_label_home_add_cards_10
                if len(deck.list) == i:
                    jump .chooseOption
            "reload":
                $ i = len(deck.list)
                call label_home_add_cards("reload", "Add Reload to your deck?", False) from _call_label_home_add_cards_11
                if len(deck.list) == i:
                    jump .chooseOption

    play sound "day/alarm.wav"
    pause 1.0
    j "Good luck."
    $ g.dreamProgress += 1
    call label_newDay("label_home_weirdDream") from _call_label_newDay_15
    
    

