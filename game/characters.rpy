init python:
    renpy.music.register_channel("beepy_voice", "voice")



# how to stop beep voice playing in game menu by henne-n https://www.reddit.com/r/RenPy/comments/1adb02j/dialogue_noise_still_playing_on_pause_menu/
label enter_game_menu:
    $ renpy.music.stop(channel="beepy_voice") 
    return

#VOICES 
init python:

    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/voice beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")

init python:
    def sage_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/sage beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")

init python:
    def norman_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/norman beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")

init python:
    def vin_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/vin beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")

init python:
    def rocky_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/rocky beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")

init python:
    def tara_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/tara beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")
            
init python:
    def taran_voice(event, interact=True, **kwargs):
        if not interact:
            return 

        if event == "show":
            renpy.music.play("audio/voices/taran beep.ogg",loop=True, channel="beepy_voice")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beepy_voice")


define narrator = Character(name=None, ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue",  callback=beepy_voice)

#main charas            

define p = DynamicCharacter("[pov]", color= "#7272f0",image='p', ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue",  callback=sage_voice)
define r = Character("Rocky", color= "#bd2727",image='r', ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", callback=rocky_voice)
define v = Character("Vinnie", color= "#64ffcbf3",image='v', ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", callback=vin_voice)
define n = Character("Norman", color= "#ecd75e",image='n', ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", callback=norman_voice)

#side charas            

define s = Character("The Stranger", color= "#ffffff",image="c", ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", callback=taran_voice)
define w = DynamicCharacter("[w_name]", color= "#e4d1f7",image="w", ctc="click_to_continue", ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", callback=tara_voice)

#npcs     
define omg = Character("???", color= "#ffffff", callback=taran_voice, ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", ctc="click_to_continue")
define omg2 = Character("???", color= "#ecd75e", callback=norman_voice, ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", ctc="click_to_continue")
define npc = Character("Civilian",color= "#9b9b9b", callback=beepy_voice, ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", ctc="click_to_continue")
define tv = Character("TV",color= "#5e5e5e", callback=beepy_voice, ctc_pause="click_to_continue", ctc_timedpause="click_to_continue", ctc="click_to_continue")


return