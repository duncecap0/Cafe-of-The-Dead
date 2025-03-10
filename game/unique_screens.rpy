            
screen character_stats:
    zorder 2
    hbox:
        xalign 1.0

        text "[pov] Health: [sage_health] "
        text "Norman Health: [norman_health] "
        text "Rocky Health: [rocky_health] "
        text "Vinnie Health: [vinnie_health] "
    
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

    hide screen kill_zombie
    
    scene black with pixellate
    show text "{size=+90}{b}{color=#f00}YOU HAVE PERISHED{/color}{/b}{/size}"

    call screen death_nav

return


