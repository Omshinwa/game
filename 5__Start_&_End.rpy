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
    show screen screen_debug
    if game.debug_mode:
        $ renpy.run(Start())
    if persistent.displayContentWarning:
        call screen screen_content_warning with dissolve
    $ renpy.run(Start(label="custom_main_menu"))
    return

# will dump you directly to the start label & start the game.
# You do have to return from the splashscreen label or it doesn't leave the menu context properly

# label splashscreen:
#     show splash
#     pause 0.5
#     hide splash with dissolve
#     return
#label splashscreen is displayed before anything, need a return

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

label custom_main_menu:
    show screen screen_debug
    # $ quick_menu = False
    $ quick_menu = True
    $ game.jeu_sensitive = True
    default deck = Deck()
    $ deck = Deck()
    $ deck.deck = [Card("newgame"), Card("continue"), Card("load"), Card("prefs"), Card("achievement")]
    # hide screen main_menu
    scene bg park
    show fg bar-table onlayer master zorder 2
    show joyce outfit1 smile at sitting
    with dissolve
    show screen screen_date_bottom_ui() onlayer master zorder 2
    pause 0.5
    $ deck.draw(5)
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
    use screen_deck_stack