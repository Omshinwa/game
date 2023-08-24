screen screen_home:
    use screen_trust_ui()
    use screen_day
    use screen_deck_stack

    # sensitive not renpy.get_screen("say")
    sensitive game.jeu_sensitive

    if game.day % game.dateEvery == 0:
        imagebutton:
            idle "home/door.png"
            hover im.MatrixColor("home/door.png", im.matrix.tint(1,1,0.7))
            action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
            focus_mask True

        imagebutton:
            idle "home/phone.png"
            hover im.MatrixColor("home/phone.png", im.matrix.tint(1,1,5))
            action Call("label_skip_day")
            focus_mask True
    else:
        if game.hasNewMessage():
            imagebutton:
                idle "home/phone-msg.png"
                hover im.MatrixColor("home/phone-msg.png", im.matrix.tint(1,1,5))
                action Show("screen_home_phone", None, _layer = "master")
                focus_mask True
        else:
            if game.progress[0]==0:
                add "home/phone.png"
            else:
                imagebutton:
                    idle "home/phone.png"
                    hover im.MatrixColor("home/phone.png", im.matrix.tint(1,1,5))
                    action Show("screen_home_phone", None, _layer = "master")
                    focus_mask True

        imagebutton:
            idle "home/door.png"
            hover im.MatrixColor("home/door.png", im.matrix.tint(1,1,0.7))
            action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
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
            action Call("label_home_comp")
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

screen screen_home_phone():
    
    modal True #break pauses?

    sensitive game.jeu_sensitive
            
    button:
        xsize 1.0
        ysize 1.0
        action Hide("screen_home_phone", None, _layer="master")

    fixed at switch:
        xsize 523
        ysize 918
    
        imagebutton:
            idle "home/phone-big.png"
            action [Call("label_home_phone")]
        
        
        if global_var.phoneProgress[0] in global_var.phoneLogs:
            fixed:
                
                xsize 410
                ysize 637
                xpos 40
                ypos 130

                
                viewport id "id_phonescreen":

                    yinitial 1.0
                    if not game.hasNewMessage():
                        mousewheel True

                    yadjustment phone_Scroll
                    vbox:
                        spacing 10
                        fixed:
                            ysize 0

                        for index, message in enumerate( global_var.phoneLogs[global_var.phoneProgress[0]] ):
                            
                            if index>global_var.phoneProgress[1]: #only display msg sent
                                break
                            
                            # elif index<=global_var.phoneProgress[1]-4:
                            #     continue

                            if message[0] == 0: #text msg
                                frame:
                                    padding (30, 10)
                                    background Frame("home/phone-bubble.png")
                                    text message[1] size 33 xalign 0.5
                                    
                                    xmaximum 300

                            elif message[0] == 1: #picture
                                default disp = "home/" + message[1]
                                frame:
                                    padding (30, 10)
                                    background Frame(im.MatrixColor("home/phone-bubble.png", im.matrix.tint(1.0,0.9,0.6)))
                                    imagebutton:
                                        sensitive global_var.phoneProgress[1]+1 >= len(global_var.phoneLogs[global_var.phoneProgress[0]]) # if the whole log was shown
                                        hover im.MatrixColor("Joyce/selfie/small-" + message[1], im.matrix.tint(1.3,1.3,1.3))
                                        idle "Joyce/selfie/small-" + message[1]
                                        action Show("screen_fullscreen", dissolve, "Joyce/selfie/" + message[1])
                                        xsize 200
                                        ysize 200

                            elif message[0] == 2: #my text msg
                                frame:
                                    xmaximum 300
                                    xanchor 1.0
                                    xpos 420
                                    padding (30, 10)
                                    background Frame(im.MatrixColor("home/phone-bubble-me.png", im.matrix.tint(1.3,1.3,0.5)))
                                    text message[1] size 33 xalign 0.5
                            elif message[0] == 3: #my photo
                                frame:
                                    xmaximum 300
                                    xanchor 1.0
                                    xpos 420
                                    padding (30, 10)
                                    background Frame(im.MatrixColor("home/phone-bubble-me.png", im.matrix.tint(1.65,1.0,0.95)))
                                    add "Joyce/selfie/small-" + message[1]
                                
                        fixed:
                            ysize 0

                vbar adjustment phone_Scroll xalign 1.08 ysize 600 yalign 0.5 xsize 20 bar_invert True base_bar "#fff" thumb "#aaa"#unscrollable "hide" 


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

label label_skip_day():
    menu:
        "Postpone date until next time?"
        "Yes":
            call label_newDay("label_home")
        "No":
            return
        
label label_home_tutorial():
    window hide
    $ game.day += 1
    $ game.state = "living"
    $ renpy.play("day/newday.wav", channel='sound')
    show screen screen_home onlayer master
    show black onlayer screens
    with dissolve
    pause 2.0
    # play sound "day/alarm.wav"
    # pause 2.0
    window auto

    if tutorial:
        scene bg home
        show screen screen_home onlayer master
        show black onlayer screens
        hide black onlayer screens with dissolve
        show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
        play sound "rpg/Item1.wav"
        "You will keep your stats after a successful date."
        "If you fail, they stay the way they were before."
        "{b}Lust{/b} builds up automatically after every day."
        "This is your home, this is where you can improve your deck."
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
    "You felt like you had a weird dream"
    "You cannot remember the content though."
    jump label_home

label label_home():
    $ game.state = "living"
    scene bg home
    show screen screen_home onlayer master
    show black onlayer screens
    hide black onlayer screens with dissolve

    if game.progress[0] == 2 and game.progress[1] == -1 and "cat" not in done_flag:
        $ done_flag["cat"] = 1
        play sound "day/meow.wav"
        "seems like he has something in his mouth"
        call label_home_add_cards("drink", "Add a Drink to your deck?", callback=False)


    label .gameLoop:
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    jump .gameLoop

label label_home_trash_cutscene(index):
    hide screen screen_prison
    hide screen screen_show_deck
    show expression deck.list[index].img:
        function trans_flush_card
    show screen screen_flushing(deck.list[index].img) with dissolve
    pause(1.0)
    hide screen screen_flushing
    hide expression deck.list[index].img
    $ deck.list.pop(index)
    $ renpy.call("label_newDay","label_home")

label label_home_cat:
    play sound "day/meow.wav"
    menu:
        "talk to it":
            call label_home_add_cards("talk", "Add a Small Talk to your deck?")
        "stare it":
            call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?")
        "X":
            return
    return

label label_home_comp:
    menu:
        "You log into discord"
        "Post messages":
            call label_transform_card("talk", "talk2", "Transform 1 Small Talk card into Talk?", "label_home")
        "Read messages":
            call label_transform_card("talk", "listen", "Transform 1 Small Talk card into Listen?", "label_home")
        "go to prison":
            jump label_prison 
        "X":
            return
    return

label label_home_bed:
    $ game.jeu_sensitive = False
    menu:
        "rub a quickie":
            show black with dissolve
            queue sound ["sex/sloppy.wav","sex/sloppy.wav","sex/sloppy.wav"]
            pause 2.0
            queue sound ["sex/Poison-cum.wav"]
            "Lust reset to 0"
            $ game.lust = -1
            call label_newDay("label_home")
        "dream":
            call expression "label_dream_" + str(global_var.dreamProgress)
        "X":
            return

    return

label label_home_plant():
    menu:
        "water it":
            call label_home_add_cards("calm", "Add a Calm to your deck?")
        # "meditate":
        #     call label_home_add_cards("awakening", "Add an Awakening to your deck?")
        "X":
            return
    return

label label_home_add_cards(cardID, prompt, callback="label_home"):
    show expression trans_show_card_2(Card(cardID).img) as card
    menu:
        "[prompt]"
        "yes":
            hide card
            hide screen screen_tutorial
            call label_add_card_to_deck("list", Card(cardID), 300, 500)
            if callback:
                call label_newDay(callback)
        "no":
            hide card
            hide screen screen_tutorial
    return

label label_home_phone():

    if global_var.phoneProgress[0] not in global_var.phoneLogs:
        hide screen screen_home_phone onlayer master
        return

    $ messagelog = global_var.phoneLogs[global_var.phoneProgress[0]]

    if len(messagelog)-1 > global_var.phoneProgress[1]:  #if the log hasnt been completed yet
        
        $ global_var.phoneProgress[1] += 1

        $ typeOfLastMsg = messagelog[global_var.phoneProgress[1]][0]
        $ contentLastMsg = messagelog[global_var.phoneProgress[1]][1]
        
        if typeOfLastMsg != "exe":
            play sound "day/newmsg.wav"

        elif typeOfLastMsg == "exe":
            $ commands = contentLastMsg.split("; ")
            $ global_var.phoneLogs[global_var.phoneProgress[0]].pop(global_var.phoneProgress[1])  # POP THE EXE MSGS
            $ global_var.phoneProgress[1] -= 1

            $ i = 0
            while i < len(commands):
                $ print(commands[i])
                $ exec(commands[i])
                $ i += 1
            
        
        with Dissolve(0.2)
        $ phone_Scroll.change(phone_Scroll.range)

    else:
        hide screen screen_home_phone onlayer master

    return


label label_pic3_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic3.png" at truecenter
    
    with dissolve
    pause
    "this picture has some effect on you.."
    "Lust +5"
    $ game.lust += 5
    play sound "rpg/Lust.wav"
    window hide 
    pause
    window auto
    hide expression "Joyce/selfie/pic3.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone
    return

label label_pic2_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic2.png" at truecenter
    
    with dissolve
    pause
    menu:
        "Take a picture of your cat?"
        "Yes":
            $ global_var.phoneLogs[global_var.phoneProgress[0]] += [[3, "pic-cat.png"], [0, "omggg is it yours? so cuuute"], [2, "yuuup"]]
        "No":
            $ global_var.phoneLogs[global_var.phoneProgress[0]] += [[2, "cool"]]
    window hide 
    window auto
    hide expression "Joyce/selfie/pic2.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone
    return

label label_pic4_reaction:
    default whichDress = "red"
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic4.png" at truecenter
    
    with dissolve
    pause
    menu:
        "Red":
            $ global_var.phoneLogs[global_var.phoneProgress[0]] += [[2, "I like the red dress"], [0, "the cleavage is so biiig though"],[2, "You'll pull it off"],[0, "yea I'm sure you're gonna enjoy it."],[0, ";-P"]]
            $ whichDress = "red"
        "Blue":
            $ global_var.phoneLogs[global_var.phoneProgress[0]] += [[2, "I like the blue dress"], [0, "i might not fit in anymore, "],[0, "I gained so much weight since the last time I wore it."],[2, "You'll pull it off"],[0, "near the chest area"],[0, ";-P"]]
            $ whichDress = "blue"
    window hide 
    window auto
    hide expression "Joyce/selfie/pic4.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone
    return

label label_pic1_reaction:
    $ game.jeu_sensitive = False
    # show screen screen_fullscreen("Joyce/selfie/nightgown.png", False)
    show expression "#000a"
    show expression "Joyce/selfie/pic1.png" at truecenter
    
    with dissolve
    pause
    "..."
    label .sudoku:
        "Help her by finding a number?"
        menu:
            "Yes":
                $ sudokuNumber = ["","",""]
                while type(sudokuNumber[0]) != type(1):
                    $ sudokuNumber[0] = renpy.input("What number did you find?", length=1)
                    if sudokuNumber[0].isnumeric() :
                        $ sudokuNumber[0] = int(sudokuNumber[0])
                    else:
                        "Not a number."
                while type(sudokuNumber[1]) != type(1):
                    $ sudokuNumber[1] = renpy.input("What row?", length=1)
                    if sudokuNumber[1].isnumeric() :
                        $ sudokuNumber[1] = int(sudokuNumber[1])
                    else:
                        "Not a number."
                while type(sudokuNumber[2]) != type(1):
                    $ sudokuNumber[2] = renpy.input("What column?", length=1)
                    if sudokuNumber[2].isnumeric() :
                        $ sudokuNumber[2] = int(sudokuNumber[2])
                    else:
                        "Not a number."
            
                show expression Text("{b}"+str(sudokuNumber[0])+"{/b}", color="#f00") at Transform(xpos=740+51*(sudokuNumber[2]-1), ypos=340+52*(sudokuNumber[1]-1)+ 2*(8 - sudokuNumber[1])-2*(8 - sudokuNumber[2])) as chiffre
                
                "Ok?"
                menu:
                    "Yes":
                        pass
                    "No":
                        hide chiffre
                        jump .sudoku
                
                
                define answer = """4_7_______3__7_26___2_3__75683149_5__5478___17193256_8____125_7___4_315__215_74__"""
                $ sudoku_pos = (sudokuNumber[1]-1)*9 + (sudokuNumber[2]-1)
                $ global_var.phoneLogs[3].append( [2, "There's a [sudokuNumber[0]] in row [sudokuNumber[1]], column [sudokuNumber[2]]"])
                # $ global_var.phoneLogs[3].append( [2, "sudoku_pos [sudoku_pos]"])
                if answer[sudoku_pos] == str(sudokuNumber[0]):
                    $ global_var.phoneLogs[3].append( [0, "Wow! How did you find that? Thanks!"])
                    $ global_var.phoneLogs[3].append( [2, "+4 trust"])
                    $ global_var.phoneLogs[3].append( [0, "what?"])
                    $ global_var.phoneLogs[3].append( [2, "dont worry about it ;-)"])
                    $ global_var.phoneLogs[3].append( ["exe", "game.trust+=4; renpy.call('label_home_phone')"])
                else:
                    $ global_var.phoneLogs[3].append( [0, "thanks! I'll see what I can do with that."])
            "No":
                $ global_var.phoneLogs[3].append( [2, "Good luck with that!"])
                pass
    


    window hide 
    window auto
    hide chiffre
    hide expression "Joyce/selfie/pic1.png"
    hide expression "#000a"
    with dissolve
    pause 0.5
    $ game.jeu_sensitive = True
    # $ del answer
    call label_home_phone
    return