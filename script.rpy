# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    use screen_deck_stack

label start:
    
    #set up the deck and keybinds

    default deck = Deck()

    # $ deck.list = [Card("drink"),Card("drink"),Card("drink"),Card("devil"),Card("devil"),Card("fibonacci"),Card("fibonacci"),Card("fibonacci"),Card("fibonacci"),Card("peek"),Card("peek"),]
    
    $ deck.list = [Card("talk"),Card("talk"),Card("talk"),Card("calm"),Card("spaceout"),Card("spaceout"),Card("spaceout"),Card("spaceout"),
    Card("spaceout"),Card("listen"),Card("eyecontact"),Card("draw2"),Card("touchy"),Card("pair"),Card("recycle")]

    # python:
    #     for card in cardList:
    #         deck.list.append(Card(card))

    show screen keybinds()
    show screen screen_debug

    # jump label_prison_first_time
    jump label_home
    jump test_sprites

    return