define config.modal_blocks_pause = False # setting modal on screen made pausing with time not work
define config.say_attribute_transition_layer = "master"
define config.say_attribute_transition = Dissolve(.2)

init python:
    
    class ToggleTouchMode(Action): # custom action

        def __init__(self, bool):
            self.bool = bool

        def __call__(self):
            if "touch" in config.variants:
                for index, value in enumerate(config.variants):
                    if value == "touch":
                        config.variants.pop(index)
                        break
            else:
                config.variants.insert(0, "touch")

            renpy.restart_interaction()

        def get_selected(self):
            return int("touch" in config.variants) == self.bool

screen choice(items):
    modal True
    style_prefix "choice"

    hbox: 
        spacing int( 300/(len(items)) )
        for n, i in enumerate(items):
            textbutton i.caption action i.action at anim_choice(n)

transform anim_choice(t):
    yoffset ((t%2)*2-1) * 1000
    easein 0.5 yoffset 0
    on hover:
        linear 0.1 ypos -20
    on idle:
        linear 0.1 ypos 0

    
style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_hbox:
    yalign 0.5
    # xpos 405
    # xanchor 0.5
    xalign 0.5

    # spacing gui.choice_spacing # 200 

style choice_button is default:
    properties gui.button_properties("choice_button")
    ysize 400
    xsize 300
    

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.5
    size 50
    font "fonts/Venus+Carrare.otf"

screen quick_menu():
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0
            textbutton _("menu") action ShowMenu('preferences') text_size 50 text_color "#fff" text_hover_color gui.hover_color

screen screen_debug:
    zorder 100
    key 'K_F2' action ToggleVariable("game.debug_mode",1,0)

    if game.debug_mode:
        
        text " ".join(config.variants[:-1]) align (1.0, 0.05) color "#fff"
        
        drag:
            fixed:
                xsize 500
                ysize 200
                xalign 0.0 yalign 0.3
                text "debug_mode\ngame.isHoverHand: "  + str(game.isHoverHand) + "\ngame.jeu_sensitive: " + str(game.jeu_sensitive) + "\ngame.progress: "+str(game.progress[0]) + "," + str(game.progress[1]):
                    size 40 color "#FF0" ypos 0 outlines [ (absolute(4), "#050505", absolute(0), absolute(2)) ]