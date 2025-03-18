#VOICES 
init python:
    renpy.music.register_channel("beepy_voice", "voice")

init python:
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/sfx/voice beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")

#main charas            

define p = DynamicCharacter("[pov]", color= "#684d70",image="sage", ctc="click_to_continue", callback=beepy_voice)
define r = Character("Rocky", color= "#812c2c",image="rocky", ctc="click_to_continue", callback=beepy_voice)
define v = Character("Vinnie", color= "#57ff7bf3",image="vinnie", ctc="click_to_continue", callback=beepy_voice)
define n = Character("Norman", color= "#ffb554",image="norman", ctc="click_to_continue", callback=beepy_voice)

#side charas            

define s = Character("The Stranger", color= "#ffffff",image="s", ctc="click_to_continue", callback=beepy_voice)
define w = DynamicCharacter("[w_name]", color= "#5457ff",image="tara", ctc="click_to_continue", callback=beepy_voice)

#npcs           
define omg = Character("???", callback=beepy_voice)

define npc = Character("Business Man", callback=beepy_voice)
define tv = Character("TV", callback=beepy_voice)


#SPRITES 

#sage

image side sage = "images/sprites/sage/sage.png"
image side sage chill = "images/sprites/maizie/maizie chill.png"
image side sage excited = "images/sprites/maizie/maizie excited.png"
image side sage serious = "images/sprites/maizie/maizie serious.png"

#rocky

image rocky = "images/sprites/rocky/rocky.png"
image rocky chill = "images/sprites/maizie/maizie chill.png"
image rocky excited = "images/sprites/maizie/maizie excited.png"
image rocky serious = "images/sprites/maizie/maizie serious.png"

#vinnie

image vinnie = "images/sprites/vinnie/vinnie.png"
image vinnie chill = "images/sprites/maizie/maizie chill.png"
image vinnie excited = "images/sprites/maizie/maizie excited.png"
image vinnie serious = "images/sprites/maizie/maizie serious.png"

#norman

image norman = "images/sprites/norman/norman.png"
image norman chill = "images/sprites/maizie/maizie chill.png"
image norman excited = "images/sprites/maizie/maizie excited.png"
image norman serious = "images/sprites/maizie/maizie serious.png"



#Tara

image tara = "images/sprites/tara/tara.webp"
image norman chill = "images/sprites/maizie/maizie chill.png"
image norman excited = "images/sprites/maizie/maizie excited.png"
image norman serious = "images/sprites/maizie/maizie serious.png"


#Stranger / Taran

image stranger norm = "images/sprites/stranger/stranger.png"
image norman chill = "images/sprites/maizie/maizie chill.png"
image norman excited = "images/sprites/maizie/maizie excited.png"
image norman serious = "images/sprites/maizie/maizie serious.png"

image s norm = "images/sprites/stranger/stranger.png"
image norman chill = "images/sprites/maizie/maizie chill.png"
image norman excited = "images/sprites/maizie/maizie excited.png"
image norman serious = "images/sprites/maizie/maizie serious.png"

return