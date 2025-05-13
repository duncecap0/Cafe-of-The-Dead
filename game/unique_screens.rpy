
################################################################################
## OLD Party Status Screen
################################################################################

style status_text is text:
    outlines [ (3, "#300019", 0, 0) ]
    outline_scaling "linear"

style partycheck_text is text:
    outlines [ (3, "#300019", 0, 0) ]
    outline_scaling "linear"
    line_spacing 7
        
# Icons for each party member
# Replace gui/___.png with the character specific one

image sagestatus: 
    ConditionSwitch(
        "sage_health >= 5", 'sage_healthy',
        "sage_health == 4", 'sage_healthy',
        "sage_health == 3", 'sage_healthy',
        "sage_health == 2", 'sage_hurt',
        "sage_health == 1", 'sage_hurt',
        "sage_health <= 0", 'sage_hurt',
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
image sanitystatus:
    ConditionSwitch(
        "insanity_level >= 3", "images/sprites/sage/side p 16.png",
        "insanity_level == 2", "images/sprites/sage/side p 17.png",
        "insanity_level == 1", "images/sprites/sage/side p 7.png",
        "insanity_level <= 0", "images/sprites/sage/side p 1.png",
    )

screen old_character_stats():
    zorder 2
    
    frame:
        background Frame("gui/uibox.png", 1, 1, tile="integer")
        padding (5,10)
        xalign 0.99
        yalign 0.01
        hbox:
            xalign 0.99
            spacing 3
            style_prefix "status"
            add "sage_health"
            text "[sage_health]"
            text "|"
            add "normstatus"
            text "[norman_health]"
            text "|"
            add "rockstatus"
            text "[rocky_health]"
            text "|"
            add "vinnstatus"
            text "[vinnie_health]"

################################################################################
## NEW Party Status Screen
################################################################################

## TormentedStudios button scale https://www.reddit.com/r/RenPy/comments/yvz8x8/increase_the_size_of_a_button_when_hovered_over/
## at buttonScale
image sage healthy = "gui/sage healthy.png"
image sage hurt = "gui/sage hurt.png"

image norman healthy = "gui/norm healthy.png"
image norman hurt = "gui/norm hurt.png"

image vin healthy = "gui/vin healthy.png"
image vin hurt = "gui/vin hurt.png"

image rocky healthy = "gui/rocky healthy.png"
image rocky hurt = "gui/rocky hurt.png"

image grave:
    "gui/dead.png"
    xpos -8

image paper_inventory:
    "images/paper.png"
    zoom 0.5

screen character_stats():
    zorder 2
    style_prefix "status"
    frame:
        background Frame("gui/shadow.png", 15, 15, tile="integer")
        padding (15,10)
        xalign 1.0
        hbox:

        ### SAGE 

            if sage_health <=0:
                imagebutton:
                    xpos 10
                    idle "grave"
                    hover "grave"
                    at buttonScale_sticker   
                    action [Play("sound", "audio/voices/sage beep.ogg"), ShowMenu("group_check")]
                text "[sage_health] |"

            elif sage_health >=3:
                imagebutton:
                    idle "sage healthy"
                    hover "sage healthy"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/sage beep.ogg"), ShowMenu("group_check")]
                text "[sage_health] |"    

            elif sage_health <=2:
                imagebutton:
                    idle "sage hurt"
                    hover "sage hurt"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/sage beep.ogg"), ShowMenu("group_check")]
                text "[sage_health] |"


        ### NORMAN  

            if norman_health <=0:
                imagebutton:
                    xpos 10
                    idle "grave"
                    hover "grave"
                    at buttonScale_sticker   
                    action [Play("sound", "audio/voices/norman beep.ogg"), ShowMenu("group_check")]
                text "[norman_health] | "

            elif norman_health >=3:
                imagebutton:
                    idle "norman healthy"
                    hover "norman healthy"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/norman beep.ogg"), ShowMenu("group_check")]
                text "[norman_health] |"

            elif norman_health <=2:
                imagebutton:
                    idle "norman hurt"
                    hover "norman hurt"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/norman beep.ogg"), ShowMenu("group_check")]
                text "[norman_health] |"    

        ### VINNIE 

            if vinnie_health <=0:
                imagebutton:
                    xpos 10
                    idle "grave"
                    hover "grave"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/vin beep.ogg"), ShowMenu("group_check")]
                text "[vinnie_health] |"

            elif vinnie_health >=3:
                imagebutton:
                    idle "vin healthy"
                    hover "vin healthy"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/vin beep.ogg"), ShowMenu("group_check")]
                text "[vinnie_health] |"

            elif vinnie_health <=2:
                imagebutton:
                    idle "vin hurt"
                    hover "vin hurt"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/stab.ogg"), ShowMenu("group_check")]
                text "[vinnie_health] |"    

        ### ROCKY 

            if rocky_health <= 0:
                imagebutton:
                    xpos 10
                    idle "grave"
                    hover "grave"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/stab.ogg"), ShowMenu("group_check")]
                text "[rocky_health] |"

            elif rocky_health >=3:
                imagebutton:
                    idle "rocky healthy"
                    hover "rocky healthy"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/rocky beep.ogg"), ShowMenu("group_check")]
                text "[rocky_health] |"    

            elif rocky_health <=2:
                imagebutton:
                    idle "rocky hurt"
                    hover "rocky hurt"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/rocky beep.ogg"), ShowMenu("group_check")]
                text "[rocky_health] |"    


image inventory = "gui/inventory.png"
image inventoryphone = "gui/phone/inventory.png"

image bullets = "gui/ammo.png"
image bulletsphone = "gui/phone/ammo.png"

screen ammo_stats():

    zorder 3

    frame:

        background Frame("gui/shadow.png", 1, 1, tile="integer")

        padding (5,10)

        style_prefix "status"  

        vbox:

            spacing 5

            if renpy.variant("small"):

                imagebutton:
                    idle "bulletsphone"
                    hover "bulletsphone"
                    at buttonScale_sticker
                    action Play("sound", "audio/sfx/cock.ogg")
                text "{size=*0.9}Ammo:[ammo]{/size}"

                imagebutton:
                    idle "inventoryphone"
                    hover "inventoryphone"
                    at buttonScale_sticker
                    action [Play("sound", "audio/sfx/use.ogg"), ShowMenu("inventory_menu")]
                text "{size=*0.9}Inventory{/size}"

            else:

                imagebutton:
                    idle "bullets"
                    hover "bullets"
                    at buttonScale_sticker
                    action Play("sound", "audio/sfx/cock.ogg")
                text "{size=*0.9}Ammo:[ammo]{/size}"   

                imagebutton:
                    idle "inventory"
                    hover "inventory"
                    at buttonScale_sticker
                    action [Play("sound", "audio/sfx/use.ogg"), ShowMenu("inventory_menu")]
                text "{size=*0.9}Inventory{/size}"

################################################################################
## MENU ITEMS
################################################################################

screen sanity_menu():

        tag menu
        
        use game_menu(_("Sanity Check"), scroll="viewport"):

            hbox:
                style_prefix "status"
                add "sanitystatus":
                    ypos 40
                text "{size=*2.5}Insanity Level: [insanity_level]{/size}":
                    ypos 90

image sagestick = "gui/sage sticker.png"
image normstick = "gui/norm sticker.png"
image vinstick = "gui/vin sticker.png"
image rockstick = "gui/rocky sticker.png"
image tarastick = "gui/tara sticker.png"

screen group_check():
      
    tag menu 
    style_prefix "partycheck"  
    use game_menu(_("Party Check")):
            hbox:
                ypos 40
                spacing 10
                xpos -3
                ## TormentedStudios button scale https://www.reddit.com/r/RenPy/comments/yvz8x8/increase_the_size_of_a_button_when_hovered_over/
                imagebutton:
                    idle "sagestick"
                    hover "sagestick"
                    at buttonScale_sticker
                    action [Play("sound", "audio/voices/sage beep.ogg")]
                if norman_dead == False:
                    imagebutton:
                        idle "normstick"
                        hover "normstick"
                        at buttonScale_sticker
                        action [Play("sound", "audio/voices/norman beep.ogg")]
                if vinnie_dead == False:
                    imagebutton:
                        ypos -20
                        idle "vinstick"
                        hover "vinstick"
                        at buttonScale_sticker
                        action [Play("sound", "audio/voices/vin beep.ogg")]
                if rocky_dead == False:
                    imagebutton:
                        ypos -5
                        idle "rockstick"
                        hover "rockstick"
                        at buttonScale_sticker
                        action [Play("sound", "audio/voices/rocky beep.ogg")]
                if tara == True:
                    imagebutton:
                        idle "tarastick"
                        hover "tarastick"
                        at buttonScale_sticker
                        action [Play("sound", "audio/voices/tara beep.ogg")]
            hbox:
                ypos 350
                spacing 10
                xsize -0.1
                text "Health: [sage_health] Insanity: [insanity_level]"
                if norman_dead == False and norman_affection <= 4:
                    text "Health: [norman_health] Motivated: [expose_samsara_together_3] Interest: [norman_affection]"
                elif norman_dead == False and norman_affection >= 5:
                    text "Health: [norman_health] Motivated: [expose_samsara_together_3] BOYFRIEND UNLOCKED: [norman_affection]"
                if vinnie_dead == False:
                    text "Health: [vinnie_health] Motivated: [expose_samsara_together_2]"
                if rocky_dead == False:
                    text "Health: [rocky_health] Motivated: [expose_samsara_together]"
                if tara == True:
                    text "Motivated: [tara_against_dad]"

screen achievements_menu():

    tag menu 

    use game_menu(_("Achievements"), scroll="viewport"):
        vbox:
            style_prefix "status"
            spacing 20

            if persistent.trueending == True:
                text "Achievement Unlocked: Best Friends FOREVER"
                text "Everyone PLUS secret character survive ending!"
                text "-----"
            else:
                text "Achievement Locked: Best Friends FOREVER"
                text "Everyone PLUS secret character survive ending!"
                text "-----"

            if persistent.touchtoilet5times == True:
                text "Achievement Unlocked: PROFESSIONAL TOILET INSPECTOR!"
                text "Inspect the toilet 5 times"
                text "-----"
            else:
                text "Achievement Locked: PROFESSIONAL TOILET INSPECTOR!"
                text "Inspect the toilet 5 times"
                text "-----"

            if persistent.dontuseitems == True:
                text "Achievement Unlocked: Bad MotherFucker!"
                text "Beat the game without using health items on party, any bullets, crowbar, and vinnie's knife!"
                text "-----"
            else:
                text "Achievement Locked: Bad MotherFucker!"
                text "Beat the game without using health items on party, any bullets, crowbar, and vinnie's knife!"
                text "-----"

            if persistent.killnorman == True:
                text "Achievement Unlocked: Taking The Dog Out Back"
                text "Beat the game with Norman dead"
                text "-----"
            else:
                text "Achievement Locked: Taking The Dog Out Back"
                text "Beat the game with Norman dead"
                text "-----"

            if persistent.killvin == True:
                
                text "Achievement Unlocked: Roadkill After All"
                text "Beat the game with Vinnie dead"
                text "-----"
            else:
                text "Achievement Locked: Roadkill After All"
                text "Beat the game with Vinnie dead"
                text "-----"

            if persistent.killrocky == True:
                text "Achievement Unlocked: Wolf or Fox? Now we will never know..."
                text "Beat the game with Rocky dead"
                text "-----"
            else:
                text "Achievement Locked: Wolf or Fox? Now we will never know..."
                text "Beat the game with Rocky dead"
                text "-----"

            if persistent.savetara == True:
                text "Achievement Unlocked: Coming Out The Closet"
                text "Beat the game with secret character unlocked"
                text "-----"
            else:
                text "Achievement Locked: Coming Out The Closet"
                text "Beat the game with secret character unlocked"
                text "-----"

            if persistent.tara_against_dad == True:
                text "Achievement Unlocked: Mad Father"
                text "Beat the game with secret character motivated"
                text "-----"
            else:
                text "Achievement Locked: Mad Father"
                text "Beat the game with secret character motivated"
                text "-----"

            if persistent.dontusebullets == True:
                text "Achievement Unlocked: I Don't Need No Dang Gun!"
                text "Beat the game with 3 bullets"
                text "-----"
            else:
                text "Achievement Locked: I Don't Need No Dang Gun!"
                text "Beat the game with 3 bullets"
                text "-----"

            if persistent.nosanityloss == True:
                text "Achievement Unlocked: Coffee AU"
                text "Beat the game with 0 sanity loss"
                text "-----"
            else:
                text "Achievement Locked: Coffee AU"
                text "Beat the game with 0 sanity loss"
                text "-----"

            if persistent.romancenorman == True:
                text "Achievement Unlocked: Dog Boyfriend"
                text "Beat the game with Norman romanced"
                text "-----"
            else:
                text "Achievement Locked: Dog Boyfriend"
                text "Beat the game with Norman romanced"
                text "-----"

            if persistent.petty_sage == True:
                text "Achievement Unlocked: Nice Try"
                text "Shoot at the CEO"
                text "-----"
            else:
                text "Achievement Locked: Nice Try"
                text "Shoot at the CEO"
                text "-----"

            if persistent.motivatefriends == True:
                text "Achievement Unlocked: Samsara's End"
                text "Beat the game with all friends motivated"
                text "-----"
            else:
                text "Achievement Locked: Samsara's End" 
                text "Beat the game with all friends motivated"
                text "-----"

            if persistent.hailending == True:
                text "Achievement Unlocked: Hail"
                text "Hail."
                text "-----"
            else:
                text "                                  "
                text "                                  "
                text "                                  "
                text "                                  "
                text "                                  "
                text "                                  "
                text "                                  "

                text "Achievement Locked: ???"
                text "Beat game while in possession of Norman's gun while high insanity and push Norman into danger in office confrontation with all others dead beforehand and secret character never obtained"
                text "-----"


screen inventory_menu():

        tag menu

        use game_menu(_("Inventory"), scroll="viewport"):

            vbox:
                style_prefix "status"
                spacing 20

                if sage_has_gun or norman_has_gun or vinnie_has_gun or rocky_has_gun:
                    text "Gun: It's a S&W 5946 9mm handgun, I wonder when Norman had to use it?"
                    text "-----"
                if vinnies_knife == True and vinnie_dead == False:
                    text "Vinnie's Knife: An iridescent butterfly knife Vinnie stole from some gas station, doubt it would last long in an actual fight..."
                    text "-----"
                if worker_key_collect == True:
                    text "Padlock Key: A small key used for some type of padlock."
                    text "-----"
                if crowbar_collected == True:
                    text "Crowbar: This crowbar has seen better days... it will most likely break soon."
                    text "-----"
                #if medkit_used == True:
                #    text "Medkit: It's a surprisingly advanced medical kit, it has intense antiseptics and bandages"
                #if morphine_used == True:
                #    text "Morphine: A syringe containing a clear liquid, hope the needle is clean..."
                if examined_hakim == True:
                    text "Old Paper: This paper was found on a scientist named \"Hakim Lee\"; it contains a peculiar shape pattern. It has various handwritings on it, implying more than one person wrote on it. I can only imagine how crazed they became here..."
                    add "paper_inventory"
                    text "-----"                
                if monday == True and word_puzzle_completed == False:
                    text "Diary entry that contains the letters \"MON\"."
                    text "-----"

                if tuesday_and_thursday == True and word_puzzle_completed == False:
                    text "Computer email that contains the letters \"TUE\" and \"THU\"."
                    text "-----"

                if wednesday_and_friday == True and word_puzzle_completed == False:
                    text "Worker memo that contains the letters \"WED\" and \"FRI\"."
                    text "-----"

                if puzzle_piece_a_collect == True:
                    text "USB Drive A: Looks like a USB marked with the letter \"A\" in marker."
                    text "-----"

                if puzzle_piece_b_collect == True:
                    text "USB Drive B: Looks like a USB marked with the letter \"B\" in marker."
                    text "-----"

                if drawer_key_collected == True:
                    text "Drawer Key: A very VERY small key, it must be used on some type of drawer around here."
                    text "-----"

                if keycard == True:
                    text "Employee Keycard: A keycard belonging to a Head Senior Researcher employee named \"Hakim Lee\", it has a very high level of access."
                    text "-----"

                #if crowbar_collected == True:
                    #text "Crowbar:"
                #if medkit == True:
                #   text "Medkit:"
                #if medkit == True:
                    #text "Medkit:"
                #if crowbar_collected == True:
                    #text "Crowbar:"
                #if medkit == True:
                #   text "Medkit:"


################################################################################
## RESET VARIABLES TO ZERO 0
################################################################################

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

    def addAmmo_level(delta):
        global ammo
        ammo = max(0, ammo + delta)

################################################################################
## ENDINGS NAV
################################################################################   

screen death_nav():
        vbox:
            xalign 0.5
            yalign 0.6
            spacing 25
            textbutton _("Load") action ShowMenu("load"):
                xalign 0.5
            textbutton _("Main Menu") action MainMenu()

label death_screen:
    window hide diss
    $ quick_menu = False
    hide screen character_stats with dissolve
    hide screen ammo_stats with dissolve
    play sound "audio/sfx/stinger.ogg"
    play music "audio/music/die it is then.ogg" fadein 1.0
    scene black with dissolve
    show text "{size=+90}{b}{color=#f00}{k=+10}GAME OVER{/k}{/color}{/b}{/size}":
            yalign 0.3    

    call screen death_nav

label win_screen:
    window hide diss
    play sound "audio/sfx/stinger.ogg"
    scene black with dissolve

    show text "{size=+90}{b}{k=+10}GAME OVER{/k}{/b}{/size}":
        yalign 0.3    
        
    call screen death_nav

label insane_screen:
    window hide diss
    play sound "audio/sfx/stinger.ogg"
    play music "audio/sfx/Wind.ogg" fadein 1.0
    scene black with dissolve
    show text "{size=+90}{b}{color=#f00}{k=+10}Hail.{/k}{/color}{/b}{/size}":
        yalign 0.3    

    call screen death_nav    

label sad_screen:
    window hide diss
    play sound "audio/sfx/stinger.ogg"
    play music "audio/sfx/Wind.ogg" fadein 1.0
    scene black with dissolve
    show text "{size=+90}{b}{color=#f00}{k=+10}Sad Ending{/k}{/color}{/b}{/size}":
        yalign 0.3    

    call screen death_nav  


#RED BUTTON
image red_butt:
    "gui/red_butt.png"
    rotate 0.0

image red_butt_right:
    "gui/red_butt.png"
    rotate 90.0

image red_butt_up:
    "gui/red_butt.png"
    rotate 180.0 

image red_butt_down:
    "gui/red_butt.png"
    rotate 270.0

image red_butt_left:
    "gui/red_butt.png"
    rotate 160.0

#GREEN BUTTON

image green_butt:
    "gui/green_butt.png"
    rotate 0.0

image green_butt_right:
    "gui/green_butt.png"
    rotate 90.0

image green_butt_up:
    "gui/green_butt.png"
    rotate 180.0

image green_butt_down:
    "gui/green_butt.png"
    rotate 270.0

image green_butt_left:
    "gui/green_butt.png"
    rotate 160.0

#BLUE BUTTON

image blue_butt:
    "gui/blue_butt.png"
    rotate 0.0

image blue_butt_right:
    "gui/blue_butt.png"
    rotate 90.0

image blue_butt_up:
    "gui/blue_butt.png"
    rotate 180.0

image blue_butt_down:
    "gui/blue_butt.png"
    rotate 270.0

image blue_butt_left:
    "gui/blue_butt.png"
    rotate 160.0

#YELLOW BUTTON

image yellow_butt:
    "gui/yellow_butt.png"
    rotate 0.0

image yellow_butt_right:
    "gui/yellow_butt.png"
    rotate 90.0

image yellow_butt_up:
    "gui/yellow_butt.png"
    rotate 180.0

image yellow_butt_down:
    "gui/yellow_butt.png"
    rotate 270.0
    
image yellow_butt_left:
    "gui/yellow_butt.png"
    rotate 160.0

################################################################################
## LAB MINIGAME
################################################################################  

default red_selected_count = 0
default green_selected_count = 0
default blue_selected_count = 0
default yellow_selected_count = 0


default red_butt_correct = False

default green_butt_correct = False

default blue_butt_correct = False

default yellow_butt_correct = False

label butt_puzzle_exit:
    show screen character_stats with Dissolve(0.2)
    show screen ammo_stats with Dissolve(0.2)
    hide black with Dissolve(0.2)        
    "I wonder if the correct shape pattern appears anywhere else in this lab?" with Dissolve(0.2)
    jump pnc_loop

    screen lab_minigame():
            #text "complete: [butt_puzzle_complete], yellow count: [yellow_selected_count], yellow: [yellow_butt_correct], red count: [red_selected_count], red: [red_butt_correct]":
                #xpos 80
                #ypos 100
            grid 4 1:
                yalign 0.4
                imagebutton:
                    xpos 100
                    idle "red_butt"
                    hover "red_butt"
                    selected_idle "red_butt_right"
                    selected_hover "red_butt_right"
                    action [Play("sound", "audio/sfx/butt_touch.ogg"), SetVariable("red_selected_count", red_selected_count +1), ToggleVariable("red_butt_correct", False, False)]
                    selected (red_selected_count)

                    if red_selected_count == 2:
                        action [ToggleVariable("red_butt_correct", True, False), SetVariable("red_selected_count", red_selected_count +1), Play("sound", "audio/sfx/correct beep.ogg")]
                        selected_idle "red_butt_up"
                        selected_hover "red_butt_up"

                    elif red_selected_count == 3:
                        action [ToggleVariable("red_butt_correct", False, False), SetVariable("red_selected_count", red_selected_count +1), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "red_butt_down"
                        selected_hover "red_butt_down"

                    elif red_selected_count == 4:
                        action [ToggleVariable("red_butt_correct", False, False), SetVariable("red_selected_count", red_selected_count == 0), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "red_butt_left"
                        selected_hover "red_butt_left"
                        
                imagebutton:
                    xpos 100
                    ypos 100
                    idle "green_butt"
                    hover "green_butt"
                    selected_idle "green_butt_left"
                    selected_hover "green_butt_left"
                    action [Play("sound", "audio/sfx/butt_touch.ogg"), SetVariable("green_selected_count", green_selected_count +1), ToggleVariable("green_butt_correct", False, False)]
                    selected (green_selected_count)

                    if green_selected_count == 2:
                        action [ToggleVariable("green_butt_correct", False, False), SetVariable("green_selected_count", green_selected_count +1), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "green_butt_up"
                        selected_hover "green_butt_up"

                    elif green_selected_count == 3:
                        action [ToggleVariable("green_butt_correct", True, False), SetVariable("green_selected_count", green_selected_count +1), Play("sound", "audio/sfx/correct beep.ogg")]
                        selected_idle "green_butt_down"
                        selected_hover "green_butt_down"

                    elif green_selected_count == 4:
                        action [ToggleVariable("green_butt_correct", False, False), SetVariable("green_selected_count", green_selected_count == 0), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "green_butt_right"
                        selected_hover "green_butt_right"

                imagebutton:
                    xpos -100
                    ypos 100
                    idle "blue_butt"
                    hover "blue_butt"
                    selected_idle "blue_butt_right"
                    selected_hover "blue_butt_right"
                    action [Play("sound", "audio/sfx/butt_touch.ogg"), SetVariable("blue_selected_count", blue_selected_count +1), ToggleVariable("blue_butt_correct", False, False)]
                    selected (blue_selected_count)

                    if blue_selected_count == 2:
                        action [ToggleVariable("blue_butt_correct", True, False), SetVariable("blue_selected_count", blue_selected_count +1), Play("sound", "audio/sfx/correct beep.ogg")]
                        selected_idle "blue_butt_up"
                        selected_hover "blue_butt_up"

                    elif blue_selected_count == 3:
                        action [ToggleVariable("blue_butt_correct", False, False), SetVariable("blue_selected_count", blue_selected_count +1), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "blue_butt_down"
                        selected_hover "blue_butt_down"

                    elif blue_selected_count == 4:
                        action [ToggleVariable("blue_butt_correct", False, False), SetVariable("blue_selected_count", blue_selected_count == 0), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "blue_butt_left"
                        selected_hover "blue_butt_left"

                imagebutton:
                    xpos -270
                    ypos 100
                    idle "yellow_butt_down"
                    hover "yellow_butt_down"
                    selected_idle "yellow_butt_right"
                    selected_hover "yellow_butt_right"
                    action [Play("sound", "audio/sfx/butt_touch.ogg"), SetVariable("yellow_selected_count", yellow_selected_count +1), ToggleVariable("yellow_butt_correct", False, False)]
                    selected (yellow_selected_count)

                    if yellow_selected_count == 2:
                        action [ToggleVariable("yellow_butt_correct", True, False), SetVariable("yellow_selected_count", yellow_selected_count +1), Play("sound", "audio/sfx/correct beep.ogg")]
                        selected_idle "yellow_butt_up"
                        selected_hover "yellow_butt_up"

                    elif yellow_selected_count == 3:
                        action [ToggleVariable("yellow_butt_correct", False, False), SetVariable("yellow_selected_count", yellow_selected_count +1), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "yellow_butt"
                        selected_hover "yellow_butt"

                    elif yellow_selected_count == 4:
                        action [ToggleVariable("yellow_butt_correct", False, False), SetVariable("yellow_selected_count", yellow_selected_count == 0), Play("sound", "audio/sfx/butt_touch.ogg")]
                        selected_idle "yellow_butt_left"
                        selected_hover "yellow_butt_left"

            frame:
                background Frame("gui/uibox.png", 200, 20, tile="integer")
                padding (30,20)
                xpos 100
                ypos 590
                if yellow_butt_correct == True and blue_butt_correct == True and green_butt_correct == True and red_butt_correct == True:
                    textbutton "Exit: PUZZLE COMPLETE!":
                        style_prefix "status"
                        ypos -5
                        action [ToggleVariable("butt_puzzle_complete", True, False), Play("sound", "audio/sfx/zap.ogg"), Jump("butt_puzzle_done")]
                else:
                    textbutton "Exit":
                        style_prefix "status"
                        ypos -5
                        action Jump("butt_puzzle_exit")

    screen exit_button():
            frame:
                background Frame("gui/uibox.png", 20, 20, tile="integer")
                padding (30,20)
                xpos 100
                ypos 590
                textbutton "Exit":
                    style_prefix "status"
                    ypos -5
                    action Jump("paper_go_away")

################################################################################
## NEW NOTIFICATION SYSTEM
################################################################################   

## multiple notify messages from https://lemmasoft.renai.us/forums/viewtopic.php?t=47025

default notices = []

init python:

    def notify_me(m=""):
        global notices
        if m:
            notices.append(m)
        if notices:
            renpy.show_screen('notify_plus', notices=notices)
            notices = []

screen notify_plus(notices):

    zorder 100
    style_prefix "notify"

    for dd, i in enumerate(notices):
        frame at notify_plus_appear(dd*3.5):
            text i

    timer 4.25+(dd*3.5) action Hide('notify_plus')

transform notify_plus_appear(dd=0):
    on show:
        yoffset dd*1
        alpha 0 xanchor 1.0 xpos 0.0
        pause dd
        linear .25 alpha 1.0 xalign 0.0
        pause 3.25
        linear .5 alpha 0.0

return


