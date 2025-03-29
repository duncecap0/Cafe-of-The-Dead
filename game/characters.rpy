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

define p = DynamicCharacter("[pov]", color= "#7272f0",image='p', ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue",  callback=beepy_voice)
define r = Character("Rocky", color= "#bd2727",image='r', ctc="click_to_continue", callback=beepy_voice)
define v = Character("Vinnie", color= "#64ffcbf3",image='v', ctc="click_to_continue", callback=beepy_voice)
define n = Character("Norman", color= "#ecd75e",image='n', ctc="click_to_continue", callback=beepy_voice)

#side charas            

define s = Character("The Stranger", color= "#ffffff",image="c", ctc="click_to_continue", callback=beepy_voice)
define w = DynamicCharacter("[w_name]", color= "#e4d1f7",image="w", ctc="click_to_continue", callback=beepy_voice)

#npcs     
define omg = Character("???", color= "#ffffff", callback=beepy_voice, ctc="click_to_continue")
define zombie = Character("Zombie", ctc="click_to_continue")
define npc = Character("Civilian",color= "#9b9b9b", callback=beepy_voice, ctc="click_to_continue")
define tv = Character("TV",color= "#5e5e5e", callback=beepy_voice, ctc="click_to_continue")


return