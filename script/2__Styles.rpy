define config.font_name_map["font_venus_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
define config.font_name_map["font_dyslexic"] = FontGroup().add("Venus+Cormier.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
# Acier < Plomb < Carrare < Martre < Cormier
define config.font_name_map["font_carrare"] = FontGroup().add("Venus+Carrare.otf", 0x0020, 0x0020).add("Venus+Carrare.otf", 0x0022, 0x007f).add("Venus+Plomb.otf", 0x0021,0x0021).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff) #cararre doesnt have '!' 0x0021
#.add("DejaVuSans.ttf", 0x00A0,0xffff)

# define config.font_name_map["font_carrare"] = FontGroup().add("Venus+Carrare.otf", 0x0022, 0x007f).add("DejaVuSans.ttf", 0x00A0,0xffff) #.add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff) #check if you have the ♥︎ emoji U+2665

define config.font_name_map["font_venus_acier"] = FontGroup().add("DejaVuSans.ttf", 0x002A, 0x002A).add("Venus+Plomb.otf", 0x0020, 0x007f).add("DejaVuSans.ttf", 0x00A0,0x00B2).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
#.add("Venus+Carrare.otf", 0x0020, 0x007f)

style default:
    properties gui.text_properties()
    language gui.language
    # size 40
    font "font_carrare"
    # font "_OpenDyslexic3-Regular.ttf"
    # font FontGroup().add("DejaVuSans.ttf", "²","²").add("FRABK.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    # font FontGroup().add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff).add("DejaVuSans.ttf", "²","²")

style outline_text:
    color "#000000"
    outlines [ (absolute(4), "#ffffff", absolute(0), absolute(2)) ]
    font "font_venus_cormier"

style outline_dyslexic:
    color "#fff"
    outlines [ (absolute(4), "#050505", absolute(0), absolute(2)) ]
    font "font_venus_cormier"

style style_small_numbers:
    color "#fff"
    outlines [ (absolute(4), "#050505", absolute(0), absolute(2)) ]
    font "font_carrare"

style style_card_effect:
    xalign 0.5
    yalign 0.4
    adjust_spacing True
    textalign 0.5
    font "font_venus_acier"
    # font "_OpenDyslexic3-Regular.ttf"

style quirky_command:
    color "#ffffff"
    # outlines [ (absolute(8), "#181d2899", absolute(0), absolute(10)), (absolute(10), "#25d7ff", absolute(0), absolute(0)), (5, "#000000", absolute(0), absolute(0)) ]
    outlines [ (8, "#181d2899", 0, 10), (10, gui.hover_color, 0, 0), (5, "#000000", 0, 0) ]
    font "font_carrare"
    size 100
    adjust_spacing True



init python:
    # def tintImg(img, color):
    #     return Transform(img, matrixcolor=TintMatrix(color))

    def colorizeImg(img, color):
        return Transform(img, matrixcolor=ColorizeMatrix(color[0],color[1]))

    def bwImg(img, value=0.0):
        return Transform(img, matrixcolor=SaturationMatrix(value))

transform tintImg(child, color): #DOES NOT WORK IF THE IMAGE ISNT FULL SCREEN, use this on hover when idle uses showInteractible(), if not, just use Transform()
    # contains:
    child
    matrixcolor TintMatrix(color)

transform showInteractible(child, xyalign=(0.5,0.5)):
    matrixcolor IdentityMatrix()
    contains:
        child
    contains:
        "click-me"
        align xyalign
        alpha (0.0 if child in done_flag["buttons"] else 1.0)

image click-me-small:
    "ui/click-me.png"
    anchor (0.5,0.5)
    subpixel True
    parallel:
        ease 3.0 zoom 0.0
        ease 0.5 zoom 0.5
        repeat
    parallel:
        linear 3.0 yoffset -20
        yoffset 40
        linear 0.5 yoffset 30
        repeat

image click-me:
    xysize (250, 250)
    contains:
        pause 0.5
        "click-me-small"
        pos (0.3,0.6)
    contains:
        pause 1.5
        "click-me-small"
        pos (0.4,0.3)
    contains:
        "click-me-small"
        pos (0.75,0.3)
    contains:
        pause 2.5
        "click-me-small"
        pos (0.25,0.35)
    contains:
        "click-me-small"
        pos (0.6,0.7)
    contains:
        pause 0.7
        "click-me-small"
        pos (0.5,0.4)
    contains:
        pause 2.0
        "click-me-small"
        pos (0.7,0.6)
 
    