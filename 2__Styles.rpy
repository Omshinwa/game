style default:
    properties gui.text_properties()
    language gui.language
    font FontGroup().add("FRABK.TTF", 0x0020, 0x007f).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)

style outline_text:
    color "#000000"
    outlines [ (absolute(5), "#ffffff", absolute(0), absolute(0)) ]
    font "ui"

style quirky_command:
    color "#ffffff"
    # outlines [ (absolute(8), "#181d2899", absolute(0), absolute(10)), (absolute(10), "#25d7ff", absolute(0), absolute(0)), (5, "#000000", absolute(0), absolute(0)) ]
    outlines [ (8, "#181d2899", 0, 10), (10, "#25d7ff", 0, 0), (5, "#000000", 0, 0) ]
    font "quirky_command"
    size 100
    adjust_spacing True
    # caret None
    # outline_scaling "step"