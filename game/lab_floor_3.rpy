

#variables

default tara_against_dad = False
default tara_hostage = False

default vinnie_lab_death = False
default rocky_lab_death = False
default norman_lab_death = False

default expose_samsara_together_3 = False

#ITEMS

default keycard = False
default pills = False

#PIECE PUZZLE

default puzzle_piece_b_collect = False
default puzzle_piece_a_collect = False

default piece_puzzle_b = False
default piece_puzzle_a = False

#Final boss
default boss_juggernaut_zombie = True
default boss_zombie_horde = True

label lab_floor_3:
    scene black with dissolve
    stop sound
    stop music
    pause 1.0
    scene elevator with dissolve
    "The elevator comes to a slow stop and the doors begin to slide open"
    $ current_room = "lab_start" # this initializes the point'n'click segment to display the correct set of buttons.
    scene lab main room with dissolve
    "Well here we are in the lab let's look for a way out through here"
    if tara == True:
        w "I know he's my father but if you see him, don't hesitate to use force if necessary he's a dangerous man"
        if vinnie_dead == True:
            v "PERMISSION TO WHOOP ASS GRANTED"
        if rocky_dead == True:
            r "I didn't need permission but thanks I guess"
        if norman_dead == True:
            n "We'll use diplomacy to solve our problems!"
        if insanity_level >=0:
            "I'll personally kill him for putting me through this"
        p "Don't worry, we'll be on the lookout for him"
    
    jump pnc_loop



##LAB ROOMS
## YES THERE ARE A LOT ;(

##LAB DOWNSTAIRS HUB
label lab_start:
    scene lab main room with dissolve
    $ current_room = "lab_start" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS CENTER BOTTOM ROOM

label lab_puzzle_b_room:
    scene lab main room with dissolve
    $ current_room = "lab_puzzle_b_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS LEFT ROOMs

label lab_radio:
    scene lab radio with dissolve
    $ current_room = "lab_radio" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS RIGHT ROOMS
label lab_test_room:
    scene lab test with dissolve
    $ current_room = "lab_test_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_downstairs_hall:
    scene lab hall with dissolve
    $ current_room = "lab_downstairs_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_puzzle_piece_a_collect_room:
    scene lab storage with dissolve
    $ current_room = "lab_puzzle_piece_a_collect_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

#UPSTAIRS !!!!!!!

label lab_upstairs:
    scene lab upstairs main room with dissolve
    $ current_room = "lab_upstairs" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#UPSTAIRS LEFT ROOMS !!!!!!!

label lab_upstairs_left_hall:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_left_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label lab_puzzle_a_room:
    scene lab puzzle with dissolve
    $ current_room = "lab_puzzle_a_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_puzzle_piece_b_collect_room:
    scene lab storage with dissolve
    $ current_room = "lab_puzzle_piece_b_collect_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#UPSTAIRS RIGHT ROOMS DONT CONFUSE FOR RIGHT-MOST ROOMS !!!!!!!
##### RIGHT !!!!!!!!!!!!!!!!

label lab_upstairs_right_hall:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_right_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_desk:
    scene lab desk with dissolve
    $ current_room = "lab_desk" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_upstairs_test_room:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_test_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop



#UPSTAIRS RIGHT-MOST ROOMS DONT CONFUSE FOR RIGHT ROOMS !!!!!!!
##### RIGHT-MOST !!!!!!!!!!!!!!!!

label lab_upstairs_rightmost_hall:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_rightmost_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_keycard_room:
    scene lab keycard room with dissolve
    $ current_room = "lab_keycard_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_tanks:
    scene lab tanks with dissolve
    $ current_room = "lab_tanks" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_boss_room:
    scene lab tanks with dissolve
    $ current_room = "lab_tanks" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#LAB POINT AND CLICK LABELS

label radio:
    
    p "The telecommunications in this room seem to be malfunctioning, don't think we'll be able to contact anyone within here. We have to find someplace else"

    jump pnc_loop

label bullets:
    "Looks like two bullets are on the floor..."
    if norman_has_gun:
        $ ammo += 2
        "Norman stuffs them into his pockets"
    else:
        $ ammo += 2
        "I stuff them into my hoodie"
    jump pnc_loop    

label bioreactor:
    p "These tanks house some type of organism, hope they don't get out"
    if tara == True:
        w "These are bioreactors, they most likely contain the patients kidnapped from local medical facilities implanted with the virus"
    if norman_dead == False:
        "The patients... we found them..."
    if rocky_dead == False:
        "I- I don't see my mom in any of these. That means she's ok right? Right?"
        if vinnie_dead == False:
            v "Yeah me neither! You're mom is fine she's safe I promise!"
    if vinnie_dead == False:
        v "This is sick... how could they do this?"

label puzzle_piece_a_collect:
    $ puzzle_piece_a_collect == True
    "I collect puzzle piece A"
    $ renpy.notify("Puzzle Piece A has been added to your inventory!")
    jump pnc_loop

label pills:
    "There's some pill capsules on the floor"
    if vinnie_dead == False:
        v "Those look like painkillers, you can tell from the coloring and shape"
        menu pill_choose:
            "Who should I heal?"

            "Me":
                $ sage_health +=1
                $ pills == True

            "Norman":
                if sage_health <= 4:
                    n "Awww thank you [pov]!!! But, I think you should take them... you don't look so good..."
                else:
                    $ norman_health +=1
                    $ pills == True
                    n "Thanks [pov]! I feel better already!"

            "Vinnie":
                $ vinnie_health +=1
                $ pills == True
                v "Wow, I am just a PERUSER today!!!"

            "Rocky":
                $ pills == True
                $ rocky_health +=1
                r "I've never been more thankful for random floor pills before in my life..."
    
    else:
        menu pill_risk:
            "Should I risk using them? It may be useful..."
            
            "Me":
                $ sage_health +=1
                $ pills == True

            "Norman":
                if norman_affection >= 0:
                    $ norman_health +=1
                    $ pills == True
                    n "I trust you with my life[pov]! I'm sure it'll be fine!"
                    jump pnc_loop    
                else:
                    n "Don't take this the wrong way [pov]... but I don't trust it..."
                    jump pill_risk

            "Vinnie":
                if insanity >= 0:
                    $ vinnie_health +=1
                    $ pills == True
                    v "No"
                    v "I'm not just gonna be eating random shit off the floor, I worked too hard to get back in to that again..."
                    jump pill_risk
                else:
                    v "..."
                    v "Ok, I'll trust you..."
                    jump pnc_loop

            "Rocky":
                $ rocky_health +=1
                $ pills == True

                r "I'm a big guy, so if it {i}is{/i} something bad it won't hit too hard... right?"
            
    jump pnc_loop    

label keycard_slider:
    if keycard == False:
        "This needs some type of identification key to get through..."
    else:
        play sound "audio/sfx/correct beep.ogg"
        "I slide the keycard through and loud beep confirms it!"
    jump pnc_loop   

label lab_note_1:

    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Frank Daniels- Junior Researcher- I was 11 when I promised my father I would find a cure for him. He died 2 months later. He would be so proud to see his boy working to prevent the same tragedy for others.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I know what we're doing may seem to wrong to others but two wrongs CAN make a right as along as you have a system of checks and balances.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I'm going to make sure losing your loved ones from a disease is a thing of the past.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}For you dad.{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"

    if norman_dead == False:
        n "Guess the researchers aren't as one note as we thought... their goal was to help, at least some were..."

    p "The road to hell is paved with good intentions..." 

    if rocky_dead == False:
        r "Oh please you're giving them too credit! If they  were so innocent how did they let this happen? Liars, the lot of them"

    if vinnie_dead == False:
        v "A system of checks and balances only works if the system is ALSO being checked and balanced..."

    if tara == True:
        t "...Father... couldn't you see how much this meant to people... how... why... "
    if norman_dead == False:
        n "These people... they're so... confusing... if you wanted to help people... then why cause all these monstrosities?"
        n "It's like... my parents... they say they love me but then act the opposite..."
        n "I don't know how to feel about them. They're big donors and associates to a lot of corporations, including Samsara. They... helped... fuel this..."
        n "They're two-faced, they act so sweet and innocent and pose me with them to create a happy family image for the public"
        n "Behind closed doors they've had all these high expectations for me to take over their work and locked me out of their wealth because I have to \"earn\" it..."
        n "They're never there for me when I need it, always busy somewhere else. Every time I need their help they tell me to quit bothering them..."
        n "My whole life has been me acting alone, until I met all of you... my first friends..."
        menu:
            "Find a new family!":
                $ expose_samsara_together_3 == True
                $ norman_affection += 1
                p "Norman you'll always have a home within my heart..."
                if rocky_dead == True:
                    p "Rocky loved you..."
                else:
                    p "Rocky loves you..."

                if vinnie_dead == True:
                    p "Vinnie loved you..."
                else:
                    p "Vinnie loves you..."

                if tara == True:
                    p "Tara is so grateful for us saving her"
                p "And I-"
                p "..."
                n "..."
                n "...Thank you [pov], you've told me what I needed to hear..."
                n "From now on, I'm done with my family's nonsense"
                n "Remember what you said?"
                p "Never forgot."
                if rocky_dead and vinnie_dead == True and tara == False:
                    n "You're what matters to me now..."
                else:
                    n "You're all what matters to me now..."
                "Norman stares deep into my eyes before getting nervous and looking away..."
                if insanity_level == 0 and norman_affection >= 2:
                    "So cute..."
                "I read a poem during class presentation about how you're real family is the one who truly cares about you, not who's tied through blood"
                "Guess it really stuck to him, and me..."

            "Sounds rough":
                n "...Yeah it is..."

    jump pnc_loop

label lab_note_2:

    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Jen Zhara- Lab Technician- The patients from the hospital seem nervous. We told them it will be okay, it's all for the good of society, their efforts won't go to waste.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}That seemed to have pacified them for now. We target people that would have died anyway, so what's the the point if they die during our experiments?{/font}"
    centered "{font=Dudu_Calligraphy.ttf}Better to go being useful than wasting away in a bed somewhere. Our virus experimentation seems to be going places.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}We're putting strand #33 in the samsara coffee now; we'll be judging the effects on the local population by seeing the hospital intake. We initially were against it but the CEO made a passionate argument for it.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}If what we're doing has such a minimal impact when compared to the common cold. Then where's the harm in being one step closer to curing the curse of mortality?{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"

    p "Thats what they were doing to the patients... what exactly does the coffee do?"

    if rocky_dead == False:
        "Rocky charges forwards and repeatedly punches the screen with his fists"

        if vinnie_dead == False:
            v "Rocky! No! Stop!"

        if norman_dead == False:
            n "*gasp* Calm down please! Your fist is bleeding! "
    
        if tara == True:
    
            w "Yeah go ahead! Smash the thing that hundreds gave their lives for! I'm sure the data on there want important or anything!"
            r "GAVE?!?!? More like stolen! Listen here! PEOPLE were INFECTED by this. Oh sorry! I guess daddy's little girl never had to worry about being hurt like the rest of us?! Must be nice being born into the 1 percent!"
            w "Relax, it said here \"strand 33\" having similar effects to the common cold, they were most likely testing how their manufactured virus would survive amongst healthy hosts they didn't have access to. If it was anything bigger the apocalypse would have happened much sooner"
            r "I made my friends and family victims to their experiments with the damn coffee! If they wanted to experiment they should have done it on themselves!" 
            w "Real smart, how could sick people work in the first plac-"

            if expose_samsara_together == True:
                "I touch Tara's shoulder and whisper about Rocky's mother, she's stunned in place for a moment before closing her eyes and starts solemnly nodding her head and recomposing herself"
            else:
                "I touch Tara's shoulder and whisper about Rocky's home life, she's stunned in place for a moment before closing her eyes and starts solemnly nodding her head and recomposing herself"
            w "..."
            w "...You're right... I'm downplaying it aren't I... and by extension... downplaying your suffering... It was heinous for them to have the populace unknowingly ingest the coffee"
            w "I just didn't want those horrors to go to waste... It could be possible for people to return here and backwards engineer a cure of some sort?" 
            w "We come from two different worlds... one good one bad,  I- just didn't want the place where I came from... to be pure bad. Because, then what would that make me?"
            w  "...and I'm still making it about me... when you're the one suffering... I'm sorry..."
            r "..."
            r "...Its fine, I may have overreacted. As long as you keep in mind that things happening here are unjustifiable... we'll be good"
            r "..."
            r "I shouldn't have destroyed all this stuff too... people COULD change this for the better; my anger got the best of me..."
            #Show rocky blush
            r "Sorry"
            #Show Tara happy
            w "..."
            "..."
        
    elif tara = False:

        "Rocky continues punching the screen until it blacks out and his fist is a mess"

        n "..."

        if insanity_level == 0:
            p "Stop it! I'm mad too but this isn't helping anyone!"

        v "Rocky please stop you're scaring me..."
        "He stops when he hears those words and wordlessly turns around"
        r "..."
        r "... sorry, let's just go..."
        "..."

    else:
        pass

    jump pnc_loop


label lab_note_3:

    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Hakim Lee Head Senior researcher- Artificial Womb Experiment- Take #3- SUCCESS{/font}"
    centered "{font=Dudu_Calligraphy.ttf}First lab grown subject successfully developed from a solo male. The subject exhibits zero abnormalities and appears to be fully conscious. Subject is female and was created using the CEO's DNA. {/font}"
    centered "{font=Dudu_Calligraphy.ttf}He seems oddly intrigued by her. In all my years of working with him, I've never seen him so interested in another life that wasn't his...{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I wonder if he even recognizes her as her own unique life form, or as an extension of him? Taran what happened to you... you are not the man who recruited me all those years ago{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"

    if tara == True:
        w "This is where I was created... I never had a mother only father and Samsara to look after me... I wonder if I {i}am{/i} a carbon copy of father and turn out to repeat his mistakes..."

        menu:

            "The fact that your questioning it means you're not" if insanity_level == 0:
                $ tara_against_dad == True
                p "We are not our parents... the destiny you forge for yourself is your choice to make only, not anybody else's"
                w "..."
                w "Why, yes I suppose you are right... Why not stop focusing on his life and start focusing on mine"
                w "My entire life has been composed of figuring out if my father is really who he says he is and trying to fix his mistakes to save him..."
                w "From now on, I'll be doing it to save the world, and this is his last mistake..."
                p "That's the spirit!"
                w "Father, I don't want to hurt you or anyone else... but if the time comes... I'm ready..."

            "...":
                w "..."
                pass
    else:
        pass

    jump pnc_loop


label lab_note_4:

    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Daniel McGee- Research Assistant- Finally! AFTER YEARS FINALLY!!! We have successfully created a virus that doesn't kill the host AND overrides other diseases the former may have!{/font}"
    centered "{font=Dudu_Calligraphy.ttf}This isn't what we were achieving in our search for immortality but it's the closest we're gonna get! The entire lab has been celebrating for the past couple days!{/font}"
    centered "{font=Dudu_Calligraphy.ttf}Our families will be cured! Disease is a thing of the past! We dont care if we dont have permission from the CEO anymore! We're dispatching it in the chem trails ASAP! I'm saving you Grandma! Only downside is that it makes subjects near brain dead{/font}"
    centered "{font=Dudu_Calligraphy.ttf}The CEO has been even more quiet and solitary than usual, is he not happy with what we've achieved? He said he wanted to make one final adjustment to the virus before we dispatch it... guess that's reasonable.. {/font}"
    centered "{font=Dudu_Calligraphy.ttf}. we're already releasing it without his permission so might as well let the head researcher and founder work his magic? Perhaps he saw a flaw we didn't...{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"
    if vinnie_dead == False:
        v "Welp, this is how it spread... guess I better apologize to Rocky for saying his conspiracies were stupid..."

    if rocky_dead == True and vinnie_dead == False:

        v "Rocky if your out there... I'm sorry"

    if rocky_dead == False and vinnie_dead == False:

        v "NOT!!! I will never apologize even {i}IF{/i} the frogs turn gay!!!"
        r "Even in my moment of glory you still find a way to be petty, I'm not letting you get in the way of my validation!!"
        "Rocky strikes a stupid pose and does a victory dance while pointing at a sulking Vinnie'"
        r "OH YEAH, SUCK IT VINNIE"
        v "WHATEVER DUDE! Let's get out of here..."

    if vinnie_dead == True and rocky_dead == False:

        r "Guess the chem trail conspiracy was true... Vinnie... you would be so pissed if you were still here... I can even hear you doing your pouty voice whenever something goes wrong heh"
    
    if norman_dead == False:

        n "The flaw the CEO incorporated... that has to be it... the zombie virus..."

    p "This was no accident, the CEO planned this all out. He wanted to watch the world burn"
    
    if tara == True:

        t "... you told me since I was a little girl this was supposed to help people, you lied to me! YOU LIED TO ME!!"
        t "... you really are no different from your monsters, this isn't forgivable, we're gonna make you pay for all the lives you took..."
        "Tara says in clenched teeth"

    jump pnc_loop


label keycard:
    $ keycard == True
    "I look around the drawers and find an employee keycard!"
    jump pnc_loop

label bullet:
    "Looks like a single bullet...."
    if norman_has_gun:
        $ ammo += 1
        "Norman stuffs it into his pockets"
    else:
        $ ammo += 1
        "I stuff it into my hoodie"
    jump pnc_loop

label puzzle_piece_b_collect:
    $ puzzle_piece_b_collect == True
    "I collect puzzle piece B"
    $ renpy.notify("Puzzle Piece B has been added to your inventory!")

    jump pnc_loop

label locked_master_door:
    if piece_puzzle_a and piece_puzzle_b:
        "I enter through the door"
        jump boss_battle
    else:
        "This door won't open unless we activate something around here..."
    jump pnc_loop


label piece_puzzle_a:
    if puzzle_piece_a_collect:
        $ piece_puzzle_a == True
        "I solve it"
    else:
        "This needs it's respective piece to open..."
    jump pnc_loop

label piece_puzzle_b:
    if puzzle_piece_b_collect == True:
        $ piece_puzzle_b == True
        "I solve it"
    else:
        "This needs it's respective piece to open..."
    jump pnc_loop


##LAB BOSS BATTLE ENDING
label boss_battle:
    scene black with dissolve
    "Here we are... it's taken so long but we're finally here..."
    scene boss battle with dissolve
    "..."
    s "..."
    s "...Ah, you're here. I have to say I'm impressed with how far you've progressed. I figured the juggernaut would dispose of you"
    s "I've been watching you know. There are cameras all over the facility. I've been with you ever since you stepped foot into this facility"
    "The CEO is on a slight raised platform from the rest of us with a control panel"
    if norman_dead == False:
        n "Sir! You need to stop what you're doing at once! Let us out of here!"
        s "The exit is right where you came from; never mind the inevitable horde bound to eat you from the inside out though..."

        if rocky_dead or vinnie_dead == True:
            s "You're deceased friends seem to have gotten a head start on you! Why don't you take a page from their book and step outside?"     

    if vinnie_dead == False:
        v "Everything you've done is revolting! How could life have no meaning to you?"
        s "What's revolting is how every entity in the world, doesn't see the glory being made here..."

        if rocky_dead == True:
            s "You're Maned Wolf friend would have loved the changes I had in mind. The little people is always at the forefront of my mind. They are so desperate which makes them easy for manipulation"
        if norman_dead == True:
            s "The Golden Retriever comes from a higher echelon then the rest of you, I have personally met his family in a business dealing with me. He would agree with me"   

    if rocky_dead == False:
        r "Listen here old timer, if you don't point us to the exit I'll knock you on your ass and kick your teeth in!"
        s "Oh my how unrestrained, would you still behave this way if you were alone?"

        if vinnie_dead == True:
            s "Are you making up for your lack of ferocity with saving the opossum? They died because of you. I'm sure you know that"
        if norman_dead == True:
            s "I'm sure the Golden Retriever would'nt be a fan of your attitude, good thing they're not here right now right?"   

    if tara == True:
        w "Father! How could you! You betrayed me and the people that trusted you with your actions! I- I don't know you anymore, you've broken my heart!"
        s "My daughter, step away from them. It's a family business no?"
        w "I will not! Get away from me!"
    p "It's not too late to stop, just call up a helicopter to get us out of here and you can make a cure!"
    if insanity_level >= 2:
        s "Golden coming from you of all people, I've seen how you really act... You don't like your friends as much as pretend to huh?"
        s "Were you trying to get them all killed? Or do you just not care either way?"
    else:
        s "Oh it's you the leader I presume? You've done well guiding everyone... Props to you I suppose..."
        if norman_affection >= 3:
            s "You even made yourself a little boyfriend in all this, I wonder if you took advantage of the situation for this very purpose"
            if norman_dead == True:
                s "Too bad you couldn't protect them! I'm sure their last thoughts were of pretending they were in your arm's instead of the monsters"
    s "Eons worths of research was conducted here by me, the little lambs baptized in rotten flesh and putrid blood were guided into the mouth of god"
    s "In other words, me"
    s "I tied the noose around all my researchers necks and let them go! Their sacrifices were not in vain look were they got me!"
    s "They wanted to use MY research for themselves and their families! Idiots! It was for MY immortality! My ascent to godhood!"
    s "My IQ is unmatched, I was put into this world to guide it, All I needed was the time which the project was meant to achieve"
    s "When they wanted to use it for something else... I corrupted it into this zombie virus. I realized the world only cares about each other, so I need to remake it to care about ME and only ME as the one who guides them out of armageddon!"
    s "I needed to tie up a few loose ends here, so I got this here private military force of mine to shoot up any survivors and blow up the building so none can tell what really happened here!"
    "The CEO kicks one of the many armored men's corpses in the head"
    s "Of course, {i}they{/i} had to be dispatched too, so I ordered them all to kill one another! The were infected by a special of the virus a long time ago and are completely bound to my will"
    s "Hmm if you're not up for jumping into this here pit of hydrofluoric acid, then there is an alternative..."
    "The CEO presses a button on the control panel near him and activates two large metal doors on our left and right which reveals..."
    "10 zombies and 1 one juggernaut zombie!"
    "This is serious, if I make one mistake it would mean instantaneous death..."
    if tara == True:
        w "Father no!"
label save_norman_finale:
    if norman_dead == False:
        if norman_affection >= 0:
            n "[pov]! Behind you! I won't let them hurt you!"
            "Norman runs up behind me and delivers a jump kick to the zombie behind me!"
            jump save_vinnie_finale
        else:
            n "Ah! I need help!"
            if norman_has_gun == True:
                "Norman's gun was wrestled out of his hand by one of the zombies"
            jump boss_zombies_v_norman
    else:
        jump save_vinnie_finale

        menu boss_zombies_v_norman:

            "Use Tara against the CEO" if tara == True:
                jump boss_aftermath

            "Take off the helmet of the juggernaut zombie" if boss_juggernaut_zombie == True:
                jump the_juggernaut

            "I save myself and do nothing!":
                $ insanity_level += 1
                $ norman_health -=1
                if norman_health <= 1:
                    $ norman_lab_death == True
                play sound "audio/sfx/punch.ogg"
                n "Yeowch!"
                "Norman is hurt..."
                jump save_vinnie_finale

            "Push Norman into danger" if insanity_level >= 1 and norman_affection <= 1 and tara == False and rocky_dead and vinnie_dead == True:
                $ norman_health -=5
                $ insanity_level == 100
                $ norman_dead == True
                n "HELP ME!! HELP ME!!"
                $ norman_lab_push_death == True
                "Were Norman's last words before being lost to the horde..."
                jump boss_aftermath

            "I tell Vinnie to use their knife" if vinnies_knife == True:
                $ vinnies_knife = False
                v "I'll protect you Normie!"
                n "Thank you Vinnie!"
                "Vinnie stabs one of the zombies attacking Norman but loses the knife in the process"
                jump save_vinnie_finale
           
            "I tell Vinnie to save Norman!" if vinnies_knife == False:
                if expose_samsara_together_2 == True:
                    v "I got you Norman!"
                    "Vinnie helps Norman with no issue"
                else:
                    $ vinnie_health -= 1
                    v "Got it! I'll save you Norm! OW!"
                    "Vinnie punches the man but gets punched back HARD in the face"
                    if vinnie_health <= 1:
                        $ vinnie_lab_death == True
                jump save_vinnie_finale

            "I skewer the zombies with my horns!":
                if norman_affection >= 0:
                    play sound "audio/sfx/punch.ogg"
                    "I'm not letting HIM die!" with hpunch
                    n "Woah, That was awesome [pov]!"
                else:
                    $ sage_health -= 1
                    play sound "audio/sfx/punch.ogg"
                    "I take some damage in return..." with hpunch
                    if sage_health <= 1:
                        jump death_screen
                    n "Thanks!"
                jump save_vinnie_finale
            
            "I shoot the zombies!" if sage_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I shoot the zombie attacking Norman!"
                jump save_vinnie_finale

            "I shoot the zombies!" if norman_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I pick up the gun he dropped and shoot the zombie attacking Norman! I'm in control of the gun from now"
                jump save_vinnie_finale       

            "I crowbar the zombies!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/punch.ogg"
                $ crowbar_collected == False
                "I use the crowbar against the zombies! But the horde yanks it out of my hands and it gets lost in the stampede"
                jump save_vinnie_finale

            "I tell Rocky to save Norman!" if rocky_dead == False:
                if expose_samsara_together:
                    play sound "audio/sfx/punch.ogg"
                    r "GET BEHIND ME!"
                    n "GOT IT!"
                    jump save_vinnie_finale
                elif crowbar_collected:
                    play sound "audio/sfx/punch.ogg"
                    $ crowbar_collected == False
                    r "HUT!"
                    "Rocky uses the crowbar against the zombies but the horde yanks it out of his hand and it gets lost in the stampede"
                    jump save_vinnie_finale
                else:
                    play sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 1
                    r "URGH!"
                    "Rocky uses his body to shell Norman from danger but gets hurt in retaliation"
                    if rocky_health <= 1:
                        $ rocky_lab_death == True
                    jump save_vinnie_finale

label save_vinnie_finale:
    if vinnie_dead == False:
        v "S-stay away!"
        if expose_samsara_together_2 == True:
            v "NO! I'M NOT LETTING ANY OF YOU HURT ME OR MY FRIENDS ANYMORE!!! I'M TIRED OF BEING AFRAID!"
            "Vinnie uses their claws to gouge the throat of one of the zombies!"
            jump save_rocky_finale
        else:
            jump boss_zombies_v_vinnie
    else:
        jump save_rocky_finale

        menu boss_zombies_v_vinnie:

            "Use Tara against the CEO" if tara == True:
                jump boss_aftermath

            "Take off the helmet of the juggernaut zombie" if boss_juggernaut_zombie == True:
                jump the_juggernaut

            "I save myself and do nothing!":
                $ insanity_level += 1
                $ vinnie_health -=1
                play sound "audio/sfx/punch.ogg"
                n "Yeowch!"
                "Norman is hurt..."

            "Push Vinnie into danger" if insanity_level >= 1 and tara == False and rocky_dead and norman_dead == True:
                $ vinnie_health -=5
                $ insanity_level == 100
                $ vinnie_dead == True
                v "ROCKY!!"
                "Were Vinnie's last words before being lost to the horde..."
                $ vinnie_lab_push_death == True

            "I tell Vinnie use their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                v "EAT IT YOU LIMP DICK SON OF A BITCH!!!"
                "The knife was lost in the process..."
           
            "I tell Norman to save Vinnie!" if norman_dead == False:
                if norman_affection >= 1:
                    n "YOU'RE NOT DYING ON MY WATCH!"
                    "Norman does a high kick so hard it knocks a zombie's head off! Norman helps Vinnie with no issue"
                else:
                    $ norman_health -= 1
                    if norman_health <= 1:
                        $ norman_lab_death == True
                    n "YOU'RE NOT DYING ON MY WATCH!"
                    "Norman gets hurt in retaliation"

            "I attack the zombies!":
                $ sage_health -= 1
                play sound "audio/sfx/punch.ogg"
                v "THANK YOU GOAT PERSON!" with hpunch
                "I get hurt in return..."
            
            "I shoot the zombies!" if sage_has_gun == True  and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I shoot the zombie!"

            "I crowbar the zombies!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/punch.ogg"
                $ crowbar_collected == False
                "I use the crowbar against the zombies! But the horde yanks it out of my hands and it gets lost in the stampede"

            "I tell Rocky to save Vinnie!" if rocky_dead == False:
                if expose_samsara_together == True:
                    play sound "audio/sfx/punch.ogg"
                    "Rocky sprints at full force while punching any zombie thats get in his way to the ground, he then pummels the zombie attacking Vinnie to ground"
                elif crowbar_collected:
                    play sound "audio/sfx/punch.ogg"
                    $ crowbar_collected == False
                    r "HUT!"
                    "Rocky uses the crowbar against the zombies but the horde yanks it out of his hand and it gets lost in the stampede"
                else:
                    play sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 1
                    if rocky_health <= 1:
                        $ rocky_lab_death == True
                    r "URGH!"
                    "Rocky uses his body to shell Vinnie from danger but gets hurt in retaliation"

label save_rocky_finale:
    if rocky_dead == False:
        r "AAGH!"
        if expose_samsara_together == True:
            r "AAAAAAAAAAAAAAGHHHHHHHHH!!!"
            "Rocky lifts a zombie over his head and throws it into the horde at full force!"
            jump boss_aftermath
        else:
            jump boss_zombies_v_rocky
    else:
        jump boss_aftermath

        menu boss_zombies_v_rocky:

            "Use Tara against the CEO" if tara == True:
                $ tara_hostage = True
                jump boss_aftermath

            "Take off the helmet of the juggernaut zombie" if boss_juggernaut_zombie == True:
                jump the_juggernaut

            "I save myself and do nothing!":
                $ insanity_level += 1
                $ rocky_health -=1
                play sound "audio/sfx/punch.ogg"
                r "Oof!"
                if rocky_health <= 1:
                    $ rocky_lab_death == True

            "Push Rocky into danger" if insanity_level >= 1 and norman_affection <= 1 and tara == False and norman_dead and vinnie_dead == True:
                $ rocky_health -=10
                $ insanity_level == 100
                $ rocky_dead == True
                $ rocky_lab_push_death == True
                r "VINNIE! I'LL SEE YOU SOON!"
                "Were Rocky's last words before being lost to the horde..."

            "I tell Vinnie to use their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                v "I'll protect you Rocko!"
                r "Thankya!"
                "Vinnie stabs one of the zombies attacking Rocky but loses the knife in the process"
           
            "I tell Vinnie to save Rocky!" if vinnies_knife == False:
                if expose_samsara_together_2 == True:
                    r "I got you Rocky!"
                    "They pierce their claws through a zombies eyes! Vinnie saves Rocky with no issue!"
                else:
                    $ vinnie_health -= 1
                    v "Got it! I'll save you Rocko! OW!"
                    "Vinnie kicks the zombies but gets hurt"
                    if vinnie_health <= 1:
                        $ vinnie_lab_death == True

            "I skewer the zombies with my horns!":
                $ sage_health -= 1
                play sound "audio/sfx/punch.ogg"
                "I take some damage in return..." with hpunch
                if sage_health <= 1:
                    jump death_screen
                r "Thankya!"
            
            "I shoot the zombies!" if sage_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I shoot the zombie attacking Norman!"
            
            "I Tell Rocky to use the crowbar!" if crowbar_collected == True:
                play sound "audio/sfx/punch.ogg"
                $ crowbar_collected == False
                "Rocky use the crowbar against the zombies! But the horde yanks it out of his hands and it gets lost in the stampede"

            "I tell Norman to save Rocky!" if norman_dead == False:
                $ norman_health -= 1
                if norman_health <= 1:
                    $ norman_lab_death == True
                n "Here I go! URGRGH!!"
                "Norman gets damaged in turn..."

label the_juggernaut:
        $ boss_juggernaut_zombie == False
        play sound "audio/sfx/punch.ogg"
        "I dash and jump on top of the juggernaut zombie like before, as I'm on it's shoulder's I rip off his helmet and throw it into the acid pit!"
        queue sound "audio/sfx/zombie moan.ogg"
        if norman_dead == False:
            "Norman takes his chance to tear off some more of the juggernaut's armor!"
        if vinnie_dead == False:
            "Vinnie uses their claws rip out it's eyes!"
        if rocky_dead == False:
            "Rocky uses his jaws to inflict large gashes upon it's neck!"
        "The juggernaut moans in distress before jumping into vat of acid to chase after his helmet, it takes the majority of the zombies along with it"

label boss_aftermath:
    if tara_hostage == True:
        "Strangely it seems the zombies are ignoring Tara"
        if sage_has_gun == True:
            "I grab her and point a gun towards her head"
        else:
            "I grab her and threaten to throw her into the pit of acid"
        if insanity_level == 0:
            p "Play along ok?"
            "I whisper in Tara's ear as she nods in understanding"
        p "I'll kill her if you don't stop!"
        s "Halt!"
        "The CEO raises his fist and presses a button on the console which dispenses some type of powder of zombies which causes them to be stunned and then drop catatonic"
        s "Return her to me..."
        "I let Tara go as she stares daggers into her father's eyes"

    if norman_lab_death == True:
        $ norman_dead == True
        "Norman was lost, I presume he was eaten whole as I don't see his corpse anywhere"

    if rocky_lab_death == True:
        $ rocky_dead = True
        "Rocky couldn't make the onslaught, he was eaten alive"

    if vinnie_lab_death == True:
        $ vinnie_dead = True
        "Vinnie didn't survive, the horde lifted them and threw them over the ledge"

    s "That's enough of this! I'm giving you one last chance to give up! You're destroying ALL my research! You're setting society back by generations!"
    s "Are you too dense to understand this? I give up, I'll offer an alternative to where I wipe all you're memories of what happened here and call for an escort out of this city"
    if norman_dead == False:
        n "Does he really have the ability to wipe minds or is he bluffing?"
    if vinnie_dead == False:
        n "He's gotta be bluffing! He's just saying that because we caught his ass!"
    if rocky_dead == True:
        r "You're shitting me if you think we're letting you get away scot-free!"
    p "So there is a way out of here..."
    if insanity_level == 0:
        p "You know it's not too late, you can come with us and answer for your crimes peacefully..."
    s "I- It's too late for me anyways... I... was bit..."
    "He rolls up his sleeve and reveals a large bite on his arm"
    p "I see.. that makes an escape for you unnecessary right?"
    s "Indeed, there is no cure"
    if tara == True:
        w "No! No! NO!! Father you can't die! You can't!"
        s "I am sorry my daughter... It's over for me..."
        w "You did such terrible things. Such disgusting things! Why! Why are you still trying to hurt me! Even now!"
        s "...Tara... I've never called you by your name to your face... Tara... you're father can't provide the life you need..."
        s "I see it now, before when you were created. I deluded myself into thinking you were nothing but a clone of me. You aren't though... I see it now, especially with the friends you made"
        s "You tried so hard to protect everyone here and expose me as the monster I am... Tara... There's something wrong with my brain... I can't think like you do..."
        s "I want to become god of this universe and guide the world into a new era of progression. I am aware that it's not something a typical person would think but I still do"
        s "Even now, after all this death and destruction I am going to continue my ways. It hasn't changed me one bit, which made me realize how this affects you"
        s "You are going to die if you keep following me Tara. The new world will have me as it's sole ruler, no one can be equal to my power."
        w "But you're changing right now don't you see!?! Snap out of it! Come back to me! Quit your experiments and business and we go back to our home and make a new life there!"
        w "All you need to do is put everything away and turn yourself into the police, don't shut me out!"
        s "I'm not changing... if I was given the opportunity I would kill all of you if it guaranteed me my rightful place of godhood!"
        w "Do it! Do it now then! If that's true why haven't you killed me yet!"
        s "I-"
        w "Look me in the eyes when you say it! I don't believe your words for a second! I know you'r head isn't right! But it's right enough to acknowledge your daughter for crying out loud!"
        s "I- I- AAAAAAAAAAAAAAAAAAAAAAAAAAAGHHHHHHH!!!!!!!"
        "The CEO clutches his head before running away from us and throwing himself off off the ledge and into the pit"
        w "NOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!"
        w "WHY! WHY! FATHER!"
        "Tara breaks down crying while on her knees"
        if norman_dead == False:
            n "Oh Tara I'm so sorry..."
            "Norman pats her back as he gazes upon the abyss"
        if vinnie_dead == False:
            v "Guess there was something deep in him that knew"  
        if rocky_dead == False:
            r "..."
            r "This doesn't fix what he's done. But at least one part of his mind knew it wasn't right"
        p "One half dominant, making him the monster that we knew. The other half deep inside, only coming out when he saw the first and only person he cared about..."    
        "We find the elevator out of here and call for a chopper using his control panel"
    else:
        p "Just let us go then, your empire is finished. There's nothing for you here anymore"
        s "..."
        "The CEO looks back and fourth before sighing and pressing a button on the control panel that reveals an elevator door"
        s "Leads straight to the rooftop..."
        if norman_dead == False:
            n "Thank you for coming to reason..."
        if vinnie_dead == False:
            v "Finally a way out!"  
        if rocky_dead == False:
            r "...? I don't know if I can trust this..."
        s "Just one last thing... "
        "We all turn around and didn't even notice he was standing over the ledge"
        s "... Prepare for the second coming..."
        "He throws himself into to the pit below"
        "..."

        if vinnie_dead == False:
            v "Geez..."
            if rocky_dead == True:
                v "Fucker deserved worse for what happened to Rocky..."
        if rocky_dead == False:
            r "Guess that's that taken care of..."
            if vinnie_dead == True:
                r "I wish I had the chance to rip his fucking throat out for what he caused happen to Vinnie..."
        if norman_dead == False:
            n "Oh..."

        "I stand in disbelief before heading for the elevator, I decide to take a look at the control panel to check if he called for a chopper"
        "...!"
        n "Hey! He set the neurotoxin gas defenses level to ON for the elevator systems here!"    
        if norman_dead == False:
            n "Better switch that off! I'm sure the ventilation system will get rid of it in due time!"                    
        if rocky_dead == False:
            r "...I REALLY wish he was still here so I could kill him..."
        if vinnie_dead == False:
            "Wow! Even after death he's still just as vindictive!"

    pause 0.3
    scene elevator with dissolve
    "..."
    "I can't believe after all this time it's over..."
    "The deaths, the zombies, the people out to kill us.. it's all over..."
    if norman_dead or rocky_dead or vinnie_dead and insanity_level == 0:
        "I just wish everyone we came with made it out along too..."
    if norman_dead == False:
        n "Chin up! We've done it [pov]!"

        if norman_affection >=1:
            "Norman comes up to me while I'm stewing and nuzzles my nose with his"

    if insanity_level >=1 and vinnie_dead and rocky_dead and norman_dead == True and tara == False:
        "I did it, I lived. I left the others to their fates so {i}I{/i} could live"
        "...They..."
        "I didn't even know them for that long. Why {i}should{/i} I feel guilty? In this new world it's about survival. It's about {i}me{/i}, everyone else is secondary"
        "Friendship is overrated, it's a trap people pull on you to make feel like you owe them things."
        "I am the one in control of people's fates. If I wanted to I could kill them. I decide who lives and who dies. I am the god of this world"
        "Kneel before me, the second coming won't be as soft as the last..."
        "..."
        "I feel like I'm forgetting something?"
        "..."
        "If I forgot... It must not be important..."
        "..."

    if vinnie_dead and rocky_dead and norman_dead == False:
        v "WE FUCKIN DID IT LADIES AND GENTLEMEN! WE CAME STRAIGHT IN THIS PLACE WITH ONE GOAL IN MIND! SURVIVAL! AND PULLED IT OFF!!!!"
        v "WOOOOOHOOOOOOO YEAHHHH!!!! JUMP FOR JOY HOS!!!!"
        if norman_affection >=5:
            V "AND THE BEST PART IS THAT [pov!u] AND NORMAN GET TO GET LAID!!!!!!!!!!!!!!"
            n "VINNIE! NO!"
            p "Are you for real..."
            r "Eww! You're gonna scare them away from each other!!"
        r "Vinnie man, come on stop with this!"
        "Vinnie is bouncing up and down while shaking Rock with him!!"
        v "YIPEE KI-YAY MOFOS!!!!!!!!! WE'RE ALL ALIVE HAHAHAHAHAHAHA!!!!!!!!!!!!"
        n "We did it! We did it! We get to live! Haha!"
        v "KISS ME LIKE YOU MEAN IT ROCKY! PUCKER UP!"
        if tara == True:
            w "Indeed! Indubitably! Without a doubt! \"Abso-fruitly\" if you will, considering who I'm traveling with..."
            p "Hey is that homophobia I hear?"
            w "No! Not at all I support you all very much!"
            v "Hmmm my homophobic vision senses it deep within your soul..."
            v "RELEASE IT!! MY PATIENT! LET THE HOMOPHOBIA FLOW THROUGH YOU!!! Rocky this isn't safe place for you anymore, we're the straight club now!"
        r "The hell? I'm the straightest guy here! Just take a look at you!"
        if norman_affection >=5:
            r "Two of you literally {i}dating{/i} each other!"
        r "What's gayer than that!"
        v "Ummm I think your search history is when I was trying to look up something is!!"
        r "...! Tha- That's- It was just the firefighter recruitment site!"
        v "ER! WRONG! Why were all of those firefighters exclusively men and half nake-"
        "Rocky bear hugs Vinnie before strangling them in the corner!"
        r "IF THE ZOMBIES DIDN'T KILL YOU I WILL!"
        v "HELP MEEEEEEE!!!!!!!!"
        n "Hahahaha!!!"
        p "You people are insane. I love it."
        if tara == True:
            w "Ha! You're all hilarious! I've gotta stick with you!"
        p "Ah, sounds like the elevator is coming to a stop"
        p "Guys, let's make a promise... let's be together... forever..."
        "Everyone turns towards me and motions for a group hug"
        v "I love you guys! You're welcome to huck rocks at the city hall with me anytime!"
        r "I'll carve time out of my schedule to hang out with you all more! Screw the endless hours! I'm sick of it!"
        n "I love you all more than my actual family!"
        if tara == True:
            w "I'm my own person now thanks to you all! Thank you so much!"
    else:
        if vinnie_dead == False and rocky_dead == True:
            v "I did it Rocky, we did it for you... We lived... Thank you Rocky, you're still motivating me to keep going..."
            if norman_dead == True:
                v "I couldn't protect Norman either... I failed you two... we swore to keep him safe and I fucked up like I always do..."
                v "Why did I live?"

        if rocky_dead == False and vinnie_dead == True:
            r "I lived Vinnie but, at what cost? You died and I lived... You'll always be in my heart, you're still cheering me on..."
            if norman_dead == True:
                r "Norman died because of me Vinnie, I couldn't protect any of the people I love... I couldn't keep our promise to protect him..."
        if tara == True:
            if vinnie_dead or norman_dead or rocky_dead == True:
                w "I'm so sorry about your friends..."
            w "At least we survived..."
        if insanity_level == 0:
            "They're dead and there's nothing I could do about it. I wanted to keep my new friends, my new family, safe but..."
            "I'm so sorry I failed you... now we pay the price for death..."        

        "..."

        pause 0.3
        scene black with dissolve
        pause 0.2
return



