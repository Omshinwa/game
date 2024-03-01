define config.font_name_map["font_venus_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
define config.font_name_map["font_dyslexic"] = FontGroup().add("Venus+Cormier.otf", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
# Acier < Plomb < Carrare < Martre < Cormier
define config.font_name_map["font_carrare"] = FontGroup().add("Venus+Carrare.otf", 0x0020, 0x0020).add("Venus+Carrare.otf", 0x0022, 0x007f).add("Venus+Plomb.otf", 0x0021,0x0021).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff) #cararre doesnt have '!' 0x0021
#.add("DejaVuSans.ttf", 0x00A0,0xffff)

# define config.font_name_map["font_carrare"] = FontGroup().add("Venus+Carrare.otf", 0x0022, 0x007f).add("DejaVuSans.ttf", 0x00A0,0xffff) #.add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff) #check if you have the ♥︎ emoji U+2665

define config.font_name_map["font_venus_acier"] = FontGroup().add("DejaVuSans.ttf", 0x002A, 0x002A).add("Venus+Plomb.otf", 0x0020, 0x007f).add("DejaVuSans.ttf", 0x00A0,0x00B2).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
#.add("Venus+Carrare.otf", 0x0020, 0x007f)

define gui.matrix_green_colorize = ColorizeMatrix("#009f5d","#dfd")

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
    outlines [ (5, "#ffffff", 0, 2) ]
    font "font_venus_cormier"

style outline_dyslexic:
    color "#fff"
    outlines [ (4, "#050505", 0, 2) ]
    font "font_venus_cormier"

style style_small_numbers:
    color "#fff"
    outlines [ (4, "#050505", 0, 2) ]
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
    # outlines [ (8, "#181d2899", 0, absolute(10)), (absolute(10), "#25d7ff", 0, 0), (5, "#000000", 0, 0) ]
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

transform showInteractible(child, pos=(0.5,0.5)):
    matrixcolor IdentityMatrix()
    contains:
        child
    contains:
        generate_anim_AE("images/ui/click-me/click-me_",34)
        anchor (0.5, 0.5)
        pos pos
        alpha (0.0 if child in done_flag["buttons"] else 1.0)
