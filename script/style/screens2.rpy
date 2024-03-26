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
            textbutton i.caption action i.action xsize max(300,len(i.caption)*7) ysize max(400,len(i.caption)*10) at anim_choice(n)

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
    xalign 0.5

style choice_button is default:
    properties gui.button_properties("choice_button")
    # background Frame('gui/button/choice_idle_bac_test.png')

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.5
    size 50
    font "fonts/Venus+Carrare.otf"
    

screen quick_menu():
    
    key 'K_F2' action [Show("screen_debug"),ToggleVariable("game.debug_mode")]
    key 'K_2' action ShowMenu("layered_image_visualizer")

    zorder 100

    if _in_replay:
        textbutton _("end replay") action EndReplay(False) xalign 1.0 yalign 1.0 text_color "#fff" text_hover_color "#b2f5ce"
    else:
        if quick_menu:
            
            if renpy.variant("touch"):
                hbox:
                    xanchor 1.0
                    xpos 1920
                    yalign 0.0
                    textbutton _("<back<") action Rollback() text_size 70 text_color "#fff" text_hover_color "#b2f5ce"
                    textbutton (".") action NullAction() text_size 70 text_color "#fff"
                    textbutton _(">skip>") action Skip() text_size 70 text_color "#fff" text_hover_color "#b2f5ce"
                vbox:
                    style_prefix "quick"

                    xanchor 1.0
                    xpos 1920
                    yalign 1.0
                    textbutton _("menu") action ShowMenu('preferences') text_size 70 text_color "#fff" text_hover_color "#b2f5ce" 
            else:
                vbox:
                    style_prefix "quick"

                    xanchor 1.0
                    xpos 1920
                    yalign 1.0
                    textbutton _("menu") action ShowMenu('preferences') text_size 50 text_color "#fff" text_hover_color "#b2f5ce" 


style style_debug_text:
    size 40 color "#FF0" ypos 0 outlines [ (4, "#050505", 0, 2) ]
screen screen_debug():
    zorder 100

    if game.debug_mode:
        
        text " ".join(config.variants[:-1]) align (1.0, 0.05) color "#fff"
        
        drag:
            xalign 0.0 yalign 1.0
            vbox:
                text "game.isHoverHand: "  + str(game.isHoverHand) + "\ngame.jeu_sensitive: " + str(game.jeu_sensitive) + "\ngame.progress: "+str(game.progress[0]) + "," + str(game.progress[1]) style "style_debug_text"
                if game.state == "dating" or game.state == "sexing":
                    if game.state == "sexing":
                        text "anim_speed: " + str(animation_speed) + " ( " + str(date.animation_speed) + " )" style "style_debug_text"
                    text "date.lust: " + str(date.lust) style "style_debug_text"
                    text "date.turn: " + str(date.turn) style "style_debug_text"
                text "label:" + (current_label) style "style_debug_text"
                text str(renpy.game.context().current) style "style_debug_text"
                if renpy.get_attributes("joyce"):
                    text "joyce " + " ".join(renpy.get_attributes("joyce")) style "style_debug_text"
                    