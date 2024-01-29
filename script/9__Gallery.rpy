define config.enter_replay_transition = pixellate
define config.exit_replay_transition = pixellate

init python:
    class customGallery(Gallery):
        def make_button(self, name, unlocked, locked=None, hover_border=None, idle_border=None, style=None, **properties):
        
            action = self.Action(name)

            if locked is None:
                locked = self.locked_button

            if hover_border is None:
                hover_border = self.hover_border

            if idle_border is None:
                idle_border = self.idle_border

            if style is None:

                if (config.script_version is not None) and (config.script_version <= (7, 0, 0)):
                    style = "button"
                else:
                    style = "empty"
            return Button(action=action, child=unlocked, insensitive_child=Transform(unlocked, matrixcolor=OpacityMatrix(0.2) ), hover_foreground=hover_border, idle_foreground=idle_border, style=style, **properties)

    # Step 1. Create the gallery object.
    gallery = customGallery()
    gallery.locked_button = Solid("#0005")
    gallery.hover_border = Solid("#ff83")
    gallery.idle_border = Solid("#0000")
    
    #DEFINING SELFIES
    gallery.button("01")
    gallery.unlock_image("Joyce/selfie/pic1.png")

    gallery.button("02")
    gallery.unlock_image("Joyce/selfie/pic2.png")

    gallery.button("03")
    gallery.unlock_image("Joyce/selfie/pic3.png")

    gallery.button("04")
    gallery.unlock_image("Joyce/selfie/pic4.png")

    gallery.button("05")
    gallery.unlock_image("Joyce/selfie/pic5-blue.png")
    gallery.unlock_image("Joyce/selfie/pic5-red.png")

    gallery.button("06")
    gallery.unlock_image("Joyce/selfie/pic6.png")


    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    gallery.button("07")
    gallery.condition("achievement.has('Exodia')")
    gallery.image("pic7")

screen screen_gallery:

    default mode = "cg"

    # Ensure this replaces the main menu.
    tag menu

    modal True

    
    grid 2 1:
        xfill True
        yfill True
        align (0.5, 0.0) xysize (0.9, 0.15)
        button:
            action SetScreenVariable("mode","cg") 
            if mode == "cg":
                add "#be4242" 
            else:
                add "#929292" 

            text _("CGs") color "#fff"  hover_color gui.hover_color align (0.5, 0.5)
        button:
            action SetScreenVariable("mode","replay") 
            if mode == "replay":
                add "#be4242" 
            else:
                add "#929292" 
            text _("REPLAY")  color "#fff"  hover_color gui.hover_color align (0.5, 0.5)

    if mode == "cg":
        use screen_gallery_cg
    else:
        use screen_gallery_replay


    # Displays a set of images in the gallery, or indicates that the images
    # are locked. This is given the following arguments:
    #
    # locked
    #     True if the image is locked.
    # displayables
    #     A list of transformed displayables that should be shown to the user.
    # index
    #     A 1-based index of the image being shown.
    # count
    #     The number of images attached to the current button.
    # gallery
    #     The image gallery object.

style style_text_button:
    
    color "#fff"
    hover_color gui.hover_color
    xalign 0.5
    yalign 0.5

screen screen_gallery_replay:
    fixed:
        align (0.5, 0.7) xysize (0.9, 0.8)
        add "#222" 

        # A grid of buttons.
        grid 4 3:
            align (0.5, 0.5)
            xfill True
            yfill True

            # Call make_button to show a particular button.
            textbutton "footjob" action Replay("label_footjob") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "footjob" action Call("label_footjob") style "style_text_button" text_color "#fff" text_hover_color gui.hover_color
            textbutton "handjob" action Replay("label_handjob") style "style_text_button"


            # The screen is responsible for returning to the main menu. It could also
            # navigate to other gallery screens.
            textbutton "Return" action MainMenu(confirm=False,save=False) text_color "#fff" text_hover_color gui.hover_color xalign 0.5 yalign 0.5

screen screen_gallery_cg:
    fixed:
        align (0.5, 0.7) xysize (0.9, 0.8)
        add "#222" 

        # A grid of buttons.
        grid 4 3:
            align (0.5, 0.5)
            xfill True
            yfill True

            # Call make_button to show a particular button.
            add gallery.make_button("01", "small-pic1", xalign=0.5, yalign=0.5)
            add gallery.make_button("02", "small-pic2", xalign=0.5, yalign=0.5)
            add gallery.make_button("03", "small-pic3", xalign=0.5, yalign=0.5)
            add gallery.make_button("04", "small-pic4", xalign=0.5, yalign=0.5)
            add gallery.make_button("05", "small-pic5-blue", xalign=0.5, yalign=0.5)
            add gallery.make_button("06", "small-pic6", xalign=0.5, yalign=0.5)
            add gallery.make_button("07", "small-pic7", xalign=0.5, yalign=0.5)


            # The screen is responsible for returning to the main menu. It could also
            # navigate to other gallery screens.
            textbutton "Return" action MainMenu(confirm=False,save=False) text_color "#fff" text_hover_color gui.hover_color xalign 0.5 yalign 0.5

screen _gallery(locked, displayables, index, count, gallery, **properties):
        tag menu
        # modal True #you can remove that, then clicking automatically goes to the next image
        add "#000a"
        if locked:
            # add "#000"
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
            for d in displayables:
                add d:
                    xalign 0.5
                    yalign 0.5

        if gallery.slideshow:
            timer gallery.slideshow_delay action Return("next") repeat True

        key "game_menu" action gallery.Return()

        use gallery_navigation(gallery=gallery)

screen gallery_navigation(gallery):
    tag menu
    hbox:
        spacing 20

        style_group "gallery"
        align (.98, .98)

        textbutton _("prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
        textbutton _("next") action gallery.Next(unlocked=gallery.unlocked_advance)
        textbutton _("slideshow") action gallery.ToggleSlideshow()
        textbutton _("return") action gallery.Return()

init python:
    def label_callback(name, abnormal):
        store.current_label = name

    config.label_callback = label_callback

screen screen_replay(label):
    vbox:
        textbutton _("speed up") action [SetVariable("game.jeu_sensitive", False), Function(date.speedUp),Pause(0.3)]
        textbutton _("speed down") action [SetVariable("game.jeu_sensitive", False), Function(date.speedDown),Pause(0.3)]
        textbutton _("V2") action [SetVariable("game.jeu_sensitive", False), Call(label + "_v2")]
        textbutton _("CUM") action [SetVariable("game.jeu_sensitive", False), Call(label + "_isLost")]
        textbutton _("Win") action [SetVariable("game.jeu_sensitive", False), Call(label + "_isWin")]
        textbutton _("update") action [SetVariable("game.jeu_sensitive", False), Function(update_animationSpeed)]
