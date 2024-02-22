init python:
    basic_achievements = (
        ("Exodia", "Complete and play Origin of the World."),
        ("Suspicious", "Avoid getting stripPoker_got_drugged."),
        ("Third Base", "Have sex with Joyce."),
        ("Progress..?", "Finish the first act."),
        ("Progress!", "Finish the second act."),
    )
    achievement.register("Exodia")

    def grant_with_notification(achievement_name):
        print(achievement_name)
        if not achievement.has(achievement_name):
            renpy.notify(_("Got the achievement ' %s ' !" % achievement_name)  )
            achievement.grant(achievement_name)

    achievement.grant_with_notification = grant_with_notification

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
        action MainMenu(confirm=False,save=False)

    textbutton _("Forget All(!)"):
        style "return_button"
        xalign 0.5
        text_color "#fff"
        text_hover_color "#ff0"
        action Function(achievement.clear_all)
