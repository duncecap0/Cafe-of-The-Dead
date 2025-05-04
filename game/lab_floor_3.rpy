
#variables
default tara_against_dad = False
default tara_hostage = False
default ceo_caught_bluff = False
default vinnie_lab_death = False
default rocky_lab_death = False
default norman_lab_death = False

default norman_lab_push_death = False
default vinnie_lab_push_death = False
default rocky_lab_push_death = False

default rocky_tantrum = False
default tara_seen_tank = False

default expose_samsara_together_3 = False

default keycard_accepted = False

default examined_lab_note_2 = False

default examined_hakim = False

default n_pill_reject = False

default butt_puzzle_complete = False

default examined_interface = True

#ITEMS
default drawer_key_collected = False
default keycard = False
default pills = False
default lab_ammo_1_collected = False
default lab_ammo_2_collected = False

#PIECE PUZZLE

default puzzle_piece_b_collect = False
default puzzle_piece_a_collect = False

default piece_puzzle_b = False
default piece_puzzle_a = False

#Final boss
default boss_juggernaut_zombie = True
default boss_zombie_horde = True

label lab_floor_3:
    play sound "audio/sfx/elevatording.ogg"
    "The elevator comes to a slow stop and the doors begin to slide open"
    play music "audio/music/FLOOR_3.mp3"
    scene lab main room with Dissolve(0.2)
    show screen character_stats with Dissolve(0.2)
    show screen ammo_stats with Dissolve(0.2)
    $ current_room = "lab_start" # this initializes the point'n'click segment to display the correct set of buttons.
    "It's the lab...{w=.3} let's look for a way out through here"
    if tara == True:
        show w 15 at right2 with Dissolve(0.2)
        w "I know he's my father but if you see him, {w=.3}don't hesitate to use force if necessary he's a dangerous man"
        if vinnie_dead == False:
            show v 5 at right with Dissolve(0.2)
            v "PERMISSION TO WHOOP ASS GRANTED"
        if rocky_dead == False:
            show r 10 at left with Dissolve(0.2)
            r "I didn't need permission but thanks I guess"
        if norman_dead == False:
            show n 1 with Dissolve(0.2)
            n "We'll use diplomacy to solve our problems!"
        if insanity_level >=1:
            show static_anim with Dissolve(0.2)
            play audio "audio/sfx/static.ogg"
            camera:
                perspective True
                easein_bounce 0.54 zpos -20 
            pause 0.3
            hide static_anim with Dissolve(0.2)
            camera:
                reset
            "I'll personally kill him for putting me through this"
        p 4"Don't worry,{w=.3} I'll be on the lookout for him"

    if vinnie_dead == False and rocky_dead == False and norman_dead == False:
        show v 2 4 at right with Dissolve(0.2)
        v "IT'S THE FINAL COUNTDOWN!! DUH DUH DUH DUHHHH!!!"
        show r 2a at left with Dissolve(0.2)
        r "SHUT UP!"
    if norman_dead == False:
        show n 2 with Dissolve(0.2)
        n "We can do this!"
    p 1"This place is huge, {w=.3}gonna be a hard time navigating"
    if vinnie_dead == False and rocky_dead == False and norman_dead == False:
        p "It shouldn't be a problem for us!"
 
    scene lab main room with Dissolve(0.2)
    jump lab_start



##LAB ROOMS
## YES THERE ARE A LOT ;(

##LAB DOWNSTAIRS HUB
label lab_start:
    window hide diss
    scene lab main room with Dissolve(0.2)
    $ current_room = "lab_start" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS CENTER BOTTOM ROOM

label lab_puzzle_b_room:
    window hide diss
    scene lab puzzle room with Dissolve(0.2)
    $ current_room = "lab_puzzle_b_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS LEFT ROOMs

label lab_radio:
    window hide diss
    scene lab radio with Dissolve(0.2)
    $ current_room = "lab_radio" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS RIGHT ROOMS
label lab_tanks_room:
    window hide diss
    scene lab tanks with Dissolve(0.2)
    $ current_room = "lab_tanks_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_downstairs_hall:
    window hide diss
    scene lab keycard entrance with Dissolve(0.2)
    $ current_room = "lab_downstairs_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_hakim_room:
    window hide diss
    scene lab side room with Dissolve(0.2)
    $ current_room = "lab_hakim_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_puzzle_piece_a_collect_room:
    window hide diss
    scene lab orientation puzzle room with Dissolve(0.2)
    $ current_room = "lab_puzzle_piece_a_collect_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

#UPSTAIRS !!!!!!!

label lab_upstairs:
    window hide diss

    scene lab upstairs main room with Dissolve(0.2)
    $ current_room = "lab_upstairs" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#UPSTAIRS LEFT ROOMS !!!!!!!

label lab_upstairs_left_hall:
    window hide diss

    scene lab upstairs left hall with Dissolve(0.2)
    $ current_room = "lab_upstairs_left_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label lab_puzzle_a_room:
    window hide diss

    scene lab puzzle room with Dissolve(0.2)
    $ current_room = "lab_puzzle_a_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_puzzle_piece_b_collect_room:
    window hide diss

    scene lab orientation puzzle room with Dissolve(0.2)
    $ current_room = "lab_puzzle_piece_b_collect_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_closet_room:
    window hide diss

    scene lab closet with Dissolve(0.2)
    $ current_room = "lab_closet_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

#UPSTAIRS RIGHT ROOMS DONT CONFUSE FOR RIGHT-MOST ROOMS !!!!!!!
##### RIGHT !!!!!!!!!!!!!!!!

label lab_upstairs_right_hall:
    window hide diss

    scene lab upstairs right hall with Dissolve(0.2)
    $ current_room = "lab_upstairs_right_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_desk:
    window hide diss

    scene lab desk with Dissolve(0.2)
    $ current_room = "lab_desk" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_keycard_room:
    window hide diss

    scene lab keycard room with Dissolve(0.2)
    $ current_room = "lab_keycard_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_tara_tank:
    window hide diss

    scene lab tara tank with Dissolve(0.2)
    $ current_room = "lab_tara_tank" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_upstairs_test_room:
    window hide diss

    scene lab upstairs test room with Dissolve(0.2)
    $ current_room = "lab_upstairs_test_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#UPSTAIRS RIGHT-MOST ROOMS DONT CONFUSE FOR RIGHT ROOMS !!!!!!!
##### RIGHT-MOST !!!!!!!!!!!!!!!!

label lab_upstairs_rightmost_hall:
    window hide diss

    scene lab hall with Dissolve(0.2)
    $ current_room = "lab_upstairs_rightmost_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_keycard_entrance_room:
    window hide diss

    scene lab keycard entrance with Dissolve(0.2)
    $ current_room = "lab_keycard_entrance_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

#LAB POINT AND CLICK LABELS

#lab puzzle shenanigans

label puzzle_piece_a_collect:
    $ puzzle_piece_a_collect = True
    "A USB drive identified with the letter \"A\" in marker is on the floor... I stash it away"
    $ renpy.notify("USB Drive A has been added to your inventory!")
    jump pnc_loop

label puzzle_piece_b_collect:
    $ puzzle_piece_b_collect = True
    "A USB drive identified with the letter \"B\" in marker is on the floor... I stash it away"
    $ renpy.notify("USB Drive B has been added to your inventory!")
    jump pnc_loop

label drawer_key:
    $ drawer_key_collected = True
    "I find a very small key!"
    $ renpy.notify("Drawer Key has been added to your inventory!")
    jump pnc_loop

label piece_puzzle_a:
    if piece_puzzle_a == True:
        "USB plug A has already been activated!"
    elif puzzle_piece_a_collect == True:
        $ piece_puzzle_a = True
        $ puzzle_piece_a_collect = False
        $ renpy.notify("USB Drive A has been removed from your inventory!")
        play sound "audio/sfx/correct beep.ogg"
        "I insert USB Drive A into it's respective place and a loud beep confirms I solve it!"
    else:
        play sound "audio/sfx/wrong beep.ogg"
        "A USB plug on this device is marked \"A\" and needs it to be activated"

    jump pnc_loop

label piece_puzzle_b:

    if piece_puzzle_b == True:
        "USB plug B has already been activated!"
    elif puzzle_piece_b_collect == True:
        $ piece_puzzle_b = True
        $ puzzle_piece_b_collect = False
        $ renpy.notify("USB Drive B has been removed from your inventory!")
        play sound "audio/sfx/correct beep.ogg"
        "I insert USB Drive B into it's respective place and a loud beep confirms I solve it!"
    else:
        play sound "audio/sfx/wrong beep.ogg"
        "A USB plug on this device is marked \"B\" and needs it to be activated"

    jump pnc_loop

#everything else


label locked_master_door:
    if butt_puzzle_complete == True:
        menu:
            "The way is open now! Should I go through or keep exploring?"
            
            "Let's keep looking around":
                jump pnc_loop

            "Enter through":
                jump boss_battle
    else:
        "This way is blocked off with a laser gate, it won't open unless I override it with some type of device around here..."
    jump pnc_loop

label butt_puzzle_intro:
    
    if butt_puzzle_complete == True:

        "This is complete"
        jump pnc_loop

    elif piece_puzzle_a == False or piece_puzzle_b == False and butt_puzzle_complete == False:

        "This interface looks connected to the laser gate, hmm it's not working... I need to trigger something around here to turn this on"
        jump pnc_loop 

    elif piece_puzzle_a == True and piece_puzzle_b == True and butt_puzzle_complete == False:
        if examined_interface == False:
            $ examined_interface = True
            "The interface works now that I activated the machines!"
        window hide diss
        $ quick_menu = True
        hide screen character_stats with Dissolve(0.1)
        hide screen ammo_stats with Dissolve(0.1)
        show black with Dissolve(.1):
            alpha.6
        call screen lab_minigame

label butt_puzzle_done:
    hide screen lab_minigame with Dissolve(0.2)
    hide black with Dissolve(0.2)
    show screen character_stats with Dissolve(0.2)
    show screen ammo_stats with Dissolve(0.2)    
    "Yes! That finally gives control over the laser gate to the right! It's permeable now!"
    jump pnc_loop


label radio:
    
    p 1"The telecommunications in this room seem to be malfunctioning,{w=.3} don't think I'll be able to contact anyone within here. {w=.3}I have to find someplace else"
    "Huh? There's some text on the screen that says \"BIOREACTOR KEYCARD ENTRY HALL SIDE ROOM = SALVATION\""
    "What does this mean?"
    jump pnc_loop

label bullets:
    $ lab_ammo_2_collected = True
    "Looks like two bullets are on the floor..."
    if norman_has_gun:
        $ ammo += 2
        play sound "audio/sfx/use.ogg"
        "Norman stuffs them into his pockets"
    else:
        $ ammo += 2
        play sound "audio/sfx/use.ogg"
        "I stuff them into my hoodie"
    
    jump pnc_loop    


label bioreactor:
    p 4"These tanks house some type of organism, {w=.3}hope they don't get out"
    if tara == True:
        show w 2 at right2 with Dissolve(0.2)
        w "These are bioreactors, {w=.3}they most likely contain the patients kidnapped from local medical facilities implanted with the virus"
    if norman_dead == False:
        show n 8 with Dissolve(0.2)
        n "The patients...{w=.3} we found them..."
    if rocky_dead == False:
        show r 2 at left with Dissolve(0.2)
        r "I- {w=.3}I don't see my mom in any of these.{w=.3} That means she's ok right? Right?"
        if vinnie_dead == False:
            show v 11 at right with Dissolve(0.2)
            v "Yeah me neither;{w=.3} Your mom is fine, {w=.3}she's safe I promise!"
    if vinnie_dead == False:
        show v 11 at right with Dissolve(0.2)
        v "This is sick...{w=.3} how could they do this?"
    scene lab tanks
    jump pnc_loop


label keycard_slider:
    if keycard == False:
        "It needs some type of identification key to get through..."
        
    elif keycard == True:
        $ keycard_accepted = True
        play sound "audio/sfx/correct beep.ogg"
        "I slide the keycard through the device and loud beep confirms it!"
    jump pnc_loop   

label hakim_lab_go_away:
    $ current_room = "hakim_lab_go_away"
    $ examined_hakim = True
    $ renpy.notify("Old Paper was added to your inventory!")
    "A dead scientist with the nametag \"Hakim Lee\"... What's this paper in his hands?"
    window hide diss
    show paper at center with moveinbottom
    show screen exit_button
    jump pnc_loop

label paper_go_away:
    hide screen exit_button with Dissolve(0.2)
    show paper at offscreen_bottom with move
    hide paper
    "How ominous... these shapes must be important for something around here..."
    jump lab_hakim_room

label pills:

        "There's some pills here on the table"
        play sound "audio/sfx/use.ogg"
        if vinnie_dead == False:
            show v 2 3 with Dissolve(0.2)
            with vpunch
            v "DON'T TOUCH THAT!"
            show v 4
            extend "These pills are too nondescript for me to properly analyze! I really wouldn't trust it..."
            v 8"My best guess is that it's some type of opioid, since we don't know the name, administering an inaccurate dosage could be fatal"
            #v "DON'T TOUCH THAT! Those look like Fentanyl Buccal Tablets!{w=.3} You can tell from the coloring and shape!" #it'd be funny it it was Sildenafil or something {w=.3}HA!"
            if norman_dead == False:
                show n 1 at left with Dissolve(0.2)
                n "Woah close one... {w=.3}good thing we have you Vinnie!"
            if rocky_dead == False:
                show r 1 at right with Dissolve(0.2)
                r "Yikes,{w=.3} imagine if we took that?{w=.3} Don't want that to happen to your body..."
            p 15"Ah,{w=.3} I see.{w=.3} Thank you.{w=.3} If you weren't here I would've downed the whole thing..."
            v 9"Hehe, no problemo~!"
            v 2 4"It'd be funny if it was Sildenafil or something {w=.3}HA!"
            $ pills = True

        else:
            menu pill_risk:
                "Should I risk using them? {w=.3}It seems dangerous... "
            
                "Use on me":
                    $ pills = True
                    "I stay in place for a good while to see if the pills will have any negative effects"
                    "..."
                    "I lean onto the table as my head and stomach start pounding in pain!"
                    p 7"Ohh I don't feel so good... {w=.3}maybe I shouldn't have taken them..."
                    if norman_dead == False:
                        n "[pov!u] [pov!u]! {w=.3}ARE YOU OKAY!?!{w=.3} SPEAK TO ME!{w=.3} TRY TO MAKE YOURSELF THROW UP!"
                    if rocky_dead == False:
                        r "[pov]...{w=.3} Your face... {w=.3}Are you-!"
                    $ sage_health -=2    
                    if sage_health == 0:
                        jump death_screen
                    else:
                        pause 0.5
                        p "Don't worry... {w=.3}I'll get over it...{w=.3} I just need to... {w=.3}walk it off..."
                        if norman_dead == False:
                            n "[pov]!{w=.3} Feel free to lean on me! {w=.3}It's gonna be ok!"
                        if rocky_dead == False:
                            r "Don't try to be a hardass...{w=.3} give a holler if you feel worse...{w=.3} OK?"
                        "I slowly stumble out of the room..."

                "Use on Norman" if norman_dead == False and n_pill_reject == False:
                    if sage_health <= 2 and insanity_level <= 1:
                        $ n_pill_reject = True
                        show n 1 with Dissolve(0.2)
                        n "Awww thank you [pov]!!! But,{w=.3} I think you should take them... {w=.3}you don't look so good..."
                        jump pill_risk                    
                    #if norman_affection >= 3:
                        #$ norman_affection += 1
                        #$ pills = True
                        #show n 2 with Dissolve(0.2)
                        #n "I trust you with my life [pov]!{w=.3} I'm sure it'll be fine!"
                        #$ addNormhealth(-2)
                        #pause 1.0
                        #"..."
                        #"We wait a bit before "
                    else:
                        n "I don't think I deserve such a gift...{w=.3} we're at the final act....{w=.3} I can power through!"
                        jump pill_risk

                "Use on Rocky" if rocky_dead == False:
                    $ pills = True
                    show r 1 with Dissolve(0.2)
                    r "It's worth the risk, I'm a big guy, so if it {i}is{/i} something bad it won't hit too hard... {w=.6}right?"
                    p 4"Let's wait a bit to see if it would do anything..."
                    pause 1.0
                    $ addRockyhealth(-2)
                    r 8"Oughhh... {w=.3}Those pills...{w=.3} not sitting well..."
                    if norman_dead == False:
                        show n 5 at left with Dissolve(0.2)
                        n 5"Rocky! {w=.3}Are you gonna be ok!{w=.3} Here lean on me!{w=.3} Try to make yourself throw up!"
                        r "Unghhhh Norman..."
                        n "Rocky!{w=.3} Rocky! {w=.3}NOOOO!"
                    r "Oh godddd...{w=.3} my stomach..."
                    if insanity_level == 0:
                        p 7"Rocky!{w=.3} Put your fingers down your throat!"
                    "Rocky's irises look smaller and his complexion turns pale... {w=.3}he stumbles back and forth before..."
                    show r 8 at offscreen_bottom with move
                    with vpunch 
                    "..!"
                    "Rocky collapses to the floor"
                    if norman_dead == False:
                        n "AH!{w=.3} NO!{w=.3} NO!"
                        "Norman wraps his arms around Rocky"
                    p 7"Rocky! {w=.3}Wake up! {w=.3}Don't do this!"
                    if insanity_level == 0:
                        "Why did I have to give him all those pills!{w=.3} Dammit!{w=.3} I'm a dumbass!"
                    "..."
                    if rocky_health == 0:
                        $ rocky_dead = True
                        if norman_dead == False:
                            n "He- {w=.3}He-.... {w=.3}he's not breathing!"
                            if insanity_level == 0:
                                p "Let's do CPR!"
                            "Norman panics for a moment before performing CPR"
                            n "Wake up!{w=.3} WAKE UP ROCKY!"
                            n "I can't lose you AND Vinnie in just one day!"
                            "Norman starts doing mouth-to-mouth, he starts sobbing the longer he does it..."
                            "..."
                            pause 1.0
                            "I lost track of how long we've been here but it feels like hours... {w=.3}I gently put my hand on Norman's back"
                            p 2"...Norman... {w=.3}I don't think he's...{w=.3} gonna..."
                            "He rises from sobbing on Rocky's chest"
                            n 8"..."
                            n 6"I know...{w=.3} let's keep... {w=.3}going..."
                            "..."
                            if insanity_level == 0:
                                p 2"I'm so sorry...{w=.3} it's my fault..."
                                n 8"...{w=.3}No I'm just as guilty... {w=.3}I never stopped it..."
                                "..."
                        else:
                            "I rush over to Rocky and start doing chest compressions!"
                            "..."
                            "Time passes it feels like it's been hours..."
                            "Rocky...."
                            "Is..."
                            "..."
                            if insanity == 0:
                                "I- {w=.5}I killed him..."
                                "He died because of me.{w=.3} I gave him the pills. {w=.3}I basically murdered him with my own hands"
                                "The first person I killed was my own friend.{w=.3} He liked sacrificing his own well being to protect his friends and this is how I repay it?"
                                "...{w=.3}I'm a monster..."
                                "What's the point of me being..." # here
                                "..."
                                pause 1.0
                                "No... {w=.3}don't give up...{w=.3} I've almost reached the end..."
                                "Just...{w=.3} keep going..."

                    else: 
                        r 6"Nfff... {w=.3}stop... {w=.3}I'm good...{w=.3} just felt a lil' {w=.3}dizzy... is all"
                        if norman_dead == False:
                            n "Oh my god!{w=.3} I-{w=.5} I thought you were a goner for a moment there!"
                        r 10"It'll take more than some pills to make {i}me{/i}"
                        p 13"Jesus man!{w=.3} Don't scare me like that!"
                        if insanity_level == 0:
                            "... Thank goodness he's ok... {w=.3}If I were to kill my own friend... {w=.3}I-"
                            "..."
                            "I don't know the person I would become..."

                "Leave pills alone":
                    pass

        scene lab radio with Dissolve(0.2)
        jump pnc_loop    


label bullet:
    $ lab_ammo_1_collected = True
    "Looks like a single bullet...."
    if norman_has_gun:
        play sound "audio/sfx/use.ogg"
        $ ammo += 1
        "Norman stuffs it into his pockets"
    else:
        play sound "audio/sfx/use.ogg"
        $ ammo += 1
        "I stuff it into my hoodie"

    jump pnc_loop


label keycard:
    play sound "audio/sfx/use.ogg"
    "A locked small drawer..."
    if keycard == True:
        "The drawer is empty..."
    elif drawer_key_collected == True:
        $ keycard = True
        $ renpy.notify("Employee Keycard was added to your inventory!")
        "I use the key I found to unlock it! {w=.3}I look around the drawer and find an employee keycard!"
    else:
        "It needs a key to open"

    jump pnc_loop


label lab_note_2:
    window hide diss
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Frank Daniels- Junior Researcher- I was 11 when I promised my father I would find a cure for him. He died 2 months later. He would be so proud to see his boy working to prevent the same tragedy for others.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I know what we're doing may seem to wrong to others but two wrongs CAN make a right as along as you have a system of checks and balances.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I'm going to make sure losing your loved ones from illness is a thing of the past.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}For you dad.{/font}"
    hide black with Dissolve(0.2)
    play sound "audio/sfx/page turn.ogg"
    if examined_lab_note_2 == True:
        scene lab closet with Dissolve(0.2)
        jump pnc_loop
    else:
        $ examined_lab_note_2 = True
        if norman_dead == False:
            show n 8 with Dissolve(0.2)
            n "Guess the researchers aren't as one note as we thought... {w=.3}their goal was to help, at least some were..."

        p 4"The road to hell is paved with good intentions..." 

        if rocky_dead == False:
            show r 2 at left with Dissolve(0.2)
            r "Oh please you're giving them too credit! If they were so innocent how did they let this happen?{w=.3} Liars,{w=.3} the lot of them"

        if vinnie_dead == False:
            show v 11 at right with Dissolve(0.2)
            v "A system of checks and balances only works if the system is ALSO being checked and balanced..."

        if tara == True:
            show w 15 at right2 with Dissolve(0.2)
            w "...Father...{w=.3} couldn't you see how much this meant to people...{w=.3} how...{w=.3} why... "
        if norman_dead == False:
            n 8"These people... {w=.3}they're so...{w=.3} confusing... {w=.3}if you wanted to help people... {w=.3}then why cause all these monstrosities?"
            n "It's like...{w=.3} my parents...{w=.3} they say they love me but then act the opposite..."
            n 3a"I don't know how to feel about them.{w=.3} They're big donors and associates to a lot of corporations, including Samsara.{w=.3} They...{w=.3} helped... {w=.3}fuel this..."
            n "They're two-faced, {w=.3}they act so sweet and innocent and pose me with them to create a happy family image for the public"
            n 8"Behind closed doors they've had all these high expectations for me to take over their work and locked me out of their wealth because I have to \"earn\" it..."
            n "They're never there for me when I need it, always busy somewhere else.{w=.3} Every time I need their help they tell me to quit bothering them..."
            n 6"My whole life has been me acting alone, until I met all of you...{w=.3} my first friends..."
            menu:
                "Find a new family!" if insanity_level == 0 or norman_affection >= 3:
                    $ expose_samsara_together_3 = True
                    $ norman_affection += 1
                    p 3"Norman you'll always have a home within my heart..."
                    if rocky_dead == True:
                        p 3"Rocky loved you..."
                    else:
                        p 3"Rocky loves you..."

                    if vinnie_dead == True:
                        p 3"Vinnie loved you..."
                    else:
                        p 3"Vinnie loves you..."

                    if tara == True:
                        p 3"Tara is so grateful for us saving her"
                    if norman_affection >= 3:
                        p 4"And I-"
                    p 4"..."
                    show n 9 with Dissolve(0.2)
                    n "..."
                    n 6"...Thank you [pov], {w=.3}you've told me what I needed to hear..."
                    n 1"From now on, I'm done with my family's nonsense"
                    n "Remember what you said?"
                    p 1"Never forgot."
                    if norman_affection >= 2:
                        if rocky_dead == True and vinnie_dead == True and tara == False:
                            n 1"You're...{w=.3} all that matters to me now..."
                        else:
                            n 9"You matter... {w=.3}so much to me..."
                        "Norman stares deep into my eyes before getting nervous and looking away..."
                        if insanity_level == 0:
                            "So cute..."
                    "I read a poem during class presentation about how your real family is the one who truly cares about you, {w=.3}not who's tied through blood"
                    "Guess it really stuck to him, {w=.5}and me..."

                "Sounds rough":
                    n 8"...Yeah it is..."
            if rocky_dead == False:
                r 11"Norman,{w=.3} you're like the most mature one out of all of us, {w=.3}even though me and Vin are older than you... {w=.3}Always had our backs and set our sights straight..."
                r "What kind of friend would I be if I weren't there for you? {w=.3}I'll always have your back too little buddy...{w=.3} no matter what..."
            if vinnie_dead == False:
                v 12"You really did save me and rocky, {w=.3}we were just sort of aimlessly drifting in life, until we met you. {w=.3}You made us realize that we had passions"
                v "My medical degree to save lives... {w=.3}Rocky's architect degree to build housing for low income families...{w=.3} we would never have put it into action..."
            if tara == True:
                w 4"I haven't been with you for too long but I can tell you've had quite the affect on people's lives..."
                w "When you have someone you can trust... {w=.3}don't let them go...{w=.3} because you never know if it'll be the last time you'll be with them..."
            if norman_dead == False:
                n "..."    
    scene lab closet with Dissolve(0.2)
    jump pnc_loop

label lab_note_1:
    play sound "audio/sfx/digi beep.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Jen Zhara- Lab Technician- The patients from the hospital seem nervous. We told them it will be ok, it's all for the good of society, their efforts won't go to waste.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}That seemed to have pacified them for now. We target people that would have died anyway, so what's the the point if they die during our experiments?{/font}"
    centered "{font=Dudu_Calligraphy.ttf}Better to go being useful than wasting away in a bed somewhere. Our virus experimentation seems to be going places.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}We're putting strand #33 in the Samsara coffee now; we'll be judging the effects on the local population by seeing the hospital intake. We initially were against it but the CEO made a passionate argument for it.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}If what we're doing has such a minimal impact when compared to the common cold. Then where's the harm in being one step closer to curing the curse of mortality?{/font}"
    hide black with Dissolve(0.2)
    play sound "audio/sfx/digi beep.ogg"

    p 4"Thats what they were doing to the patients...{w=.3} what exactly does the coffee do?"
    if rocky_dead == False and rocky_tantrum == False:
        $ rocky_tantrum = True
        $ renpy.music.set_pause(True, channel="music")
        show r 3a with moveinleft
        play sound "audio/voices/rocky roar.ogg"
        queue sound "audio/sfx/window smash.ogg"
        queue sound "audio/sfx/punch.ogg"
        queue sound "audio/sfx/zap.ogg"
        queue sound "audio/sfx/window smash.ogg"
        queue sound "audio/sfx/punch.ogg"
        queue sound "audio/sfx/zap.ogg"
        show r at hop_loop
        "Rocky charges forwards and repeatedly punches the screen with his fists" with hpunch
        if vinnie_dead == False:
            show v 2 1 at right 
            v "Rocky! No! Stop!"

        if norman_dead == False:
            show n 5 at left with Dissolve(0.2)
            n "*gasp* {w=.3}Calm down please!{w=.3} Your fist is bleeding!"
            hide n with Dissolve(0.2)
        hide v with Dissolve(0.2)
        r "BASTARDS!!!!!!!!"
        if tara == True:
            show w 2 at right with Dissolve(0.2)
            w "Yeah go ahead! Smash the thing that hundreds gave their lives for! {w=.3}I'm sure the data on there want important or anything!"
            show r 3a at hop
            r "GAVE?!?!? More like stolen! {w=.3}Listen here! PEOPLE were INFECTED by this.{w=.3} Oh sorry! I guess daddy's little girl never had to worry about being hurt like the rest of us!!! Must be nice being born into the 1 percent!"
            w "Relax,{w=.3} it said here \"strand 33 having similar effects to the common cold\",{w=.3} they were most likely testing how their manufactured virus would survive amongst healthy hosts they didn't have access to"
            w "If it was anything bigger the apocalypse would have happened much sooner"
            r "I made my friends and family victims to their experiments with the damn coffee! {w=.3}If they wanted to experiment they should have done it on themselves!" 
            w "Real smart, how could sick people work in the first plac-"
            hide r with Dissolve(0.2)
            hide w with Dissolve(0.2)
            if expose_samsara_together == True:
                "I touch Tara's shoulder and whisper about Rocky's mother, {w=.3}she's stunned in place for a moment before closing her eyes and starts solemnly nodding her head and recomposing herself"
            else:
                "I touch Tara's shoulder and whisper about Rocky's home life,{w=.3} she's stunned in place for a moment before closing her eyes and starts solemnly nodding her head and recomposing herself"
            show w 14 at right with Dissolve(0.2)
            show r 3a with Dissolve(0.2)
            w "..."
            w 3"...{w=.3}You're right...{w=.3} I'm downplaying it aren't I...{w=.3} and by extension...{w=.3} downplaying your suffering... {w=.3}It was heinous for them to have the populace unknowingly ingest the coffee"
            w "I just didn't want those horrors to go to waste... {w=.3}It could be possible for people to return here and backwards engineer a cure of some sort?" 
            w 8"We come from two different worlds... one good one bad, {w=.3} I- {w=.3}just didn't want the place where I came from...{w=.3} to be pure bad.{w=.3} Because,{w=.3} then what would that make me?"
            w 14"...{w=.3}and I'm still making it about me...{w=.3} when you're the one suffering...{w=.3} I'm sorry..."
            r 4a"..."
            r 3"...{w=.3}Its fine,{w=.3} I may have overreacted.{w=.3} As long as you keep in mind that the things happening here are unjustifiable... {w=.3}we'll be good"
            r 1"..."
            r 3"I shouldn't have destroyed all this stuff too...{w=.3} people probably {w=.2}COULD{w=.2} use this for the better;{w=.3}  my anger got the best of me..."
            r 7"..."
            r "Sorry... {w=.3}if I scared you..."
            w 5"...{w=.3}It's fine... {w=.3}I overreacted too..."
            "..."
            hide r with Dissolve(0.2)
            hide w with Dissolve(0.2)
            if vinnie_dead == False:
                show v 1 with Dissolve(0.2)
                v "Rocky...{w=.3} you've changed..."
            $ renpy.music.set_pause(False, channel="music")
        elif tara == False:

            "Rocky continues punching the screen until it blacks out and his fist is a mess"
            if norman_dead == False:
                n "..."

            if insanity_level == 0:
                p 14"Stop it! {w=.3}I'm mad too but this isn't helping anyone!"
            if vinnie_dead == False:
                v "Rocky please stop you're scaring me..."
            hide r with Dissolve(0.2)
            "He stops when he hears those words and wordlessly turns around"
            r "..."
            r "...{w=.3}sorry,{w=.3} let's just go..."
            "..."
            $ renpy.music.set_pause(False, channel="music") 
    else:
        pass
    scene lab desk with Dissolve(0.2)
    jump pnc_loop

# tara tank
label lab_note_3:
    stop music fadeout 1.0
    play music "audio/music/successful failure.ogg"
    play sound "audio/sfx/digi beep.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Hakim Lee- Head Senior Researcher- Artificial Womb Experiment- Take #6- SUCCESS{/font}"
    centered "{font=Dudu_Calligraphy.ttf}First lab grown subject successfully developed from a solo male. The subject exhibits zero abnormalities and appears to be fully conscious. Subject is female and was created using the CEO's DNA. {/font}"
    centered "{font=Dudu_Calligraphy.ttf}He seems oddly intrigued by her. In all my years of working with him, I've never seen him so interested in another life that wasn't his...{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I wonder if he even recognizes her as her own unique life form, or as an extension of him? Taran what happened to you... you are not the man who recruited me all those years ago{/font}"
    hide black with Dissolve(0.2)
    if keycard == True:
        "This is who the keycard belongs to... {w=.3}seems like a real important guy... {w=.3}How much did he know was happening here? And could {w=.3}{i}he{/i}{w=.3} even stop it if he wanted to?"
    if tara == True and tara_seen_tank == False:
        $ tara_seen_tank = True
        show w 2 with Dissolve(0.2)
        "Tara steps closer next to me to read the text as well"
        if rocky_dead == False or norman_dead == False or vinnie_dead == False:
            "We're the only ones in this part of the room"
        w "This is where I was created...{w=.3} I never had a mother only a father and Samsara to look after me... {w=.3}I wonder if I {i}am{/i} a carbon copy of father and turn out to repeat his mistakes..."

        menu:

            "The fact that you're questioning it means you're not" if insanity_level == 0:
                $ tara_against_dad = True
                p 2"We are not our parents... {w=.3}the destiny you forge for yourself is your choice to make only, {w=.3}not anybody else's"
                w 14"..."
                w 11"Why,{w=.3} yes I suppose you are right... {w=.3}Why not stop focusing on his life and start focusing on mine"
                w 2"My entire life has been composed of discovering his true nature and fixing his mistakes to protect us..."
                w 5"From now on,{w=.3} I'll be doing it to save the world, {w=.3}and this is his last mistake..."
                p 13"That's the spirit!"
                w 1"Father, {w=.3}I don't want to hurt you or anyone else... {w=.3}but if the time comes...{w=.3} I'm ready..."

            "...":
                w 14"..."
                pass
    hide w with Dissolve(0.2)
    stop music fadeout 1.0
    play music "audio/music/FLOOR_3.mp3" fadein 1.0
    jump pnc_loop


label lab_note_4:
    window hide diss
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Daniel McGee- Research Assistant- Finally! AFTER YEARS FINALLY!!! We have successfully created a virus that doesn't kill the host AND overrides other diseases the former may have!{/font}"
    centered "{font=Dudu_Calligraphy.ttf}This isn't what we were achieving in our search for immortality but it's the closest we're gonna get! The entire lab has been celebrating for the past couple days!{/font}"
    centered "{font=Dudu_Calligraphy.ttf}Our families will be cured! Disease is a thing of the past! We don't care if we don't have permission from the CEO anymore! We're dispatching it in the chem trails ASAP! I'm saving you Grandma! Only downside is that it makes subjects near brain dead...{/font}"
    centered "{font=Dudu_Calligraphy.ttf}The CEO has been even more quiet and solitary than usual, is he not happy with what we've achieved? He said he wanted to make one final adjustment to the virus before we dispatch it... guess that's reasonable.. {/font}"
    centered "{font=Dudu_Calligraphy.ttf}We're already releasing it without his permission so might as well let the head researcher and founder work his magic? Perhaps he saw a flaw we didn't...{/font}"
    hide black with Dissolve(0.2)
    play sound "audio/sfx/page turn.ogg"
    if vinnie_dead == False:
        show v 25 at right with Dissolve(0.2)
        v "Welp, {w=.3}this is how it started out...{w=.3} guess I better apologize to Rocky for saying his conspiracies were stupid..."

    if rocky_dead == True and vinnie_dead == False:
        show v 2 2 at right with Dissolve(0.2)
        v "Rocky if you're out there...{w=.3} I'm sorry"
        hide v with Dissolve(0.2)

    if rocky_dead == False and vinnie_dead == False:
        v 2 4"NOT!!! I will never apologize even {i}IF{/i} the frogs turn gay!!!"
        show r 3 with Dissolve(0.2)
        show v 2 at right
        r "Even in my moment of glory you still find a way to be petty,{w=.3} I'm not letting you get in the way of my validation!!"
        hide r with Dissolve(0.2)
        hide v with Dissolve(0.2)
        "Rocky strikes a stupid pose and does a victory dance while pointing at a sulking Vinnie"
        show v 4 at right with Dissolve(0.2)
        show r 10 with Dissolve(0.2)
        r "OH YEAH, SUCK IT VINNIE"
        show v 4 at offscreen_left with move
        v "WHATEVER DUDE! Let's get out of here..."
        show r 10 at offscreen_right with move
        hide v
        pause 0.3
        hide r 
    if vinnie_dead == True and rocky_dead == False:
        show r 6 with Dissolve(0.2)
        r "Guess the chem trail conspiracy was true... {w=.3}Vinnie...{w=.3} you would be so pissed if you were still here...{w=.3} I can even hear you doing your pouty voice whenever something goes wrong heh"
        hide r with Dissolve(0.2)
    if norman_dead == False:
        show n 6 with Dissolve(0.2)
        n "The flaw the CEO incorporated... {w=.3}that has to be it... {w=.3}the zombie virus..."
        hide n with Dissolve(0.2)

    p 2"This was no accident, {w=.3}the CEO planned this all out. {w=.3}He wanted to watch the world burn"
    
    if tara == True:
        show w 14 with Dissolve(0.2)
        w "...{w=.3}you told me since I was a little girl this was supposed to help people,{w=.3} you lied to me! YOU LIED TO ME!!"
        w "...{w=.3}you really are no different from your monsters,{w=.3} this isn't forgivable, we're gonna make you pay for all the lives you took..."
        "Tara says in clenched teeth"
        hide w with Dissolve(0.2)
    jump pnc_loop



##LAB BOSS BATTLE ENDING
label boss_battle:
    scene black with dissolve
    hide screen character_stats with dissolve
    hide screen ammo_stats with dissolve
    play music "audio/music/stranger no more.ogg" fadein 1.0
    $ renpy.notify("All unnecessary items have been discarded from your inventory. This is the end.")
    $ examined_hakim = False
    $ keycard = False
    $ drawer_key_collected = False
    "Here we are... {w=.3}it's taken so long but we're finally here..."
    scene boss battle with fade
    show snow1
    show snow2 with dissolve
    "..."
    show c 15 with dissolve
    s "..."
    show c 14 with dissolve
    s "...Ah,{w=.3} you're here.{w=.3} I have to say I'm impressed with how far you've progressed.{w=.3} I figured the juggernaut would dispose of you"
    s 1"I've been watching you, you know. {w=.3}There are cameras all over this building. {w=.3}I've been with you ever since you stepped foot into this building..."
    "The CEO is on an elevated platform with a control panel"
    if norman_dead == False:
        show n 5 at left with Dissolve(0.2)
        n "Sir!{w=.3} You need to stop what you're doing at once!{w=.3} Let us out of here!"
        s 7"The exit is right where you came from;{w=.3} never mind the inevitable horde bound to eat you from the inside out though..."

        if rocky_dead or vinnie_dead == True:
            s 2"Your deceased friends seem to have gotten a head start on you! {w=.3}Why don't you take a page from their book and step outside?"     
        hide n 5 with Dissolve(0.2)
    if vinnie_dead == False:
        show v 2 at right with Dissolve(0.2)
        v "Everything you've done is revolting! {w=.3}How could life have no meaning to you?"
        s 6"What's revolting is how every entity in the world, {w=.3}doesn't see the glory being made here..."

        if rocky_dead == True:
            s 2"Your Maned Wolf friend would have loved the changes I would of made. {w=.3}The little people are always at the forefront of my mind.{w=.3} They are so {i}desperate{/i} which makes them easy for manipulation"
            if rocky_cafe_death == True:
                s 2"He died so quickly!{w=.3} I never saw him on camera! {w=.3}He must have died when this all started outside"
        if norman_dead == True:
            s 1"That Golden Retriever came from a higher echelon then the rest of you,{w=.3} I have personally met his family in a business dealing with me. {w=.3}He would have agreed with me"   
        hide v 2 with Dissolve(0.2)

    if rocky_dead == False:
        show r 4a at left with Dissolve(0.2)
        r "Listen here old timer, {w=.3}if you don't point us to the exit I'll knock you on your ass and kick your teeth in!"
        s 7"Oh my how unrestrained, {w=.3}would you still behave this way if you were alone?"

        if vinnie_dead == True:
            s 3"Are you making up for your lack of ferocity with saving the Opossum?{w=.3} They died because of you.{w=.3} But I'm sure {i}you{/i} know that already..."
        if norman_dead == True:
            s 12"The Golden Retriever would'nt be a fan of your lack of compassion,{w=.3} good thing they're not here {w=.5}right?"   
        hide r 4a with Dissolve(0.2)

    if tara == True:
        show w 6 at right with Dissolve(0.2)
        w "Father!{w=.3} How could you! {w=.3}You betrayed me and the people that trusted you with your actions! {w=.3}I- {w=.3}I don't know you anymore, {w=.3}you've broken my heart!"
        s 9"My daughter, step away from them.{w=.3} It's a family business no?"
        w 8"I will not!{w=.3} Get away from me!"
        hide w 6 with Dissolve(0.2)
    p 4"Just radio in a helicopter and make a cure or something! It's not too late to stop this!"
    if closet_broken == True and tara == False:
        s 6"{cps=*2.0}{b}{size=*1.3}YOU PRETEND TO BE BETTER THAN ME BUT YOU LEFT THAT GIRL BEHIND KNOWING FULL WELL YOU COULD HAVE FUCKING SAVED HER YOU PIECE OF SHIT!{/size}{/b}{/cps}"
        s "DON'T EVEN TRY TO PRETEND YOU DID ALL YOU COULD. {w=.3}I SEE EVERYTHING.{w=.3} I KNOW EVERYTHING. {w=.3}IF I WANTED TO I COULD BLOW YOU ALL UP!"
        s "YOU LEFT HER THERE,{w=.3} JUST LEFT HER TO HER OWN FATE WHILE YOU RAN AWAY! GOOD THING{w=.4} I-{w=.3} SHE-"
        s 5"She..."
        s 8"..."
        "He was enraged but stopped himself before surely jumping at me"
        s 9"{cps=*0.9}Ah,{w=.2} excuse me...{w=.3} where were we? {w=.5}Oh that's right I remember...{/cps} Ahem!"
    if insanity_level >= 2 or vinnie_dead == True or norman_dead == True or rocky_dead == True:
        s 6"Priceless coming from you of all people, {w=.3}I've seen how you really act... {w=.3}You don't like your friends as much as pretend to huh?"
        s 12"Were you trying to get them all killed? {w=.3}Or do you just not care either way?"
    else:
        s 3"Oh it's you the leader I presume? You've done {i}so{/i} well guiding everyone... {w=.3}Props to you I suppose..."
        if norman_affection >= 5:
            s 1"You even made yourself a little boyfriend in all this,{w=.3} I wonder if you took advantage of the situation for this very purpose"
            if norman_dead == True:
                s 2"Too bad you couldn't protect them!{w=.3} I'm sure their last thoughts were of pretending they were in your arm's instead of the monsters"
    if norman_dead == True:
        s 3 "Bye bye Golden Retriever! I'm afraid your little crush didn't reciprocate your feelings...{w=.3} Yes, I DO know of them...{w=.3} their parents have been quite useful to me!"
        s 7 "It's funny how hundreds of thousands of dollars makes people think you're in debt to them. {w=.3}HA!{w=.3} Did they think of me as a family friend or something?{w=.3} IDIOTS!!!"
    if rocky_dead == True:
        s 9"Poor Maned Wolf..." 
        show c 12
        extend "I'm afraid your mother will die as sad, lonely, and pathetic just like you!{w=.3}  Eh,{w=.3} that's probably what he really wanted deep down...{w=.3} Why keep that financial drain you call a parent alive anyways?"
        s 10"Oh my apologies that was rude of me..."
        show c 12
        extend "is his genus more related to a fox? If only I cared enough to find out..."
    if vinnie_dead == True:
        s 9"And erm..{w=.3} apologies... {w=.3}I can't seem to remember your Opossum friend too well..."
        show c 3
        extend " Looks like all their neediness and attention seeking failed in the end!{w=.3} They can decompose and become as vulgar as they acted!"
        s 7"It would'nt leave any impression on me whatsoever! As in life,{w=.3} as in death...{w=.3} Heh,{w=.3} humorous..."
    if vinnie_dead == True and rocky_dead == True:
        s 5"Oh no both the poor clueless lovers are dead..."
        show c 6
        extend "they're fucking each other whilst burning in hell...{w=.3} does that make you feel better?"
    if vinnie_dead == True and rocky_dead == True and norman_dead == True:
        s 3"Wow nice job leading the team champ! {w=.3}Be honest,{w=.3} it was satisfying to watch them die{w=.3} no?"
        s 2"You're really some type of sick freak...{w=.3} I would be blushing if I weren't so hellbent on killing you..."
    if ammo >=3:
        s "Were you saving all those bullets for something important? {w=.3}Jeez, we got a bit of a hoarder here..."
        if vinnie_dead == True or rocky_dead == True or norman_dead == True:
            s "Good thing you used them wisely to save that one friend of yours!{w=.5} {i}Oh wait...{/i}" 
    s 7"Eons worths of research was conducted here,{w=.3} the little lambs baptized in rotten flesh and putrid blood were guided into the mouth of god"
    s 2"In other words,{w=.9} me"
    s 3"I tied the noose around all my researchers necks and let them go! {w=.3}Their sacrifices were not in vain look where they got me!"
    s 4"They wanted to use MY research for themselves and their families! {w=.3}Idiots! {w=.3}It was for MY immortality!{w=.3} My ascent to godhood!"
    s 10"My IQ is unmatched, I was put into this world to guide it, {w=.3}All I needed was the time which the project was meant to achieve"
    s 6"When they wanted to use it for something else...{w=.3} I corrupted it into this zombie virus.{w=.3} I realized the world only cares about each other"
    s "So I need to remake it to care about ME and only ME as the one who guides them out of armageddon!"
    s 3"I needed to tie up a few loose ends here,{w=.3} so I got this here private military force of mine to shoot up any survivors and blow up the building so none can tell what really happened here!"
    show c 3 at hop
    play sound "audio/sfx/hit13.ogg"
    "The CEO kicks one of the many armored men's corpses in the head"
    s 2"Of course,{w=.3} {i}they{/i} had to be dispatched too,{w=.3} so I ordered them all to kill one another!{w=.3} The were infected by a special form of the virus a long time ago and are completely bound to my will"
    s 6"Hmm if you're not up for jumping into this here pit of hydrofluoric acid, {w=.3}then there is an alternative..."
    if norman_secret_death == True and ammo >= 1:
        play sound "audio/sfx/shoot.ogg"
        show c 9 at shiver
        with vpunch
        "He reaches to press a button but I draw the gun and shoot him in the chest"
        show c 9 at shiver
        s "Ough!"
        p 16"Whoops"
        jump shut_the_fuck_up
    hide c 7 with Dissolve(0.2)
    play music "audio/music/live or die intro.ogg"
    queue music "audio/music/live or die.ogg"
    show screen character_stats with Dissolve(0.2)
    show screen ammo_stats with Dissolve(0.2)
    "The CEO presses a button on the control panel near him and activates two large metal doors on our left and right which reveals..."
    play sound "audio/sfx/zombie (2).ogg"
    queue sound "audio/sfx/Zombie_04.ogg"

    show bluzom at left with moveinleft
    show bluzom at shiver_loop_left

    show orangzom at right with moveinright
    show orangzom at shiver_loop_right

    show breadly at left with moveinleft
    show breadly at shiver_loop_left

    show dunce at right with moveinright
    show dunce at shiver_loop_right

    queue sound "audio/sfx/Zombie URGH.ogg"

    show naut with Dissolve(0.2)
    show naut at hop_loop
    "10 zombies and 1 one juggernaut zombie!"
    "This is serious,{w=.3}if I make one mistake it would mean instantaneous death..."
    if tara == True:
        show w 6 with Dissolve(0.2)
        w "Father no!"
        hide w 6 with Dissolve(0.2)
    if vinnie_dead == True and rocky_dead == True and norman_dead == True:
        jump the_juggernaut

label save_norman_finale:
    if norman_dead == False:
        if norman_affection >= 5:
            show n 5 with Dissolve(0.2)
            n "[pov]!{w=.3} Behind you! {w=.3}I won't let them hurt you!"
            show n at hop
            "Norman runs up behind me and delivers a jump kick to the zombie behind me!"
            hide n with Dissolve(0.2)
            jump save_vinnie_finale
        else:
            show n 5 with Dissolve(0.2)
            n "Ah!{w=.3} I need help!"
            if norman_has_gun == True and ammo >= 1:
                $ renpy.notify("Gun has been removed from your inventory!")
                "Norman's gun was wrestled out of his hand by one of the zombies"
            show n 5 at hop_loop
            jump boss_zombies_v_norman
    else:
        jump save_vinnie_finale

        menu boss_zombies_v_norman:

            "Shoot at the CEO" if sage_has_gun == True and ammo >= 1:
                if persistent.petty_sage == False:
                    $ renpy.notify("Achievement Unlocked: Nice Try")
                    $ persistent.petty_sage = True
                    play audio "audio/sfx/achievement.ogg"
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                "I tried shooting at the CEO but he ducked behind his control panel, he's too high up to get an accurate shot or attack..."
                s "Hahahaha!!!{w=.3} Stop it! {w=.3}You're too funny! It's unsightly!!{w=.3} Hahahaha!!!!"
                "I wasted a bullet for nothing!"
                $ addNormhealth(-1)
                play sound "audio/sfx/hit.ogg"
                with hpunch
                "Norman was hurt during our exchange..."
                if norman_health == 0:
                    $ norman_lab_death = True
                    jump save_vinnie_finale
                else:
                    jump boss_zombies_v_norman

            "Use Tara against the CEO" if tara == True and ceo_caught_bluff == False:
                if rocky_dead == True and norman_dead == True and vinnie_dead == True:
                    $ tara_hostage = True
                    jump boss_aftermath
                else:
                    $ ceo_caught_bluff = True
                    p 14 "Look at your daughter!{w=.3} How could you put her through this!"
                    s "Hmm? My daughter is perfectly safe!{w=.3} Haven't you noticed she isn't being targeted?"
                    s "If you're referring to her disapproval...{w=.3} then shut it! {w=.3}It's typical child rebelliousness!{w=.3} She'll grow used to the role I have in mine for her!"
                    w "I will never!{w=.3} Stop right now! {w=.3}Leave them alone!"
                    s "Tsk{w=.3}, being a parent is so difficult sometimes..."
                    p 14"I-{w=.3} I'll kill her i-{w=.3}if you don't stop this!"
                    s "HAHAHAHAHA NICE TRY I KNOW YOU'RE BLUFFING! YOU'RE TOO SOFT TO HURT HER!!!"
                    "Dammit he caught my ruse..."
                    $ addNormhealth(-1)
                    play sound "audio/sfx/hit.ogg"
                    with hpunch
                    "Norman was hurt during our exchange..."
                    if norman_health == 0:
                        $ norman_lab_death = True
                        jump save_vinnie_finale
                    else:
                        jump boss_zombies_v_norman

            #"Take off the helmet of the juggernaut zombie" if boss_juggernaut_zombie == True:
                #jump the_juggernaut

            "I save myself and do nothing!":
                $ addInsanity_level(1)
                show static_anim with Dissolve(0.2)
                play audio "audio/sfx/static.ogg"
                camera:
                    perspective True
                    easein_bounce 0.54 zpos -20
                pause 0.3 
                $ addNormhealth(-4)
                hide static_anim with Dissolve(0.2)
                camera:
                    reset
                if norman_health == 0:
                    $ norman_lab_death = True
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/Zombie URGH.ogg"
                n "Yeowch!" with hpunch
                "Norman is hurt..."

            #"Push Norman into danger" if insanity_level >= 1 and norman_affection <= 1 and tara == False and rocky_dead and vinnie_dead == True:
            #    $ addNormhealth(-5)
            #    $ insanity_level == 90
            #    $ norman_dead = True
            #    n "HELP ME!! HELP ME!!"
            #    $ norman_lab_push_death == True
            #    "Were Norman's last words before being lost to the horde..."
            #    jump boss_aftermath

            "I tell Vinnie to use their knife" if vinnies_knife == True and vinnie_dead == False:
                $ vinnies_knife = False
                $ renpy.notify("Vinnie's Knife has been removed from your inventory!")
                show v 2 at right with moveinright
                play sound "audio/sfx/stab.ogg"
                queue sound "audio/sfx/Zombie Struggling.ogg"
                v "I'll protect you Normie!" with hpunch
                n "Thank you Vinnie!"
                "Vinnie stabs one of the zombies attacking Norman but loses the knife in the process"
           
            "I tell Vinnie to save Norman!" if vinnies_knife == False and vinnie_dead == False:
                if expose_samsara_together_2 == True:
                    show v 2 at right with moveinright
                    play sound "audio/sfx/hit.ogg"
                    queue sound "audio/sfx/Zombie Struggling.ogg"
                    v "I got you Norman!" with hpunch
                    "Vinnie helps Norman with no issue"
                else:
                    $ addVinhealth(-1)
                    show v 2 at right with moveinright
                    play sound "audio/sfx/hit.ogg"
                    queue sound "audio/sfx/Zombie URGH.ogg"
                    v "Got it! {w=.3}I'll save you Norm! OW!" with hpunch
                    "Vinnie punches the man but gets punched back HARD in the face"
                    show v 2 1 at offscreen_bottom with move
                    if vinnie_health == 0:
                        $ vinnie_lab_death = True

            "I skewer the zombies with my horns!":
                if norman_affection >= 5:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/Zombie Growling.ogg"
                    "I'm not letting HIM die!" with hpunch
                    n 2"Woah, That was awesome [pov]!"
                else:
                    $ sage_health -= 1
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/Zombie Growling.ogg"
                    "I take some damage in return..." with hpunch
                    if sage_health == 0:
                        jump death_screen
                    n 2"Thanks!"
            
            "I shoot the zombies!" if sage_has_gun == True and ammo >= 1:
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                queue sound "audio/sfx/Zombie URGH.ogg"
                "I shoot the zombie attacking Norman!"

            "I pick up the gun and shoot the zombies!" if norman_has_gun == True and ammo >= 1:
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                queue sound "audio/sfx/Zombie URGH.ogg"
                $ renpy.notify("Gun has been added to your inventory!")
                "I pick up the gun he dropped and shoot the zombie attacking Norman! I'm in control of the gun from now on"

            "I crowbar the zombies!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/hit.ogg"
                queue sound "audio/sfx/Zombie URGH.ogg"
                $ crowbar_collected = False
                $ renpy.notify("Crowbar has been removed from your inventory!")
                "I use the crowbar against the zombies! But the horde yanks it out of my hands and it gets lost in the stampede" with hpunch

            "I tell Rocky to save Norman!" if rocky_dead == False:
                if expose_samsara_together == True:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/Zombie Growling.ogg"
                    show r 1a at left with moveinleft
                    r "GET BEHIND ME!" with hpunch
                    n "GOT IT!"
                    hide r 1a with Dissolve(0.2)
                elif crowbar_collected == True and expose_samsara_together == False:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/Zombie URGH.ogg"
                    $ crowbar_collected = False
                    $ renpy.notify("Crowbar has been removed from your inventory!")
                    show r 1a at left with moveinleft
                    r "HUT!" with hpunch
                    "Rocky uses the crowbar against the zombies but the horde yanks it out of his hand and it gets lost in the stampede"
                    hide r 1a with Dissolve(0.2)
                else:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/Monster_00.ogg"
                    $ addRockyhealth(-1)
                    show r 1a at left with moveinleft
                    r "URGH!" with hpunch
                    "Rocky uses his body to shell Norman from danger but gets hurt in retaliation"
                    if rocky_health == 0:
                        $ rocky_lab_death = True
                    hide r 1a with Dissolve(0.2)
                hide n with Dissolve(0.2)
                hide r with Dissolve(0.2)
                hide v with Dissolve(0.2)

label save_vinnie_finale:
    if vinnie_dead == False:
        hide n with Dissolve(0.2)
        show v 2 at center with Dissolve(0.2)
        v "Get lost!"
        show v 2 at hop_loop
        if expose_samsara_together_2 == True:
            show v 2 at hop
            v "NO! {w=.3}I'M NOT LETTING ANY OF YOU HURT ME OR MY FRIENDS ANYMORE!!! I'M TIRED OF BEING AFRAID!"
            "Vinnie uses their claws to gouge the throat of one of the zombies!"
            jump save_rocky_finale
        else:
            jump boss_zombies_v_vinnie
    else:
        jump save_rocky_finale

        menu boss_zombies_v_vinnie:

            "Shoot at the CEO" if sage_has_gun == True and ammo >= 1:
                if persistent.petty_sage == False:
                    $ renpy.notify("Achievement Unlocked: Nice Try")
                    $ persistent.petty_sage = True
                    play audio "audio/sfx/achievement.ogg"
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                "I tried shooting at the CEO but he ducked behind his control panel,{w=.3} he's too high up to get an accurate shot or attack..."
                s "Hahahaha!!! Stop it! You're too funny! It's unsightly!! Hahahaha!!!!"
                "I wasted a bullet for nothing!"

                $ addVinhealth(-1)
                play sound "audio/sfx/hit12.ogg"
                with hpunch
                "Vinnie was hurt during our exchange..."
                if vinnie_health == 0:
                    hide v with Dissolve(0.2)
                    $ vinnie_lab_death = True
                    jump save_rocky_finale
                else:
                    jump boss_zombies_v_vinnie

            "Use Tara against the CEO" if tara == True and ceo_caught_bluff == False:
                if rocky_dead == True and norman_dead == True and vinnie_dead == True:
                    $ tara_hostage = True
                    jump boss_aftermath
                else:
                    $ ceo_caught_bluff = True
                    p 14 "Look at your daughter!{w=.3} How could you put her through this!"
                    s "Hmm? My daughter is perfectly safe!{w=.3} Haven't you noticed she isn't being targeted?"
                    s "If you're referring to her dissaproval...{w=.3} then shut it! {w=.3}It's typical child rebelliousness!{w=.3} She'll grow used to the role I have in mine for her!"
                    w "I will never!{w=.3} Stop right now! {w=.3}Leave them alone!"
                    s "Tsk{w=.3}, being a parent is so difficult sometimes..."
                    p 14"I-{w=.3} I'll kill her i-{w=.3}if you don't stop this!"
                    s "HAHAHAHAHA NICE TRY I KNOW YOU'RE BLUFFING! YOU'RE TOO SOFT TO HURT HER!!!"
                    "Dammit he caught my ruse..."
                    $ addVinhealth(-1)
                    play sound "audio/sfx/hit.ogg"
                    with hpunch
                    "Vinnie was hurt during our exchange..."
                    if vinnie_health == 0:
                        $ vinnie_lab_death = True
                        jump save_rocky_finale
                    else:
                        jump boss_zombies_v_vinnie

            #"Take off the helmet of the juggernaut zombie" if boss_juggernaut_zombie == True:
                #jump the_juggernaut

            "I save myself and do nothing!":
                show static_anim with Dissolve(0.2)
                play audio "audio/sfx/static.ogg"
                camera:
                    perspective True
                    easein_bounce 0.54 zpos -20
                pause 0.3 
                hide static_anim with Dissolve(0.2)
                camera:
                    reset
                $ addInsanity_level(1)
                $ addVinhealth(-3)
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/zombie-19.ogg"
                v "AGH!" with hpunch
                "Vinnie is hurt..."
                if vinnie_health == 0:
                    $ vinnie_lab_death = True

            #"Push Vinnie into danger" if insanity_level >= 1 and tara == False and rocky_dead and norman_dead == True:
            #    $ addVinhealth(-5)
            #    $ insanity_level == 90
            #    $ vinnie_dead = True
            #    show v 2 at offscreen with move
            #    v "ROCKY!!" with hpunch
            #    "Were Vinnie's last words before being lost to the horde..."
            #    $ vinnie_lab_push_death == True

            "I tell Vinnie use their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                $ renpy.notify("Vinnie's Knife has been removed from your inventory!")
                play sound "audio/sfx/stab.ogg"
                queue sound "audio/sfx/zombie-19.ogg"
                v "EAT IT YOU LIMP DICK SON OF A BITCH!!!" with hpunch
                "The knife was lost in the process..."
           
            "I tell Norman to save Vinnie!" if norman_dead == False:
                if expose_samsara_together_3 == True:
                    show n 5 at left with moveinleft
                    play sound "audio/sfx/hit12.ogg"
                    queue sound "audio/sfx/zombie-19.ogg"
                    n "YOU'RE NOT DYING ON MY WATCH!" with hpunch
                    "Norman does a high kick so hard it knocks a zombie's head off! Norman helps Vinnie with no issue"
                else:
                    show n 5 at left with moveinleft
                    $ addNormhealth(-1)
                    if norman_health == 0:
                        $ norman_lab_death = True
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/zombie-19.ogg"
                    n "YOU'RE NOT DYING ON MY WATCH!" with hpunch
                    "Norman gets hurt in retaliation"

            "I attack the zombies!":
                $ sage_health -= 1
                if sage_health == 0:
                    jump death_screen
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/zombie-19.ogg"
                v "THANK YOU GOAT PERSON!" with hpunch
                "I get hurt in return..."
            
            "I shoot the zombies!" if sage_has_gun == True and ammo >= 1:
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                queue sound "audio/sfx/zombie-19.ogg"
                "I shoot the zombie!"

            "I crowbar the zombies!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/hit13.ogg"
                queue sound "audio/sfx/zombie-19.ogg"
                $ crowbar_collected == False
                $ renpy.notify("Crowbar has been removed from your inventory!")
                "I use the crowbar against the zombies! But the horde yanks it out of my hands and it gets lost in the stampede" with hpunch

            "I tell Rocky to save Vinnie!" if rocky_dead == False:
                show r 1a at right with moveinright
                if expose_samsara_together == True:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/zombie-19.ogg"
                    "Rocky sprints at full force while punching any zombie thats get in his way to the ground, he then pummels the zombie attacking Vinnie to ground" with hpunch
                elif crowbar_collected == True and expose_samsara_together == False:
                    play sound "audio/sfx/hit13.ogg"
                    queue sound "audio/sfx/zombie-19.ogg"
                    $ crowbar_collected = False
                    $ renpy.notify("Crowbar has been removed from your inventory!")
                    r "HUT!"
                    "Rocky uses the crowbar against the zombies but the horde yanks it out of his hand and it gets lost in the stampede" with hpunch
                else:
                    play sound "audio/sfx/hit12.ogg"
                    $ addRockyhealth(-1)
                    if rocky_health == 0:
                        $ rocky_lab_death = True
                    r "URGH!"
                    "Rocky uses his body to shell Vinnie from danger but gets hurt in retaliation" with hpunch
        hide r with Dissolve(0.2)
        hide n with Dissolve(0.2)
        hide v with Dissolve(0.2)

label save_rocky_finale:
    if rocky_dead == False:
        show r 3a at shiver_loop_center with Dissolve(0.2)
        r "AAGH!"
        if expose_samsara_together == True:
            play sound "audio/voices/rocky roar.ogg"
            r "AAAAAAAAAAAAAAGHHHHHHHHH!!!"
            play sound "audio/sfx/zombie-22.ogg"
            "Rocky lifts a zombie over his head and throws it into the horde at full force!"
            jump the_juggernaut
        else:
            jump boss_zombies_v_rocky
    else:
        jump the_juggernaut

        menu boss_zombies_v_rocky:

            "Shoot at the CEO" if sage_has_gun == True and ammo >= 1:
                if persistent.petty_sage == False:
                    $ renpy.notify("Achievement Unlocked: Nice Try")
                    $ persistent.petty_sage = True
                    play audio "audio/sfx/achievement.ogg"
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                "I tried shooting at the CEO but he ducked behind his control panel, he's too high up to get an accurate shot or attack..."
                s "Hahahaha!!! Stop it! You're too funny! It's unsightly!! Hahahaha!!!!"
                "I wasted a bullet for nothing!"
                $ addRockyhealth(-1)
                play sound "audio/sfx/hit.ogg"
                with hpunch
                "Rocky was hurt during our exchange..."
                if rocky_health == 0:
                    $ rocky_lab_death = True
                    jump the_juggernaut
                else:
                    jump boss_zombies_v_rocky

            "Use Tara against the CEO" if tara == True and ceo_caught_bluff == False:
                if rocky_dead == True and norman_dead == True and vinnie_dead == True:
                    $ tara_hostage = True
                    jump boss_aftermath
                else:
                    $ ceo_caught_bluff = True
                    p 14 "Look at your daughter!{w=.3} How could you put her through this!"
                    s "Hmm? My daughter is perfectly safe!{w=.3} Haven't you noticed she isn't being targeted?"
                    s "If you're referring to her dissaproval...{w=.3} then shut it! {w=.3}It's typical child rebelliousness!{w=.3} She'll grow used to the role I have in mine for her!"
                    w "I will never!{w=.3} Stop right now! {w=.3}Leave them alone!"
                    s "Tsk{w=.3}, being a parent is so difficult sometimes..."
                    p 14"I-{w=.3} I'll kill her i-{w=.3}if you don't stop this!"
                    s "HAHAHAHAHA NICE TRY I KNOW YOU'RE BLUFFING! YOU'RE TOO SOFT TO HURT HER!!!"
                    "Dammit he caught my ruse..."
                    $ addRockyhealth(-1)
                    play sound "audio/sfx/hit.ogg"
                    with hpunch
                    "Rocky was hurt during our exchange..."
                    if rocky_health == 0:
                        $ rocky_lab_death = True
                        jump the_juggernaut
                    else:
                        jump boss_zombies_v_rocky


            #"Take off the helmet of the juggernaut zombie" if boss_juggernaut_zombie == True:
                #jump the_juggernaut

            "I save myself and do nothing!":
                show static_anim with Dissolve(0.2)
                play audio "audio/sfx/static.ogg"
                camera:
                    perspective True
                    easein_bounce 0.54 zpos -20
                pause 0.3 
                hide static_anim with Dissolve(0.2)
                camera:
                    reset
                $ addInsanity_level(1)
                $ addRockyhealth(-6)
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/Zombie_03.ogg"
                r "Oof!"
                if rocky_health == 0:
                    $ rocky_lab_death = True

            #"Push Rocky into danger" if insanity_level >= 1 and norman_affection <= 1 and tara == False and norman_dead and vinnie_dead == True:
            #    $ addRockyhealth(-10)
            #    $ insanity_level == 90
            #    $ rocky_dead = True
            #    $ rocky_lab_push_death = True
            #    show r 3a at offscreen_bottom with move
            #    r "VINNIE! I'LL SEE YOU SOON!" with hpunch
            #    "Were Rocky's last words before being lost to the horde..."

            "I tell Vinnie to use their knife!" if vinnies_knife == True and vinnie_dead == False:
                show v 2 3 at right with moveinright
                play sound "audio/sfx/stab.ogg"
                queue sound "audio/sfx/Zombie_03.ogg"
                v "I'll protect you Rocko!" with hpunch
                r 10"Thankya!"
                $ renpy.notify("Vinnie's Knife has been removed from your inventory!")
                $ vinnies_knife = False
                "Vinnie stabs one of the zombies attacking Rocky but loses the knife in the process"
           
            "I tell Vinnie to save Rocky!" if vinnies_knife == False and vinnie_dead == False:
                show v 2 3 at right with moveinright
                if expose_samsara_together_2 == True:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/Zombie_03.ogg"
                    v "I got you Rocky!"
                    "They pierce their claws through a zombies eyes! Vinnie saves Rocky with no issue!" with hpunch
                else:
                    $ addVinhealth(-1)
                    play sound "audio/sfx/stab.ogg"
                    queue sound "audio/sfx/Zombie_03.ogg"
                    v "Got it! I'll save you Rocko! OW!" with hpunch
                    "Vinnie kicks the zombies but gets hurt"
                    if vinnie_health == 0:
                        $ vinnie_lab_death = True

            "I skewer the zombies with my horns!":
                $ sage_health -= 1
                play sound "audio/sfx/hit13.ogg"
                queue sound "audio/sfx/Zombie_03.ogg"
                "I take some damage in return..." with hpunch
                if sage_health == 0:
                    jump death_screen
                r 10"Thankya [pov]!"
            
            "I shoot the zombies!" if sage_has_gun == True and ammo >= 1:
                $ addAmmo_level(-1)
                play sound "audio/sfx/shoot.ogg"
                with vpunch
                queue sound "audio/sfx/Zombie_03.ogg"
                "I shoot the zombie attacking Rocky!"
            
            "I Tell Rocky to use the crowbar!" if crowbar_collected == True:
                play sound "audio/sfx/hit13.ogg"
                queue sound "audio/sfx/Zombie_03.ogg"
                $ crowbar_collected = False
                $ renpy.notify("Crowbar has been removed from your inventory!")
                "Rocky use the crowbar against the zombies! But the horde yanks it out of his hands and it gets lost in the stampede" with hpunch

            "I tell Norman to save Rocky!" if norman_dead == False:
                if expose_samsara_together_3 == True:
                    show n 5 at left with moveinleft
                    play sound "audio/sfx/hit12.ogg"
                    queue sound "audio/sfx/Zombie_03.ogg"
                    n "NO MORE DEATHS ON MY WATCH!"
                    r "WOW THAT WAS AMAZING!!!"
                else:
                    show n 5 at left with moveinleft
                    $ addNormhealth(-1)
                    play sound "audio/sfx/hit.ogg"
                    queue sound "audio/sfx/Zombie_03.ogg"
                    if norman_health == 0:
                        $ norman_lab_death = True
                    n "Here I go! URGRGH!!"with hpunch
                    "Norman gets damaged in turn..."

label the_juggernaut:
        $ boss_juggernaut_zombie = False
        play sound "audio/sfx/hit12.ogg"
        show naut 2
        "I jump on top of the juggernaut zombie like before, as I'm riding its shoulders I rip off his helmet and throw it into the acid pit below!"
        queue sound "audio/sfx/Monster_00.ogg"
        queue sound "audio/sfx/monster-1.ogg"
        queue sound "audio/sfx/hit13.ogg"
        queue sound "audio/sfx/monster-3.ogg"
        queue sound "audio/sfx/monster-10.ogg"
        if norman_lab_death == True:
            $ norman_dead = True

        if rocky_lab_death == True:
            $ rocky_dead = True

        if vinnie_lab_death == True:
            $ vinnie_dead = True

        if norman_dead == False:
            show n 5 at left with moveinright
            "Norman takes his chance to tear off some more of the juggernaut's armor!"
            show n 5 at offscreen_right with move
        if vinnie_dead == False:
            show v 3 at right with moveinleft
            "Vinnie uses their claws rip out it's eyes!"
            show v 3 at offscreen_left with move
        if rocky_dead == False:
            show r 3a at right2 with moveinright
            "Rocky uses his jaws to inflict large gashes upon it's neck!"
            show r 3a at offscreen_left with move
        if tara == True:
            show w 4 at left with moveinright
            "Tara picked up some debris and is chucking at it's face, knocking it off balance!"
            show w 4 at offscreen_right with move
        "The juggernaut moans in distress before jumping into the vat of acid to chase after his helmet, it takes the majority of the zombies along with it"
        pause 1.0
label boss_aftermath:
    scene boss battle with Dissolve(0.2)
    hide screen character_stats with Dissolve(0.2)
    hide screen ammo_stats with Dissolve(0.2)
    show snow1
    show snow2
    if tara_hostage == True:
        show w 6 with Dissolve(0.2)
        "Strangely it seems the zombies are ignoring Tara"
        play sound "audio/sfx/cock.ogg"
        if sage_has_gun == True:
            "I grab her and point a gun towards her head"
        else:
            "I grab her and threaten to throw her into the pit of acid"
        if insanity_level <= 2:
            p "Play along ok?"
            show w 3
            "I whisper in Tara's ear as she nods in understanding"
        p 14"I'll kill her if you don't stop!"
        show w 3 at right with move
        show c 6 with Dissolve(0.2)
        s 1"Halt!"
    show powder
    "The CEO raises his fist and slams it down onto his control panel which dispenses some type of powder from above"
    "It rains onto the zombie horde below them and they drop to ground while flailing wildly,{w=.3} until eventually,{w=.3} they stop moving entirely..."
    hide powder with Dissolve(0.2)
    if tara_hostage == True:
        s 10"Return her to me..."
        show w 2
        "I let Tara go as she stares daggers into her father's eyes"
    stop music fadeout 1.0    
    play music "audio/music/Night_Joe.mp3"

    if norman_lab_death == True:
        $ norman_dead = True
        "Norman was lost, {w=.3}I presume he was eaten whole as I don't see his corpse anywhere"

        if norman_affection >= 4:
            "Norman,{w=.3} my Norman... {w=.3}no...{w=.3} I will avenge you..."
            "...{w=.3}I loved you..."
                
        elif insanity_level >= 2:
            "Oh well, no skin off my nose"

        if norman_has_gun:
            "I quickly snatch the gun he had while on my way"

    if rocky_lab_death == True:
        $ rocky_dead = True
        "Rocky couldn't make the onslaught, he was eaten alive"

    if vinnie_lab_death == True:
        $ vinnie_dead = True
        "Vinnie didn't survive,{w=.3} the horde lifted them and threw them over the ledge"
        
    show c 6 with Dissolve(0.2)
    show c 6 at hop_loop
    s "That's enough of this!{w=.3} I'm giving you one last chance to give up!{w=.3} You're destroying ALL my research! {w=.3}You're setting society back by generations!"
    show c 6 at hop
    s "Are you too dense to understand this?!?! {w=.3}I'll even offer an alternative to where I wipe all you're memories of what happened here and call for an escort out of this city"
   
    if norman_dead == True:
        pass
    else:
        show n 8 at left1 with Dissolve(0.2)
        n "Does he really have the ability to wipe minds or is he bluffing?"
        hide n with Dissolve(0.2)
    if vinnie_dead == True:
        pass
    else:
        show v 2 at right with Dissolve(0.2)
        v "He's gotta be bluffing!{w=.3} He's just saying that because we caught his ass!"
        hide v with Dissolve(0.2)
    if rocky_dead == True:
        pass
    else:
        show r 3a at left with Dissolve(0.2)
        r "You're shitting me if you think we're letting you get away scot-free!"
        hide r with Dissolve(0.2)
    p 1"So there is a way out of here..."
    if insanity_level <= 1:
        p 4"You know it's not too late,{w=.3} you can come with and answer for your crimes peacefully..."
    s 8"..."
    pause 1.0
    s 9"I-{w=.3} It's too late for me anyways... {w=.3}I... {w=.9}was bit..."
    "He rolls up his sleeve and shirt to reveal two bite marks"
    p 2"I see..{w=.3} that makes an escape for you unnecessary right?"
    s 5"Indeed,{w=.3} there is no cure... I... {w=.3}I... {w=.3} tried and failed...{w=.3} for the first time in my life.... {w=.3} I can't s-succeed..."
    if tara == True:
        hide n with Dissolve(0.2)
        hide r with Dissolve(0.2)
        hide v with Dissolve(0.2)
        show w 9 at right with moveinright
        w 9"No! No! NO!! {w=.3}Father you can't die! You can't!"
        s 9"I am sorry my daughter...{w=.3} It's over for me..."
        w 7"You did such terrible things. Such disgusting things!{w=.3} Why!{w=.3} Why are you still trying to hurt me! Even now!"
        s 10"...{w=.3}Tara... {w=.3}I've never called you by your name to your face...{w=.9} Tara... {w=.5}your father can't provide the life you need..."
        s "I see it now, before when you were created. I deluded myself into thinking you were nothing but a clone of me.{w=.3} You aren't though... {w=.3}I see it now,{w=.3} especially with the attempts you've made against me"
        show c 6 at shiver
        "He shoots me a dirty look before looking back at Tara"
        s 5"You tried so hard to protect everyone here and expose me as the monster I am... {w=.3}Tara... {w=.3}There's something wrong with my brain... {w=.3}I can't think like you do..."
        s "I want to become god of this universe and guide the world into a new era of progression.{w=.3} I am aware that it's not something a typical person would think {w=.9}but I do..."
        s "Even now, {w=.3}after all this death and destruction I am going to continue my ways. {w=.3}It hasn't changed me one bit, {w=.3}which made me realize how this affects you"
        pause 1.0
        s "..."
        s 9"You are going to die if you keep following me Tara. {w=.3}The new world will have me as it's sole ruler, {w=.3}no one can be equal to my power."
        w 15"But you're changing right now don't you see!?!{w=.3} Snap out of it! Come back to me!{w=.3} Quit your experiments and business and we can go back home and start from scratch!"
        w 9"PLEASE! {w=.3}I'M BEGGING FOR YOU TO COME BACK!"
        w "All you need to do is stop this and turn yourself into the police,{w=.3} don't shut me out!"
        show c 4 at shiver_loop
        s "I'm not changing... {w=.3}if I was given the opportunity I would kill all of you if it guaranteed me my rightful place of godhood!"
        w 9"Do it! Do it now then! {w=.3}If that's true why haven't you killed me yet!"
        show c 5 at hop
        s "I-"
        show w 15 at hop
        w "Look me in the eyes when you say it! {w=.3}I don't believe your words for a second!{w=.3} I know your head isn't right!{w=.3} But it's right enough to acknowledge your daughter for crying out loud!"
        show c 4 at shiver_loop
        s "I- {w=.3}I- {w=.8}AAAAAAAAAAAAAAAAAAAAAAAAAAAGHHHHHHH!!!!!!!"
        play sound "audio/sfx/short run.ogg"
        show c 4 at offscreen_bottom with move
        show w 9 at center with move
        "The CEO clutches his head before running away and jumping into the pit below"
        show w 9 at hop
        w "NOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!"
        show w 9 at hop
        w "WHY{w=.3}! WHY!{w=.3} FATHER!"
        show w 9 at sink
        "Tara breaks down crying while on her knees"
        show w 9 at shiver
        w "No!{w=.3} No!{w=.3} NOOO!!!"
        if norman_dead == False:
            show n 8 at left with moveinleft
            n "Oh Tara I'm so sorry..."
            pause 1.0
            show w 14 at sink_rise
            w "no...{w=.3}I should be the one sorry...{w=.3} for what he's done to all you..."
            "Norman pats her back as he gazes upon the abyss"
        else:
            show w 14 at sink_rise
        if vinnie_dead == False:
            show v 2 at right with moveinright
            v "Guess there was something deep in him that knew"
            w "...He wanted to protect me... {w=.3}even the insane man who killed thousands is still a father in the end..."
            w "Still...{w=.3} it wasn't right for him to..."  
        if rocky_dead == False:
            show r 1 at left with moveinleft
            show w 14 at right2 with move
            show n 8 at left1 with move
            r "..."
            r 2"This doesn't fix what he's done.{w=.3} But at least one part of his mind knew it wasn't right"
        w 7"I know...{w=.3} he was a monster but...{w=.3} I really thought I could bring him back..."
        p 4"One half dominant, {w=.3}making him the monster that we knew. {w=.3}The other half deep inside,{w=.3} only coming out when he saw the first and only person he cared about..."    
        scene black with Dissolve(0.2)
        "Tara slowly stands up before walking over to the control panel"
        if norman_dead == False:
            "Norman helps guide her and is gently comforting her along the way"
            n "It's gonna be ok... {w=.3}you're with us now...{w=.3} he would want you to escape..."
            w "...{w=.3}I'll be ok...{w=.3} don't worry... {w=.3}I just need time...{w=.3}. thank you..."
        if vinnie_dead == False:
            v "Ah! {w=.3}Over here!"
        if rocky_dead == False:
            r "Are we really about to get out of here?"        
        "We find the elevator out of here and call for a chopper using his control panel"
    else:
        label shut_the_fuck_up:
            if norman_secret_death == True and ammo >= 1:
                s "Agh... {w=.3}so that's how far you've fallen... {w=.3}How much further will you go I wonder?"
        if norman_dead and rocky_dead and vinnie_dead and tara == False:
            p 17"Let me go then.{w=.5}{b} Now.{/b}"
            if norman_secret_death == True and ammo >= 1:
                s 8"..."
                "He slowly rises and clutches his wounded chest.{w=.3} He nearly falls over"
                "He's lucky I didn't shoot him in the head, {w=.3}oh, {w=.3}I guess rather {i}unlucky{/i} because I'm not giving him a quick fate..."
        else:
            p 4"Just let us go then,{w=.3} your empire is finished. {w=.3}There's nothing for you here anymore"
        pause 0.5
        s 5"..."
        show c 5 at left1 with move
        pause 0.3
        show c 5 at center with move
        show c 5 at right2 with move
        pause 0.3
        show c 5 at center with move
        "The CEO looks back and fourth before sighing and pressing a button on the control panel that reveals an elevator door"
        play sound "audio/sfx/elevatording.ogg"
        play audio "audio/sfx/vent.ogg"
        pause 0.5
        s "Leads straight to the rooftop..."
        if norman_dead == False:
            show n 6 at left1 with moveinleft
            n "Thank you for coming to reason..."
        if vinnie_dead == False:
            show v 2 at right with moveinright
            v "Finally a way out!"  
        if rocky_dead == False:
            show r 1 at left with moveinright
            r "...? {w=.3}I don't know if I can trust this..."
        s 1"Just one last thing... "

        if norman_dead and rocky_dead and vinnie_dead and tara == False:
            "He's standing near the ledge"
        else:
            "We all turn around and didn't even notice he was standing near the ledge"

        hide v with Dissolve(0.2)
        hide w with Dissolve(0.2)
        hide r with Dissolve(0.2)
        hide n with Dissolve(0.2)
        $ renpy.music.set_pause(True, channel="music")

        show black with Dissolve(0.2):
            alpha 0.8     
        show c 2 at center:
            ease 0.5 zoom 0.9
        s 2"{w=.3}{cps=*0.5} Prepare for the second coming.{/cps}"
        if insanity_level >=1 and vinnie_dead == True and rocky_dead == True and norman_dead == True and tara == False:
            s 5"{cps=*0.5}I see it right now in this very room. {w=.5}How... {w=.9}haunting...{/cps}"
        
        show c 2 at offscreen_bottom with move
        $ renpy.music.set_pause(False, channel="music") 
        "He throws himself into to the pit below"
        hide c 2
        "..."
        hide black with Dissolve(0.2)
        if norman_secret_death == True:
            "Good riddance"
        if vinnie_dead == False:
            show v 12 at right with Dissolve(0.2)
            v 12"Geez..."
            if rocky_dead == True:
                v 2"Fucker deserved worse for what happened to Rocky..."
            if norman_dead == True:
                v 2"That rotten bastard killed Norman..."                
        if rocky_dead == False:
            show r 2 at left with Dissolve(0.2)
            r 2"Guess that's that taken care of..."
            if vinnie_dead == True:
                r 2a"I wish I had the chance to rip his fucking throat out for what he caused happen to Vinnie..."
            if norman_dead == True:
                r 2a"No sympathies whatsoever, HE KILLED NORMAN!"
        if norman_dead == False:
            show n 8 at left1 with Dissolve(0.2) 
            n 8"Oh..."
        pause 0.5
        "I stand in shock before heading for the elevator,{w=.3} I decide to take a look at the control panel to check if he called for a chopper"
        if norman_dead == False and tara == False:
            "...!"
            n 5"Hey!{w=.3} He set the neurotoxin gas defenses level to ON for the elevator systems here!"    
            n "Better switch that off!{w=.3} I'm sure the ventilation system will get rid of it in due time!"                    
            if rocky_dead == False and tara == False:
                r 2"...I REALLY wish he was still here so I could kill him..."
            if vinnie_dead == False and tara == False and norman_dead == False:
                v 2"Wow! {w=.3}Even after death he's still just as vindictive!"
        if vinnie_dead == False and tara == False:
            v 2 "Let's just get out of here... the acid fumes burn my eyes..."
        #if norman_dead == False:
            #n "So much death, so much pain. Finally over..."
        

    pause 0.5

    scene elevator with Dissolve(0.2)
    play sound "audio/sfx/elevatording.ogg"
    pause 0.5
    "..."
    "I can't believe after all this time it's over..."
    "The deaths,{w=.3} the zombies, the people out to kill us...{w=.3} it's all over..."
    if norman_dead == True and insanity_level == 0 or rocky_dead == True and insanity_level == 0  or vinnie_dead == True and insanity_level == 0:
        "I just wish everyone I came with made it out too..."
    if norman_dead == False:
        show n 1 with Dissolve(0.2)
        n "Chin up!{w=.3} We've done it [pov]!"

        if norman_affection >=5:
            show n 4 at hop with Dissolve(0.2)
            p 11"Hehe yeah we did"
            "Norman comes up to me while I'm stewing and nuzzles my nose with his"

    if insanity_level >=1 and vinnie_dead == True and rocky_dead == True and norman_dead == True and tara == False:
        scene black with fade
        play music "audio/sfx/Wind.ogg"
        "I did it,{w=.3} I lived. {w=.3}I left the others to their fates so {i}I{/i} could live"
        "...{w=.3}They..."
        "I didn't even know them for that long. Why {i}should{/i} I feel guilty?{w=.3} In this new world it's about survival.{w=.3} It's about {i}me{/i}, {w=.3}everyone else is secondary"
        "Friendship is overrated,{w=.3} it's a trap people put you in to make you feel like you owe them something."
        "I am the one in control of people's fates. {w=.3}If I wanted to I could kill them. I decide who lives and who dies. {w=.3}I am the god of this world"
        "Kneel before me,{w=.3} the second coming won't be as soft as the last..."
        "..."
        "I feel like I'm forgetting something?"
        "..."
        "If I forgot...{w=.3} It must not be important..."
        "..."

    if vinnie_dead == False and rocky_dead == False and norman_dead == False:
        show v 2 4 at right with Dissolve(0.2)
        v "WE FUCKIN DID IT LADIES AND GENTLEMEN! {w=.3}WE CAME STRAIGHT IN THIS PLACE WITH ONE GOAL IN MIND! SURVIVAL! AND PULLED IT OFF!!!!"
        v "WOOOOOHOOOOOOO YEAHHHH!!!! {w=.3}JUMP FOR JOY HOS!!!!"
        if norman_affection >=5:
            v "AND THE BEST PART IS THAT [pov!u] AND NORMAN GET TO GET LAID!!!!!!!!!!!!!!"
            n 16"VINNIE!{w=.3} NO!"
            p 9"Are you for real dude..."
            show r 3 at left with Dissolve(0.2)
            r 3"Eww! You're gonna scare them away from each other!!"
        show r 2 at left with Dissolve(0.2)
        r 2"Vinnie,{w=.3} dude,{w=.3} come on stop with this!"
        "Vinnie is bouncing up and down while shaking Rock with them!!!"
        v "YIPEE KI-YAY MOFOS!!!!!!!!!{w=.3} WE'RE ALL ALIVE HAHAHAHAHAHAHA!!!!!!!!!!!!"
        n 2"We did it!{w=.3} We did it! {w=.3}We get to live! Haha!"
        v 22"KISS ME LIKE YOU MEAN IT ROCKY! PUCKER UP!"
        r 3"Ugh!"
        if tara == True:
            show w 11 at left1 with Dissolve(0.2)
            w 11"We survived indeed! Indubitably! Without a doubt! \"Abso-fruitly\" if you will, {w=.3}considering who I'm traveling with..."
            p 8"Hey is that homophobia I hear?"
            w 4"No!{w=.3} Not at all I support you all very much!"
            v 1"Hmmm my homophobic vision senses it deep within your soul..."
            v 6"RELEASE IT!! MY PATIENT! {w=.3}LET THE HOMOPHOBIA FLOW THROUGH YOU!!! {w=.3}Rocky this isn't a safe place for you anymore, {w=.3}we're the straight club now!"
        r 1a"The hell? I'm the straightest guy here! Just take a look at you!"
        if norman_affection >=5:
            r 3"Also, {w=.3}two of you are literally {i}dating{/i} each other!"
        r 3"What's gayer than that!"
        v 27"Ummm def your search history when I was trying to look something up!!!"
        r 3a"...! {w=.3}Tha- {w=.3}That's- {w=.3}It was just the firefighter recruitment site!"
        v 2 4"ERRRR! {w=.3}WRONG! {w=.3}Why were all of those firefighters exclusively men and half nake-"
        "Rocky bear hugs Vinnie before strangling them in the corner!"
        r "IF THE ZOMBIES DIDN'T KILL YOU I WILL!"
        v 2 3"HELP MEEEEEEE!!!!!!!!"
        show r 3a at offscreen_right with move
        show v 2 3 at offscreen_left with move

        n 2"Hahahaha!!!"
        p 8"You people are insane.{w=.3} I love it."
        if tara == True:
            w 13"Ha! You're all hilarious!{w=.3} I've gotta stick with you!"
        p 15"Ah, {w=.3}sounds like the elevator is coming to a stop"
        p 8"Guys, {w=.3}let's make a promise... {w=.3}let's be together... {w=.5}forever..."
        "Everyone turns towards me and motions for a group hug"
        show v 1 at right with Dissolve(0.2)
        v 1"I love you guys! You're welcome to huck rocks at the city hall with me anytime!"
        show r 10 at left with Dissolve(0.2)
        r 10"I'll carve time out of my schedule to hang out with you all more! {w=.3}Screw the endless hours! I'm sick of it!"
        n 2"I love you all more than my actual family!"
        if tara == True:
            w 4"I'm my own person now thanks to you all!{w=.3} Thank you so much!"
    elif vinnie_dead or rocky_dead or norman_dead == True:
        if vinnie_dead == False and rocky_dead == True:
            show v 2 2 at right with Dissolve(0.2)
            v "I did it Rocky, we did it for you...{w=.3} We lived... {w=.3}Thank you Rocky, {w=.3}you're still motivating me to keep going..."
            if norman_dead == True:
                v "I couldn't protect Norman either...{w=.3} I failed you two... {w=.3}we swore to keep him safe and I fucked up like I always do..."
                v "Why did I live?"

        if rocky_dead == False and vinnie_dead == True:
            show r 7 at left with Dissolve(0.2)
            r "I lived Vinnie but,{w=.3} at what cost? You died and I lived... {w=.3}You'll always be in my heart, {w=.3}you'll still be cheering me on..."
            if norman_dead == True:
                r "Norman died because of me Vinnie,{w=.3} I couldn't protect any of the people I love... {w=.3}I couldn't keep our promise to protect him..."
        if tara == True:
            if vinnie_dead or norman_dead or rocky_dead == True:
                show w 14 at right2 with Dissolve(0.2)
                w "I'm so sorry about what happened to..."
                w "..."
            w "At least we survived...{w=.3} I'm sure they want you to live for them..."
        if insanity_level == 0:
            scene black with fade
            "They're dead and there's nothing I could do about it. I wanted to keep my new friends, my new family,{w=.3} safe but..."
            "I'm so sorry I failed you... {w=.3}now we pay the price for death..."        

        "..."

    pause 1.0
    jump endings
    return


