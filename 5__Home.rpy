screen screen_home:
    use screen_trust_ui()
    use screen_day
    use screen_deck_stack

    sensitive not renpy.get_screen("say")

    imagebutton:
        idle "home/door.png"
        hover im.MatrixColor("home/door.png", im.matrix.tint(1,1,0.7))
        action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
        focus_mask True
    imagebutton:
        idle "home/phone.png"
        hover im.MatrixColor("home/phone.png", im.matrix.tint(1,1,5))
        action Show("screen_home_phone", None, _layer = "master")
        focus_mask True
    imagebutton:
        idle "home/bed.png"
        hover im.MatrixColor("home/bed.png", im.matrix.tint(1,1,5))
        action Call("label_home_bed")
        focus_mask True

    imagebutton:
        idle "home/trash.png"
        hover im.MatrixColor("home/trash.png", im.matrix.tint(1,1,5))
        action Show("screen_show_deck",label_callback="label_home_trash_cutscene", instruction=_("choose a card to throw"), background="img_toilet-static")
        focus_mask True

    imagebutton:
        idle "home/comp.png"
        hover im.MatrixColor("home/comp.png", im.matrix.tint(1,1,5))
        action Jump("label_prison") #Show("screen_home_food")
        focus_mask True
    imagebutton:
        idle "home/plant.png"
        hover im.MatrixColor("home/plant.png", im.matrix.tint(1,1,5))
        action Call("label_home_plant")
        focus_mask True
    imagebutton:
        idle "home/cat.png"
        hover im.MatrixColor("home/cat.png", im.matrix.tint(1,1,5))
        action Call("label_home_cat")
        focus_mask True

label label_home(newDay = False):
    $ game.state = "living"
    $ game.jeu_sensitive = True

    if newDay:
        $ renpy.play("newday.wav", channel='sound') 
        scene bg home
        show screen screen_home onlayer master
        with Fade(0.5, 1.0, 0.5)
        
        $ game.day += 1
    else:
        scene bg home
        show screen screen_home onlayer master
        with fade

    # $ global_var["prison_cards"] = []
    # $ global_var["prison_cards"].append( Card.get_random_card() )
    # $ global_var["prison_cards"].append( Card.get_random_card() )
    # $ global_var["prison_cards"].append( Card.get_random_card() )
    # $ global_var["prison_cards"].append( Card.get_random_card() )

    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop

label label_home_trash_cutscene(index):
    hide screen screen_prison
    hide screen screen_show_deck
    show expression deck.list[index].img:
        function trans_flush_card
    show screen screen_flushing(deck.list[index].img) with dissolve
    pause(2.0)
    hide screen screen_flushing
    hide expression deck.list[index].img
    $ deck.list.pop(index)
    show screen screen_prison with dissolve
    $ renpy.call("label_home", newDay = True)

label label_home_cat:
    play sound "meow.wav"
    menu:
        "talk to it":
            call label_home_add_cards("smalltalk", "Add a Small Talk to your deck?")
        "listen to it":
            call label_home_add_cards("listen", "Add a Listen to your deck?")
        "look at it":
            call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?")
        "touch it":
            call label_home_add_cards("touchy", "Add a Touchy to your deck?")
        "X":
            return

    return

label label_home_bed:
    menu:
        "rub a quickie":
            while game.lust>0:
                $ game.lust -= 5
                if game.lust < 0:
                    $ game.lust = 0
            call label_home(True)
        "listen to it":
            call label_home_add_cards("listen", "Add a Listen to your deck?")
        "X":
            return

    return

label label_home_plant():
    menu:
        "water it":
            call label_home_add_cards("calm", "Add a Calm to your deck?")
        "meditate":
            call label_home_add_cards("awakening", "Add an Awakening to your deck?")
        "X":
            return
    return

label label_home_add_cards(cardID, prompt):
    show expression trans_show_card_2(Card(cardID).img) as card
    menu:
        "[prompt]"
        "yes":
            hide card
            call label_add_card_to_deck("list", cardID, 300, 500)
            $ hide_all_screens_but("home")
            $ game.nextDay("label_home")
        "no":
            hide card
            hide screen screen_tutorial
    return

label label_home_phone():
    $ messagelog = global_var["phoneLogs"][global_var["phoneProgress"][0]]

    if len(messagelog)-1 > global_var["phoneProgress"][1]:  #if the log hasnt been completed yet

        $ global_var["phoneProgress"][1] += 1

        $ typeOfLastMsg = messagelog[global_var["phoneProgress"][1]][0]
        $ contentLastMsg = messagelog[global_var["phoneProgress"][1]][1]

        if typeOfLastMsg == "exe":
            $ commands = contentLastMsg.split("; ")
            $ print(commands)
            $ i = 0
            while i < len(commands):
                $ print(commands[i])
                $ exec(commands[i])
                $ i += 1

    else:
        hide screen screen_home_phone onlayer master

    return

screen screen_home_phone():
    modal True

    sensitive game.jeu_sensitive
            
    button:
        xsize 1.0
        ysize 1.0
        action Hide("screen_home_phone", None, _layer="master")

    fixed at switch:
        imagebutton:
            idle "home/phone-big.png"
            action Call("label_home_phone")
        xsize 523
        ysize 918
        
        fixed: #phone screen
            xsize 420
            ysize 637
            xalign 0.5
            ypos 130
            vbox:
                spacing 10
                for index, message in enumerate(global_var["phoneLogs"][global_var["phoneProgress"][0]]):

                    if index>global_var["phoneProgress"][1]: #only display msg sent
                        break

                    if message[0] == 0: #text msg
                        frame:
                            padding (30, 10)
                            background Frame("home/bubble-speech.png")
                            text message[1] size 33 xalign 0.5
                            
                            xmaximum 300

                    elif message[0] == 1: #picture
                        default disp = "home/" + message[1]
                        frame:
                            padding (30, 10)
                            background Frame("home/bubble-speech-interact.png")
                            imagebutton:
                                sensitive global_var["phoneProgress"][1]+1 >= len(global_var["phoneLogs"][global_var["phoneProgress"][0]]) # if the whole log was shown
                                hover im.MatrixColor("home/" + message[1], im.matrix.tint(1.3,1.3,1.3))
                                idle "home/" + message[1]
                                action Show("screen_fullscreen", dissolve, "Joyce/selfie/" + message[1])
                                xsize 200
                                ysize 200

label label_pic1_reaction:
    $ game.jeu_sensitive = False
    # show screen screen_fullscreen("Joyce/selfie/nightgown.png", False)
    show expression "#000a"
    show expression "Joyce/selfie/pic1.png" at truecenter
    
    with dissolve
    pause
    "this picture has some effect on you.."
    "Lust +2"
    $ game.lust += 2
    window hide 
    pause
    window auto
    hide expression "Joyce/selfie/pic1.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True

screen screen_fullscreen(disp):
    # modal True
    button:
        xsize 1.0
        ysize 1.0
        action [Hide("screen_fullscreen", dissolve), Hide("screen_home_phone")]
    add "#000a"
    add disp:
        xalign 0.5
        yalign 0.5

transform switch:
    on show:
        ypos -1000 xalign 0.9
        ease 0.5 ypos 100
    on hide:
        ypos 100 xalign 0.9
        ease 0.5 ypos -1000