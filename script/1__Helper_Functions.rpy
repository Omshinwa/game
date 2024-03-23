init python:

    # check if attr is shown
    def has_attribute(attr):
        if renpy.get_attributes("joyce"):
            if attr in renpy.get_attributes("joyce"):
                return True
        return False
    
    def default_card_behavior(cardName):
        if cardName in date.playedThisTurn:
            return
        if renpy.has_label(date.name + "_"+cardName):
            renpy.call(date.name + "_"+cardName) 
        else:
            if renpy.has_label("label_reaction_"+cardName):
                renpy.call("label_reaction_"+cardName)