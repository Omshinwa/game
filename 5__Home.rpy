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
    # sensitive not renpy.get_screen("say")
    sensitive game.jeu_sensitive

    if game.day % game.dateEvery == 0: # today theres a date
        
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

    else:

        if game.debug_mode:
            imagebutton:
                idle "home/door.png"
                hover Transform("home/door.png", matrixcolor=TintMatrix((255,255,178)))
                action [Hide("screen_home"), Jump("label_" + game.story[game.progress[0]])]
                focus_mask True
        else:
            add "home/door.png"     
            
        imagebutton:
            idle tintImg("home/bed.png",(255,255,1275))
            hover "home/bed.png"
            action Call("label_home_bed")
            focus_mask True

        imagebutton:
            # idle colorizeImg("home/trash.png",("#000","#ffd")) 
            # idle tintImg("home/trash.png","#ffd") 
            idle tintImg("home/trash.png",(255,255,1275))
            hover "home/trash.png"
            action Call("label_home_trash")
            focus_mask True

        imagebutton:
            idle "home/comp.png"
            hover Transform("home/comp.png", matrixcolor=TintMatrix((255,255,1275)))
            action Call("label_home_comp")
            focus_mask True

        if g.plant < 4:
            imagebutton:
                idle "home/plant-"+str(g.plant)+".png"
                hover Transform("home/plant-"+str(g.plant)+".png", matrixcolor=TintMatrix((255,255,1275)))
                action Call("label_home_plant")
                focus_mask True
        else:
            imagebutton:
                idle "home/plant-3.png"
                hover Transform("home/plant-3.png", matrixcolor=TintMatrix((255,255,1275)))
                action Call("label_home_plant")
                focus_mask True

        imagebutton:
            idle "home/cat.png"
            hover Transform("home/cat.png", matrixcolor=TintMatrix((255,255,1275)))
            action Call("label_home_cat")
            focus_mask True

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

screen screen_home_end:
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
    if g.water:
        $ g.water = False
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
    show screen screen_home_end onlayer master
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
        call screen screen_show_deck(label_callback="label_home_trash_cutscene", instruction=_("choose a card to throw"), background="#0000")
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
            "stare it":
                call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?") from _call_label_home_add_cards_2
            "X":
                return

    else:
        menu:
            "talk to it":
                call label_home_add_cards("talk", "Add a Small Talk to your deck?") from _call_label_home_add_cards_3
            "stare it":
                call label_home_add_cards("eyecontact", "Add an Eye Contact to your deck?") from _call_label_home_add_cards_4
            "look what it found":
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
            queue sound ["sex/Poison-cum.wav"]
            "Lust reset to zero"
            $ game.lust = -1 * eval(game.lustPerDay)
            $ g.trashbin.append( [Image("home/tissue.png"), renpy.random.randint(-150, 150), renpy.random.random()/5+0.4, renpy.random.random()/4+0.550] )
            call label_newDay("label_home") from _call_label_newDay_3
        "dream":
            call expression "label_dream_0" from _call_expression
        "X":
            return

    return

label label_big_tree_thank_you():
    if 10 > g.plant >= 4:
        "'Thank you'"
        "?!"
        "You feel like you just heard a voice."
        $ g.plant = 99
    call screen screen_gameloop()
    return

label label_water_the_plant():
    if g.plant == 0:
        "You feel like the plant is already growing."
    elif g.plant == 1:
        "You feel like the plant is getting bigger."
    elif g.plant == 2:
        "You feel like the plant is going to be massive."
    elif g.plant == 3:
        "You feel like the plant is going to take over the world."
    elif g.plant == 4:
        `It will take some more time for it to grow.`
    if g.plant<5:
        $ g.water = True
    call label_newDay('label_home') from _call_label_newDay_4

label label_home_plant():
    if g.plant <= 0:
        menu:
            "water it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant") from _call_label_home_add_cards_8
            "X":
                return
    elif g.plant <= 1:
        menu:
            "water it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant") from _call_label_home_add_cards_12
            "meditate":
                call label_home_add_cards("maxcalm", "Add a MaxCalm to your deck?") from _call_label_home_add_cards_13
            "X":
                return    
    elif g.plant <= 2:
        menu:
            "water it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant") from _call_label_home_add_cards_14
            "meditate":
                call label_home_add_cards("maxcalm", "Add a MaxCalm to your deck?") from _call_label_home_add_cards_15
            "admire it":
                call label_home_add_cards("newday", "Add a NewDay to your deck?") from _call_label_home_add_cards_16
            "X":
                return
    else:
        menu:
            "water it":
                call label_home_add_cards("calm", "Add a Calm to your deck?", callback="label_water_the_plant") from _call_label_home_add_cards_17
            "meditate":
                call label_home_add_cards("maxcalm", "Add a MaxCalm to your deck?") from _call_label_home_add_cards_18
            "admire it":
                call label_home_add_cards("newday", "Add a NewDay to your deck?") from _call_label_home_add_cards_19
            "study it":
                call label_home_add_cards("fibonacci", "Add a Fibonacci to your deck?") from _call_label_home_add_cards_20
            "X":
                return
    return

label label_home_add_cards(cardID, prompt, callback=True):
    show expression trans_show_card_2(Card(cardID).img) as card
    menu:
        "[prompt]"
        "yes":
            hide card
            hide screen screen_tutorial
            call label_add_card_to_deck("list", Card(cardID), 300, 500) from _call_label_add_card_to_deck_2
            if callback:
                if callback == True:
                    call label_newDay('label_home') from _call_label_newDay_23
                else:
                    call expression callback from _call_expression_10
        "no":
            hide card
            hide screen screen_tutorial
    return


label label_pic3_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic3.png" at truecenter
    
    with dissolve
    pause
    "This picture is turning you on…"
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
    call label_home_phone from _call_label_home_phone
    return

label label_pic7_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic7.png" at truecenter
    
    with dissolve
    pause
    "It seems like she took care of your cat while you were away."
    "Maybe she's not so bad."
    "The End"
    window hide
    show screen game_complete with Dissolve(2.0)
    return

label label_pic6_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic6.png" at truecenter
    
    with dissolve
    pause
    "This picture is turning you on…"
    "Lust +20"
    $ game.lust += 20
    play sound "rpg/Lust.wav"
    window hide 
    pause
    window auto
    hide expression "Joyce/selfie/pic6.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone from _call_label_home_phone_1
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
            $ g.phoneLogs[g.phoneProgress[0]] += [[3, "pic-cat.png"], [0, "omggg is it yours? so cuuute"], [2, "yuuup"]]
        "No":
            $ g.phoneLogs[g.phoneProgress[0]] += [[2, "cool"]]
    window hide 
    window auto
    hide expression "Joyce/selfie/pic2.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone from _call_label_home_phone_2
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
            $ g.phoneLogs[g.phoneProgress[0]] += [[2, "I like the red dress"], [0, "the cleavage is so biiig though"],[2, "You'll pull it off"],[0, "yea I'm sure you're gonna enjoy the view."],[0, ";-P"]]
            $ whichDress = "red"
        "Blue":
            $ g.phoneLogs[g.phoneProgress[0]] += [[2, "I like the blue dress"], [0, "i might not fit in anymore, "],[0, "I gained so much weight since the last time I wore it."],[2, "You'll pull it off"],[0, "near the chest area"],[0, ";-P"]]
            $ whichDress = "blue"
    window hide 
    window auto
    hide expression "Joyce/selfie/pic4.png"
    hide expression "#000a"
    with dissolve
    $ game.jeu_sensitive = True
    call label_home_phone from _call_label_home_phone_3
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
                $ g.phoneLogs[3].append( [2, "There's a [sudokuNumber[0]] in row [sudokuNumber[1]], column [sudokuNumber[2]]"])
                # $ g.phoneLogs[3].append( [2, "sudoku_pos [sudoku_pos]"])
                if len(answer) <= sudoku_pos and answer[sudoku_pos] == str(sudokuNumber[0]):
                    $ g.phoneLogs[3].append( [0, "Wow! How did you find that? Thanks!"])
                    $ g.phoneLogs[3].append( [2, "+3 trust, +3 attraction"])
                    $ g.phoneLogs[3].append( [0, "what?"])
                    $ g.phoneLogs[3].append( [2, "dont worry about it ;-)"])
                    $ g.phoneLogs[3].append( ["exe", "game.trust+=3; game.attraction+=3; renpy.call('label_home_phone')"])
                else:
                    $ g.phoneLogs[3].append( [0, "thanks! I'll see what I can do with that."])
            "No":
                $ g.phoneLogs[3].append( [2, "Good luck with that!"])
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
    call label_home_phone from _call_label_home_phone_4
    return