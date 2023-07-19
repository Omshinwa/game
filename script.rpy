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
    # jump label_cowgirl_start
    jump label_prison
    return

label label_prison:
    $ global_var = {"page":0}
    scene bg prison
    show screen screen_card_deck
    call screen screen_gameloop()


label label_cowgirl_start:
    scene bg bbt

    show joyce standing at default
    show fg bbt-table 

    j "Hello, you must be Kevin."
    j "I'm Joyce"
    show joyce sitting at default
    j "Hi, this is your first date no?"


    show joyce cowgirl at toobig

    j "I'll tell you how to get a successful date"
    j "Let the date begin!"

    call beginDuel()

    label .gameLoop:
        $ current_speed = game.animation_speed
        $ game.jeu_sensitive = False

        if current_speed != game.animation_speed:
            show joyce cowgirl

        if game.orgasm >= game.orgasmMax:
            j "i'm..{w=1.0}{nw}"
            j "it's coming !{w=1.0}{nw}"
            show joyce cowgirl-orgasm 
            j "kyaaa{w=1.0}{nw}"
            pause(2)
            show joyce cowgirl-normal at top
            pause(1)
            j "huff.."
            j "i-i came"
            
            show joyce sitting at default
        
        if game.pleasure >= game.pleasureMax:
            "i'm gonna coooom"
    
        $ game.jeu_sensitive = True
        call screen screen_gameloop()
    call .gameLoop

    # This ends the game.

    return