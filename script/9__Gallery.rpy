init python:

    # Step 1. Create the gallery object.
    gallery = Gallery()
    # gallery.locked_button = Solid("#0005")
    gallery.hover_border = Solid("#0ff1")
    gallery.idle_border = Solid("#ff05")
    
    #SELFIES
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

    # Ensure this replaces the main menu.
    tag menu

    modal True
    add "#222"

    # A grid of buttons.
    grid 4 3:

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

python:
        style.gallery = Style(style.default)
        style.gallery_button.background = None
        style.gallery_button_text.color = "#666"
        style.gallery_button_text.hover_color = "#fff"
        style.gallery_button_text.selected_color = "#fff"
        style.gallery_button_text.size = 16