label label_dream_0:
    
    show black
    with fade
    pause 0.5
    scene bg dream
    show black
    if global_var.dreamProgress == 0:
        hide black with Dissolve(2.0)
        "?"
        show joyce outfitdream null at depied onlayer master zorder 2
        with Dissolve(1.0)
        pause
        j "Hello [povname]"
        j "Did you miss me that much?"
        menu:
            "yes":
                j "hehe"
                j "Good, I like honest boys"
                j "I'll give you a reward"
            "no":
                j "Aw I'm hurt"
                j "You sure you have nothing in your mind?"
        j "What would you like to do to me?"
    else:
        hide black with Dissolve(1.0)
        show joyce outfitdream null at depied onlayer master zorder 2
        with Dissolve(0.5)
        pause 0.5
        j "So quick to come back"
        j "Did you come here to get a card."
        j "Or did you come here to eye on my body?"
    "You can transform an Eye Contact card."
    menu:
        "flirt":
            call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?")

        "be touchy":
            call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?")
    
    if global_var.dreamProgress == 0:
        j "Did this give you any new ideas?"
        j "I hope you use those ideas for the next date.."
        play sound "day/alarm.wav"
        pause 1.0
        j "It seems like our time is up."
    j "See you soon cowboy."
    $ global_var.dreamProgress = 1
    call label_newDay("label_home_weirdDream")
  


########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################


label label_dream_afterAddedCards(cards):
    $ i = 0
    while i < len(cards):
        call label_add_card_to_deck( "list", cards[i])
        $ deck.list.append( cards[i] )
        $ i += 1
    $ deck.list.sort()

    hide screen screen_dream_addCards with dissolve
    return

screen screen_dream_addCards(sixCards):
    add "#000a"
    modal True
    
    fixed:
        xpos -550
        use screen_add_cards( sixCards[:2], "label_dream_afterAddedCards")
    fixed:
        xpos 0
        use screen_add_cards( sixCards[2:4], "label_dream_afterAddedCards")
    fixed:
        xpos 550
        use screen_add_cards( sixCards[4:], "label_dream_afterAddedCards")

    text "Choose which set of cards to add" xalign 0.5 style "quirky_command" ypos 150 xsize 1800 at animated_text
