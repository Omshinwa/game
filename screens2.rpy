screen choice(items):
    style_prefix "choice"

    hbox:
        for i in items:
            textbutton i.caption action i.action

style choice_hbox is hbox
# style choice_button is button
# style choice_button_text is button_text

style choice_hbox:
    yalign 0.5
    # xpos 405
    # xanchor 0.5
    xalign 0.5

    spacing 200 # gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    ysize 400
    xsize 300
    

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.5
    size 50