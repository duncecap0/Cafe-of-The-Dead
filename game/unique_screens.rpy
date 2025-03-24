            
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


