label death_screen:
    play sound "audio/sfx/stinger.ogg"
    play music "audio/music/mixkit-feedback-dreams-588- Eugenio Mininni.ogg"
    scene black with pixellate
    show text "{size=+90}{b}{color=#f00}YOU HAVE PERISHED{/color}{/b}{/size}"

    call screen death_nav

return

    