#############################################################################
##                                                                                     
##
##        ███████  ██████ ██████  ███████ ███████ ███    ██ ███████ 
##        ██      ██      ██   ██ ██      ██      ████   ██ ██      
##        ███████ ██      ██████  █████   █████   ██ ██  ██ ███████ 
##             ██ ██      ██   ██ ██      ██      ██  ██ ██      ██ 
##        ███████  ██████ ██   ██ ███████ ███████ ██   ████ ███████ 
##
##
#############################################################################

screen screen_home_phone:
    
    modal True

    sensitive game.jeu_sensitive
    
    # if hidePhone:
    #     button:
    #         xsize 1.0
    #         ysize 1.0
    #         action Hide("screen_home_phone", None, _layer="master")
    # else:
    #     button:
    #         xsize 1.0
    #         ysize 1.0
    #         action Call("label_home_phone")


    button:
        xsize 1.0
        ysize 1.0
        action Call("label_home_phone")


    fixed at trs_phone:
        xsize 523
        ysize 918
    
        imagebutton:
            idle "home/phone-big.png"
            action [Call("label_home_phone")]
        
        
        if g.phoneProgress[0] in g.phoneLogs:
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

                        for index, message in enumerate( g.phoneLogs[g.phoneProgress[0]] ):
                            
                            if index>g.phoneProgress[1]: #only display msg sent
                                break
                    
                            #text msg
                            if message[0] == 0: 
                                frame:
                                    padding (30, 10)
                                    background Frame("home/phone-bubble.png")
                                    text message[1] size 33 xalign 0.5
                                    
                                    xmaximum 300

                            #picture
                            elif message[0] == 1: 
                                default disp = "home/" + message[1]
                                frame:
                                    padding (30, 10)
                                    background Frame(Transform("home/phone-bubble.png", matrixcolor=TintMatrix((255,230,153))))
                                    imagebutton:
                                        sensitive g.phoneProgress[1]+1 >= len(g.phoneLogs[g.phoneProgress[0]]) # if the whole log was shown
                                        hover tintImg("Joyce/selfie/small-" + message[1], (1.3*255,1.3*255,1.3*255))
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
                                    background Frame(Transform("home/phone-bubble-me.png", matrixcolor=TintMatrix((332,332,128))))
                                    text message[1] size 33 xalign 0.5
                            elif message[0] == 3: #my photo
                                frame:
                                    xmaximum 300
                                    xanchor 1.0
                                    xpos 420
                                    padding (30, 10)
                                    background Frame(Transform("home/phone-bubble-me.png", matrixcolor=TintMatrix((421,255,242))))
                                    add "Joyce/selfie/small-" + message[1]
                                
                        fixed:
                            ysize 0

                vbar adjustment phone_Scroll xalign 1.08 ysize 600 yalign 0.5 xsize 20 bar_invert True base_bar "#fff" thumb "#aaa"

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

# make the phone logic progress through the log
label label_home_phone():

    if g.phoneProgress[0] not in g.phoneLogs:
        hide screen screen_home_phone onlayer master
        return

    $ messagelog = g.phoneLogs[g.phoneProgress[0]]

    if len(messagelog)-1 > g.phoneProgress[1]:  #if the log hasnt been completed yet
        
        $ g.phoneProgress[1] += 1

        $ typeOfLastMsg = messagelog[g.phoneProgress[1]][0]
        $ contentLastMsg = messagelog[g.phoneProgress[1]][1]
        
        if typeOfLastMsg != "exe":
            play sound "day/newmsg.wav"

        elif typeOfLastMsg == "exe":
            $ commands = contentLastMsg.split("; ")
            $ g.phoneLogs[g.phoneProgress[0]].pop(g.phoneProgress[1])  # POP THE EXE MSGS
            $ g.phoneProgress[1] -= 1

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


###
###
###             REACTIONS TO PICTURES
###
### Function(renpy.mark_image_seen,"Joyce/selfie/" + message[1]


label label_pic2_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic2.png" at truecenter
    $ renpy.mark_image_seen("Joyce/selfie/pic2.png")
    
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
    $ renpy.mark_image_seen("Joyce/selfie/pic4.png")
    
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

label label_pic3_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic3.png" at truecenter
    $ renpy.mark_image_seen("Joyce/selfie/pic3.png")
    
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

label label_pic6_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic6.png" at truecenter
    $ renpy.mark_image_seen("Joyce/selfie/pic6.png")
    
    with dissolve
    pause
    "This picture is turning you on..."
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

label label_pic7_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic7.png" at truecenter
    $ renpy.mark_image_seen("Joyce/selfie/pic7.png")
    
    with dissolve
    pause
    "It seems like she took care of your cat while you were away."
    "Maybe she's not so bad."
    "The End"
    window hide
    show screen game_complete with Dissolve(2.0)
    return


label label_pic1_reaction:
    $ game.jeu_sensitive = False
    show expression "#000a"
    show expression "Joyce/selfie/pic1.png" at truecenter
    $ renpy.mark_image_seen("Joyce/selfie/pic1.png")
    
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
                
                
                $ answer = """4_7_______3__7_26___2_3__75683149_5__5478___17193256_8____125_7___4_315__215_74__"""
                $ sudoku_pos = (sudokuNumber[1]-1)*9 + (sudokuNumber[2]-1)
                $ osef = "There's a [sudokuNumber[0]] in row [sudokuNumber[1]], column [sudokuNumber[2]]"
                $ g.phoneLogs[3].append( [2, osef])
                $ del osef
                if sudokuNumber[1]==0 or sudokuNumber[2]==0:
                    $ g.phoneLogs[3].append( [0, "Em..."])
                    $ g.phoneLogs[3].append( [0, "Nevermind..."])
                elif answer[sudoku_pos] == str(sudokuNumber[0]): # len(answer) > sudoku_pos and 
                    $ g.phoneLogs[3].append( [0, "Wow! How did you find that? Thanks!"])
                    $ g.phoneLogs[3].append( [2, "+3 trust, +3 attraction"])
                    $ g.phoneLogs[3].append( [0, "what?"])
                    $ g.phoneLogs[3].append( [2, "dont worry about it ;-)"])
                    $ g.phoneLogs[3].append( ["exe", "game.trust+=3; game.attraction+=3; renpy.call('label_home_phone')"])
                    $ renpy.with_statement(ImageDissolve("gui/transition.png", 0.2, reverse=True) )
                elif answer[sudoku_pos] == "_":
                    $ g.phoneLogs[3].append( [0, "Em, I already put a number there..."])
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