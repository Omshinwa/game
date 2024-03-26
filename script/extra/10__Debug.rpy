# # BACKWARD COMPATIBILITY SAVE STUFF
# default game._lustPerDay = "game.progress[0] + 1"
# default game.act = 0

default game = Game()
# default date = Date("date")
default date.neutralJoyce = "joyce null"

init 50 python:
    deckdebug = Deck()
    for card in cardList:
        if "value" in cardList[card]:
            deckdebug.list.append(Card(card))
    deckdebug.list += [Card("ask"),Card("listen"),Card("chat"),Card("eyecontact"),Card("touchy"),Card("flirt"),Card("listen"),Card("touchy")]

    # when we wanna jump into a label but have empty deck, no lust etc

    def debug_deck_playtest():
        global deck, game, date
        if len(deck.list) == 0:
            deck = deckdebug
            game.lustMax = 50
            date.lustMax = 50

label label_image_tools:
    call screen image_tools


screen screen_debug_menu():
    fixed:
        add "#222" 

        # A grid of buttons.
        vpgrid cols 5:
            align (0.5, 0.5)
            xfill True
            yfill True
            textbutton "Image Tools" action Call("label_image_tools") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "library" action Call("label_library") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "DOGGY" action Call("label_doggy") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "jogging" action Call("label_jogging") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "poker" action Call("label_stripPoker") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "picnic" action Call("label_picnic") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "beach" action Call("label_beach") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "footjob" action Call("label_footjob") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "handjob" action Call("label_handjob") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "titjob" action Call("label_titjob") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "blowjob" action Call("label_blowjob") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "cowgirl" action Call("label_cowgirl") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color

            # The screen is responsible for returning to the main menu. It could also
            # navigate to other gallery screens.
            textbutton "Return" action MainMenu(confirm=False,save=False) text_color "#fff" text_hover_color gui.hover_color xalign 0.5 yalign 0.5
