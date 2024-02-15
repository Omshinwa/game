label label_dream_0:
    if game.progress[0] >= 3 or game.progress[0] >= 2 and game.progress[1]>0:
        jump label_dream_1

    show black
    with fade
    pause 0.5
    scene bg dream
    show black
    if g.dreamProgress == 0:
        hide black with Dissolve(2.0)
        "?"
        show joyce outfitdream null at trs_depied onlayer master zorder 2
        with Dissolve(1.0)
        pause
        j "Hello, [povname]."
        j "Did you miss me that much?"
        menu:
            "Yes":
                j "hehe."
                j "Good, I like honest boys."
                j "I'll give you a reward…"
            "No":
                j "Oh, how cold hearted…"
                j "Don't I make you feel some way?"
        j "What do you want to do to me?"
    else:
        hide black
        show joyce outfitdream null at trs_depied onlayer master zorder 2
        with Dissolve(0.5)
        j "Back already?"
        j "Did you come here to get a card…"
        j "Or did you want to get a good look at me?"
    "You can transform an Eye Contact card."
    label .chooseOption:
        menu:
            "flirt":
                $ i = len([item for item in deck.list if item.name == "eyecontact"])
                call label_transform_card("eyecontact", "flirt", "Transform 1 Eye Contact card into Flirt?") from _call_label_transform_card_4
                if len([item for item in deck.list if item.name == "eyecontact"]) == i:
                    jump .chooseOption
            "be touchy":
                $ i = len([item for item in deck.list if item.name == "eyecontact"])
                call label_transform_card("eyecontact", "touchy", "Transform 1 Eye Contact card into Touchy?") from _call_label_transform_card_5
                if len([item for item in deck.list if item.name == "eyecontact"]) == i:
                    jump .chooseOption
            "X":
                pass
    
    if g.dreamProgress == 0:
        j "Did this give you any new ideas?"
        j "I hope you use those ideas for our next date…"
        play sound "day/alarm.wav"
        pause 1.0
        j "It seems our time is up."
    j "See you soon, cowboy."
    $ g.dreamProgress = 1
    
    call label_newDay("label_home_weirdDream") from _call_label_newDay_13
  


########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################


# label label_dream_afterAddedCards(cards):
#     $ i = 0
#     while i < len(cards):
#         call label_add_card_to_deck( "list", cards[i])
#         $ deck.list.append( cards[i] )
#         $ i += 1
#     $ deck.list.sort()

#     hide screen screen_dream_addCards with dissolve
#     return

# screen screen_dream_addCards(sixCards):
#     add "#000a"
#     modal True
    
#     fixed:
#         xpos -550
#         use screen_add_cards( sixCards[:2], "label_dream_afterAddedCards")
#     fixed:
#         xpos 0
#         use screen_add_cards( sixCards[2:4], "label_dream_afterAddedCards")
#     fixed:
#         xpos 550
#         use screen_add_cards( sixCards[4:], "label_dream_afterAddedCards")

#     text "Choose which set of cards to add" xalign 0.5 style "quirky_command" ypos 150 xsize 1800 at animated_text
