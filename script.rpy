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
    call label_game_init
    $ game.progress = 8
    jump label_prison
    return