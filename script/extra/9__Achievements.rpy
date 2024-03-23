init python:
    basic_achievements = (
        ("Exodia", "Complete and play Origin of the World."),
        ("Suspicious", "Avoid getting stripPoker_got_drugged."),
        ("Third Base", "Have sex with Joyce."),
        ("Progress..?", "Finish the first act."),
        ("Progress!", "Finish the second act."),
        ("Space Conquest", "Make a Space themed deck"),
        ("Space Conquest", "Have 10 'do nothing' in your deck."),
        ("Hand Full", "Have 8 cards in hand."),
        ("Hand xtra Full", "Have 15 cards in hand."),
        ("Explosion", "Change one of you stat by 100 or more in one go."),
    )
    achievement.register("Exodia")

    def grant_with_notification(achievement_name):
        print(achievement_name)
        if not achievement.has(achievement_name):
            renpy.notify(_("Got the achievement ' %s ' !" % achievement_name)  )
            achievement.grant(achievement_name)

    achievement.grant_with_notification = grant_with_notification

screen screen_achievement():
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


# secret devlog
"""
Q: Who's Joyce? Is it someone you know?
A: She's losely inspired by a coworker I knew, at least that's where her name comes from. Mostly she's fictionnary.

Q: Do you have BDSM fetishes?
A: Not really. I just thought for a card-based game, you needed some kind of opposition for it to make sense. Hence the "don't cum" mechanic, it's like Health Points in a RPG. This is mostly the reason for the BDSM content lol. 

Back a few months/years ago I had another small project (that never came to fruition) with a blonde girl who you get stranded on
an island with. You play some card games with her. In general I just like card games.

The real idea of this game came when I played "Queen of Hearts" by uskprod, it was a rather small indie game for a gamejam, but I had a blast playing it. The gameloop is already present, it's a good proof of concept. I just thought it could need some polish, better artwork, and deeper card mechanics.
https://uskprod.itch.io/queen-of-hearts
The SM part came because I thought it would be the best way to put a confrontational game mechanic, you fight against her but how? You resist cumming from her, that's it. I also think the idea of progressively having harder and harder challenges was hot.

I redrew Joyce's sprite for the full game, it took quite a while actually.
I would just keep redesigning again and again.
Ultimately I changed the lighting on her face (you can see the left side is almost all white).
This is inspired by old japanese Visual Novel, the art of some studio like elf. Their sprite work was really good and you can see
this distintive lighting that really emphasizes the volume of the face.
"""