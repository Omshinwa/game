define BALANCE = {"keepStat":True}

define j = Character(None, image="joyce", kind=bubble)
define rat = Character(None, image="rat", kind=bubble)

default povname = "William"
# define pov = Character(None, what_italic=True)#, what_prefix='"', what_suffix='"')
    
default game = Game()
default date = Date("date")

# The game starts here.

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

screen Content_Warning():
    add "#000"
    vbox:
        xalign 0.5
        fixed:
            add "#1a1e38"
            xsize 1400
            xalign 0.5
            text """
{color=#f00}{b}Content Warning{/b}{/color}

All the characters, places, and events are purely fictional and for entertainment purposes only. All the characters in this game that engage in sexual activities in any way are 18 years of age or older. 
This game features depictions of sexual assault. The author does not condone rape. If you don't feel comfortable viewing such content, you are advised to close the game.
            
By clicking play you agree that you are at least 18 years old and consent to seeing explicit content.
            """  color "#ffffff" xsize 1300 xalign 0.5 yalign 0.2 size 40 justify True textalign 0.5
            button:
                text _("Play") size 50 align (0.5,0.5)
                action Jump("start2")
                yalign 0.85 xalign 0.2 xysize (200,200) background "#fff"
                hover_background "#8080ff"
            button:
                text _("Quit") size 50 align (0.5,0.5)
                action Call("_confirm_quit") 
                yalign 0.85 xalign 0.8 xysize (200,200) background "#fff"
                hover_background "#8080ff"

label start:
    show screen Content_Warning()
    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop

label start2:
    hide screen Content_Warning
    #set up the deck and keybinds

    default deck = Deck()

    python:
        CARD_IMG_DICT = {}
        for card in cardList:
            CARD_IMG_DICT[card] = Image("cards/" + card + ".png")

    $ deck.list = [Card("talk"),Card("talk"),Card("talk"),Card("calm"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    Card("spaceout"),Card("listen"),Card("eyecontact"),Card("draw2"),Card("touchy"),Card("pair"),Card("recycle")]

    # python:
    #     for card in cardList:
    #         deck.list.append(Card(card))
    
    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "William"

    $ game.day = 0
    show screen keybinds()
    show screen screen_debug

    jump label_tutorial

    # jump label_home
    # jump test_sprites

    return