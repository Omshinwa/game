# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character(None, image="joyce", kind=bubble) # Eileen
$ config.tag_transform["joyce"] = "myLoc"
$ config.tag_transform["fg"] = "myLoc"

style default:
    size 50
# The game starts here.

label start:
    call game_init
    # jump label_second_date
    # jump label_first_date
    # jump label_cowgirl_start
    # jump label_footjob_start
    jump label_prison
    return

label label_prison:
    scene bg prison
    show screen screen_prison
    label .gameLoop:
        call screen screen_gameloop()
    jump .gameLoop
