################################################################################
## Party Status Screen
################################################################################

style status_text is text:
    outlines [ (3, "#300019", 0, 0) ]
    outline_scaling "linear"

# Icons for each party member
# Replace s/___.png with the character specific one
image sagestatus:
    ConditionSwitch(
        "sage_health >= 5", "gui/sage healthy.png",
        "sage_health == 4", "gui/sage healthy.png",
        "sage_health == 3", "gui/sage healthy.png",
        "sage_health == 2", "gui/sage hurt.png",
        "sage_health == 1", "gui/sage hurt.png",
        "sage_health <= 0", "gui/dead.png",
    )

image rockstatus:
    ConditionSwitch(
        "rocky_health >= 5", "gui/rocky healthy.png",
        "rocky_health == 4", "gui/rocky healthy.png",
        "rocky_health == 3", "gui/rocky healthy.png",
        "rocky_health == 2", "gui/rocky hurt.png",
        "rocky_health == 1", "gui/rocky hurt.png",
        "rocky_health <= 0", "gui/dead.png",
    )
image normstatus:
    ConditionSwitch(
        "norman_health >= 4", "gui/norm healthy.png",
        "norman_health == 3", "gui/norm healthy.png",
        "norman_health == 2", "gui/norm hurt.png",
        "norman_health == 1", "gui/norm hurt.png",
        "norman_health <= 0", "gui/dead.png",
    )
image vinnstatus:
    ConditionSwitch(
        "vinnie_health >= 3", "gui/vin healthy.png",
        "vinnie_health == 2", "gui/vin hurt.png",
        "vinnie_health == 1", "gui/vin hurt.png",
        "vinnie_health <= 0", "gui/dead.png",
    )
image ammostatus:
    ConditionSwitch(
        "ammo >= 9", "gui/ammo.png",
        "ammo == 8", "gui/ammo.png",
        "ammo == 7", "gui/ammo.png",
        "ammo == 7", "gui/ammo.png",
        "ammo == 6", "gui/ammo.png",
        "ammo == 5", "gui/ammo.png",
        "ammo == 4", "gui/ammo.png",
        "ammo == 3", "gui/ammo.png",
        "ammo == 2", "gui/ammo.png",
        "ammo == 1", "gui/ammo.png",
        "ammo <= 0", "gui/ammo.png",
    )



screen character_stats():
    zorder 2
    frame:
        background Frame("gui/uibox.png", 25, 25, tile="integer")
        padding (30,25)
        xalign 0.99
        yalign 0.01
        hbox:
            style_prefix "status"
            text "[pov]:[sage_health]"
            add "sagestatus"
            text " | "
            text "Norman:[norman_health]"
            add "normstatus"
            text " | "
            text "Rocky:[rocky_health]"
            add "rockstatus"
            text " | "
            text "Vinnie:[vinnie_health]"
            add "vinnstatus"

            #text "[pov] Health: [sage_health] "
            #text "Norman Health: [norman_health] "
            #text "Rocky Health: [rocky_health] "
            #text "Vinnie Health: [vinnie_health] "

screen ammo_stats():
    zorder 3
    frame:
        background Frame("gui/uibox.png", 25, 25, tile="integer")
        padding (30,25)
        xalign 0.01
        yalign 0.01
        hbox:
            style_prefix "status"
            add "ammostatus"
            text " Ammo: [ammo]"
            #text "Insanity: [insanity_level]"

        
## Link to resetting variables to 0 code:
# https://www.reddit.com/r/RenPy/comments/1798uyn/dont_allow_variables_get_below_zero/
init python:

    def addRockyhealth(delta):
        global rocky_health
        rocky_health = max(0, rocky_health + delta)

    def addVinhealth(delta):
        global vinnie_health
        vinnie_health = max(0, vinnie_health + delta)

    def addNormhealth(delta):
        global norman_health
        norman_health = max(0, norman_health + delta)

    def addInsanity_level(delta):
        global insanity_level
        insanity_level = max(0, insanity_level + delta)

screen death_nav():
    
        vbox:
            xalign 0.5
            yalign 0.6
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Main Menu") action MainMenu()

label death_screen:
    window hide diss
    $ quick_menu = False
    hide screen character_stats with dissolve
    hide screen ammo_stats with dissolve
    play sound "audio/sfx/stinger.ogg"
    play music "audio/music/die it is then.ogg" fadein 1.0
    scene black with pixellate
    show text "{size=+90}{b}{color=#f00}{k=+20}GAME OVER{/color}{/b}{/size}{/k}":
            yalign 0.3    

    call screen death_nav


label win_screen:
    window hide diss
    play sound "audio/sfx/stinger.ogg"
    scene black with pixellate

    show text "{size=+90}{b}GAME OVER{/b}{/size}":
        yalign 0.3    
        
    call screen death_nav

label insane_screen:
    window hide diss
    play sound "audio/sfx/stinger.ogg"
    play music "audio/sfx/Wind.ogg" fadein 1.0
    scene black with pixellate
    show text "{size=+90}{b}{color=#f00}Hail.{/color}{/b}{/size}":
        yalign 0.3    

    call screen death_nav    

return


