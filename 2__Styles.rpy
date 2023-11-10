define config.font_name_map["font_venus_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
define config.font_name_map["font_dyslexic"] = FontGroup().add("Venus+Cormier.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
# Acier < Plomb < Carrare < Martre < Cormier
define config.font_name_map["font_carrare"] = FontGroup().add("Venus+Carrare.otf", 0x0022, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)

define config.font_name_map["font_venus_acier"] = FontGroup().add("Venus+Plomb.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    

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
    outlines [ (absolute(5), "#ffffff", absolute(0), absolute(3)) ]
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

style quirky_command:
    color "#ffffff"
    # outlines [ (absolute(8), "#181d2899", absolute(0), absolute(10)), (absolute(10), "#25d7ff", absolute(0), absolute(0)), (5, "#000000", absolute(0), absolute(0)) ]
    outlines [ (8, "#181d2899", 0, 10), (10, gui.hover_color, 0, 0), (5, "#000000", 0, 0) ]
    font "font_carrare"
    size 100
    adjust_spacing True
    # caret None
    # outline_scaling "step"



init python:
    # def tintImg(img, color):
    #     return Transform(img, matrixcolor=TintMatrix(color))

    def colorizeImg(img, color):
        return Transform(img, matrixcolor=ColorizeMatrix(color[0],color[1]))

    def bwImg(img, value=0.0):
        return Transform(img, matrixcolor=SaturationMatrix(value))

transform tintImg(child, color):
    contains:
        child
        matrixcolor TintMatrix(color)

transform showInteractible(child, xyalign=(0.5,0.5)):
    contains:
        child
    contains:
        "ui/click-me.png"
        align xyalign
        parallel:
            rotate 0.0
            pause 0.2
            rotate 10
            pause 0.2
            rotate 20
            pause 0.2
            repeat