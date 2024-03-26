init python:
    class Date():
        def __init__(self, dateOrSex, name=None, **kwargs):
            
            if name == None:
                self.name = current_label
            else:
                self.name = "label_"+name
            # self.name = name #get the name of current label to set the name of this date
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
            
            self.objectives = {}
            
            if "neutralJoyce" in kwargs:
                self.neutralJoyce = kwargs["neutralJoyce"]
            else:
                self.neutralJoyce = "joyce null"


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
                self._isLost = None
                if game.state == "dating":
                    self._isLost = "len(deck.deck) == 0 or (date.lust > date.trust and date.lust > date.attraction) or date.turnLeft == 0"
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
                self.endTurn = self.name + "_endTurn"

            self.ydisplace = Transform( ypos=1080 )

            self.drink = 3
            self.turn = 0
            self.naked = False
            self.lustMax = game.lustMax
            self.lust = game.lust
            self.trust = game.trust
            self.attraction = game.attraction

            self.lastPlayed = None
            self.playedThisTurn = []

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
                    self.animation_speed -= 1
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

        def increment(self, which, value, resetAllMultiplier = True, useMultiplier=True, negative=False): #
            before = getattr(self,which)
            if useMultiplier:
                if which == "trust":
                    self.trust += value * self.trustMultiplier * self.allMultiplierOnce
                elif which == "attraction":
                    self.attraction += value * self.attractionMultiplier * self.allMultiplierOnce
                elif which == "lust":
                    if value>0:
                        renpy.sound.play("rpg/Lust.wav", relative_volume=max(0.5,0.08*value))
                    if negative:
                        self.lust += value * self.lustMultiplier * self.allMultiplierOnce
                    else:
                        if self.lust<0 and value<0:
                            return
                        else:
                            self.lust += value * self.lustMultiplier * self.allMultiplierOnce
                            if value < 0:
                                self.lust = max(0, self.lust)
                    if resetAllMultiplier:
                        self.lustMultiplier = 1
                else:
                    raise Exception("no valid specified argument: which") 
                if resetAllMultiplier:
                    self.allMultiplierOnce = 1
            else:
                setattr(self, which, getattr(self,which) + value )
                
   
        def replay_mode(self):
            renpy.say("","replay/debug mode is on, setting isLost to False and isWin to False and game.progress to -1")
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
    $ date.animation_speed = 1
    
    if game.state == "sexing":

        if (_in_replay or game.debug_mode):
            show screen screen_replay(date.name)
            $ deck.hand = [Card("undress")] #useful to have a card in hand so it doesnt skip turns
            $ update_animationSpeed()
            return
        
        $ update_animationSpeed(changeSprite=False)

    if game.progress[1] == -1:
        $ game.progress[1] = 0

    $ debug_deck_playtest()
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
    play sound "date/_datestart2.mp3"
    hide date-start  onlayer screens with moveoutbottom

    if game.state == "dating":
        if date.lust > date.trust and date.lust > date.attraction:
            pause 0.5
            play sound "rpg/onTheEdge.wav"
            show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
            hide screen screen_tutorial with dissolve
    elif game.state == "sexing":
        if date.lust + date.lustPerTurn >= date.lustMax:
            pause 0.5
            play sound "rpg/onTheEdge.wav"
            show screen screen_tutorial("misc/tutorial-objectives.png") with dissolve
            hide screen screen_tutorial with dissolve
    return

label label_gameLoop():
    label .gameLoop:
        $ game.jeu_sensitive = False

        if date.isWin():
            call label_after_successful_Date_common
            $ renpy.call(date.name + "_Win")
            if game.state == "date":
                call label_newDay("label_home")
            else:
                call label_newDay("label_prison")
        elif date.isLost():
            call label_Lost_common
        
        if len(deck.hand) == 0:
            call label_endTurn_common
        $ game.jeu_sensitive = True

        if game.state == "dating":
            if hasattr(date, "neutralJoyce"):
                $ renpy.show(date.neutralJoyce)
            with Dissolve(0.1)
        
        call screen screen_gameloop()
        
    jump .gameLoop

label label_endTurn_common():
    # """
    # this label is called after every turn
    # """
    $ game.jeu_sensitive = False

    if not renpy.sound.is_playing("sound"): #if it was triggered automatically
        pause 0.3
        play sound "card/switch.mp3"

    if game.state == "sexing":
        $ date.lust += date.lustPerTurn
        $ date.orgasm += date.lustPerTurn # times the sensitivity

    pause 0.3 #allows for the animation to be played

    $ date.playedThisTurn = []
    $ date.attractionMultiplier = 1
    $ date.trustMultiplier = 1
    $ date.turn += 1
    $ game.progress[1] = max(date.turn, game.progress[1])

    if game.state == "sexing" and date.lust + date.lustPerTurn >= date.lustMax:
        play sound "rpg/onTheEdge.wav" volume 0.5
        pause 0.5
    else:
        play sound "rpg/Item1_quiz.mp3"
        pause 0.3

    $ renpy.call(date.endTurn)

    if not date.isLost():
        $ handSize = len(deck.hand)
        while handSize < 5 and len(deck.deck)>0:
            $ deck.draw(1)
            $ handSize = len(deck.hand)
    else:
        if game.state == "dating":
            call label_Lost_common
            call label_newDay("label_home")
        elif game.state == "sexing":
            $ renpy.call(date.name + "_Lost")
            call label_newDay("label_prison")

    return

label label_after_successful_Date_common():
    hide screen screen_date_ui
    hide screen screen_sex_ui
    hide screen screen_dick_ui
    with dissolve

    if game.state == "dating":
        play sound "rpg/Holy5.wav"
        show date-nice at truecenter onlayer screens with blinds
        pause 0.5
        hide date-nice onlayer screens with moveoutbottom
    
    # if BALANCE["keepStat"]:
    $ game.lust = max(0,date.lust)
    $ game.trust = date.trust 
    $ game.attraction = date.attraction
    # else:
    #     $ game.lust = 0 #date.lust
    #     $ game.trust = 0 #date.trust
    #     $ game.attraction = 0 #date.attraction
    
    $ date.objectives["lust"] = -999
    $ date.objectives["trust"] = -999
    $ date.objectives["attraction"] = -999

    $ game.progress[0] += 1
    $ game.progress[1] = -1
    $ g.phoneProgress[0] += 1
    $ g.phoneProgress[1] = 0

    $ game.animation_speed = 0
    
    return

label label_Lost_common():
    if _in_replay or game.debug_mode :
        $ renpy.end_replay()

    if game.state == "dating":
        play sound "rpg/Fall1.wav"
        show date-fail onlayer screens at truecenter with blinds
        pause 0.3
        hide date-fail onlayer screens with moveoutbottom
        hide screen screen_date_ui with dissolve
        show joyce null

    if renpy.has_label(date.name + "_Lost"):
        call expression date.name + "_Lost"
    else:
        call label_reaction_default_Lost()

    if game.state == "dating":
        call label_newDay("label_home")
    else:
        call label_newDay("label_prison")
    return