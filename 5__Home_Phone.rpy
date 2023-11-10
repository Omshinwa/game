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
    
    modal True #break pauses?

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


    fixed at switch:
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
                            
                            # elif index<=g.phoneProgress[1]-4:
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

                vbar adjustment phone_Scroll xalign 1.08 ysize 600 yalign 0.5 xsize 20 bar_invert True base_bar "#fff" thumb "#aaa"#unscrollable "hide" 

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
