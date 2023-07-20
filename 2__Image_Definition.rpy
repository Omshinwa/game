init python:
    def play_sexsound(trans, st, at, filename):
        renpy.play(filename, channel='voice')
        return None
   
transform toobig:
    yalign 0.0
    ypos -100
    zoom 0.9

transform default:
    xalign 0.5
    yanchor 1.0
    ypos 1080 - 200
    zoom 1.0

transform top:
    zoom 1.0
    xalign 0.5
    yalign 0.0

    
image joyce cowgirl:
    "Joyce/sex/cowgirl (1).png"
    pause(0.1 / game.animation_speed_hash[game.animation_speed])

    function renpy.curry(play_sexsound)(filename="draw.mp3") #hacky

    "Joyce/sex/cowgirl (2).png"
    pause(0.1 / game.animation_speed_hash[game.animation_speed])
    "Joyce/sex/cowgirl (3).png"
    pause(0.1 / game.animation_speed_hash[game.animation_speed])
    "Joyce/sex/cowgirl (4).png"
    pause(0.1 / game.animation_speed_hash[game.animation_speed])
    "Joyce/sex/cowgirl (5).png"
    pause(0.1 / game.animation_speed_hash[game.animation_speed])
    "Joyce/sex/cowgirl (6).png"
    pause(0.1 / game.animation_speed_hash[game.animation_speed])
    repeat

image card_zone_bg:
    xalign 1.0 
    "ui/card_zone_bg.png"
    linear 3.0 xalign 0.0
    repeat

image joyce cowgirl-orgasm:
    "Joyce/sex/cowgirl-orgasm (1).png"
    pause(0.1)
    "Joyce/sex/cowgirl-orgasm (2).png"
    pause(0.1)
    repeat