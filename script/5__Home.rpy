#############################################################################
##                                                                                     
##
##     #######    #####  ######    #######  #######  ###   ##   #######
##     ##       ###      ##   ##   ##       ##       ####  ##   ##
##     #######  ##       ######    #####    #####    ## ## ##   #######
##          ##  ###      ##  ##    ##       ##       ##  ####        ##
##     #######    #####  ##   ##   #######  #######  ##   ###   #######
##
##
#############################################################################

screen screen_home:

    sensitive game.jeu_sensitive

    if game.day % game.dateEvery == 0: # IF today theres a date
        
        add bwImg("home/comp.png")
        add bwImg("home/bed.png")

        imagebutton:
            idle "home/door-open.png"
            hover Transform("home/door-open.png", matrixcolor=TintMatrix((255,255,178)))
            action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
            focus_mask True

        imagebutton:
            idle "home/phone.png"
            hover Transform("home/phone.png", matrixcolor=TintMatrix((255,255,1275)))
            action Call("label_skip_day")
            focus_mask True

        if g.plant < 4:
            add "home/plant-"+str(g.plant)+".png"
        else:
            add "home/plant-3.png"

        add "home/trash.png"

    else: # IF today theres no date

        if game.debug_mode:
            imagebutton:
                idle "home/door.png"
                hover Transform("home/door.png", matrixcolor=TintMatrix((255,255,178)))
                action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
                focus_mask True
        else:
            add "home/door.png"     
            
        imagebutton:
            idle showInteractible("home/bed.png", (0.99,0.6))
            hover Transform("home/bed.png", matrixcolor=TintMatrix((255,255,1275)))
            action [AddToSet(done_flag["buttons"], "home/bed.png"), Call("label_home_bed")]
            focus_mask True
            sensitive True

        imagebutton:
            idle showInteractible("home/trash.png", (0.08,0.95))
            hover Transform("home/trash.png", matrixcolor=TintMatrix((255,255,1275)))
            action [AddToSet(done_flag["buttons"], "home/trash.png"), Call("label_home_trash")]
            focus_mask True
            sensitive True

        imagebutton:
            idle showInteractible("home/comp.png",(0.25,0.3))
            hover Transform("home/comp.png", matrixcolor=TintMatrix((255,255,1275)))
            action [AddToSet(done_flag["buttons"], "home/comp.png"), Call("label_home_comp")]
            focus_mask True
            sensitive True

        if g.plant < 4:
            imagebutton:
                idle showInteractible("home/plant-"+str(g.plant)+".png",(0.05,0.5))
                hover tintImg("home/plant-"+str(g.plant)+".png", (255,255,1275))
                action [AddToSet(done_flag["buttons"], "home/plant-"+str(g.plant)+".png"), Call("label_home_plant")]
                focus_mask True
                sensitive True
        else:
            imagebutton:
                idle "home/plant-3.png"
                hover Transform("home/plant-3.png", matrixcolor=TintMatrix((255,255,1275)))
                action Call("label_home_plant")
                focus_mask True

        imagebutton:
            idle showInteractible("home/cat.png",(0.45,0.85))
            hover Transform("home/cat.png", matrixcolor=TintMatrix((255,255,1275)))
            action [AddToSet(done_flag["buttons"], "home/cat.png"), Call("label_home_cat")]
            focus_mask True
            selected True
            sensitive True

        if game.hasNewMessage():
            imagebutton:
                idle "home/phone-msg.png"
                hover Transform("home/phone-msg.png", matrixcolor=TintMatrix((255,255,1275)))
                action Show("screen_home_phone", None, _layer = "master")
                focus_mask None

        else:
            if game.progress[0]==0:
                add "home/phone.png"
            else:
                imagebutton:
                    idle "home/phone.png"
                    hover Transform("home/phone.png", matrixcolor=TintMatrix((255,255,1275)))
                    action Show("screen_home_phone", None, _layer = "master")
                    focus_mask True

    use screen_trust_ui()
    use screen_day
    use screen_deck_stack

screen screen_home_end_act_2:
    use screen_day
    use screen_deck_stack

    # sensitive not renpy.get_screen("say")
    sensitive game.jeu_sensitive

    if game.hasNewMessage():
        imagebutton:
            idle "home/phone-msg.png"
            hover Transform("home/phone-msg.png", matrixcolor=TintMatrix((255,255,1275)))
            action Show("screen_home_phone", None, _layer = "master")
            focus_mask True
    else:
        imagebutton:
            idle "home/phone.png"
            hover Transform("home/phone.png", matrixcolor=TintMatrix((255,255,1275)))
            action Show("screen_home_phone", None, _layer = "master")
            focus_mask True

    imagebutton:
        idle "home/cat.png"
        hover Transform("home/cat.png", matrixcolor=TintMatrix((255,255,1275)))
        action Play("sound", "day/meow.wav")
        focus_mask True

    if g.plant >= 4:
        imagebutton:
            idle "home/plant-5.png"
            hover Transform("home/plant-5.png", matrixcolor=TintMatrix((255,255,1275)))
            action Jump("label_big_tree_thank_you")
            focus_mask True
    else:
        add "home/plant-"+str(g.plant)+".png"

    add "home/trash.png"


#############################################################################
##                                                                                     
##
##          ██       █████  ██████  ███████ ██      ███████ 
##          ██      ██   ██ ██   ██ ██      ██      ██      
##          ██      ███████ ██████  █████   ██      ███████ 
##          ██      ██   ██ ██   ██ ██      ██           ██ 
##          ███████ ██   ██ ██████  ███████ ███████ ███████ 
##
##
#############################################################################


label label_home():
    # make the plant grow

    if g.water > 0:
        $ g.water -= 1
        if g.water == 0:
            $ g.water = -1
            $ g.plant += 1

    if game.progress[0]*2>g.phoneProgress[0] and game.day%game.dateEvery==game.dateEvery-1:
        $ g.phoneProgress[0] += 1
        $ g.phoneProgress[1] = 0

    $ game.state = "living"
    scene bg home
    show screen screen_home onlayer master
    show black
    hide black
    hide black onlayer screens
    with dissolve
    hide screen screen_day

    if game.progress[0] == 2 and game.progress[1] == -1 and "cat" not in done_flag:
        $ done_flag["cat"] = 1
        play sound "day/meow.wav"
        "?"
        "Seems like the cat has something in its mouth.."
        "It's a card!"
        call label_home_add_cards("drink", "Add a Drink to your deck?", callback=False) from _call_label_home_add_cards

    elif game.progress[0] == 4 and game.progress[1] == -1 and done_flag["cat"] == 1:
        $ done_flag["cat"] = 2
        play sound "day/meow.wav"
        "?"
        "Seems like the cat has something in its mouth"
        "It's a card!"
        call label_home_add_cards("devil", "Add a Devil to your deck?", callback=False) from _call_label_home_add_cards_6

    label .gameLoop:
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    jump .gameLoop

label label_home_end():

    $ game.state = "living"
    scene bg home
    show screen screen_home_end_act_2 onlayer master
    show black
    hide black with dissolve
    hide screen screen_day

    label .gameLoop:
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    jump .gameLoop

label label_skip_day():
    menu:
        "Postpone date until next time?"
        "Yes":
            call label_newDay("label_home") from _call_label_newDay_2
        "No":
            return
        
label label_home_tutorial():

    if tutorial:
        scene bg home
        show screen screen_home onlayer master
        show black 
        hide black with dissolve
        play sound "rpg/Item1.wav"
        "This is your home. You can improve your deck here."
        show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
        "You will keep your stats after a successful date."
        "If you fail, your stats will stay as they were before."
        "{b}Lust{/b} builds up automatically after every day."
        "Try to build a stronger deck before the second date!"
        hide screen screen_tutorial
        show black onlayer screens with dissolve
        $ tutorial = False

    jump label_home

label label_home_weirdDream():
    $ game.state = "living"
    scene bg home
    show screen screen_home onlayer master
    show black onlayer screens
    hide black onlayer screens with dissolve
    "You feel like you had a weird dream…"
    "But you can't remember what it was about."
    jump label_home

label label_home_trash():

    if len(g.trashbin) == 3 and g.findFromTrash:
        $ g.findFromTrash = False
        $ game.jeu_sensitive = False
        "?"
        "There's something inside the trash…"
        call label_home_add_cards("recycle", "Add a Recycle to your deck?", False) from _call_label_home_add_cards_7
        return
    else:
        show screen screen_trashbin
        call screen screen_show_deck(var_label_callback="label_home_trash_cutscene", instruction=_("choose a card to throw"), background="#0000")
        hide screen screen_trashbin
        return


label label_home_trash_cutscene(index):
    hide screen screen_show_deck
    $ temp = [deck.list[index].img, renpy.random.randint(-150, 150), renpy.random.random()/5+0.4, renpy.random.random()/4+0.550]
    show expression temp[0] at throw_away_home(temp[1],temp[2],temp[3]) onlayer screens
    pause(0.6)
    play sound "day/tap.wav"
    pause(0.4)
    $ g.trashbin.append( temp )
    $ deck.list.pop(index)
    $ del temp
    hide screen screen_trashbin
    hide expression temp[0] onlayer screens
    $ renpy.call("label_newDay","label_home")
    return

screen screen_trashbin():
    add "trash-static"
    for trash in g.trashbin:
        # if trash != g.trashbin[-1]: #dont count the last one
        add trash[0]:
            zoom 0.5 rotate trash[1] xalign trash[2] yalign trash[3]
    # add g.trashbin[-1][0] at throw_away_home(g.trashbin[-1][1],g.trashbin[-1][2],g.trashbin[-1][3])

label label_home_cat:
    play sound "day/meow.wav"
    
    if game.progress[0]<2:
        menu:
            "talk to it":
                call label_home_add_cards("talk", "Add a Small Talk to your deck?") from _call_label_home_add_cards_1
            "stare at it":
                call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?") from _call_label_home_add_cards_2
            "X":
                return

    else:
        menu:
            "talk to it":
                call label_home_add_cards("talk", "Add a Small Talk to your deck?") from _call_label_home_add_cards_3
            "stare at it":
                call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?") from _call_label_home_add_cards_4
            "look at what it found":
                call label_home_add_cards("drink", "Add a Drink! to your deck?") from _call_label_home_add_cards_5
            "X":
                return
    return


label label_home_comp:

    if game.debug_mode:
        menu:
            "You log into discord"
            "Post messages":
                call label_transform_card("talk", "talk2", "Transform 1 Small Talk card into Talk?", "label_home") from _call_label_transform_card
            "Read messages":
                call label_transform_card("talk", "listen", "Transform 1 Small Talk card into Listen?", "label_home") from _call_label_transform_card_1
            "go to prison":
                jump label_prison 
            "X":
                return
        
    else:
        menu:
            "You log into discord"
            "Post messages":
                call label_transform_card("talk", "talk2", "Transform 1 Small Talk card into Talk?", "label_home") from _call_label_transform_card_2
            "Read messages":
                call label_transform_card("talk", "listen", "Transform 1 Small Talk card into Listen?", "label_home") from _call_label_transform_card_3
            "X":
                return
    return

label label_home_bed:
    $ game.jeu_sensitive = False
    menu:
        "take care of your lust":
            show black with dissolve
            queue sound ["sex/sloppy.wav","sex/sloppy.wav","sex/sloppy.wav"]
            pause 2.0
            queue sound ["sex/_Poison-cum.wav"]
            "Lust reset to zero"
            $ game.lust = -1 * eval(game.lustPerDay)
            
            python:
                if renpy.random.random() > 0.5:
                    g.trashbin.append( [Image("home/tissue.png"), renpy.random.randint(-180, 180), renpy.random.random()/5+0.4, renpy.random.random()/4+0.550] )
                else:
                    g.trashbin.append( [Image("home/tissue2.png"), renpy.random.randint(-180, 180), renpy.random.random()/5+0.4, renpy.random.random()/4+0.550] )
            call label_newDay("label_home") from _call_label_newDay_3
        "dream":
            call expression "label_dream_0" from _call_expression
        "X":
            return

    return

label label_big_tree_thank_you():
    if 98 > g.plant >= 4:
        "'Thank you'"
        "?!"
        "You feel like you just heard a voice."
        $ g.plant = 99
    call screen screen_gameloop()
    return

label label_water_the_plant():
    if g.plant >= 4:
        "It needs time to grow now, not water."
        return
    elif g.water > 0:
        "You've already recently watered it."
        return
    menu:
        "Maybe watering it will help it grow?"
        "Sure":
            jump .water_the_plant
        "X":
            return

    label .water_the_plant: 
        play sound "day/watering-the-plant-with.mp3"
        if g.plant == 0:
            "You feel like the plant is already growing."
        elif g.plant == 1:
            "You feel like the plant is getting bigger."
        elif g.plant == 2:
            "You feel like the plant is going to be massive."
        elif g.plant == 3:
            "You feel like the plant is going to take over the world."
            $ g.plant = 4
        $ g.water = 7
        call label_newDay('label_home') from _call_label_newDay_4

label label_home_plant():
    if g.plant == 0:
        menu:
            "water it":
                jump label_water_the_plant
            "X":
                return
    elif g.plant == 1:
        menu:
            "water it":
                jump label_water_the_plant
            "smell it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant")
            "X":
                return    
    elif g.plant == 2:
        menu:
            "water it":
                jump label_water_the_plant
            "smell it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant")
            "meditate":
                call label_home_add_cards("maxcalm", "Add a MaxCalm to your deck?")
            "X":
                return
    elif g.plant >= 3:
        menu:
            "water it":
                jump label_water_the_plant
            "smell it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant")
            "meditate":
                call label_home_add_cards("maxcalm", "Add a MaxCalm to your deck?")
            "study it":
                call label_home_add_cards("fibonacci", "Add a Fibonacci to your deck?")
            "X":
                return
    return

label label_home_add_cards(cardID, prompt, callback=True):
    show expression trans_show_card_2(Card(cardID).img) as card
    menu:
        "[prompt]"
        "Yes":
            hide card
            hide screen screen_tutorial
            call label_add_card_to_deck("list", Card(cardID), 300, 500) from _call_label_add_card_to_deck_2
            if callback:
                if callback == True:
                    call label_newDay('label_home') from _call_label_newDay_23
                else:
                    call expression callback from _call_expression_10
        "No":
            hide card
            hide screen screen_tutorial
    return