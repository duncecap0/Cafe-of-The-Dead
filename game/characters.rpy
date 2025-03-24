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

define p = DynamicCharacter("[pov]", color= "#57578f",image='p', ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue",  callback=beepy_voice)
define r = Character("Rocky", color= "#812c2c",image='r', ctc="click_to_continue", callback=beepy_voice)
define v = Character("Vinnie", color= "#57ffc7f3",image='v', ctc="click_to_continue", callback=beepy_voice)
define n = Character("Norman", color= "#daca74",image='n', ctc="click_to_continue", callback=beepy_voice)

#side charas            

define s = Character("The Stranger", color= "#ffffff",image="c", ctc="click_to_continue", callback=beepy_voice)
define w = DynamicCharacter("[w_name]", color= "#e4d1f7",image="w", ctc="click_to_continue", callback=beepy_voice)

#npcs     
define omg = Character("???", callback=beepy_voice, ctc="click_to_continue")
define zombie = Character("Zombie", ctc="click_to_continue")
define npc = Character("Civilian", callback=beepy_voice, ctc="click_to_continue")
define tv = Character("TV", callback=beepy_voice, ctc="click_to_continue")


return