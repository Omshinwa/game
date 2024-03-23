#############################################################################
##                                                                                     
##
##                ███████ ████████  █████  ██████  ████████ 
##                ██         ██    ██   ██ ██   ██    ██    
##                ███████    ██    ███████ ██████     ██    
##                     ██    ██    ██   ██ ██   ██    ██    
##                ███████    ██    ██   ██ ██   ██    ██   
##
##
#############################################################################


label main_menu:

    # $ game.debug_mode = True
    show screen screen_debug
    if persistent.displayContentWarning:
        call screen screen_content_warning with dissolve
    $ renpy.run(Start(label="custom_main_menu"))
    return


label splashscreen:
    show splash
    pause 0.5
    hide splash with dissolve
    return
# label splashscreen is displayed before anything, need a return


screen screen_content_warning():
    add "#000"
    vbox:
        xalign 0.5
        fixed:
            add "#1a1e38"
            xsize 1400
            xalign 0.5
            text """
    {color=#f00}{b}Content Warning{/b}{/color}

    All the characters, places, and events are purely fictional and for entertainment purposes only. All the characters are 18 years of age or older. 

    This game feature sex scenes, if you don't feel comfortable viewing such content, you are advised to close the game.
                
    By clicking play you agree that you are at least 18 years old and consent to seeing explicit content.
                """  color "#ffffff" xsize 1300 xalign 0.5 yalign 0.2 size 40 justify True textalign 0.5
            button:
                text _("Play") size 50 align (0.5,0.5)
                action [SetVariable("persistent.displayContentWarning", False), Start(label="custom_main_menu")]
                yalign 0.85 xalign 0.2 xysize (200,200) background "#fff"
                hover_background "#8080ff"
            button:
                text _("Quit") size 50 align (0.5,0.5)
                action Quit(False)
                yalign 0.85 xalign 0.8 xysize (200,200) background "#fff"
                hover_background "#8080ff"

"""
This is the custom main menu with joyce in the casino
"""

label custom_main_menu:

    $ game = Game()
    $ date = Date("date")
    # $ preferences.fullscreen = True
    
    $ renpy.set_return_stack([])

    show screen screen_debug
    # $ quick_menu = False
    $ quick_menu = True
    $ game.jeu_sensitive = False 
    $ deck = Deck()
    $ deck.deck = [Card("newgame"), Card("prefs"), Card("achievement"), Card("memory"), Card("lang"), Card("fullscreen"), Card("debug")]

    scene bg casino at trs_bg_blur
    show fg poker-table onlayer master zorder 2 
    show joyce outfitcasino smile hair_braids at trs_sitting, trs_slowbreath
    show joyce_hand_poker onlayer master zorder 2
    with dissolve
    show screen screen_date_bottom_ui() onlayer master zorder 2
    show screen screen_dating_deck_stack onlayer master zorder 2
    $ deck.draw(7)
    $ game.jeu_sensitive = True
    # $ renpy.say(j, "Which game are we playing?")
    j "Which game are we playing?"
    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop


#############################################################################
##                                                                                     
##
##                      ███████ ███    ██ ██████  
##                      ██      ████   ██ ██   ██ 
##                      █████   ██ ██  ██ ██   ██ 
##                      ██      ██  ██ ██ ██   ██ 
##                      ███████ ██   ████ ██████  
##
##
#############################################################################

screen game_complete():
    $ i = ["1","2","3","4","5-"+whichDress,"6","7","1","2","3"]
    add "#ffb6e1"

    fixed at image_qui_defile:
        xsize 500 xpos 20
        for index,img in enumerate(i):
            add "Joyce/selfie/pic"+img+".png" xysize 500,500 ypos index*510 alpha .7
    fixed:
        xsize 1100 xpos 550
        text "Thanks for playing '{b}Dating Joyce{/b}' v0.5 for the Summer of Smut Jam.\n\nI plan on making a full release of the game soon.\n\nFollow my itch.io to get notified!":
            color "#ffffff" xalign 0.5 yalign 0.6 size 40 justify True textalign 0.5
        text "Game completed in [game.day] days !":
            color "#ffffff" xalign 0.7 ypos 150 style "quirky_command" textalign 0.5

    text "Omshinwa18" yalign 0.85 xalign 0.8 size 60 style "outline_text"
    textbutton _("https://omshinwa18.itch.io/ (click me)") action OpenURL("https://omshinwa18.itch.io/") yalign 0.9 xalign 0.8 
    textbutton _("@Omshinwa18 (click me)") action OpenURL("https://twitter.com/Omshinwa18") yalign 0.94 xalign 0.8 
    # Consider leaving a good review if you enjoyed the game, it goes a long way to help me keep working!
    use screen_deck_stack

# credits: people in the renpy server:
# renpytom Junior @juniorthejunior Pinky! HB38  Fen (Feniks) + link seronis Jse(idk how much he helped lol)
# Consider leaving a good review if you enjoyed the game, it goes a long way to help me keep working!



## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Game made by {a=https://twitter.com/Omshinwa18}Omshinwa{/a}.

Thank you for playing (and hopefully) buying the game. If you didn't buy the
game, please and go buy it, that would really help me lol. If you DID buy it,
my bad, thank you again.

I want to thank the people from the Renpy discord server, they were very helpful
and friendly. In no particular order: HB38, Junior, Jse, Pinky!, seronic. I also
used Feniks' renpy tools @ feniksdev.com

Thank you renpytom for building such an amazing free tool and community.

Other people I want to mention: Gwenael.

I also want to thank my girlfriend for bearing with me while I was making this
stupid project lol. Also my mother, she took very much care of me, cooked for me,
did the laundry etc. I am very spoiled.
""")


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        frame:
            vbox:

                label "{size=+20}[config.name!t]{/size}"
                text _("Version [config.version!t]\n")

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

                text ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_frame:
    background Frame("gui/blue_gradient.png")

style about_label_text:
    size gui.label_text_size

