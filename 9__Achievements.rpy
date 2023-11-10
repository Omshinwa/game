init python:
    basic_achievements = (
        ("Exodia", "Complete and play Origin of the World."),
        ("Suspicious", "Avoid getting drugged."),
        ("Third Base", "Have sex with Joyce."),
        ("Progress..?", "Finish the first act."),
        ("Progress!", "Finish the second act."),
    )
    achievement.register("Exodia")

screen screen_achievement:
    modal True
    add "#222"
    text "{color=#888}why this shit" align (0.5,0.5)
    vbox:
        for name, desc in basic_achievements:
            if achievement.has(name):
                text "{color=#ff6}done! " + name + ":{/color} {color=#ccc}" + desc + "{/color}"
            else:
                text "{color=#777}???: " + desc + "{/color}"
    
    textbutton _("Return"):
        style "return_button"
        text_color "#fff"
        text_hover_color "#ff0"
        action Return()
