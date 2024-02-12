init python:
    class Date():
        def __init__(self, dateOrSex, name="", **kwargs):

            self.name = name #get the name of current label to set the name of this date
            game.jeu_sensitive = False;

            if dateOrSex == "date":
                game.state = "dating"
            elif dateOrSex == "sex":
                game.state = "sexing"
            else:
                raise Exception

            if "turnLeft" in kwargs:
                self._turnLeft = kwargs["turnLeft"]
            else:
                self._turnLeft = 0

            
            self.config = {}

            self.objectives = {}
            if "objectif_trust" in kwargs:
                self.objectives["trust"] = kwargs["objectif_trust"]
            else:
                self.objectives["trust"] = -999
            
            if "objectif_attraction" in kwargs:
                self.objectives["attraction"] = kwargs["objectif_attraction"]
            else:
                self.objectives["attraction"] = -999
            
            if "objectif_lust" in kwargs:
                self.objectives["lust"] = kwargs["objectif_lust"]
            else:
                self.objectives["lust"] = -999

            if "isLost" in kwargs:
                self._isLost = kwargs["isLost"]
            else:
                if game.state == "dating":
                    self._isLost = "len(deck.deck) == 0 or (date.lust > date.trust and date.lust > date.attraction) or date.turnLeft == 1"
                else:
                    self._isLost = "date.lust >= date.lustMax"

            if "isWin" in kwargs:
                self._isWin = kwargs["isWin"]
            else:
                self._isWin = "date.lust >= date.objectives['lust'] and date.attraction >= date.objectives['attraction'] and date.trust >= date.objectives['trust']"

            # label to call at the end of every turn
            if "endTurn" in kwargs:
                self.endTurn = kwargs["endTurn"]
            else:
                self.endTurn = ""

            self.ydisplace = Transform( ypos=1080 )

            self.drink = 3
            self.turn = 0
            self.naked = False
            self.lustMax = -99
            self.lust = -99
            self.trust = -99
            self.attraction = -99

            self.trustMultiplier = 1
            self.attractionMultiplier= 1
            self.lustMultiplier = 1

            self.allMultiplierOnce= 1

            self.orgasmMax = 60
            self.orgasm = 0

            self.animation_speed = 0
            self.animation_speed_hash = [10, 0.3, 0.22, 0.15, 0.1, 0.067]
            self.animation_lust = [1,5,10,15,20,25,30]
            
            if "lustPerTurn" in kwargs:
                self.lustPerTurn = kwargs["lustPerTurn"]
            else:
                self.lustPerTurn = 0

            if _in_replay or game.debug_mode:
                if dateOrSex == "sex":
                    self.replay_mode()

            # reaction is a dictionary of    card : label
            # you play a card X, it will lead you to label Y after.
            self.reaction = {}

        @property
        def turnLeft(self):
            return self._turnLeft - self.turn

        def speedUp(self, useMultiplier=False):    
            global animation_speed
            
            if self.animation_speed < len(self.animation_speed_hash) - 1:
                self.animation_speed += 1
                update_animationSpeed()

            if useMultiplier:
                i = 1
                while i < self.lustMultiplier and self.animation_speed < len(self.animation_speed_hash) - 1:
                    renpy.pause(0.3)
                    self.animation_speed += 1
                    update_animationSpeed()
                i += 1

        def speedDown(self, useMultiplier=False):
            global animation_speed   
            
            if self.animation_speed > 1:
                self.animation_speed -= 1
                update_animationSpeed()

            if useMultiplier:
                i = 1
                while i < self.lustMultiplier and self.animation_speed > 1:
                    renpy.pause(0.3)
                    self.animation_speed += 1
                    update_animationSpeed()
                i += 1

        def isLost(self):
            return eval(self._isLost)
        def isWin(self):
            return eval(self._isWin)

        def updateYdisplace(self):
            # game.jeu_sensitive and 
            if game.isHoverHand:
                self.ydisplace = trsfm_cards_go_up
            else:
                self.ydisplace = trsfm_cards_go_down
            
            return self.ydisplace

        def increment(self, which, value, resetAllMultiplier = True, useMultiplier=True, negative=False): #allow
            if useMultiplier:
                if which == "trust":
                    self.trust += value * self.trustMultiplier * self.allMultiplierOnce
                elif which == "attraction":
                    self.attraction += value * self.attractionMultiplier * self.allMultiplierOnce
                elif which == "lust":
                    self.lust += value * self.lustMultiplier * self.allMultiplierOnce
                    # if negative:
                    #     self.lust += value * self.lustMultiplier * self.allMultiplierOnce
                    # else:
                    #     if self.lust<0 and value<0:
                    #         pass
                    #     else:
                    #         self.lust += value * self.lustMultiplier * self.allMultiplierOnce
                    #         if value < 0:
                    #             self.lust = max(0, self.lust)
                else:
                    raise Exception("no valid specified argument: which") 
                if resetAllMultiplier:
                    self.allMultiplierOnce = 1
            else:
                setattr(self, which, getattr(self,which) + value )
                
            if value<0:
                renpy.with_statement(ImageDissolve("gui/transition.png", 0.2))
            else:
                renpy.with_statement(ImageDissolve("gui/transition.png", 0.2, reverse=True) )
                
        def replay_mode(self):
            renpy.say("","debug mode is on, setting isLost to False and isWin to False and game.progress to -1")
            game.progress[1] == -1
            self._isLost = "False"
            self._isWin = "False"

#############################################################################
##                                                                                     
##
##          ██       █████  ██████  ███████ ██      ███████ 
##          ██      ██   ██ ██   ██ ██      ██      ██      
##          ██      ███████ ██████  █████   ██      ███████ 
##          ██      ██   ██ ██   ██ ██      ██           ██ 
##          ███████ ██   ██ ██████  ███████ ███████ ███████ 
##
##
#############################################################################                
                
label label_beginDuel_common():

    $ game.jeu_sensitive = False;

    $ date.lust = game.lust
    $ date.lustMax = game.lustMax
    $ date.lustMultiplier = 1
    $ date.trust = game.trust
    $ date.trustMultiplier = 1
    $ date.attraction = game.attraction
    $ date.attractionMultiplier = 1
    
    $ date.animation_speed = 1

    $ deck.drink = 3

    if _in_replay or game.debug_mode:
        show screen screen_replay(date.name)
        if game.state == "sex":
            $ update_animationSpeed()
            $ deck.hand = [Card("undress")]
            return

    if game.progress[1] == -1:
        $ game.progress[1] = 0

    $ deck.deck = deck.list.copy()
    $ deck.shuffle()
    $ deck.discard_pile = []
    $ deck.hand = []

    if game.state == "dating":
        show screen screen_date_ui()
    else:
        show screen screen_sex_ui()
    hide screen screen_day
    with dissolve

    $ deck.draw(5)

    play sound "rpg/Wind1.wav"
    show date-start onlayer screens at truecenter with blinds
    pause 0.4
    play sound "date/datestart2.mp3"
    hide date-start  onlayer screens with moveoutbottom

    if game.state == "dating":
        if date.lust > date.trust and date.lust > date.attraction:
            pause 0.5
            play sound "rpg/Sonic1-onTheEdge.wav"
            show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
            hide screen screen_tutorial with dissolve
    elif game.state == "sexing":
        if date.lust > date.lustMax:
            pause 0.5
            play sound "rpg/Sonic1-onTheEdge.wav"
            show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
            hide screen screen_tutorial with dissolve
    return

label label_sex_endTurn():
    $ i=0
    # while i < date.animation_lust[date.animation_speed]:
    #     $ date.lust += 1
    #     $ date.orgasm += 1
    #     $ i += 1
    #     pause(1.0/ date.animation_lust[date.animation_speed])

    play sound "card/switch.mp3"
    
    while i < date.lustPerTurn:
        $ date.lust += 1
        $ date.orgasm += 1
        $ i += 1
        pause(1.0/ date.lustPerTurn)
    return

label label_endTurn_common():

    $ date.attractionMultiplier = 1
    $ date.trustMultiplier = 1
    $ date.lustMultiplier = 1
    $ date.turn += 1
    $ game.progress[1] = max(date.turn, game.progress[1])

    $ handSize = len(deck.hand)

    if game.state == "sexing" and date.lust + date.lustPerTurn >= date.lustMax:
        play sound "rpg/Sonic1-onTheEdge.wav" volume 0.5
        pause 0.5
    else:
        play sound "rpg/Item1.wav"
        pause 0.3

    while handSize < 5 and len(deck.deck)>0:
        $ deck.draw(1)
        $ handSize = len(deck.hand)
    
    $ game.jeu_sensitive = True;

    if game.state == "dating":
        show joyce null with dissolve

    return

label label_after_successful_Date_common():

    hide screen screen_date_ui
    hide screen screen_sex_ui
    hide screen screen_dick_ui
    with dissolve

    if game.state == "dating":
        play sound "rpg/Holy5.wav"
        show date-nice at truecenter onlayer screens with blinds
        pause 0.3
        hide date-nice onlayer screens with moveoutbottom
    
    if BALANCE["keepStat"]:
        $ game.lust = max(0,date.lust)
        $ game.trust = date.trust 
        $ game.attraction = date.attraction
    else:
        $ game.lust = 0 #date.lust
        $ game.trust = 0 #date.trust
        $ game.attraction = 0 #date.attraction
    
    $ date.objectives["lust"] = -999
    $ date.objectives["trust"] = -999
    $ date.objectives["attraction"] = -999

    $ game.progress[0] += 1
    $ game.progress[1] = -1
    $ g.phoneProgress[0] += 1
    $ g.phoneProgress[1] = 0

    $ game.animation_speed = 0

    if game.state == "dating":
        show joyce null with dissolve
    return

label label_date_isLost_common(var_label_callback = "label_home"):
    # """
    # this label is called after every turn
    # """
    play sound "card/switch.mp3"
    $ game.jeu_sensitive = False

    if date.isLost():

        if _in_replay or game.debug_mode :
            $ renpy.end_replay()

        play sound "rpg/Fall1.wav"
        show date-fail onlayer screens at truecenter with blinds
        pause 0.3
        hide date-fail onlayer screens with moveoutbottom

        if date.lust > date.trust and date.lust > date.attraction:
            show joyce null
            hide screen screen_date_ui with dissolve
            if game.progress[0]<4:
                j armscrossed upset "Um... don't you think I can notice?"
                j "Sorry but I'm gonna go. I'm really not in the mood today."
                j "Let's do this another day."
            else:
                if game.progress[1]<3:
                    j foxy armscrossed "You're getting a bit too horny, aren't you?"
                    j smile "Seems like today's not your day."
                    j tongue "Hehe, try next time. "
                    j smirk "My door is always open for you."
                else:
                    j foxy armscrossed "Ooh bad play."
                    j smile "You should take your time."
                    j "You don't need to burst everything in one go."
                    j "Just focus on each step, one at a time."
                    j wink tongue "Big boy."

        elif len(deck.deck) == 0:
            show joyce null
            hide screen screen_date_ui with dissolve
            if game.progress[0]<4:
                j eyeside armscrossed "..."
                j "Seems like you've run out of things to say."
                j "I guess the date's over then..."
                j "Next time, think about other topics to talk about."
                
        elif date.turnLeft <= 1:
            show joyce null
            hide screen screen_date_ui with dissolve
            if game.progress[0]<4:
                j eyeside armscrossed "Oh, look at the time!"
                j "Sorry, I gotta go."
                j "That kinda dragged on anyway, right?"
                j "Maybe we can do this another day? See ya."
            else:
                if game.progress[1]<3:
                    j foxy armscrossed "Oh, look at the time!"
                    j smile "Seems like today's not your day."
                    j tongue "Hehe, try next time."
                    j smirk "My door is always open for you."
                else:
                    j foxy armscrossed "Ooh time's up."
                    j smile "You should take your time."
                    j "You don't need to burst everything in one go."
                    j "Just focus on each step, one at a time."
                    j wink tongue "Big boy."

        hide joyce with dissolve

        if not BALANCE["keepStat"]:
            $ date.lust = 0
            $ date.trust = 0
            $ date.attraction = 0
        call label_newDay(var_label_callback)

    return