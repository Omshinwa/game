init python:
    config.console = True
    preferences.skip_unseen = True

    def nullfunction(*args):
        return

    renpy.music.register_channel("sexsfx", "voice")
    renpy.music.register_channel("sexvoice", "voice")
    renpy.music.register_channel("drawcard", "sfx")
    renpy.music.register_channel("activatecard", "sfx", loop=False)


    class Game():
        def __init__(self):
            self.jeu_sensitive = True
            self.card_xsize = 230
            self.card_ysize = 330

            self.lustMax = 30
            self.lust = 0

            self.trust = 0
            self.attraction = 0

            self.trustMultiplier = 1
            self.attractionMultiplier= 1
            self.lustMultiplier = 1

            self.allMultiplierOnce= 1

            self.state = "" #either "dating" or "deckbuilding"

            self.isHoverHand = False

            self.story = ["tutorial", "bubbleTea", "terrasse", "barDate", "stripPoker", "footjob", "handjob", "blowjob", "cowgirl", "start"]
            self.progress = [0,-1] # left is progress, right is numbers of turns 

            self.day = 3

            self.lastPlayed = None
            self.cardPlaying = None

            self.debug_mode = 0

            self.dateEvery = 4

            self.lustPerDay = "game.progress[0] + 1"

        @staticmethod
        def hasNewMessage():
            if g.phoneProgress[0] not in g.phoneLogs:
                return False
            return g.phoneProgress[1]<len(g.phoneLogs[g.phoneProgress[0]])-1


label label_null(*args):
    return

#######################################################

##            global var g:

default g.day_rat_appears = 0 #when does the rat appear
default g.findFromTrash = True #get a Recycle card when you threw away enough cards
default g.card_per_line = 7
default g.phoneLogs = {
    1:[
        [0, "heloo~ it's joyce"],[0, "are you free in 3 days?"],[0, "let's meet up again!"],
    ],
    2:[
        [0, "heeey"],[0, "wanna get some drinks tmr?"],[0, "There's a bubble tea place I like."],[2, "Okay see you there."]
    ],
    3:[
        [0, "today was so fun!"],[0, "I hope to see you next time too!"],[0, "right now i'm stuck on a sudoku haha"],[1, "pic1.png"], ["exe", "renpy.call('label_pic1_reaction')"]
    ],
    4:[
        [0, "hey look at this kitty"], [0, "she followed me around"], [0,"such a cutie! I wished I had a cat."], [1, "pic2.png"], ["exe", "renpy.call('label_pic2_reaction')"]
    ],
    5:[
        [0, "I know where to go next time!"],[0, "let's go to a fancy bar!"], [0, "how about it"], [2, "Good idea!"], [2, "Let's try and dress a bit fancy haha"], [0, "ooh good idea!"], [0, "Alright that's a plan then."],[0, "im gonna go to sleep now"],[0, "good niight <3"],[1, "pic3.png"], ["exe", "renpy.call('label_pic3_reaction')", [2, "goodnight"]]
    ],
    6:[
        [0, "about the fancy bar"],[0, "I don't know what to wear for tomorrow"],[0, "which dress do you think looks better?"],[1, "pic4.png"], ["exe", "renpy.call('label_pic4_reaction')"]
    ],
    7:[
        [1, "pic5-red.png"],[0, "By the way, I came here without wearing any panties"],["exe", "renpy.call('label_pic5_reaction')"],[0, "Did you notice? ;-P"],
    ],
    8:[
        [0, "I looved this bar"],[0, "I felt like such a lady, thanks for helping me choose the dress."],[2, "No problem, you were such a sight! I love spending time with you."],[0, "same <3"],[0, "hey.. about next time"],[0, "How about coming to my house?"],[2, "sure! I'd love to."],[0, "nice I'll send you the address"],[0, "See you <3"]
    ],
    9:[
        [1, "pic6.png"],["exe", "renpy.call('label_pic6_reaction')"], [0, "Oh no I didn't mean to send this pic!"],[2, "Really?"],[0, ":-P"],[0, "It's an appetizer for tomorrow"],[2, "Wow, i'm excited"],[0, "<3"]
    ],
    10:[
        [1, "pic7.png"],["exe", "renpy.call('label_pic7_reaction')"]
    ],
    }
default g.phoneProgress = [0,0] # first number is "day" second is tracking which msg
default g.prison_cards = []
default g.dreamProgress = 0
default g.trashbin = [] # array of (image, angle, xpos, ypos)
default g.bubbleTea_share_drink = False
default g.plant = 0
default g.water = False

default persistent.displayContentWarning = True

default phone_Scroll = ui.adjustment(range=0, value=0, step=None, page=1, changed=None, adjustable=None, ranged=None, force_step=False)
