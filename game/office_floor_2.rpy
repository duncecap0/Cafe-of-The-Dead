

#variables 
default password_attempts = 0
default word_puzzle_completed = False

default closet_broken = False

default monday = False
default wednesday_and_friday = False
default tuesday_and_thursday = False
default examined_computer = False
#deaths
default norman_secret_death = False

default norman_office_death = False
default vinnie_office_death = False
default rocky_office_death = False

#weapons
#default scissors = False


#examinations
default juggernaut_zombie = True

default examined_window = False

default save_tara_1 = False
default save_tara_2 = False

default tara = False

default medkit_used = False

default morphine_used = False

default medkit_for_tara = False
default morphine_for_tara = False

default vinnie_helped_tara = False


default examined_tara = False

default expose_samsara_together_2 = False


#password
define password = "widen moth future"
define password2 = "WIDEN, MOTH, FUTURE "
define password3 = "widen, moth, future"
define password4 = "WIDEN MOTH FUTURE"
define password5 = "widenmothfuture"
define password6 = "WIDENMOTHFUTURE"
define password7 = "widen moth and future"
define password8 = "widen moth and future"
define password9 = "WIDEN AND MOTH AND FUTURE"
define password10 = "widen and moth and future"
define password11 = "Widen Moth and Future"
define password12 = "Widen Moth Future"
define password13 = "Widen moth future"
define password14 = "Widen, moth, and future"
define password15 = "Widen, Moth, and Future"
define password16 = "widen, moth and future"


define password_input = "Use keyboard to input words"


label office_floor_2:
    $ w_name = "Injured Woman"
    stop sound
    stop music fadeout 1.0
    pause 1.0
    hide screen character_stats with dissolve
    hide screen ammo_stats with dissolve
    scene elevator with dissolve

    "We all sit in silence for a good while,{w=.3} just trying to take it all in..."

    play sound "audio/sfx/elevatording.ogg"

    "Norman already pressed the button for us to go into the office space,{w=.3} we think survivors are in there..."
    ##NORMAN GETS DEPRESSED DIALOGUE TREE

    play music "audio/music/Going_Up.mp3"

    if rocky_dead == True or vinnie_dead == True:
        "The elevator's music is playing as if it were mocking our losses..."
    if vinnie_dead == True and rocky_dead == False:
        #"Rocky has Vinnie's lifeless body's head resting on his lap, {w=.3} eyes closed as if they were sleeping;{w=.3}  Rocky seemed to be lost in them..."
        "Rocky hasn't spoken a word since it happened,{w=.3} the rest of us are too afraid to speak until-"
    show n 8 with dissolve
    n "..."
    n "We've gotten pretty far now haven't we?"
    if rocky_dead == True or vinnie_dead == True:
        n "I know we've had some losses on the way... {w=.3}things won't be the same without them..."
        label norman_death_reaction:
        if rocky_dead == True:
            n 3a"Rocky's protectiveness,{w=.3} bravery, and caring nature... {w=.3}always making sure everyone was happy even if it hurt him... {w=.3}he was my first best friend you know... {w=.3}I still can't grasp he's..."
        if vinnie_dead == True:
            n 3a"Vinnie's charm, love, and acceptance....{w=.3} always trying to get people to not wallow in misery for too long... {w=.3}they wanted this friend group to exist more than anything...."
            n 1"Ah! {w=.3}Look at me getting emotional...{w=.3} we have work to do no? Haha..."
        menu:
            "I'm sorry for your losses":
                $ addInsanity_level(-1)
                $ norman_affection += 1
                show n 5 at hop
                n "...!"
                n 8"They're your losses to you know...{w=.3} just because you're the newest member doesn't mean that your worth less...{size=*0.8}{w=.9} especially to me...{/size}"
                p 2"They're your friends, our friends,{w=.3} how can you not be sad?{w=.3} It's ok to let it out Norman...{w=.3} to feel pain is to be alive..."
                n "..."
                if vinnie_dead == False and rocky_dead == True:
                    show v 12 at right with dissolve
                    v "I miss him too Norman...{w=.3} I don't think I'll ever be able to live like how he wanted me to,{w=.3} but if you having nothing to lose you have nothing to gain? Remember his words you told me?"
                elif rocky_dead == False and vinnie_dead == True:
                    show r 7 at left with dissolve
                    r "I miss them too Norman...{w=.3}  I'll never be able to laugh like how they made me,{w=.3} but if you having nothing to lose you have nothing to gain!"
                if rocky_dead == False or vinnie_dead == False:
                    hide n 5 with dissolve
                    hide r with dissolve
                    hide v with dissolve
                    n "Guys... {w=.3} I... {w=.3} I c-{w=.3} can't..."
                    "Norman begins sobbing uncontrollably before leaping into our arms...{w=.3} we all hug until we hear sniffling die down...{w=.3} I don't even know if it's from Norman or not..."
                else:
                    hide n 5 with dissolve
                    n "[pov]... {w=.3} I...{w=.3}  I c-{w=.3}can't..."
                    "Norman begins sobbing uncontrollably before leaping into my arms... {w=.3}we hug until I hear the sniffling die down..."
                    scene black with dissolve
                    "I don't want to let go..."
                    pause 1.0
                    scene elevator with dissolve
                n "Thank you...{w=.3} I needed that..."
                "A minute passes before everyone goes back to their respective part of the elevator, {w=.3}until Norman sidles up next to me again"

            "Don't get sappy.":
                $ norman_affection -= 1 
                $ addInsanity_level(1)
                show n 5 at hop
                n 5"{w=.3}...Oh...{w=.3} I suppose you're... {w=.3}right..."
                "Norman looks as if I had just slapped him,{w=.3} not my fault someone isn't focusing on the fact we could die at any minute..."
                hide n with dissolve
    else:
        show n 2 at hop
        n 2"We haven't had any losses yet! Go team us!"
        if insanity_level == 0:
            n 2"[pov]... I'm so proud of you...{w=.3} you're like a natural born leader...."
            n 8"That's one of the things I've always admired about you...{w=.3} so dead-set on their beliefs and willing to speak out! {w=.3}You may seem quiet to the naked eye but that's because people don't look hard enough!"
            n "You're able to speak louder than a million people with just a single sentence.{w=.3} You can accomplish what people only dream of doing; that's not an easy skill,{w=.3}I can assure you that..."
    
            menu:
                "Thanks":
                    n "No Problem [pov]!"

                "I admire you too Norman":
                    $ norman_affection += 1
                    if vinnie_dead == False:
                        show n 5 at shiver
                        n "[pov]...?{w=.3} D-{w=.3} don't say stuff like that out loud!{w=.3} Vinnie would NEVER let me hear the end of it.."
                    else:
                        show n 5 at shiver
                        show n 3 with dissolve
                        n "[pov]...? {w=.3}D-{w=.3} don't say stuff like that out loud! What if someone hears that?"
                        p "It's true though,{w=.3} strength and responsibility like Rocky, {w=.3}smarts and charm as Vinnie...{w=.3} and you say I'm the skillful one but I could only dream of being like you"
                        show n 3 at sink
                        "Norman has been staring down at the ground the whole time,{w=.3} I think I see his cheeks blush red..."
                        show n 3 at sink_rise
                        n "[pov]...{w=.3} thank you...{w=.3} truly..."
                        p "Don't mention it,{w=.3} I'll never forget it."
                        if vinnie_dead == False:
                            show v 27 at right with moveinright
                            show v 27 at offscreen_right with moveinright
                            hide v 27 with dissolve
                            "I'm pretty sure I caught Vinnie sneaking peeks at us;{w=.2} I don't care,{w=.3} let them watch..."
                        if rocky_dead == False:
                            "Rocky has been staring at his watch for far too long to be unsuspecting; {w=.2} as if he were trying to give us room,{w=.3} good."

    if norman_has_gun == False:
        if rocky_has_gun == True:
            $ rocky_has_gun = False
            show r 1 at left with dissolve
            if vinnie_dead == True:
                r "Your gun..."
            else:
                r "Here! {w=.3}Take your gun back Norman!"
        elif vinnie_has_gun == True:
            $ vinnie_has_gun = False
            show v 15 at right with dissolve
            v "TAKE THIS GUN AWAY FROM ME PLEASE NORM-NORM!!! {w=.3}I'm not a good shot at all..."
        elif sage_has_gun == True:
            p 1"Also,{w=.3} I believe this gun belongs to you?"
            if insanity_level == 0 or norman_affection >= 2:
                n 1"Hmm how about you keep it from now on [pov]! {w=.3}You proved yourself capable today!"
                p 4"You sure?{w=.3} I'm not a marksman or have the training that you do..."
                n "Says the one that doesn't panic at a moment's notice! Haha!{w=.3} Just take it you goof!"
                $ sage_has_gun = True
                jump office_floor_2_survivor_banter
        $ norman_has_gun = True
        n 2"Thanks! {w=.3}Good thing I never leave home without it!"

label office_floor_2_survivor_banter:
    if rocky_dead == False and vinnie_dead == False:
        show r 11 at left with dissolve
        r 11"That battle was intense! {w=.3}Glad we made it through alright!"
        show v 3 at right with dissolve
        v 3"Yeah that was ass up in shit's creek!{w=.3} Thanks to [pov]'s star spangling advice we got out there"
        r 2"Don't forget it was {i}my{/i} battle expertise that saved you all..."
        v "CALM YOU'RE DOUBLE D TIG OL BITTIES WOMAN!{w=.3} I'm not trying to accuse anyone of anything just saying that {i}I{/i} think some people pulled their weight more than others..."
        r 2a"...{w=.3} That's exactly what a fucking accusation is you dumb slut..."
        v 9"EXCUSE ME, AM I THE ONE WHO THINKS THAT ALL ASSASSINATED PRESIDENTS FAKED THEIR DEATHS TO JOIN THE SHADOW COUNCIL AND PULL THE STRINGS WITHOUT US KNOWING?!?!"
        r "THAT ASSASSINATION WAS TOTALLY STAGED AND I CAN PROVE IT!{w=.3} WHY DO YOU THINK ALL THEIR FRIENDS JUST SO HAPPENED TO DIE THE FOLLOWING YEARS HUH?!?!"
        v 1"They died because they were old as fuck and all that coke from their younger years caught up to them!"
        r "YOU TAKE THAT BACK YOU SHEEPLE!!!"
        v 5"Correct term is {w=.3}\"Sherson\"{w=.3} {i}actually{i}..."
        n 5"Guys, {w=.3}isn't that word a little offensive to [pov]?"
        "They're too busy continuously shouting back and fourth about conspiracy theories and the Deep State to hear..."
    elif rocky_dead == True and vinnie_dead == False:
        "I hear Vinnie chanting Rocky's name quietly under their breath as if it were a hastened prayer;{w=.3} I don't think they even noticed what they were doing..."
        if insanity_level == 0:
            "I reach out to squeeze Vinnie's shoulders who jumps in response"
            p 4"Hey Vinnie?{w=.3} It's gonna be ok bud...{w=.3} I didn't know you guys for too long but I can tell Rocky loved you...{w=.3} remember that we're here for you if you need anything got that?"
            v 2 2"..."
            v "...Thank you...{w=.3} [pov]... {w=.3}he was like family to me... {w=.3}I..."
            v "..."
            v "You and Norman are my family as well.{w=.3} Got it?"
            if norman_affection >= 1:
                p 3"...{w=.3} Norman especially is like a..."
            p 1"...{w=.3} I'm so grat-"
    elif rocky_dead == False and vinnie_dead == True:
        "I hear Rocky muttering something under his breath...{w=.3} I think it's some type of religious prayer?"
        if insanity_level == 0:
            "I reach out to touch Rocky's back who says nothing in response"
            p 4"Hey Rocky?{w=.3} It's gonna be ok big guy... {w=.3}I didn't know you guys for too long but I can tell Vinnie loved you... {w=.3}remember that we're here for you if you need anything got that?"
            r 7"..."
            r 8"...Thank you...[pov]...{w=.3} they were like family to me...{w=.3} maybe even a...."
            r "God,{w=.3} I wonder what mom and pa are up to right now...{w=.3} hope their safe..."
            r 7"..."
            r 3"You and Norman are my family too?{w=.3} Got it?"
            if norman_affection >= 0:
                p 3"...{w=.3}Norman especially is like a..."
            p 1"...{w=.3}I'm so grat-"
    if insanity_level >= 1 and norman_affection == 0:
        "..."
        "The air feels like it's flexing as awkward silence fills the room"
        "I couldn't help but notice Norman staring intensely at my back when he thinks I'm looking away,{w=.3} what's he so wary of? {w=.3}He's treating me as if I were one of the monsters..."
        "..."
    play sound "audio/sfx/elevatording.ogg"
    "The elevator comes to a sudden stop as the doors slide open"
    stop music fadeout 1.0
    n 5"Hello is anyone-"
    play music "audio/music/FLOOR_2.mp3"
    scene office start with dissolve
    show screen character_stats with dissolve
    show screen ammo_stats with dissolve
    extend " What in the world happened here!{w=.3} It's nothing but dead bodies!"

    p 4"They're not as fortunate as we thought they would be,{w=.3} it's putrid in here..."
    
    if rocky_dead == True and vinnie_dead == False: 
        show v 12 at right with dissolve
        v 12"There goes another hope... {w=.3}Rocky... {w=.3}I tried..."

    elif vinnie_dead == True and rocky_dead == False:
        show r 8 at left with dissolve
        r "So many corpses...{w=.3} is this what Vinnie is gonna look like soon?"

    elif rocky_dead == False and vinnie_dead == False: 
        show v 22 at right with dissolve
        v 22"I should have remembered those clamps I bought for rocky since those would be real useful in blocking my nose"
        show r 4a at left with dissolve
        r 4a"Ugh the smell-"
        show r 2
        extend " Wait, what were you talking about?!?"

    show n 2 with dissolve
    n 2"Let's not give up there has to be someone alive here!"
    jump office_start


##OFFICE ROOMS

label office_start:
    window hide diss
    scene office start with dissolve
    $ current_room = "office_start" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label office_hall:
    window hide diss
    scene office hall with dissolve
    $ current_room = "office_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label office_restroom:
    window hide diss
    scene office restroom with dissolve
    $ current_room = "office_restroom" 
    jump pnc_loop

label office_closet:
    window hide diss
    scene office closet with dissolve
    $ current_room = "office_closet" 
    jump pnc_loop

label office_desks:
    window hide diss
    scene office desks with dissolve
    $ current_room = "office_desks" 
    jump pnc_loop


label office_breakroom:
    window hide diss
    scene office breakroom with dissolve
    $ current_room = "office_breakroom" 
    jump pnc_loop

label office_boardroom:
    window hide diss
    scene office board room with dissolve
    $ current_room = "office_boardroom" 
    jump pnc_loop

label office_computerdesk:
    window hide diss
    scene office computer with dissolve
    $ current_room = "office_computerdesk" 
    jump pnc_loop

### POINT'n'CLICK LABELS ###

label office_corpse:
    "Various corpses are strewn about,{w=.3} some seem to have been eaten while a few are shredded with bullet holes.{w=.3} I don't understand how they were able to die if they had access to guns..."
    "...{w=.3}Where even are the people with guns if they're not dead in here?"
    if norman_dead == False:
        show n 3a with dissolve
        n "Doesn't this seem similar to how the people on the mechanical floor died?"
        hide n 3a with dissolve
    jump pnc_loop


label office_window:
    scene city view with dissolve
    $ examined_window = True
    play sound "audio/sfx/Wind.ogg"
    "The city is set aflame and seemingly empty of life... with only hordes of zombies shambling together flooding the streets,{w=.3} the sky is burning as smoke fills the air"

    if vinnie_dead == False:
        v "Things got worse since we last saw outside..."
    if rocky_dead == False:
        r "...{w=.3} I'll save you mom and dad,{w=.3} this will only take a bit longer"
    n "..."
    "Norman's staring blankly at the floor;{w=.3} as if he cant comprehend whats happening outside"

    menu:

        "It'll be ok Norman, don't worry":
            $ addInsanity_level(-1)
            $ norman_affection += 1
            n "T-{w=.3}thank you" 
            "Norman blurts out while still staring downwards"
    
        "Don't get distracted":
            $ addInsanity_level(1) 
            n "..."
    scene office start with dissolve
    jump pnc_loop

    label toilets:
        #"Enough with the toilets!"
        "What did I expect to get out of a toilet?"
        if vinnie_dead == False:
            show v 17 with dissolve
            v "Office workers usually do drug deals in here, {w=.3}hang on let me check behind one..."
            if norman_dead == False:
                show n 2 at right with dissolve
                n "Wow!{w=.3} That's so smart!"
            if rocky_dead == False:
                show r 10 at left with dissolve
                r "Looks like your teen years weren't as useless as everyone thought!"
                v 2"Shut it! NPC!"
            v 1"AHA! Found some morphine taped underneath this one!{w=.3} Who wants restroom drugs!?!?!"
            if norman_dead == False:
                n 5"Hang on hang on!{w=.3} Do we have to use it right now? {w=.3}Let's save it for when we really need it!{w=.3} Morphine isn't something to be played around with!"

            menu morphine_choice:
                "Who should I use it on?"

                "Me":
                    play sound "audio/sfx/use.ogg"
                    $ morphine_used = True
                    $ sage_health +=1

                "Norman" if norman_dead == False:

                    if closet_broken == True:
                        n "We should give it to the woman in the closet! Not ourselves!"
                        jump morphine_choice
                    else:
                        play sound "audio/sfx/use.ogg"
                        $ addNormhealth(1)
                        $ morphine_used = True
                        n "Never done drugs before..."

                "Rocky" if rocky_dead == False:
                    if closet_broken == True:
                        r 1"Shouldn't we use it on that one girl?"
                        jump morphine_choice
                    else:
                        $ addRockyhealth(1)
                        play sound "audio/sfx/use.ogg"
                        $ morphine_used = True
                        r 1"Reminds me of when I broke my back at the warehouse..."

                "Vinnie" if vinnie_dead == False:
                    if closet_broken == True:
                        v 2"That girl could use this instead!"
                        jump morphine_choice
                    else:
                        play sound "audio/sfx/use.ogg"
                        $ addVinhealth(1)
                        $ morphine_used = True
                        v 25"I hope I don't get addicted to these things again...."

                "Leave for now it may be useful later":
                    pass
                
                "Use on injured woman" if closet_broken == True and tara == False:
                    $ morphine_for_tara = True
                    jump injured_woman_closet
            scene office restroom with dissolve
            jump pnc_loop
        else:
            scene office restroom with dissolve
            jump pnc_loop

label blocked_closet:
    if tara == True:
        scene office closet with dissolve
        show w 8 with dissolve
        w "...I'm fine, {w=.3}thanks for checking up on me. {w=.3}Sorry but,{w=.3} I need to rest for a little bit longer before I join you..."
        if word_puzzle_completed == True:
            w 4"You solved the riddle!?! {w=.3}Great! Now we can go the next floor!"
            menu:
                "Let's go to the next floor!":
                    jump office_floor_ending

                "Let me continue exploring this floor":
                    w 5"Oh ok! {w=.3}That's smart! Make sure to be thorough!"
                    scene office hall with dissolve
                    jump pnc_loop
        else:
            if rocky_dead == False:
                show r 1a at left with dissolve
                r "Nobody will hurt you if I'm here,{w=.3} trust me"
            if norman_dead == False:
                show n 2 at right2 with dissolve
                n "Take all the time you need!"
            if vinnie_dead == False:
                show v 10 at right with dissolve
                v "She's lost a lot of blood, {w=.3}please don't make her walk around [pov]..."
            menu computer_hints:
                "Help me with the computer puzzle":
                    w 2 "The express elevator is sealed behind a digital poem input, {w=.3}it's definitely related to the days of the week!"
                    if vinnie_dead == False:
                        v 2 "What if it had to be inputted a certain way to match the context of the sentence?"
                    if rocky_dead == False:
                        r 11 "Try unscrambling letters from highlighted words" 
                    menu:
                        "Help me more":
                                w 1 "A note fell from one of the higher up's pockets... {w=.3}It had the word {color=#f00}{u}OTH{/u}{/color} on it..."
                                menu:
                                    "Help me EVEN MORE":
                                        w 3 "I remember the phrase {color=#f00}{u}FUTURE{/u}{/color} being passed around a lot by higher ups..."
                                        menu:
                                            "Hit me baby one more time!":
                                                w 4"Hahaha! {w=.3}I remember {color=#f00}{u}_IDEN{/u}{/color} being on another note...{w=.3} looks like it's missing a letter..."                                
                                                menu:
                                                    "HELP ME!!!":
                                                        if vinnie_dead == True:
                                                            w 1"Try unscrambling all the letters from the days of the week around here into a word that would fit into the context of the sentence."
                                                        else:
                                                            v 2 3"DUDE C'MON!" with hpunch
                                                            v "Try unscrambling all the letters from the days of the week around here into a word that would fit into the context of the sentence."
                                                            if rocky_dead == False:
                                                                r 10"DUDE! VINNIE! CHILLAX!"
                                                                v "I'M SCREAMING BECAUSE [pov!u] COMPELS ME TO!" with vpunch
                                                                n 10"Jeez Vin! relax! You're going crazy!"
                                                                v 2 4"AAAAAAAAAAAAAAAAAAAAAA!!!!!!!" with hpunch
                                                
                                                    "Bye":
                                                        pass
                                            "Bye":
                                                pass
                                    "Bye":
                                        pass


                        "Bye":
                            pass
                    
                "Ok bye":
                    pass

        scene office hall with dissolve
        jump pnc_loop

    if closet_broken == False:

        play sound "audio/sfx/door open.ogg"
        "The door to this room won't budge as if it were locked from the inside"

        menu:
            "Sacrifice weapon to break it down?":
                pass
            "Leave door alone":
                jump pnc_loop

        if crowbar_collected and rocky_dead == True:
            $ closet_broken = True
            $ crowbar_collected = False
            play sound "audio/sfx/break.ogg"
            "I use the crowbar to break the handle, {w=.3}the crowbar is mutually as broken afterwards..."
            jump injured_woman_closet

        elif expose_samsara_together and rocky_dead == False:
            $ closet_broken = True
            play sound "audio/sfx/break.ogg"
            "Rocky is able to bust the door down!"
            jump injured_woman_closet

        elif crowbar_collected == True and expose_samsara_together == False and rocky_dead == False:
            $ closet_broken = True
            $ crowbar_collected = False
            play sound "audio/sfx/break.ogg"
            "Fortunately, Rocky uses the crowbar to break the handle,{w=.3} the crowbar also breaks in the process..."

            jump injured_woman_closet

        elif rocky_dead == True and vinnies_knife == True and vinnie_dead == False:
            $ closet_broken = True
            $ vinnies_knife = False
            play sound "audio/sfx/break.ogg"
            "Fortunately, Vinnie uses their knife to slowly wear away the handle over time. Unfortunately, {w=.3}it breaks as consequence..."
            jump injured_woman_closet

        elif vinnies_knife == False and crowbar_collected == False and rocky_dead == True:
            $ closet_broken = True
            "I have nothing to break the handle, should the gun be used?"
        
            menu:
                    "Shoot 4 times to break open the door handle":
                        play sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/break.ogg"

                        pause 0.3
                        "The handle breaks and I'm able to enter"
                        jump injured_woman_closet

                    "Find something else":
                        jump pnc_loop
        
    else:
        jump injured_woman_closet

label injured_woman_closet:
    scene office closet with dissolve
    $ w_name = "Injured Woman"

    if examined_tara == False:
        $ examined_tara = True
        show w 14 at right2 with dissolve
        w "..."
        "A bloodied female Pine Marten lies on the floor, her arm seems to be missing"
        p 7"Hello! Are you OK?"
        if rocky_dead == False:
            show r 2 at left with dissolve
            r "You're safe now! We're here for you! There {i}were{/i} other people here! Good thing we checked!"
        if vinnie_dead == False:
            show v 2 3 at right with dissolve
            v "There's so much blood!!{w=.3} How are you even still alive?!?!"
            v "Don't worry I'm a med student! {w=.3}I could help you I just need the supplies!"
        if norman_dead == False:
            show n 5 at left1 with dissolve
            n "Oh my god I'm so happy to know we're not alone! We need to save her!"
    show w 14 with dissolve
    if vinnie_dead == True:
        p 1"If only we had Vinnie, they were a med student who would have excelled here... she may be a lost cause without them..."
    menu try_save_woman:
        "That arm wound is brutal, {w=.3}how do I help with that?"


        "Use Med kit" if medkit_for_tara == True and vinnie_helped_tara == False and save_tara_1 == False:
            $ medkit_used = True
            $ save_tara_1 = True
            w 15"...{w=.3}rearrange... {w=.3}letters... {w=.3}days..{w=.3} of week..."
            if save_tara_1 and save_tara_2 == True:
                jump saved_tara
            else:
                "She's a little better, {w=.3}but not fully healed...{w=.3} she won't last long without further treatment,{w=.3} I wonder if there's anything else to give her?"
                jump try_save_woman

        "Have Vinnie help her in place of Med kit" if vinnie_dead == False and vinnie_helped_tara == False and save_tara_2 == False:
            show black with dissolve
            play sound "audio/sfx/use.ogg"
            pause 1.0
            $ save_tara_1 = True
            $ vinnie_helped_tara = True
            v 1"Here!{w=.3} That should do it!"
            hide black with dissolve
            w 15"t-thank you...{w=.3} rearrange... {w=.3}letters... {w=.3}days..{w=.3} of week..."
            if save_tara_1 and save_tara_2 == True:
                jump saved_tara
            else:
                "She's a little better,{w=.3} but not fully healed... {w=.3}she won't last long without further treatment,{w=.3} I wonder if there's anything else to give her?"
                jump try_save_woman

        "Use Morphine" if morphine_for_tara == True and save_tara_2 == False:
            $ morphine_used = True
            $ save_tara_2 = True
            w 15"You...{w=.3} must go to... {w=.3}top floor...{w=.3} only way out..."
            if save_tara_1 and save_tara_2 == True:
                jump saved_tara
            else:
                "She's a little better, {w=.3}but not fully healed...{w=.3} she won't last long without further treatment,{w=.3} I wonder if there's anything else to give her?"
                jump try_save_woman
                
        "Leave to look for stuff":
            p 4"I have nothing on me right now, {w=.3}maybe there's something else around?"
            if vinnie_dead == True:
                "Without Vinnie it's hopeless to help a wound this severe... {w=.3}she has no arm..."
            
    scene office hall with dissolve
    $ current_room = "office_hall"
    jump pnc_loop

label saved_tara:
    "She's better now!"
    $ tara = True
    $ w_name = "Tara"
    w 16 "T-{w=.3}thank you.. {w=.3}I won't forget this, {w=.5}truly. {w=.3}My name is Tara,{w=.3} I'm an employee here... {w=.3}when I heard you bust through the door...{w=.3} I really thought it was over for me...{w=.3} We were all called here today for an \"important\" meeting."
    w 1 "We waited patiently, {w=.3}until people in black body armour showed up and started shooting everybody dead, me and a couple other people ducked under our desks when we saw"
    w 8 "They shouted at us to line up until all of the sudden...{w=.3} The deceased rose back up again to attack us AND the armoured men!"
    w 15 "I started running when the men were distracted... {w=.3}It all happened so fast... {w=.3}I tried to call the others in here but they were... {w=.3}but they..."
    w 14 "..."        
    w 11"And then I realized...{w=.3}I was bit...{w=.3} and thought... {w=.3}cutting off the bite from the source would solve it...?{w=.3} I... {w=.5}honestly don't know if it worked... {w=.3}I was so desperate..."
    w 12"If you see me trying to take a chomp out of any of you..."
    w 13 "Just kill me... {w=.3}I don't want anyone else being hurt today...{w=.3} there's been so much blood spilled...{w=.3} too much..."
    show w 1 at shiver
    "Tara shudders for a bit before recomposing herself"
    if vinnie_dead == False:
        show v 4 at right with dissolve
        v "Sounds like you've been through a lot"

    if rocky_dead == False:
        show r 1 at left with dissolve
        r "I'm sorry to hear that"
    if norman_dead == False:
        show n 5 at right2 with dissolve
        n "I...{w=.5}I feel awful you had to experience that.{w=.3} We'll protect you from now on! {w=.3}Alright?!"
        n "We didn't see any of the armoured people outside so they must have gotten away!{w=.3} We'll be on guard for them!"
    p 1 "Yikes, {w=.3}they just started shooting for no reason? {w=.3}Sounds like the company planned for you all to die here... {w=.3}why is that?"
    w 2"I've noticed that Samsara has been heading towards a dark path, {w=.3}so I investigated the company's records and found shady dealings with the local medical facilities around here"
    w 1"The upper floors HAVE to be involved,{w=.3} all of us on the lower floors wanted to leave when when they started cracking things down, {w=.3}They usually go through the express elevator right outside this room"
    w 8"It's locked up tight,{w=.3} you need to crack the code to be able to enter. {w=.3}I found out that the password input is hidden behind a false wall in the boardroom. {w=.3}We need to solve it!"
    if rocky_dead == False:
        r 2"No offense but, {w=.3}we're just trying to get out of here not solve a mystery"
        w 13"Heh,{w=.3} none taken"
    w 1"The upper floors have a comms room. {w=.3}We could signal for help and call in a chopper to save us"
    if norman_dead == False:
        n 1"Ok [pov] let's check out the boardroom!{w=.3} Are you gonna be alright here Tara?"
    show w at hop
    pause 0.3
    show w at shiver
    pause 0.3
    show w at sink
    "Tara tries to get up, winces, and then sits back down..."
    if vinnie_dead == False:
        v 1"Try not moving!{w=.3} You've already lost a lot of blood I'll take care of this alright?"
        "Vinnie spends a while dressing Tara's wound"
        v 3"Just stay here for now.{w=.3} Don't overwork yourself we've got it under control!"
    w 5"Alright,{w=.3} I trust you to handle this situation. {w=.3}I can't exactly get up, doctor's orders..."

    scene office hall with dissolve
    $ current_room = "office_hall"        
    jump pnc_loop

    label medkit_choice:

            "I find a med kit in one of the top cabinets"

            menu medkit_choice_2_electric_boogalo:
                "Who should I use it on?"
    
                "Me":
                    if vinnie_dead == False:
                        $ sage_health +=2
                        $ medkit_used = True
                        show v 1 with dissolve
                        v "Here [pov] I could help you out with that!"
                        if insanity_level == 0:
                            p 13 "I'm grateful, thank you"
                    else:
                        $ medkit_used = True
                        $ sage_health +=1

                "Norman" if norman_dead == False:
                    if save_tara_1 == True or closet_broken == False:
                        if vinnie_dead == False:
                            $ addNormhealth(1)
                            $ medkit_used = True
                            show v 1 at right with dissolve
                            show n 2 at right2 with dissolve
                            v "Here Norman I could help you out with that!"
                            n "Thank you Vin!"
                        else:
                            $ addNormhealth(1)
                            $ medkit_used = True
                            show n 2 with dissolve
                            n "Neat! {w=.3}Here I could tie the bandages too!"
                            n 3a"..."
                            n 8"The medical equipment reminds me of Vinnie..." 
                    elif closet_broken == True and tara == False:
                        show n 2 with dissolve
                        n "Hey I have an idea!{w=.3} Let's use this for the girl we found in the closet instead!"
                        hide n with dissolve
                        jump medkit_choice_2_electric_boogalo
                
                "Rocky" if rocky_dead == False:
                    if save_tara_1 == True or closet_broken == False:
                        if vinnie_dead == False:
                            $ addRockyhealth(2)
                            $ medkit_used = True
                            show v 19 at right with dissolve
                            show r 5 at right2 with dissolve
                            v "Here Rocky I could help you out with that!"
                            r "I could wrap my own wounds, don't need no help or anything... {w=.5}but I guess I'll let you feel useful for once..."
                        else:
                            $ addRockyhealth(1)
                            $ medkit_used = True
                            show r 7 with dissolve
                            r 7 "I can't use this as well without Vinnie...{w=.5} They would know how to properly do all this medical stuff..."                            
                    elif closet_broken == True and tara == False:
                        show r 1a with dissolve 
                        r "Let's use this on the girl ya dingus!"
                        hide r with dissolve
                        jump medkit_choice_2_electric_boogalo

                "Vinnie" if vinnie_dead == False:
                    if save_tara_1 == True or closet_broken == False:
                        $ addRockyhealth(-1) 
                        $ addVinhealth(2)
                        $ medkit_used = True
                        show v 1 with dissolve 
                        v "Ooo! {w=.3}I'm actually a medical professional in training so I could use this pretty well!"
                    elif closet_broken == True and tara == False:
                        show v 4 with dissolve 
                        v "Let's use this for the girl in the closet instead! {w=.3}I could use some of the supplies without wasting them on her!"
                        hide v with dissolve
                        jump medkit_choice_2_electric_boogalo
                        
                "Leave for now it may be useful later":
                        scene office breakroom with dissolve
                        jump pnc_loop

                "Use on injured woman" if closet_broken == True and tara == False and vinnie_helped_tara == False:
                    $ medkit_for_tara = True
                    jump injured_woman_closet
            scene office breakroom with dissolve
            jump pnc_loop

label word_puzzle:
    scene computer with dissolve
    if word_puzzle_completed == True:
        "The password has already been inputted, I should check the elevator to go to the next floor"
        scene office computer with dissolve
        jump pnc_loop

    "\"Her eyes {color=#f00}_ _ _ _ _ {/color} at the sight of them,\""
    "\"they ravage through the other researchers like {color=#f00}_ _ _ _{/color}s to a flame\""
    "The {color=#f00}_ _ _ _ _ _{/color} is bleak as I grow more weary"
    "Days scramble together the longer she stays"
    if examined_computer == True:
        jump get_password
    else:
        $ examined_computer = True
        if tara == True:
            "This must be what Tara was talking about, {w=.3}we need to fill in the blanks to be able to access the higher floors"
        else:
            "I'm not sure what this does but it must be important if it were hidden behind a wall, {w=.3}we need to fill in the blanks to be able to access the higher floors"
        "The clues to solving this must be hidden around this floor,{w=.3} if I were to look around some more a pattern may emerge from the clues I collect..."
        jump get_password
return


label secret_elevator:

    if word_puzzle_completed == True:
        menu:
            "Continue to the next floor?":
                jump office_floor_ending
            "Keep exploring current floor":
                jump pnc_loop

    else:
        p 14"Looks like another elevator,{w=.3} it won't open no matter how many times I call for it"
        if norman_dead == False:
            show n 1 with dissolve
            n "This has to be the express elevator that leads to the higher floor!{w=.3} If the telecommunications isn't here it should be up there!"
            hide n with dissolve
        if tara == True:
            p 1"Tara said it should be accessible once I crack the code the in the boardroom's false wall"
        else:
            p 1"There has to be some terminal around here to open this"
        jump pnc_loop



label worker_diary:
    if monday == True:
        show black with Dissolve(1.):
            alpha.9
        show text "{color=#f00}{size=+100}{u}MON{/u}{/color}{/size}" with dissolve
        "This has the letters {color=#f00}{u}MON{/u}{/color}. Maybe if I used these letters to craft something else specifically?"
        hide text with dissolve
        hide black with dissolve
    else:
        $ monday = True
        play sound "audio/sfx/page turn.ogg"
        show black with Dissolve(1.):
            alpha.9
        centered "{color=#f00}{u}MON{/u}{/color}-{font=Dudu_Calligraphy.ttf} Sandra Keyes - I'm not too sure what our goal is anymore. Before, it was leasing floors, then that coffee company took over and now we're cooperating with hospitals?{/font}"
        centered "{font=Dudu_Calligraphy.ttf}A lot of patient transfers and faculty being taken to the higher floors... some of them finally explained what was going during the board meeting. SO many crazy words I've never even heard before!{/font}"
        centered "{font=Dudu_Calligraphy.ttf}I thought it was a joke but no one was laughing. Its something about virology...? What the hell could they possibly be doing up there!{/font}"
        centered "{font=Dudu_Calligraphy.ttf}I'm talking to Ashley about this later and we're gonna have a word with the higher ups about this crazy talk!{/font}"
        hide black with dissolve
        play sound "audio/sfx/page turn.ogg"

        p 4"Guess not even THESE employees knew what was going on"

        if rocky_dead == False:
            show r 4a at left with dissolve
            r "Why even expand to something else? You're a coffee business for crying out loud!"
        if vinnie_dead == False:
            show v 2 with dissolve
            v "There's always something going on behind the scenes...{w=.3} ask yourself what your favorite product is; then ask someone who worked on it;{w=.3} then you'll find out its all about the profit, {w=.3}never about the those who bring it to life..."
            v "Worker abuse takes place everywhere because people can get away with it. When was the last time you thought about your cashier's income and how their boss treats them? {w=.3}You don't do you? {w=.3}If we did we wouldn't be here now would we..."
        if norman_dead == False:
            show n 8 at right with dissolve
            n "Jobs should help people with their lives, {w=.3}not take them away..." 
        if vinnie_dead == False:
            v 4"Huh? {w=.3}Also,{w=.3} the date on this is highlighted FURIOUSLY!!{w=.3} is this related to something?"
            hide v 4 with dissolve
        else:
            "Hmm the date on this is highlighted quite furiously,{w=.3} is this related to something?"
    scene office desks with dissolve 
    jump pnc_loop


label worker_email:
    if tuesday_and_thursday == True:
        show black with Dissolve(1.):
                alpha.8
        show text "{color=#f00}{size=+100}{u}TUE{/u}{/color}{/size}, {color=#f00}{size=+100}{u}THU{/u}{/size}{/color}" with dissolve
        "This has the letters {color=#f00}{u}TUE{/u}{/color} and {color=#f00}{u}THU{/u}{/color}. Maybe if I used these letters to craft something else specifically?"
        hide text with dissolve
        hide black with dissolve
    else:
        $ tuesday_and_thursday = True
        play sound "audio/sfx/digi beep.ogg"
        show black with Dissolve(1.):
                alpha.8
        centered "{color=#f00}{u}TUE{/u}{/color}-{font=Dudu_Calligraphy.ttf} Daniel Walsh - Jesus, things have gotten brutal the past few months. Everything's shifted to pure medical research with just a skeleton crew managing the coffee side of their business{/font}"
        centered "{font=Dudu_Calligraphy.ttf} Now there's a work quota we have to meet or else we get \"fired\". All of the sudden these riot gear guys started roaming around the halls like they're patrolling something{/font}"
        centered "{font=Dudu_Calligraphy.ttf}They’re holding way too overkill of equipment for simple security so what are they here for? They seem particularly needed in the higher floors... {/font}"
        centered "{font=Dudu_Calligraphy.ttf}My buddy Charlie couldn't deal with all the changes so he quit last {/font}{color=#f00}{u}THU{/u}{/color}{font=Dudu_Calligraphy.ttf}. He never answer my calls anymore.{/font}"
        centered "{font=Dudu_Calligraphy.ttf}The CEO seemed so nice in passing... but how could he have let this happen? I don't want to work here anymore but I'm scared I'll find out what happened to Charlie if I do...{/font}"
        hide black with dissolve

        p 1"Armoured men? {w=.3}Disappearances?{w=.3} Work quota?{w=.3} Sounds like they didn't have much agency..."
        
        if vinnie_dead == False:
            show v 2 with dissolve
            v "Exactly why you never sign your soul away to a corporate entity. {w=.3}You become another cog in the endless wheel.{w=.3} The cruelest part is,{w=.3} even if you DO know what will happen you still have no choice but to submit"
            v "Most aren't fortunate enough to pick the job they want...{w=.3} \"why don't you just quit?\" {w=.3}Because theres never not strings attached,{w=.3} be it a strike on your record or no income"
    
        p 4"Welcome to hell,{w=.3} your work shift starts now"
   
        if rocky_dead == False:
            show r 7 at left with dissolve
            r "You may think the business you work with would never take advantage of you like others.{w=.3} But the truth is,{w=.3} money comes first" 
            r 1"Whether it be demotions,{w=.3} firings,{w=.3} or write offs. {w=.3}You aren't safe with any type of management.{w=.3} They'll swap their models as they see fit. {w=.3}Profit comes first"
   
        if norman_dead == False:
            show n 8 at right with dissolve
            n "Sounds like you've been through a lot...{w=.3}I- {w=.3}I've never really had to get a job..."

        if vinnie_dead == False and norman_dead == False:
            v 9"It's OK! {w=.3}We still love you,{w=.3} you trust fund baby!!!"
            n 2"You have such a way with words you goofball!"
        "Hmm the dates on this is highlighted quite furiously, {w=.3}is this related to something?"
    scene office board room with dissolve
    jump pnc_loop    


label worker_memo:
    if wednesday_and_friday == True:
        show black with Dissolve(1.):
                alpha.8
        show text "{color=#f00}{size=+100}{u}WED{/u}{/color}{/size}, {color=#f00}{size=+100}{u}FRI{/u}{/size}{/color}" with dissolve
        "This has the letters {color=#f00}{u}WED{/u}{/color} and {color=#f00}{u}FRI{/u}{/color}. Maybe if I used these letters to craft something else specifically?"
        hide text with dissolve
        hide black with dissolve

    else:
        $ wednesday_and_friday = True
        play sound "audio/sfx/page turn.ogg"
        show black with Dissolve(1.):
                alpha.8
        centered "{color=#f00}{u}WED{/u}{/color}{font=Dudu_Calligraphy.ttf}- Ashley Cooper - Ethics Officer :REMINDER TO BELOVED SAMSARA ENTERPRISES EMPLOYEES:{/font}"
        centered "{font=Dudu_Calligraphy.ttf}We've heard your dissatisfaction with a particular conduct we practice here at Samsara! We're a big happy family all in this together so you're happiness is our number one priority!~{/font}"
        centered "{font=Dudu_Calligraphy.ttf}I promise that we have heard you and we'll listen to your words! There will be representatives establishing some new changes around here on {color=#f00}{u}FRI{/u}{/color} so make sure to be here. No matter what. {/font}"
        centered "{font=Dudu_Calligraphy.ttf}:Failure to be appear will result in appropriate action:{/font}"
        hide black with dissolve
        play sound "audio/sfx/page turn.ogg"

        if vinnie_dead == False:
            show v 4 with dissolve
            v 1"Huh?,{w=.3} the dates on this is highlighted FURIOUSLY!! is this related to something?"
        else:
            "Hmm the dates on this is highlighted quite furiously, {w=.3}is this related to something?" 

        p 4"I would NOT like to meet who wrote this in person,{w=.3} seems like a real piece of work"

        if rocky_dead == False:
            show r 2a at left with dissolve
            r "Honeyed words from a seasoned liar!{w=.3} That bitch!" with vpunch

        if vinnie_dead == False:
            v 4"Ah yes the classic ol'{w=.3} \"we love you!\"{w=.3} manipulation tactic B.S."

        if norman_dead == False:
            show n 5 at right with dissolve
            n "The date they were supposed to meet was today!{w=.3} Is that related to how they're all..."
        if vinnie_dead == False:
            v 2"Man, {w=.3}it sucks how people take others for granted, her emotional exploitation on those she sees as{w=.3} \"lower\"{w=.3} than her because of her ranking just shows how insecure she is"
            v "People suffer all because of one person's much needed ego check, {w=.3}why is it that people like that are usually put in charge? {w=.3}Do you HAVE to be a scumbag to reach the top? {w=.3}Because the only way to climb that high is to step on the fingers of others?"
            v 11"I had teen parents and they had no idea how to take care of me and my siblings, we all fended for ourselves while our parents got fucked up at some random party. {w=.3}My older siblings are like our true parents"
            v "Why is it that the rest have to suffer from the sins of the few? {w=.3}As long as CPS sees that you're fed and clean they don't give a shit. {w=.3}Only reason we weren't was from OUR own efforts not our parents"
            v 12"Who came up with that system?{w=.3} They saw abused children and went on with their day. One less paper to fill out,{w=.3} is that all we are to them?"
            v "The water seeps through the cracks in the rules and drowns the rest of us...{w=.3} Why did those responsible not take better care of us?"
            v "My parents mellowed out when they got much older and apologized, {w=.3}but still, {w=.3}it's too little too late..."
            if rocky_dead == False:
                r 7 "Vin..."
            if norman_dead == False:
                n 3a"I'm so sorry Vinnie...."
            menu:
                "It's our duty to point it out,{w=.3} you're on the right track" if insanity_level == 0:
                    p 4"When you see something wrong, {w=.3}don't let them get away with it. {w=.3}It's how the cycle repeats over and over again. {w=.3}They do it because they can, {w=.3}but we won't let them.{w=.3} Right?"
                    v 2"But why should it be our responsibility if someone else messes up?"
                    p 1"It's our responsibility to call it out and make sure no one else suffers as much as we did.{w=.3} If we saw and kept silent, {w=.3}we would be complicit right?{w=.3} It's ok to take the time you need,{w=.3} but make sure it isn't too late"
                    v 11"[pov]... {w=.3}That's...{w=.3} real clever actually... {w=.3}yeah... {w=.3}YEAH!!! Corruption only exists because we let it! {w=.3}Once I get home I'm suing everyone's asses for a drazillion dollars!!!"
                    v 1"I'm gonna boycott this place and yell to this heavens how they mistreated their employees here!{w=.3} Once Samsara of all companies gets in trouble EVERYONE ELSE IS NEXT!!!"
                    $ expose_samsara_together_2 = True
                    if norman_dead == False:
                        "...!"

                "Relax, let's keep going":
                    v 12"...Whatever"

            if rocky_dead == False:
                r 7"Fuck,{w=.3} I'm sorry dude I wasn't there for you sooner. {w=.3}If {w=.3}I- I had known more about you I wouldn't have been so hard on you..."
                v 12"Man,{w=.3} don't even.{w=.3} I was like a child and we didn't even know each other at the time, what were you gonna do as a 9 year old, suplex adults twice your size?"
                v "You couldn't have known plus you had your own shit you were dealing with at the time. You were right to call out my immaturity, I take it too far sometimes. You fixed me..."
                v 11"My {i}harmless{/i} pranks and antics landed me in jail...{w=.3} You convinced me to stop where I did...{w=.3}  Who knows where I would be without you... {w=.5}thanks..."
                r "Vinnie..."
                "Rocky and Vinnie stare at each other before breaking away and taking a few steps in the opposite direction"
                show v at offscreen_right with move
                show r at offscreen_left with move
                show v at offscreen_right with move
                hide r 
            hide v with dissolve
            "They head out the room"
            if norman_dead == False:
                show n 6 at center with move
                n 6"I-{w=.3} I'm in shock,{w=.3} Vinnie told me they had a bad childhood but I didn't know how bad it was"
                n 8"Vinnie... {w=.3}Rocky... {w=.3}they had such a hard life..." 
                if rocky_dead == False:
                    extend " I need to be there for them,{w=.3} It's the least I can do as their friend"
                else:
                    extend " I failed them by not saving Rocky...{w=.3} What kind of friend am I to not be there for them?"
            menu:
                "People can be there for you too":
                    $ norman_affection += 1
                    show n 9 with dissolve
                    n 9"[pov], you're such a good person...{w=.3} I mean that... {w=.3}I'll make sure to let you know if I'm having any doubts...{w=.3} Thank you,{w=.6} for thinking about me"
                "Alright":
                    n "..."
    scene office breakroom with dissolve
    jump pnc_loop

label office_corpses:
    "Various corpses are strewn about, {w=.3}some seem to have been eaten while a few are shredded with bullet holes.{w=.3} I don't understand how they were able to die if they had access to guns..."
    "...{w=.3}Where even are the people with guns if they're not dead in here?"
    jump pnc_loop

label office_floor_ending:
    pause 0.5
    scene office hall with dissolve
    if tara == True:
        if rocky_dead == False:
            "Rocky is carrying Tara on his back"
            show w 14 at left1 with dissolve
            w "Ah, {w=.3}apologies for the inconvenience"
            show r 1 at left with dissolve
            r "Are you kidding me?!?! {w=.3}You're arm is gone!{w=.3} What kind of person would I be if I left you on your own?"
            if vinnie_dead == False:
                show v 18 with dissolve
                v "Hey! {w=.3}Make sure to take care of my patient you blockhead!{w=.3} Don't yell at her!"
                r 4a"I am LITERALLY carrying her right now how is this mistreatment???"
                v 2 4"She can smell the steak and beer on your breath from your late night binge sessions you mangy dog!"
                r 3"I haven't done that in years how are you still holding that against me?!?!"
                w 13"Hahaha!{w=.3} You have quite the friends here [pov]!"

        if rocky_dead == True and vinnie_dead == False:
            show v 2 with dissolve
            v "Are you ok?{w=.3} Can you stand?"
            "Vinnie has Tara lean on their shoulders"
            v 10"I had a friend who could of carried you better, {w=.3}he-{w=.3} he didn't make it..."
            show w 1 at left1 with dissolve
            w 1"Oh, {w=.3}I'm so sorry to hear that... {w=.3}I promise you we will hold whoever is responsible for this accountable"
            v 2 2"...{w=.3}thank you..."

        if rocky_dead and vinnie_dead == True:
            "Norman and I are standing Tara up side from side"
            show w 1 at left1 with dissolve
            w 1"Sorry, {w=.3}for slowing you two down.."
        show n 2 at right2 with dissolve
        n 2"Don't worry!{w=.3} Tara we're all in this together!" 
    if insanity_level == 0:
        p 13"I can't believe we've made it this for guys! {w=.3}We got this!"       
    if closet_broken == True and tara == False:
        show n 8 with dissolve
        n 8"I feel bad for that woman in the closet but,{w=.3} she'll most likely bleed out if we stand her up right now... {w=.3}it's best to wait and we'll come back once we find something to help her" 
    pause 0.5
    stop music
    play sound "audio/sfx/mic.ogg"
    omg "{w=.3}...{w=.5}Stop what you're doing."
    "Out of nowhere a booming voice echoes from the speakers in the ceilings"
    
    if tara == True:
        w 9"F-{w=.3} Father?!?"
        
        if rocky_dead == False:
            "Rocky sets Tara behind a potted plant"
            show w 9 at offscreen_left with move
            hide w 9
            show r 1 at left with move
            r "Here, {w=.3}don't come out no matter what..."
            if vinnie_dead == False:
                v 2"Listen to him Tara,{w=.3} don't make a noise..."

        if rocky_dead == True and vinnie_dead == False:
            "Vinnie hides Tara behind a potted plant"
            show w 9 at offscreen_left with move
            hide w 9
            show v 2 at left with move
            v "Here!{w=.3} Don't make a peep!"

        if rocky_dead and vinnie_dead == True:
            show w 9 at offscreen_left with move
            hide w 9
            show n 6 at left with move
            "Norman and I set Tara down and hide her behind a potted plant"
            n "Don't make a sound Tara..."
        w "...!"

    scene office hall with dissolve
    play sound "audio/sfx/elevator.ogg"
    "I hear the express elevator rumbling as if it were currently in use, {w=.3}it eventually comes to a sudden stop and the doors slide open to reveal..."
    show naut with dissolve
    play sound "audio/sfx/monster-1.ogg"
    play music "audio/music/live or die intro.ogg"
    queue music "audio/music/live or die.ogg"
    "A man in a black armour suit! {w=.3}He's carrying a stun baton and lunges at us!" with hpunch
   
    omg "...{w=.5}Kill them all"

    if tara or closet_broken == True:
        omg "...Get the girl once the rest are dispatched" 

    omg "...Detonate the bomb afterwards"
    show n 5 at left with dissolve
    "It charges at Norman!"
    if norman_has_gun == True and ammo >= 1:
        show n 12 at right with move
        play sound "audio/sfx/shoot.ogg"
        queue sound "audio/sfx/monster-10.ogg"
        $ ammo -= 1
        "He goes for Norman but the latter shoots a bullet straight at the man's face! His helmet protects him but Norman's gun makes it so that he goes for someone else instead!"
        hide n with dissolve
        jump vinnie_v_juggernaut

    else:
        menu:
            "What can I do to help Norman?"

            "I save myself and do nothing!":
                $ addInsanity_level(1)
                $ addNormhealth(-2)
                play sound "audio/sfx/hit.ogg"
                queue sound "audio/sfx/monster-10.ogg"
                n "Unf!" with hpunch
                "Norman is brought down to the floor from the stun baton and isn't getting up..."
                if norman_health == 0:
                    $ addNormhealth(-1)
                    $ norman_office_death = True
                jump vinnie_v_juggernaut
                
            "Push Norman into danger" if insanity_level >= 2 and norman_affection == 0 and tara == False and rocky_dead and vinnie_dead == True:
                $ addNormhealth(-5)
                $ addInsanity_level(99)
                $ norman_secret_death = True
                $ norman_office_death = True
                $ norman_dead = True
                play sound "audio/sfx/hit.ogg"
                queue sound "audio/sfx/monster-10.ogg"
                n "Unf!!" with hpunch
                "I shove Norman so he falters to the ground as the man beats him down, {w=.3}Norman is brought down to the floor from the stun baton and isn't getting up..."
                jump vinnie_v_juggernaut

            "I tell Vinnie to stab the armored man with their knife!" if vinnies_knife == True and vinnie_dead == False and vinnie_office_death == False:
                $ vinnies_knife = False
                play sound "audio/sfx/stab.ogg"
                queue sound "audio/sfx/monster-10.ogg"
                show v 2 at right with moveinright
                v "Got it! I'll save you Norm!" with hpunch
                "Vinnie rushes in front of Norman and penetrates the armored man's protected neck with their butterfly knife,{w=.3} the armored man yanks it out before crushing it with his hands"
                jump vinnie_v_juggernaut
           
            "I tell Vinnie to save Norman!" if vinnies_knife == False and vinnie_dead == False and vinnie_office_death == False: 
                show v 2 at right with moveinright
                play sound "audio/sfx/monster-10.ogg"
                if expose_samsara_together_2 == True:
                    v "I got you Norman!" with hpunch
                    "Vinnie helps Norman with no issue"
                else:
                    $ addVinhealth(-1)
                    v "Got it! I'll save you Norm! OW!"
                    "Vinnie punches the man but gets punched back HARD in the face" with hpunch
                    if vinnie_health == 0:
                        $ vinnie_office_death = True
                jump vinnie_v_juggernaut

            "I headbutt the man with my horns!":
                play sound "audio/sfx/monster-10.ogg"
                if norman_affection >= 2:
                    queue sound "audio/sfx/hit.ogg"
                    "He thinks he could attack Norman?!?{w=.3} I run forward headfirst and stab the man's chest with my horns,{w=.3} I don't care about the pain I need Norman safe!" with hpunch
                    jump vinnie_v_juggernaut
                else:
                    $ sage_health -= 1
                    queue sound "audio/sfx/hit.ogg"
                    "I run forward headfirst and stab the man's chest with my horns,{w=.3} I feel my brain hit the roof of my skull as I deter the man off course" with hpunch
                    if sage_health == 0:
                        jump death_screen             
                    jump vinnie_v_juggernaut
            
            "I shoot the man!" if sage_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                queue sound "audio/sfx/monster-10.ogg"
                "I shoot the man right in his helmet! {w=.3}It blocks the bullet but at least it distracts him from Norman" with hpunch
                jump vinnie_v_juggernaut
            
            "I crowbar the man!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/monster-10.ogg"
                $ crowbar_collected = False
                "I use my crowbar to hit the man over the head,{w=.3} he stumbles in response before grabbing it out of my arms and throwing it across the room" with hpunch
                "The crowbar was lost in the scuffle but at least Norman was protected"
                jump vinnie_v_juggernaut

            "I tell Rocky to save Norman!" if rocky_dead == False:
                play sound "audio/sfx/monster-10.ogg"
                if expose_samsara_together:
                    play sound "audio/sfx/punch.ogg"

                    show r 3a at right with moveinright
                    $ addRockyhealth(-1)
                    "Rocky tries to bear hug the man but gets punched in the chest and knocked to the floor,{w=.3} he's able to recover slightly!" with hpunch
                    r "*cough*{w=.3} *hack* {w=.3}*wheeze*"
                    if rocky_health == 0:
                        $ rocky_office_death = True
                    jump vinnie_v_juggernaut
                elif expose_samsara_together == False and crowbar_collected:
                    play sound "audio/sfx/punch.ogg"
                    show r 3a at right with moveinright
                    "Rocky tries to bear hug the man but gets punched in the chest and knocked to the floor, he looks hurt..."
                    r "*cough*{w=.3} *hack* {w=.3}*wheeze* *wheeze* {w=.3}*sputter*" with hpunch
                    $ addRockyhealth(-2) 

                    if rocky_health == 0:
                        $ rocky_office_death = True

                    jump vinnie_v_juggernaut
                else:
                    play sound "audio/sfx/hit.ogg"
                    $ addRockyhealth(-3)
                    show r 3a at right with moveinright
                    "Rocky tries to bear hug the man but gets punched in the chest and knocked to the floor,{w=.3} he looks pretty hurt and even coughs up blood..."
                    r "*cough*{w=.3} *hack* {w=.3}*cough* *wheeze* *wheeze*{w=.3} *sputter*" with hpunch

                    if rocky_health == 0:
                        $ rocky_office_death = True

                    jump vinnie_v_juggernaut

label vinnie_v_juggernaut:
    if vinnie_dead == True:
        jump rocky_v_juggernaut
    else:
        scene office hall with dissolve
        show naut with dissolve
        show v 2 at left with dissolve
        v "HEY!!! DONUT PUNCHER OVER HERE!!!"
        play sound "audio/sfx/monster-17.ogg"
        "The armored man shoots his head toward Vinnie and makes a run for them!"
        play sound "audio/sfx/short run.ogg"

        menu:
            "What can I do to help Vinnie?"

            "I save myself and do nothing!":
                $ addInsanity_level(1)
                $ addVinhealth(-2)
                play sound "audio/sfx/hit.ogg"
                queue sound "audio/sfx/monster-1.ogg"
                v 2 1"OW DAMN!!!" with hpunch
                "Vinnie is brought down to the floor from the stun baton and isn't getting up..."
                if vinnie_health == 0:
                    $ vinnie_office_death = True
                jump rocky_v_juggernaut
                
            "I tell Vinnie to stab the armored man with their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                play sound "audio/sfx/stab.ogg"

                queue sound "audio/sfx/monster-1.ogg"

                v "TAKE IT YOU FUGLY HO!!!" with hpunch
                "Vinnie dashes forward and penetrates the armored man's protected neck with their butterfly knife, {w=.3}the armored man yanks it out before crushing it with his hands"
                jump rocky_v_juggernaut
           
            "I tell Norman to save Vinnie!" if norman_dead == False and norman_office_death == False:
                $ addNormhealth(-1)
                queue sound "audio/sfx/monster-1.ogg"
                play sound "audio/sfx/punch.ogg"
                show n 5 at right with moveinright
                n "AAAAAAAAAAAHHHHH!!!!" with hpunch
                "Norman blocks Vinnie with his body but takes the strike instead!"
                if norman_health == 0:
                    $ norman_office_death = True
                jump rocky_v_juggernaut

            "I tell Norman to shoot the man!" if norman_has_gun and ammo >= 1 and norman_dead == False and norman_office_death == False:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                queue sound "audio/sfx/monster-1.ogg"

                show n 12 at right with moveinright
                "Norman shoots him in the face, the man is stunned in return!" with hpunch
                jump rocky_v_juggernaut

            "I headbutt the man with my horns!":
                $ sage_health -= 1
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/monster-1.ogg"

                "I run forward headfirst and stab the man's chest with my horns,{w=.3} I feel my brain hit the roof of my skull as I deter the man off course" with hpunch
                
                if sage_health == 0:
                    jump death_screen 

                jump rocky_v_juggernaut
            
            "I shoot the man!" if sage_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                queue sound "audio/sfx/monster-1.ogg"

                "I shoot the man right in his helmet! {w=.3}It blocks the bullet but at least it distracts him from attacking Vinnie" with hpunch
                jump rocky_v_juggernaut

            "I crowbar the man!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/hit.ogg"
                queue sound "audio/sfx/monster-1.ogg"

                $ crowbar_collected = False
                "I use my crowbar to hit the man over the head,{w=.3} he stumbles in response before grabbing it out of my arms and throwing it across the room" with hpunch
                "The crowbar was lost in the scuffle but at least Vinnie was protected"
                jump rocky_v_juggernaut

            "I tell Rocky to save Vinnie!" if rocky_dead == False:
                if expose_samsara_together:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/monster-1.ogg"
                    $ addRockyhealth(-1)
                    show r 3a at right with moveinright
                    r "NOT IF I HAVE ANYTHING TO DO WITH IT YOU CUCK!!!"
                    "Rocky blocks the strike against Vinnie,{w=.3} shrugs it off,{w=.3} and even throws a return punch which knocks the man off guard!" with hpunch
                    if rocky_health == 0:
                        $ rocky_office_death = True
                    jump rocky_v_juggernaut
                elif crowbar_collected:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/monster-1.ogg"
                    "Rocky blocks the man's baton strike with the crowbar but it gets snapped in the process, {w=.3}the man kicks rocky in the groin!" with hpunch
                    r "*wheeze*"
                    v "Rocky! No!"
                    $ addRockyhealth(-2)
                    if rocky_health == 0:
                        $ rocky_office_death = True
                    jump rocky_v_juggernaut

                else:
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/monster-1.ogg"
                    $ addRockyhealth(-3)
                    show r 3a at right with moveinright
                    "Rocky grabs the man's baton strike with his bare hands and gets struck in the process,{w=.3} the man proceeds to strike Rocky over the head with the baton. Rocky's in a terrible state..." with hpunch
                    r "Ugh... {w=.3}*cough*{w=.3} *hack*"
                    if rocky_health == 0:
                        $ rocky_office_death = True
                    jump rocky_v_juggernaut

label rocky_v_juggernaut:
    if rocky_dead == True or rocky_office_death == True:
        jump juggernaut_zombie_aftermath
    else:
        scene office hall with dissolve
        show naut with dissolve
        show r 2a at left with dissolve
        r "YOU ROTTEN BASTARD WHY DON'T YOU PICK ON SOMEONE YOUR OWN SIZE? WHAT ARE YOU WAITING FOR!" with hpunch
        play sound "audio/sfx/zombie-22.ogg"
        queue sound "audio/sfx/short run.ogg"

        menu:
            "While the man dashes furiously towards Rocky,{w=.3} must've really got under his skin, what can I do to help?"
             
            "I save myself and do nothing!":
                $ addInsanity_level(1)
                $ addRockyhealth(-3)

                if rocky_health == 0:
                    $ rocky_office_death = True

                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/Monster_00.ogg"

                show r at offscreen_bottom with move
                r "*retches*" with hpunch
                "Rocky is brought down to the floor from the stun baton and isn't getting back up at all... {w=.3}is he breathing?"
                jump juggernaut_zombie_aftermath

            "I tell Vinnie to stab the armored man with their knife!" if vinnies_knife == True and vinnie_dead == False and vinnie_office_death == False:
                $ vinnies_knife = False
                show v 2 at right with moveinright
                play sound "audio/sfx/stab.ogg"

                queue sound "audio/sfx/Monster_00.ogg"

                v "DIE YOU DICK!!"
                "Vinnie dashes forward and penetrates the armored man's protected neck with their butterfly knife,{w=.3} the armored man yanks it out before crushing it with his hands" with hpunch
                jump juggernaut_zombie_aftermath
            
            "I tell Norman to save Rocky!" if norman_dead == False and norman_office_death == False:
                $ addNormhealth(-1)
                play sound "audio/sfx/hit.ogg"

                queue sound "audio/sfx/Monster_00.ogg"
                if norman_health == 0:
                    $ norman_office_death = True
                show n 2 at right with moveinright
                n "AAAAAAAAAAAHHHHH!!!!" with hpunch
                "Norman blocks Rocky with his body but takes the strike instead!"
                jump juggernaut_zombie_aftermath

            "I tell Norman to shoot the man!" if norman_has_gun and norman_dead == False and norman_office_death == False:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                queue sound "audio/sfx/Monster_00.ogg"

                show n 12 at right with moveinright
                "Norman shoots him in the face, {w=.3}the man is stunned in return!" with hpunch
                jump juggernaut_zombie_aftermath

            "I headbutt the man with my horns!":
                $ sage_health -= 1
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/Monster_00.ogg"

                "I run forward headfirst and stab the man's chest with my horns,{w=.3} I feel my brain hit the roof of my skull as I deter the man off course" with hpunch
                
                if sage_health == 0:
                    jump death_screen

                jump juggernaut_zombie_aftermath
            
            "I shoot the man!" if sage_has_gun == True:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                queue sound "audio/sfx/Monster_00.ogg"

                "I shoot the man right in his helmet! {w=.3}It blocks the bullet but at least it distracts him from attacking Rocky" with hpunch
                jump juggernaut_zombie_aftermath
            
            "I tell Rocky to crowbar the man!" if crowbar_collected == True:
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/Monster_00.ogg"

                if expose_samsara_together == True:
                    "Rocky bashes the man over the head with it, before the man could retaliate Rocky hits him again!" with hpunch
                else:
                    $ crowbar_collected = False
                    "Rocky bashes the man over the head with it but the man grabs it and breaks it in response" with hpunch
                jump juggernaut_zombie_aftermath

            "I tell Vinnie to save Rocky!" if vinnie_dead == False and vinnie_office_death == False:
                play sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/Monster_00.ogg"

                show v 2 at right with moveinright
                if expose_samsara_together_2 == True:
                    v "SUCK ON THIS!!!" with hpunch
                    "Vinnie runs to protect Rocky and does so without a hitch!"
                else:
                    $ addVinhealth(-1)

                    if vinnie_health == 0:
                        $ vinnie_office_death = True
                    
                    "As Vinnie runs to protect Rocky, {w=.3}the armored man grabs Vinnie by the neck before throwing him to the floor" with hpunch
                    v 12"Unnhhhh..."

                jump juggernaut_zombie_aftermath

label juggernaut_zombie_aftermath:
        scene office hall with dissolve
        show naut
        if tara == True:
            show w 6 at left1 with moveinleft
            w "Leave them alone!" with hpunch
            play sound "audio/sfx/zombie attack.ogg"
            show naut at shiver
            "Apparently Tara ran off to grab a desk lamp and clubbed the man over the head with it!"
            hide w with dissolve
        if rocky_dead == True or rocky_office_death == True or rocky_health <= 0:
            pass
        else:
            show r 2 at left with dissolve
            r "HOW MUCH MORE CAN HE POSSIBLY TAKE?"
            hide r with dissolve
        play sound "audio/sfx/short run.ogg"
        "I've had enough of this, I jump onto the man's back and straddle his back, I remove his helmet to reveal..."
        with vpunch
        play sound "audio/sfx/monster-10.ogg"
        show naut 2 at shiver_loop with dissolve
        "A completely decayed face not unlike the zombies! The man groaned in returned and tried reaching for his helmet"

        if tara == True:
            show w 2 at right2 with dissolve
            show w 2 at hop
            "Tara kicks it far away from his grasp"
            hide w with dissolve

        if norman_dead == True or norman_office_death == True or norman_health <= 0:
            pass
        else:
            show n 5 at left with dissolve
            n "He's more focused on his helmet than us!"

        "He's dead set on putting back on that helmet! When his back is turned I realized he's wearing an explosive belt and has the detonator in his side pocket"
        
        if tara == True:
            show w 8 at right2 with dissolve
            w "Now's our chance!"

        if vinnie_dead == True or vinnie_office_death == True or vinnie_health <= 0:
            pass
        else:
            show v 2 at right with dissolve
            v 2"Take the detonator with you! You could explode his ass!"
            show v 16
            extend "{i} pause{/i}"

        scene black with dissolve
        play sound "audio/sfx/short run.ogg"
        if tara == True or rocky_dead == False or norman_dead == False or vinnie_dead == False:
            "I snatch the detonator away from him we all sprint into the express elevator"
        else:
            "I snatch the detonator away from him as I sprint into the express elevator"

        if vinnie_office_death == True:
            $ vinnie_dead = True
            "We're forced to leave Vinnie behind as they lay deceased on the floor"

        if rocky_office_death == True:
            $ rocky_dead = True
            "Rocky is left behind as they're no longer with us, he took quite the beating for us to escape..."
            
        if norman_office_death == True:
            $ norman_dead = True
            "Norman was killed in action, {w=.3}no time to carry him as I run"

            if norman_affection >= 2:
                "Norman, my Norman... {w=.3}no... {w=.3}I will avenge you..."
                "...{w=.3}I loved you..."
            elif insanity_level >= 2:
                "Oh well,{w=.3} no skin off my nose"

            if norman_has_gun:
                "I quickly snatch the gun he had while on my way"

        ##THEY'RE IN THE ELEVATOR NOW!!!!!!
        scene black with dissolve
        pause 0.3
        scene elevator with dissolve
        hide screen character_stats with dissolve
        hide screen ammo_stats with dissolve

        play sound "audio/sfx/elevatording.ogg"
        if tara == True or rocky_dead == False or norman_dead == False or vinnie_dead == False:
            "They urge me to press the button and as soon as I do-"
        else:
            "I press the button and as soon as I do-"
        play sound "audio/sfx/explode.ogg"
        "The elevator rumbles for a bit as is it explodes beneath us... {w=.3}I wonder if it took out the whole floor or not?" with vpunch
        stop music fadeout 1.0
        "..."
        play music "audio/music/Going_Up.mp3"

        if insanity_level >= 1:
            p 4"What a pathetic creature..."
        else:
            p 1"That was certainly quite the experience"

        "It's deadly quiet for a while..."
        label rocky_vinnie_death_reaction:
        if vinnie_office_death == True and rocky_dead == False:
            show r 8 with dissolve
            "Rocky stares absentmindedly at the floor... {w=.3}he must be thinking about Vinnie. {w=.3}I hear him whisper some,{w=.3} I think religious, {w=.3}chant under his breath"
            
            r "Vinnie... {w=.3}Vinnie... {w=.3}you-{w=.3} y-{w=.3} you can-{w=.3}'t {w=.3}be..."
            r "Dear god... {w=.3}what kind of world does this... {w=.3}who would do this?{w=.3} Why them...{w=.3} why me..."
            if norman_dead == False:
                "Norman rubs circles on his back for a bit"
                show n 8 at left with dissolve
                n "It's ok...{w=.3} It's ok... {w=.3}I miss them too... {w=.3}it's ok to cry..."
                "..."
            r "Vinnie I..."
            "Rocky's voice breaks before they quit their attempt at speaking and remain silent"
            if insanity_level >= 1:
                "Maybe they shouldn't have gotten themselves killed then..."
            else:
                "I'm gonna miss Vinnie, {w=.3}their humor, {w=.3}their voice,{w=.3} their spirit to keep us happy..."
            pause 0.3
        
        if rocky_office_death == True and vinnie_dead == False:
            call vinnie_reaction_rocky_death
            
        if tara == True:
            if rocky_office_death or vinnie_office_death or norman_office_death and tara == True:
                show w 2 at right2 with dissolve
                w "I'm so sorry about what happened..."

        if vinnie_dead == False and norman_dead == False and rocky_dead == False:
            show v 3 at right with dissolve
            show v 3 at hop_loop
            v "WE WOOOOOOOOOON!!!!!!!!!!!!{w=.3} YIIIIIIIIIPIIIIIIIIIIIEEEEE!!!!"
            v 2 4"KISS ME ON THE MOUTH ROCKY!!! {w=.3}CARRY ME BRIDAL STYLE!!!"
            show r 3 with dissolve
            if tara == True:
                r "The hell??{w=.3} I'm not carrying you!!! {w=.3}AND TARA!"
                show w 4 at left1 with dissolve
                w 4"They look so excited though! Why don't we swap places?"
                hide w with dissolve
                v 8"DOCTOR'S ORDERS THAT YOU LISTEN TO MY PATIENT'S EVERY DEMAND!!!"
            r "The hell??{w=.3} I'm not carrying you!!!"
            show r at right with move
            show v at offscreen_bottom with move
            hide v
            "Rocky grabs Vinnie's face and squishes it so Vinnie's tongue lolls out before shoving them across the elevator"
            show r at left with move
            r 10"Holy-{w=.3} I thought that was it for us Norman! I didn't think we would make it!"
            n 1"We make an amazing team!"
        
        if norman_dead == False:
            show n 1 with dissolve
            "Norman starts inspecting our wounds to see if it's anything serious"
        
        if norman_office_death == True:
            if vinnie_dead == False:
                show v 2 2 at right with dissolve
                v "Norman... {w=.3}no god no not Norman of all people..."
                if rocky_dead == True:
                    v "First Rocky now this?!?!"
                v "This is too much...{w=.3} I can't...{w=.3} I can't..."

            if rocky_dead == False:
                show r 7 with dissolve
                r "Norman... {w=.3}if you can hear this.. I-{w=.3} I failed you..."
                if vinnie_dead == True:
                    r "Couldn't protect Vinnie...{w=.3} couldn't protect you..."
                r 8"What kind of man am I? {w=.3}Why did I live..."

        if norman_dead == False:
            n 2"Great effort! Great effort!"
            if norman_affection >= 1:
                "Norman inspects me to see if I'm ok"
                if sage_health <= 2:
                    n 3a"Oh no,{w=.3} you look pretty banged up there [pov], are you ok?"
                    if insanity_level >= 1:
                        p 1"Quit fussing"
                    else:
                        p 3"I'm fine, {w=.3}thank you for asking..."
                else:
                    n 1"Glad to see you're ok [pov]!"
                    if insanity_level >= 1:
                        p 2"..."
                    else:
                        p 13"Ditto Norman!"                    

        p 4"What even was that thing? {w=.3}It looked and acted a lot like one of the zombies"
        if tara == True:
            show w 15 at left1 with dissolve
            w 15"I- I have some explaining to do.{w=.3} It's the least I can do...{w=.3} From now on there will be 100 percent honesty from me"
            if rocky_dead == False:
                show r 1
            w "The CEO is my father...{w=.3} He's always been {w=.5}{i}off{/i},{w=.3} doesn't think the same way we do. Imagine a child with a magnifying glass versus an ant colony"
            w 1"The child has no comprehension over the significance of ending one's life.{w=.3} He sees the world revolving around him,{w=.5} and only him,{w=.3} everything else is a prop or asset"
            w "The ants are his plaything and no one can convince him otherwise because ants ARE meaningless in the eyes of others"
            w "There was never anyone to stop him...{w=.3} those that could took advantage of the status he can give them so they chose to ignore it..."
            w "I suppose I was treated well enough, never directly hurt,{w=.3} just sort of...{w=.3} cast to the side.{w=.3} As if I was yet another prop that adds a nice \"family\" man flavor to his public persona"
            w 14"I noticed cracks in his fake personality as I got older, {w=.3}it was only recently that I figured out the full extent.{w=.3} When I confronted him about it,{w=.3} he put me on house arrest so I escaped and infiltrated my way here as an employee"
            w "My plan was to personally confront him in his office while working undercover but, I had no idea he had this plague in mind...{w=.3} I'm sorry for not being truthful, {w=.3}I was trying to figure out the right time to tell you"

            if insanity_level >= 1:
                "This bitch is hiding things from me,{w=.3} she can't be trusted"
            else:
                p 4"It's ok,{w=.3} I understand.{w=.3} What's important is that you're telling now" 
            if vinnie_dead == False:
                show v 11 at right with dissolve
                v 11"Talk about daddy issues girl..."
            if rocky_dead == False:
                r 7"No parent should treat their own family like that, {w=.3}what a degenerate.{w=.3} Keep close to us ok?"
            if norman_dead == False:
                n 8"I'm so sorry to hear that, {w=.3}I can relate to a distant family like that"
            w 14"That \"thing\" down there was specifically sent to retrieve me and kill you,{w=.3} I don't want to endanger you..."
            if insanity_level >= 1:
                "Maybe you'd be better left behind but I can't exactly throw you out right now..."
            p 1"Danger is everywhere here so it doesn't matter if you're gone or not, {w=.3}you're staying"             
            if vinnie_dead == False:
                v 5"MY PATIENT CAN'T LEAVE UNTIL YOU GET YOUR DOCTOR REFERRAL, STAY WITH US TARA!!!"
            if norman_dead == False:
                n 2"Yeah!!! Join us!!"
            if rocky_dead == False:
                r 11"C'mon you've lived this long going alone is a death wish"
            w 12"T- {w=.3}thank you...,{w=.3} the top floor should have access to the rooftop and we could flag a helicopter from there"
        p 4"Hmm the floor this elevator leads to is labelled as a \"laboratory\", well this should be fun..."
        scene elevator with dissolve
        "Time passes"
        pause 0.9
        if norman_dead == False and norman_affection >= 2:
            show n 3a with dissolve
            "Norman scoots very close next to me, almost leaning against my shoulder"
            n 8"Hey [pov]...{w=.3} I'm scared, {w=.3}so scared of dying..."
            if rocky_dead == True:
                n "Rocky's dead..."
            if vinnie_dead == True:
                n "Vinnie's dead..."
            if closet_broken == True and tara == False:
                n "That girl we left behind in the closet is probably dead..."
            n "How much longer do {i}we{/i} have?{w=.3} I-{w=.3} I don't want to die or see anymore dead people...{w=.3} please help me..."
            n "I'm so afraid of being seen as weak...{w=.3} because pretending to have it under control is all I have...{w=.3} I can't EVER show myself because the people who rely on me will see me as the fraud I am..."
            menu:
                "You're no fraud {i}especially{/i} to {i}me{/i}":
                    $ norman_affection +=1
                    "I wrap Norman in a tight embrace and hold him closer"
                    show n 9 with dissolve
                    n "[pov]...{w=.3} [pov]..."
                    "He only now starts hugging back,{w=.3} I think I can hear his tail wag"
                    n 4"Haahaa why can't this elevator last a little bit longer?"
                    p 9"I wish it did too..."
                    pause 0.3 
                    "We eventually unwrap our arms around each other but continue to hold hands"

                    if vinnie_dead == False and rocky_dead == False:
                        show v 2 2 at right with dissolve
                        show r 1 at left with dissolve
                        "Vinnie and Rocky are off in the corner pretending not to look at us while whispering into each other's ears"
                        v 2 2"*sniffle*{w=.3} *sniffle*{w=.3} Our lil' Normie and [pov] are becoming big grown muscular 6'9 men right before our very eyes... {w=.3}They grow up so fast I'M NOT READY TO LET THEM LEAVE THE NEST YET!! {w=.3}WAAAAAAA!!!!{w=.3} HOLD ME ROCKY!!!"
                        r 3"Stop it you're embarrassing them! If you don't shut your hag mouth you're gonna scare them away from each other! {w=.3}I'm personally very glad to see Norman and [pov] so happy,{w=.3} I've never seen either so ecstatic before"
                        v "*hic*{w=.6} I am too..."

                    if vinnie_dead == True and rocky_dead == False:
                        show r 6 at left with dissolve
                        r "I'm proud of two,{w=.3} truly, {w=.3}you have my blessing for whatever that's worth. {w=.3}Vinnie also would be cool with it, {w=.3}learn from their and my mistakes..."
                    
                    if vinnie_dead == False and rocky_dead == True:
                        show v 10 at right with dissolve
                        v "It warms my heart to see you two be together.{w=.3} Rocky also would approve,{w=.3} make sure never to let go of each other like we did..."
                    
                    if tara == True:
                        show w 13 at right2 with dissolve
                        "Tara gives a thumbs up and wink from across the elevator"
                        
                "Just forget about it":
                    pause 0.5
                    n 6"...{w=.3}I guess it can't be a problem if It's not acknowledged..."
        jump lab_floor_3

        return

#BRADLEYS WORD SCRAMBLE PUZZLE

#BRADLEY MESSAGE
#So an idea for a puzzle I had was like trying to figure out the missing word through the given letters so the test message I made was:
#"Her eyes      at the sight of them,
#they ravage through the other researchers like    s to a flame

#(Fuck I’m out of ideas pretend there's a cool line here)     MAYBE THE NEXT LINE?? _
#"The future is bleak as I grow more weary"

#Days scramble together the longer she stays"
#Letters: MON TUE WED THU FRI
#Then the missing words/the passcode would be: WIDEN, MOTH, and FUTURE

label get_password:
    $ renpy.notify("Use the keyboard to type, make sure each word is spaced from one another and entered in the order they are read")
    $ password_input = renpy.input("What's the password?", length = 25)

    if password_input == password:
        jump correct_password
    if password_input == password2:
        jump correct_password

    if password_input == password3:
        jump correct_password
    if password_input == password4:
        jump correct_password

    if password_input == password5:
        jump correct_password

    if password_input == password6:
        jump correct_password
        
    if password_input == password7:
        jump correct_password

    if password_input == password8:
        jump correct_password

    if password_input == password9:
        jump correct_password
        
    if password_input == password10:
        jump correct_password

    if password_input == password11:
        jump correct_password

    if password_input == password12:
        jump correct_password
        
    if password_input == password13:
        jump correct_password

    if password_input == password14:
        jump correct_password

    if password_input == password15:
        jump correct_password
        
    if password_input == password16:
        jump correct_password

    else:
        jump wrong_password
    return

label correct_password:
    $ word_puzzle_completed = True
    play sound "audio/sfx/correct beep.ogg"
    "{size=*1}{color=#15ff00}EXPRESS ELEVATOR ACCESS GRANTED{/color}{/size}"
    p 15"That was it! That opened up another way for us to go! I should check the elevator here now!"

    if norman_dead == False:
        n "Great job team us! Woo Woo!"
    if vinnie_dead == False:
        v "Well that was tedious!"
    if rocky_dead == False:
        r "Yeah! We got this team! Nice job [pov]!"
    if tara == True:
        p 4"Let's go get Tara and be on our way"

    menu:

        "Continue to the next floor!":
            pass

        "Let's explore around this floor more":
            scene office computer with dissolve
            jump pnc_loop

    scene black with dissolve
    if norman_dead and vinnie_dead and rocky_dead == True:
        "I make my way towards the express elevator the computer said"
    else:
        "We make our way towards the express elevator the computer said"
    jump office_floor_ending
    return

label wrong_password:
    $ password_attempts += 1
    if password_attempts >= 20:
        p 7"I CAN'T TAKE IT ANYMORE!!!!!" with hpunch
        play sound "audio/sfx/zap.ogg"
        "I SMASH THE COMPUTER KEYS OVER AND OVER AGAIN UNTIL EVENTUALLY I GET THE CORRECT ANSWER" with hpunch
        jump correct_password
    else:
        play sound "audio/sfx/wrong beep.ogg"
        "{size=*1}{color=#f00}PASSWORD INCORRECT{/color}{/size}"
        "{size=*1}{color=#f00}ONE WORD HINT: Unscramble{/color}{/size}"
        if vinnie_dead == False:
            v "Hol up! I found a sticky note underneath the desk! It says... days of week?"
            v "Dats gotta be something with the computer right?"
        hide screen input_pw_button
        scene office computer with dissolve
    jump pnc_loop
    return

screen input_pw_button():
    textbutton "Click here to input the password.":
        align (0.5,0.5)
        text_color "#ff0000"
        action [Jump("get_password"), Return()]