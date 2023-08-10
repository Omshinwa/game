screen choice(items):
    modal True
    style_prefix "choice"

    hbox: 
        spacing int( 200/(len(items)-1) )
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
