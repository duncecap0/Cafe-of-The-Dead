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
        "sage_health >= 5", "s/s_5.png",
        "sage_health == 4", "s/s_4.png",
        "sage_health == 3", "s/s_3.png",
        "sage_health == 2", "s/s_2.png",
        "sage_health == 1", "s/s_1.png",
        "sage_health == 0", "s/s_0.png",
    )

image rockstatus:
    ConditionSwitch(
        "rocky_health >= 5", "s/s_5.png",
        "rocky_health == 4", "s/s_4.png",
        "rocky_health == 3", "s/s_3.png",
        "rocky_health == 2", "s/s_2.png",
        "rocky_health == 1", "s/s_1.png",
        "rocky_health == 0", "s/s_0.png",
    )
image normstatus:
    ConditionSwitch(
        "norman_health >= 5", "s/s_5.png",
        "norman_health == 4", "s/s_4.png",
        "norman_health == 3", "s/s_3.png",
        "norman_health == 2", "s/s_2.png",
        "norman_health == 1", "s/s_1.png",
        "norman_health == 0", "s/s_0.png",
    )
image vinnstatus:
    ConditionSwitch(
        "vinnie_health >= 5", "s/s_5.png",
        "vinnie_health == 4", "s/s_4.png",
        "vinnie_health == 3", "s/s_3.png",
        "vinnie_health == 2", "s/s_2.png",
        "vinnie_health == 1", "s/s_1.png",
        "vinnie_health == 0", "s/s_0.png",
    )



screen character_stats:
    zorder 2
    frame:
        background Frame("gui/uibox.png", 25, 25, tile="integer")
        padding (30,25)
        xalign 0.99
        yalign 0.01
        hbox:
            style_prefix "status"
            text "Sage:"
            add "sagestatus"
            text " | "
            text "Norman: "
            add "normstatus"
            text " | "
            text "Rocky: "
            add "rockstatus"
            text " | "
            text "Vinnie: "
            add "vinnstatus"

            #text "[pov] Health: [sage_health] "
            #text "Norman Health: [norman_health] "
            #text "Rocky Health: [rocky_health] "
            #text "Vinnie Health: [vinnie_health] "
    
    vbox:
        xalign 1.0
        yalign 1.0

        text "Ammo: [ammo]"
        text "Insanity: [insanity_level]"

        if norman_dead == False:
            text "Norman: ALIVE"
        else:
            text "Norman: DECEASED"

        if rocky_dead == False:
            text "Rocky: ALIVE"
        else:
            text "Rocky: DECEASED"

        if vinnie_dead == False:
            text "Vinnie: ALIVE"
        else:
            text "Vinnie: DECEASED"




image zombie:
    "zombie.png"


screen kill_zombie():

    text "Click to kill or you die in 3 seconds"

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "zombie"
        action [Hide("kill_zombie")]


    timer 3.0 action Jump("death_screen")


screen death_nav():
    
        vbox:
            xalign 0.5
            yalign 0.7
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Main Menu") action MainMenu()

label death_screen:
    play sound "audio/sfx/stinger.ogg"
    play music "audio/music/mixkit-feedback-dreams-588- Eugenio Mininni.ogg"
    
    scene black with pixellate
    show text "{size=+90}{b}{color=#f00}YOU HAVE PERISHED{/color}{/b}{/size}"

    call screen death_nav

label win_screen:
    play sound "audio/sfx/stinger.ogg"
    play music "audio/music/mixkit-minimal-techno-01-162- Alejandro Magaña (A. M.).ogg"

    scene black with pixellate
    show text "{size=+90}{b}{color=#15ff00}GAME WIN{/color}{/b}{/size}"

    call screen death_nav
    
return


