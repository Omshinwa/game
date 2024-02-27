label label_jogging:
    scene bg chemin-1 at trs_bg_blur(6, "soft")
    # scene Color("#00f")
    # show fg terrasse-table onlayer master zorder 2
    "this is a planned date: jogging, right now it's still in development"
    show joyce outfitsport running breath at trs_slowbreath, trs_depied
    show bg at trs_bg_blur(4, "hard")
    j "hard"
    show bg chemin-pixel4 at trs_bg_blur(4, "hard")
    j "chemin-pixel2"
    show bg chemin-pixel4 at trs_bg_blur(4, "soft")
    j "Let's go for a run!"
    show bg chemin-10 at trs_bg_blur(4, "soft")
    j undress foxy smile sweaty "Fiou, I'm so sweaty!"
    show bg chemin-10 at trs_bg_blur(0)
    j undress foxy smile "It's so hot!"
    j outfitsport2 -undress "hehe"
    j running "RUN"
    $ test = renpy.game.context().current
    j "[test]"
    
    call label_after_successful_Date_common
    $ g.phoneProgress[0] -= 2
    $ g.phoneProgress[1] = 10
    call label_newDay("label_home")

    label .gameLoop:
        show joyce null with dissolve
        if len(deck.hand) == 0:
            pass

label label_jogging_endTurn:
    call label_date_isLost_common