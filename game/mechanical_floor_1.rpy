

#items
default crowbar_collected = False
default worker_key_collect = False
default vinnies_knife = True

#notes
default worker_journal_1_collect = False
default worker_journal_2_collect = False
default worker_journal_3_collect = False

#examinations
default examined_HVAC_machine = False

#relationships
default expose_samsara_together = False
default vinnie_body_carried = False
#who has gun?
default norman_has_gun = True
default vinnie_has_gun = False
default rocky_has_gun = False
default sage_has_gun = False

#norman looking for HVAC
default checked_hallway = False
default checked_starting = False
default checked_elevator = False
default checked_ramp = False

##INTRO
label mechanical_floor_1:
    scene fire escape with dissolve
    show black with Dissolve(1.):
        alpha.6
    "My heart beats as I march upwards, {w=.3}would we really be able to restore the power?{w=.3} Are the people here even okay?{w=.3} Would we really make it out of here?"
    hide black with dissolve

    n "Hey [pov]..."

    if norman_affection >= 0:
        n "I know you're not 100 percent on board with this but,{w=.3} please trust in me..."
        n "I'm just as afraid of you...{w=.3} I just put on a front because I don't want the others seeing how weak I really am..."
        n "Please...{w=.3} I- {w=.3}WE- won't let anything bad happen to you...{w=.3} I promise..."
    else:
        n "Thank you for backing me up earlier [pov]..."
        n "To be honest, {w=.3}I'm not sure about this myself, {w=.3}I'm glad to know I have someone to rely on..."
        n "You're someone I can trust... {w=.3} sometimes it feels like I can't really open up because I don't want to worry anyone..."
        n "I can't let them know that... {w=.3}I-{w=.3} don't really know what I'm doing..."
        n "Don't get it wrong! I'm always glad to help someone out it's like someone needs me... {w=.3}and hears me..."
        n "But, {w=.3}it's nice to have someone like that for me too..."
    n "\"Your true family is the one who choose and accept one another\"...{w=.3} That's what you said right?"
    "Norman remembered my poem from class on the presentation day..."
    if norman_affection >=0:
        p "..."
        p "Norman, {w=.3}of course I'll be there..."
        p "Don't worry, {w=.3}we ALL got your back on this..."
        p "Just look how far you've gotten us already..."
        n "...!"
        "Norman turns his head away sharply... {w=.3}I've never seen him this flustered... {w=.3}like he said,{w=.3} he always has to put on a perfect front..."
        "I swear Norman I'll ease your burdens... {w=.3}I'll let everyone else know so we can all be there for each other... {w=.3}In, {w=.3}fact we're already on the first step..."
    else:
        "..."

    pause 0.3

    scene mech room 1 with dissolve

    $ renpy.notify("Remember to save often...")
    "Here we are,{w=.3} the room is lined with pipes and exposed machinery, {w=.3}it feels humid and I can almost taste the dust in the air... {w=.3}why would they not have windows here?"
    n "It's hard to see..."
    p "That's right Golden Retrievers can't see as well in the dark,{w=.3} would it be better if someone else had the gun?"
    menu:
        n "Ok!{w=.3} But who?"

        "I'll take it, Pygmy Goats can see well in the dark":
            $ sage_has_gun = True
            $ norman_has_gun = False
            jump gun_check

        "Vinnie, Opossums have perfect night vision":
            $ vinnie_has_gun = True
            $ norman_has_gun = False
            v "Wow!{w=.3} Uh... {w=.3}o- {w=.3}ok not who I would choose but sure!{w=.3} I can dual wield my knife and gun! ENEMIES BEWARE!"
            if rocky_dead == False:
                r "Why not me?{w=.3} I DO NOT trust Vinnie with a gun..."
                v "I told you once that it's apart of Opossum culture to eat the smallest of their young and you believed me..."
                v "Why would I trust someone like that with a loaded weapon?"
                r "I uh,{w=.3} didn't want to judge cultures..."
                v "Exactly another reason if you think eating children is a valid thing to just do..."
            else:
                v "*sigh* Rocky with his Maned Wolf night vision and sturdiness would've been a better candidate..."
            jump gun_check

        "Rocky, Maned-wolves are nocturnal hunters" if rocky_dead == False:
            $ rocky_has_gun = True
            $ norman_has_gun = False
            r "Got it,{w=.3} I promise you won't regret this"
            v "Meh, {w=.3}I wouldn't trust someone who takes conspiracy theories as fact"
            r "... {w=.3}The chem-trails... {w=.3}I know it's in the chem-trails..."
            v "*sigh*{w=.3} guess this is our best option... {w=.3}I'm scared of guns..."
            jump gun_check

        "Never mind, just hang on to it Norman":
            n "Ok!"
            v "Yeah probably best for the person with the most training to keep it..."
            jump gun_check
     
     
label gun_check:

    if norman_has_gun == False:
        n "Here! {w=.2}Just flick this here to release the safety, {w=.3}remember to breathe slowly to aim for the head better,{w=.1} and press here to shoot!"
        if sage_has_gun == True:
            $ renpy.notify("You recieved Norman's Gun!")

    $ current_room = "mech_floor_main_room_1" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop
    
### MECHANICAL_FLOOR_1 PUZZLE


#MECH ROOM 
label mech_floor_main_room_1:
    window hide diss
    scene mech room 1 with dissolve
    $ current_room = "mech_floor_main_room_1"
    jump pnc_loop

label mech_floor_main_room_2:
    window hide diss
    scene mech room 2 with dissolve
    $ current_room = "mech_floor_main_room_2"
    jump pnc_loop

label mech_hallway:
    window hide diss
    scene mech hall with dissolve
    $ current_room = "mech_hallway"
    jump pnc_loop

label mech_hallway_left:
    window hide diss
    scene mech jacket with dissolve
    $ current_room = "mech_hallway_left"
    jump pnc_loop

label mech_hallway_right:
    window hide diss
    scene mech bed with dissolve
    $ current_room = "mech_hallway_right"
    jump pnc_loop


    #Examine locked ladder to upper ramp
    label mech_ladder:
        if  worker_key_collect == True:

            $ pnc_flags["crowbar_found"] = True
            
            $ crowbar_collected = True
            "The key fits perfectly as the padlock falls off"
            p "Hmm I'm the smallest so my weight shouldn't mess with the under constructed platform as much"
            v "Hey! You actually should be thankful for being as light as a feather for once!"
            if rocky_dead == False:
                r "You're one to talk string bean..."
            "I steady myself on top of the elevated platform and reach out for the crowbar"
            p "Got it!"
            n "Yay! Good Job [pov]!"

            if rocky_dead == False:
                if insanity_level >= 0:
                    "I throw the crowbar down to Rocky as I descend the ladder"
                else: 
                    "I throw the crowbar down to Rocky as a thought hits me"
                    "This is a stupid idea but worth a shot..."
                    p "Hey! Rocky! Catch THIS!"
                    r "What? Oh! OOF!"
                    "I jumped off the raised platform straight into Rocky's arms as he set down the crowbar to replace me in his arms instead"
                    r "What the hell made you think of doing that?!?!"
                    p "...Hmm intrusive thoughts?"
                    v "HAHAHAHAHAHA THATS HI-LARIOUSSS! JUST STAY IN ROCKY'S ARMS LIKE THAT! YOU LOOK LIKE YOU COULD BE HIS NEWBORN OR SOMETHING HAHAHAHA!"
                if norman_affection >= 0:
                    n "...Haaaaa... yeahhhh..."
                "Rocky sets me down as we continue our search"
            else:
                if norman_affection >= 0:
                    "Hmmm I wonder if HE could catch me..."
                    p "Geronimo!"
                    n "WOAH WOAH WOAH!"
                    "I fall on top of Norman, making him break my fall with his body as he lays on the ground"
                    n "[pov]! What was that for?!?!"
                    p "Hmm I dunno honestly..."
                    "Norman looks flustered as ever when I lock eyes with him while pinning myself above him"
                    v "JEEZUZ H CHRISTMAS GET A ROOM YOU TWO!!! NEVER THOUGHT {i}I'D{/i} BE THE THIRD WHEEL!"
                else:
                    "I throw the crowbar down to Vinnie and Norman who stumble to catch it as I descend down the ladder, I pick it up back up"
        else:
            p "The ladder is locked behind a padlock..."
            if rocky_dead == False:
                r "Workers usually have a key to this type of stuff if only we could find someone with it..."
        jump pnc_loop




#POINT AND CLICK LABELS

    #label mech_stairs:
        #"Just the fire exit from where we came from..."
        #if rocky_dead == False:
            #r "Really,{w=.3} you wanna go back already?"
        #v "Jeez!{w=.3} Don't just give up now! {w=.3}Look at me!{w=.3} If I can handle it so can y-{w=.3}you!"
        #show vinnie at shiver_loop with dissolve
        #"Vinnie says as they shiver uncontrollably"
        #hide vinnie with dissolve

        #n "It's okay [pov]... {w=.3}remember what I told you?"
        #jump pnc_loop


    #toggable image button when you get worker key
    label mech_crowbar:
        
        p "That crowbar up there would be great at smashing stuff in..."
        if rocky_dead == False:
            r "Looks like they were installing a higher level here. {w=.3}They never got the chance to finish it..."
        v "Woah it seem's pretty flimsy dunno about going up there or not... "
        jump pnc_loop
    


    #examine HVAC machine
    label hvac:
        if examined_HVAC_machine == True:
            "Just an HVAC, nothing of use..."

        if rocky_dead == False and examined_HVAC_machine == False:
            $ examined_HVAC_machine == True
            r "This here is an HVAC, stands, for heating, ventilation, and air conditioning. {w=.3}Used to work on them back when I worked odd jobs for neighbors..."
            r "Looks like it's not on right now...{w=.3} I don't know what that means for long term but for now we should be fine"
            v "Looks like you're blue collarness background has finally come to use!"
            r "You've never worked a day in your life{w=.3} {i}trust fund baby{/i}"
            v "But I'm {i}your{/i} trust fund baby...{w=.3} I can be your sugar daddy too with all that supposed trust fund if you want!"
            #show rocky blush
            r "...!"

        if rocky_dead == True and examined_HVAC_machine == False:
            $ examined_HVAC_machine == True
            n "I think this is an HVAC machine? I doubt it would help us even with power"
            v "*sigh* Rocky is experienced with mechanical stuff like this he worked plenty of odd jobs like that.. he would have been so useful here..."
            "Guess it's an HVAC"

        jump pnc_loop

    #examine work desk
    ## make this a toggleable imagebutton
    label mech_desk:
        "Looks like a personal journal, {w=.3}some of the pages have been ripped out..."
        $ worker_journal_1_collect = True
        play sound "audio/sfx/page turn.ogg"
        show black with Dissolve(1.):
                alpha.6
        centered "{font=Halogen.ttf}PROPERTY OF: Luis Garcia{/font}"
        centered "{font=Halogen.ttf}August 27- When I first started working here in Lucian's tower I was but a wee lad o'17 that came here with nothin but the clothes on his back{/font}"
        centered "{font=Halogen.ttf}The younger workers nowadays don't even know the original name! They just assumin' they always owned the place. Samsara made this fine building that kickstarted beginning businesses into just another one of their extravagant advertisements!{/font}"
        centered "{font=Halogen.ttf}Those kids even dismiss the fact that Samsara make local hospitals gouge their prices, steal their resources, and give out their patient medical records to them. I wonder who made that seem like a hoax to all the common folk? I have no idea what they want with medical records of all things... {/font}"
        centered "{font=Halogen.ttf}What resource could you want from a hospital besides medical equipment anyways?!?! The company is all types of wrong if they could do that and get away with it, must have some deal with the government to let them do that...{/font}"
        centered "{font=Halogen.ttf}They bring in the wrong crowds now... Before it was fresh faced people who wanted to change the world for the betta! Now it something 'bout \"biotech\" or whateva the hell they call it. Sounds like a load of horseshit from me!(YEAH YOU HEARD ME CORPORATE){/font}"
        centered "{font=Halogen.ttf}They had us expand the tower immensely for their more private businesses when they first bought the place out; had me sign an NDA and everything! Didn't let us know what exactly the floors were for damn do they take a helluva lot electricity.{/font}"
        centered "{font=Halogen.ttf}Those bastards took the money required to power them out of our paychecks! Not to mention they treat us like trash! I've been working here for 47 damn years! Like hell am I gonna let them get away with this! I been starting a union with us mistreated workers... I'll teach them to mess with us...{/font}"
        hide black with dissolve
        play sound "audio/sfx/page turn.ogg"
        #$ renpy.notify("Worker's Journal Entry #1 has been added to Notes!")

        if rocky_dead == False:

            r "This is horrible, just fucking disgusting. My MOM'S been forced into paying for those ridiculous prices!"
            r "I've sacrificed my entire LIFE into paying them! I've never been able to enjoy affording something because the guilt of my mom not being able to kills me as well"
            r "My dad worked my entire childhood just to keep her alive! Imagine that! Being forced to give out all your money to keep your loved one trapped in a fucking chamber where they DIE if you can't pay"
            r "No free-time for us, no family trips, no nice clothing, barely enough food to have enough energy to work the rest of the day!"
            r "We're still working our asses of! He never got to enjoy retirement! My family and others sacrificed all for a CEO's 47th trip to the Bahamas!"
            v "Rocky..."
            n "..."

            menu:
                "Now's your chance to fix it":
                    $ expose_samsara_together = True
                    r "Huh?"
                    p "Well, the business is literally going under armageddon... so what better chance than now to expose them!"
                    p "We could find evidence of their wrongdoings while going through the building and find more people in here who also want to expose them"
                    p "The apocalypse is the perfect opportunity for people who bend the law since it doesn't exist right now"
                    p "They have nothing to take advantage of anymore, and once this comes out to the public they won't have anywhere to hide"
                    n "[pov]..."
                    v "...{w=.3}That's the longest time I've heard you talk..."
                    r "...{w=.3}You're right! These fuckers are gonna get what's coming to them!"
                    r "You guys will support me in fighting them after this right?!"
                    p "Of course!"
                    v "To the end"
                    n "I'm already stashing the documents!"
                    r "Haha! Thank you guys! You're the bestest friends I could have asked for..."
                    r "I wish... {w=.3}I had met you all sooner...{w=.3} then things wouldn't have been so hard on me..."
                
                "Let's keep searching":
                    r "..."
                    r "Fine..."
                    r "{w=.3}I hope every person who allowed this was devoured alive by those monsters..."
                
            v "Rocky...{w=.3} I'm so sorry... I-{w=.3}... {w=.3}It's my fault for...{w=.3} making you care for my immature ass..."
            v "If I wasn't so stupid back then... {w=.3}I could have worked as well to help you out... "
            v "All those damn pranks I pulled on people and police... {w=.3}and the times of me making you do some dumbass shit with me for fun... {w=.3}All just for my selfishness..."
            r "..."
            r "...{w=.3}Don't say that.... {w=.3}you're one of the few people who {i}have{/i} been helping me out... {w=.3}my whole life..."
            r "The few chances I did get of free time. {w=.3}I didn't even know how to relax properly without thinking of a missed opportunity for working..."
            r "You made me think of something besides my own failures...{w=.3} I felt... {w=.3}alive for those moments with you..."
            r "Like I actually existed for something that wasn't a job..."
            v "...!"
            "Vinnie looks away,{w=.3} I think I spot a tear?{w=.3} Hard to tell in the dark..."
            if expose_samsara_together == True:
                r "Norman. {w=.3}[pov], {w=.3}that goes for you too. {w=.3}I love you guys..."
            r "Anyways, {w=.3}let's stop sulking,{w=.3} we got a job to do!"
            "Rocky steps further away by himself as Vinnie waits around in the hallway stares at his back"
        else:
            v "Ahh the wonders of a capitalist empire... we should be so thankful! I wonder what Rock would have thought of this... his family struggled with the healthcare system..."

        n "I never knew how deep Rocky's money problems went...{w=.3} Vinnie knew him better than I did"
        n "They were childhood friends you know...{w=.3} They had some type of falling and didn't meet again til college,{w=.3} I was the who convinced Rocky to see his childhood friend again when we first met"
        if rocky_dead == False:
            n "I don't think Vinnie and Rocky have been that honest with each other in a while..."
            n "I'm glad they have each other in their lives, {w=.3}they work well together no?"
        else:
            n "They worked so well together... {w=.3}I'm glad Rocky at least got to meet them before this all happened... they belonged together..."
            
        menu:
            "I'm glad I have you like they have each other":
                $ norman_affection += 1
                #show norman blush
                n "...!"
                n "[pov]... {w=.3}I'm glad to have you too..."
                n "You're a good... friend [pov],{w=.3} that means something...{w=.3} remember?"
                p "I never forgot."
                n "..."

            "Only true friends think like you do":
                n "Awww don't forget you're my friend too!"
                p "Thank you.{w=.3} Sometimes I'ts just that I feel like an outsider here..."
                n "You're no outsider... {w=.5}to me..."

        jump pnc_loop
    

    #worker key hidden in worker's coat
    #toggable imagebutton
    label mech_left_hall_jacket:
        "Looks like a large worn out worker's jacket,{w=.3} I check the pockets to see if there's anything..."
        "...! {w=.3}I feel a key in one of the pockets!"
        $ worker_key_collect = True
        p "Guys look!"
        if rocky_dead == False:
            r "That's a padlock key,{w=.3} you can tell from how small it is and the notches"
            n "Impressive! {w=.3}How did you know that!"
            r "Used to work in a warehouse and they had me lock up all sorts of stuff similar to this..."
        else:
            v "Hmm probably a padlock key... could tell from my years worth of stealing shit from faculty..."
        $ renpy.notify("Padlock key has been added to inventory!")
        jump pnc_loop
    

    #worker journal scrap 2
    ## make this a toggleable imagebutton
    label mech_right_hall_bed:
        "I pick up the loose paper scrap from the mattress"
        $ worker_journal_2_collect = True
        play sound "audio/sfx/page turn.ogg"
        show black with Dissolve(1.):
                alpha.6
        centered "{font=Halogen.ttf}September 2- Well, the union idea was a complete failure. The posse I gathered up marched straight to the head office demanding a raise and to be respected.{/font}"
        centered "{font=Halogen.ttf}When we listed off all our demands we were met with a full minute of deafening silence, then try to trick thinkin' I'm so starry-eyed youngin' with their \"Thank you for being honest with us, your concerns will be met accordingly\" B.S.!{/font}"
        centered "{font=Halogen.ttf}I've been working longer than you've been wiping your own ass boy! Don't toy with me! The workers and I rioted outside with signs in the main lobby until shouting and exposing our mistreatment until...{/font}"
        centered "{font=Halogen.ttf}Some... men in black body armour showed up, evacuated all civilians from the premises and set up a mile wide perimeter preventing anyone from seeing us... and then started just... beating us with riot batons and pepper spray{/font}"
        centered "{font=Halogen.ttf}Even when we surrendered they just kept going. I blacked out and when I woke up, I was in a bed. Some person in a suit said that I was under law to stay in these quarters and be restricted to this buildiong for the forseeable future{/font}"
        centered "{font=Halogen.ttf}They implemented some new system where employees are rewarded now for reporting any sign of dissatisfaction with their job and disciplined for not doing so... God, I still don't where some of my long time friends are for refusing to surrender...{/font}"
        centered "{font=Halogen.ttf}I'm scared to even write anymore... What if someone finds it? I have to get out here...{/font}"
        hide black with dissolve
        play sound "audio/sfx/page turn.ogg"
        #$ renpy.notify("Worker's Journal Entry #2 has been added to Notes!")
        if rocky_dead == False:
            r "How could they mistreat their workers like that?!?{w=.3} Don't they know how hard it is for some people?"
        v "Yeah, pretty fucked up how the system's just stacked against lower wage workers, {w=.3}people who claim there isn't a class system are total dumbasses when shit like this happens..."
        jump pnc_loop


    #Elevator imagebutton
    label mech_elevator:
        
    if rocky_dead == False:
        r "This is the elevator, won't turn on unless the power's on..."
    else:
        p "The elevator won't work without power"
    
    n "This is why we practice and respect the fire safety drill people!"
    v "NEEEEERRRDD!!!!"

    if norman_affection >= 0:
        p "He's my nerd..."
        v "...?"
        p "...!"
        p "OUR nerd..."
        "I'm pretty sure Norman was out of earshot for that one... {w=.3}too busy guiding himself on the walls..."
    else:
        p "He's our nerd..."
        v "Meh, {w=.3}I {i}GUESS{/i} we'll keep him..."
    
    jump pnc_loop
    

    #corpse with note
    label mech_corpse:
    $ pnc_flags["vent_unlocked"] = True
    v "OH MY FUCKING GOD IT'S A DEAD BODY! SHOOT IT! IT MIGHT BE A ZOMBIE!!!"
    if vinnie_has_gun == True:
        v "Oh hot damn I'm the one with the gun!"
    n "...{w=.3}I'm preeeeeetty sure he isn't coming back... {w=.3}wouldn't he have been roaming around here?"
    p "Hmm, {w=.3}true..."
    "I step forward and start rummaging through the bodies pockets..."
    if insanity_level >= 1:
        "Useless pile of meat..."
    else:
        "Sorry, but this is necessary..."
    v "DUUUUUDEE YOU CAN'T MAKE THIS SHIT UP!!!!!"

    if rocky_dead == False:
        r "You're braver than I thought..."
    
    n "Now that's what I call thorough!"
    "I find a hastily written scrap of paper in his hand"
    $ worker_journal_3_collect = True
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
        alpha.6
    centered "{font=Halogen.ttf}October(?) something...- Been here for who knows how long... They keep me cooped up here to set an example for the others...{/font}"
    centered "{font=Halogen.ttf}Conditions only got worse... it's a dog-eat-dog world out here now... men selling out their friend for a raise... never thought I'd see the day...{/font}"
    centered "{font=Halogen.ttf}The kids here turned from desperate for a job to piranha overnight... never thought I'd miss their smartass mouths until now...{/font}"
    centered "{font=Halogen.ttf}The workers have been getting taken more and more frequently... It's just me and a skeleton crew now... this one kid... early 20's maybe? Named Lucas been scaring me...{/font}"
    centered "{font=Halogen.ttf}He was a chef here... got called higher up to deliver private food to a V.I.P and I guess he saw something he wasn't supposed to see... forced him to be locked up here like me... I gave him my quarters while I sleep on the desk...{/font}"
    centered "{font=Halogen.ttf}Keeps ranting and raving about some monster... they must'a knocked his head up real bad to do this... he locked himself in the electric generator... said monsters can't get him there...{/font}"
    centered "{font=Halogen.ttf}Hasn't eaten in days... I try to force him to but he locked me out. I'm trying to break my way in there but I don't know if I have the strength anymore. He honestly might be better off in there. No one to force him to do his required hours{/font}"
    centered "{font=Halogen.ttf}I'm gonna save us kid. Ol' Luis will get ya outta here Lucas! And everyone else too, you're just being forced to by a broken system...{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"
    #$ renpy.notify("Worker's Journal Entry #3 has been added to Notes!")
    "..."
    "Norman approaches the body closer with me and notices something..."
    n "...{w=.3}The back of his head... {w=.3}It already has a bullet hole in it? {w=.3}Who did... {w=.3}that..."
    p "Some people just can't handle it maybe... {w=.3}he... {w=.3}you know..."
    v "Or the one crazy guy he was talking about..."

    if rocky_dead == False:
        r "Luis was a good man,{w=.3} I bet he would have gotten everyone out if he had more time..."
           
        if expose_samsara_together == True:
            r "We already decided on exposing this place! We'll pick up where you left off Luis!"
            v "Big thankies Luis!~{w=.3} I will make you internet famous so the world will remember your name!"
            n "We won't let your wish be in vain Luis!"
            if insanity_level >= 0:
                "...{w=.3}how hopeless"
            else: 
                p "I won't forget you Luis."

    jump pnc_loop


    #ELECTRIC GENERATOR DOOR IMAGE BUTTON IS IMPOSSIBLE TO GO THROUGH
    label mech_electric_door:
    "I peek through the door's tiny window and see a decomposing corpse in front of what looks like a machine"
    v "It's impossible to get through this door without the key... "

    if worker_journal_3_collect:
        "That must be Lucas..."

    if rocky_dead == False and crowbar_collected == True: 
        v "This door is locked! Hey meathead! Use your muscle gut for something good for once!"
        r "...{w=.3}I'll just pretend the door is your face!"
        "Rocky tries smashing the door and it's window in,{w=.3} but it won't budge..."
        r "*huff* {w=.3}*huff*"
        n "Don't worry Rocky! It was a good effort!"

    if rocky_dead and crowbar_collected:
        "I attempt to use the crowbar,{w=.3} but it's not use..."
        n "Don't worry [pov]! It was a good effort!"

    if worker_journal_3_collect:
        n "Didn't the note say there was another way in?"

    jump pnc_loop


    #ELECTRIC GENERATOR VENT
    #toggable image buttons that only appears if you got the worker journal 3
    label mech_vent:
        p "This vent has to be the alternative path the note was talking about"
        v "How do we get in though?"
        n "It seems real small... {w=.3}I think [pov] might be the only one who fits..."

        if rocky_dead == False:

            if expose_samsara_together == True:
                r "I got this! Watch and learn!{w=.3} I'll get us all outta here!"

                if crowbar_collected == True:
                    "Rocky enthusiastically crowbars the vent in repeatedly"
                else:
                    "Rocky enthusiastically kicks the vent in repeatedly"

                if insanity_level >= 0:
                    v "Woo Woo!{w=.3} You got this Rocky!"
                    n "You can do it!"
                    jump mechanical_floor_escape
                else:
                    p "You're mom is waiting on us!{w=.3} She's chilling in her room just knowing that Rocky the great is on his way!"
                    r "YARGHH!!!"
                    p "C'mon guys help me motivate Rocky!"
                    v "Uh uhhh- {w=.3}You're mouth smells like rotten meat and you look,{w=.3} act, {w=.3}and think like a conservative!"
                    p "ROCKY ROCKY ROCKY! You got this! Use that maned wolf strength! If Rocky can't do it! No one can!"
                    v "-Your legs are freakishly long,{w=.3}  your teeth are yellow,{w=.3}  you haven't worked out in years so stop saying ya got muscle"
                    r "*huff*"
                    p "Norman!{w=.3} Get in on this!{w=.3} Get the adrenaline flowing!"
                    n "Hmm,{w=.3} I {i}could{/i} mention how you though Vinni-"
                    r "RAAAAAAAAAAGHHH!!!!"
                    v "wait- {w=.3}wachoo u say?"

                if crowbar_collected == True:
                    "With one final overzealous crowbar bashing, he opens the vent"
                else:
                    "With one final overzealous kick,{w=.3} he opens the vent"
    
                if crowbar_collected == True:
                    r "I'M GONNA BASH YOU WITH THE CROWBAR NEXT RETRIEVER!"
                else:
                    r "I'M GONNA KICK YOU DOWN NEXT RETRIEVER!"
                
                jump mechanical_floor_escape

            elif crowbar_collected == True:
                p "You can use the crowbar to smash open the vent,{w=.3} I think Rocky is most suitable for the task"
                r "Got it!"
                "*Thud*{w=.3} Thud*{w=.3} Thud*" with hpunch
                v "C'mon Rocky... {w=.3}You got this..."
                n "Give it your all!"
                jump mechanical_floor_escape

            else:
                "We need some type of way to get this vent open it's the only way through this door..."
                jump pnc_loop

        else: 
            if crowbar_collected == True:
                "I use the crowbar to pry open the vent"
                p "Unph!"
                "Vinny and Norman take turns with me in trying to bash it open,{w=.3} it takes a long while but eventually we do, I take the crowbar with me"
                jump mechanical_floor_escape
            else:
                "We need some type of way to get this vent open it's the only way through this door..."
                jump pnc_loop


##THIS IS WHERE EVERYONE STARTS FUCKING DYING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

label mechanical_floor_escape:
    $ pnc_flags = {}
    if rocky_dead == False:
        if expose_samsara_together:
            "[pov!u] IT'S UP TO YOU NOW!"
        else:
            "After a while, {w=.3}Rocky is able to get the vent open"
            r "*huff* {w=.3}phew- {w=.3}Well-{w=.3} You can go in now [pov]!"
    scene vent with dissolve
    "I make my way through the vent,{w=.3} avoiding the massive fan blades in my way; good thing it's not on"
    scene electric generator with dissolve
    "The body in this cramped space creates a foul humid odor... {w=.3}I guess Lucas never got out of here..."
    if insanity_level >= 0:
        "Sorry for the intrusion..."
    "...? {w=.3}On close examination Lucas's corpse has a massive hole in it? If we thought he shot Luis... then did he shoot himself?"
    "...{w=.3}Then where's his gun...?"
    n "IS EVERYTHING GOOD IN THERE [pov!u]!?!?"
    p "Yeah! It's safe just real musty!"
    p "Ah,{w=.3} here's the switch...{w=.3} whoops..."
    play sound "audio/sfx/generator on.ogg" fadein 0.2
    "The switch handle broke off when I turned I shifted it, at least the power is permanently on now"
    "I can feel the walls vibrate while the building itself feels like it's booting up" with hpunch
    v "THE LIGHTS ARE ON!!! {w=.3}I CAN SEE CLEARLY NOW!~"
    n "Ahh much better!"
    play music "audio/music/mixkit-walking-dead-893- Michael Ramir C..ogg"
    play sound "audio/sfx/zombie crowd.ogg" fadein 0.3
    "A cacophony of stomping and groaning echoes throughout the room as if the entrance of hell was opened"
    if rocky_dead == False:
        r "What the hell is that?!?"
    n "Oh no they must have heard generator starting up!"
    if rocky_dead == False:
        v "More like because of numbnuts over here fucking around with the vent cover!"
        r "You were motivating me to dipshit!"
    "I try to open the door from the inside but... {w=.3}the door handle is missing! The vent!{w=.2} No wait,{w=.2} the fan must be turned on now..."
    "I put the switch handle into the electric generator in an attempt to fix it but it won't go in!"
    p "Guys!{w=.3} The door and generator handle is broken and the fan is blocking the vent out of here!{w=.3} Is there any way to turn it off from outside?!?"
    "I look through the window and see my friends avoiding the zombies,{w=.3} Norman is closest to the door"
    n "H-{w=.3} how do I get you out of there?"
    p "This is the mechanical floor!{w=.3} The HVAC's can be turned off! Go deactivate it!"
    "As Norman begins running I tell him that the HVAC is-"

    menu guide_norman:

            "Maybe in the Backroom hallway!?" if checked_hallway == False:
                $ checked_hallway = True
                if norman_has_gun == True:
                    jump norman_gun_cant_find_fan
                else:
                    jump norman_cant_find_fan

            "Maybe on top of the ramp!?" if checked_ramp == False:
                $ checked_ramp = True
                if norman_has_gun == True:
                    jump norman_gun_cant_find_fan
                else:
                    jump norman_cant_find_fan
                
            "Maybe in the room we started in!?" if examined_HVAC_machine == False:
                jump norman_deactivates_fan

            "FOR A FACT IN THE STARTING ROOM BECAUSE I CHECKED IT!!!" if examined_HVAC_machine == True:
                "I hear the fan"
                n "I Got it!"
                jump norman_deactivates_fan

            "Maybe near the elevator!?" if checked_elevator == False:
                $ checked_elevator = True
                if norman_has_gun == True:
                    jump norman_gun_cant_find_fan
                else:
                    jump norman_cant_find_fan

    label norman_cant_find_fan:
            play sound "audio/sfx/zombie attack.ogg"
            $ norman_health -= 1
            "On his way there,{w=.3} I hear a loud yelp and zombie shriek!" with hpunch
            n "Ow!{w=.3} It wasn't in there [pov]!" with vpunch
            jump guide_norman 

    label norman_gun_cant_find_fan:
            play sound "audio/sfx/shoot.ogg"
            with vpunch
            $ ammo -=1
            "I hear a loud gunshot and an injured zombie!"
            "It wasn't there [pov]! {w=.3}Sorry,{w=.3} I wasted some ammo!"
            jump guide_norman 

    label norman_deactivates_fan:
    n "That was it!{w=.3} I'll meet you at the elevator now!"

    "I hear the fan stop whirring and I immediately make my exit, {w=.3}on my way out I see Vinnie being cornered by a group of zombies!"

    if vinnie_has_gun == True:
        play sound "audio/sfx/shoot.ogg"
        "Fortunately they fire the gun so they're perfectly safe!"
        $ ammo -=1
        if rocky_dead == False:
            jump rocky_save_sequence
        else:
            jump office_floor_2
    else:
        menu:
            "I run away and abandon Vinnie":

                if rocky_dead == False and rocky_has_gun == True:
                    $ vinnie_health -= 1
                    $ insanity_level += 1
                    play sound "audio/sfx/female zombie groan.ogg"
                    v "OH FUCK SOMEBODY HELP ME IT'S BITING MY ARM!!!"
                    play sound "audio/sfx/shoot.ogg"
                    $ ammo -=1
                    r "I got you Vinnie!"
                    v "THANK YOU THANK YOU ROCKY!!"
                    jump rocky_save_sequence  
                
                if rocky_dead == False and expose_samsara_together == True:
                    $ insanity_level += 1
                    play sound "audio/sfx/female zombie groan.ogg"
                    v "OH FUCK SOMEBODY HELP ME IT'S BITING MY ARM!!!"
                    play sound "audio/sfx/punch.ogg"
                    r "I GOT YOU VINNIE!"
                    "Rocky valiantly swoops up Vinnie in his arms and carries him to safety"
                    jump rocky_save_sequence

                if rocky_dead == False and crowbar_collected == True:
                    $ vinnie_health -= 1
                    $ rocky_health -= 1
                    $ insanity_level += 1
                    play sound "audio/sfx/female zombie groan.ogg"
                    v "OH FUCK SOMEBODY HELP ME IT'S BITING MY ARM!!!"
                    play sound "audio/sfx/punch.ogg"
                    r "I got you Vinnie just get out of the way for crowbar!"
                    v "I CAN'T THEY'RE ALL ON ME! {w=.3} SHIT YOU HIT ME WITH IT YOU DICK!"
                    $ vinnie_health -= 1
                    r "BEHIND YOU!"
                    v "AAAAAAAHHH!"
                    jump rocky_save_sequence

                if rocky_dead:
                    $ vinnie_health -= 3
                    $ vinnie_dead == True
                    $ insanity_level += 1
                    play sound "audio/sfx/female zombie groan.ogg"
                    queue sound "audio/sfx/eat.ogg"
                    v "SHITSHITSHIT SOMEBODY HELP ME!!{w=.3} THEY'RE ON ME!{w=.3} THEY'RE ON ME!!!!"
                    "I hear loud chewing noises and distant screaming as I run further away"
                    jump office_floor_2

            "I headbutt the zombie attacking Vinnie with my horns!" if sage_has_gun == False:
                $ sage_health -= 1
                play sound "audio/sfx/zombie groan.ogg"
                "I was able to clear a path for Vinnie,{w=.3} but got hurt in the process when the zombie slashed my head!" with hpunch

                if rocky_dead == False:
                    jump rocky_save_sequence
                else:
                    jump office_floor_2

            "I shoot the zombies attacking Vinnie!" if sage_has_gun == True:
                play sound "audio/sfx/cock.ogg"
                queue sound "audio/sfx/shoot.ogg"
                $ ammo -=1

                "I successfully made an opening for Vinnie as they ran to the elevator!"

                if rocky_dead == False:
                    jump rocky_save_sequence
                else:
                    jump office_floor_2

            "I crowbar the zombies attacking Vinnie!" if rocky_dead == True:
                play sound "audio/sfx/zombie groan.ogg"
                queue sound "audio/sfx/punch.ogg"
                v "THANKS [pov!u]"
                "I successfully made an opening for Vinnie as they run!"

                if rocky_dead == False:
                    jump rocky_save_sequence
                else:
                    jump office_floor_2  

            "I tell Vinnie to stab the zombies with their knife!" if vinnies_knife == True:
                $ vinnie_health -= 1
                $ vinnies_knife = False
                v "Uh uhhh Ok!!{w=.3} OWWWW FUCK!!!!"
                "Their knife gets stuck in the zombie's head, {w=.3}who slashed Vinnie's arm in turn!"
                if rocky_dead == False:
                    jump rocky_save_sequence
                else:
                    jump office_floor_2

            "I tell Rocky to shoot the zombies!" if rocky_dead == False and rocky_has_gun == True:
                    play sound "audio/sfx/female zombie groan.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    $ ammo -=1
                    r "I got you Vinnie!"
                    v "THANK YOU THANK YOU ROCKY!!"
                    jump rocky_save_sequence

            "I tell Rocky to save Vinnie!" if rocky_dead == False:
                if expose_samsara_together:
                    play sound "audio/sfx/female zombie groan.ogg"
                    queue sound "audio/sfx/punch.ogg"
                    "Rocky is able to take down EVERY zombie in his path without problem!"
                    r "I got you Vinnie!"
                    v "THANK YOU THANK YOU ROCKY!!"
                    jump rocky_save_sequence
                elif crowbar_collected:
                    play sound "audio/sfx/female zombie groan.ogg"
                    queue sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 1
                    r "I got you Vinnie just get out of the way for crowbar!"
                    v "OK!"
                    jump rocky_save_sequence
                else:
                    $ rocky_health -= 3
                    "Rocky punches his way through to save Vinnie but gets badly hurt in the process!"
                    v "THANK YOU THANK YOU ROCKY!!"
                    r "D-{w=.3}don't mention it..."                  
                    jump rocky_save_sequence


            "I tell Norman to shoot the zombies!" if norman_has_gun == True:
                    play sound "audio/sfx/cock.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/zombie attack.ogg"
                    $ ammo -= 1
                    n "I'LL SAVE YOU VINNIE!"
                    "Norman was able to clear a path for Vinnie without a hitch!"
                    if rocky_dead == False:
                        jump rocky_save_sequence
                    else:
                        jump office_floor_2

            "I tell Norman to save Vinnie!" if norman_has_gun == False:
                        play sound "audio/sfx/female zombie groan.ogg"
                        queue sound "audio/sfx/punch.ogg"
                        queue sound "audio/sfx/zombie attack.ogg"
                        $ norman_health -= 1
                        n "I'LL SAVE YOU VINNIE!{w=.5} OW!"
                        "Norman was able to clear a path for Vinnie but got slashed in the process..."
                        if rocky_dead == False:
                            jump rocky_save_sequence
                        else:
                            jump office_floor_2

    label rocky_save_sequence:

        "On my way I see Rocky being restrained by zombies!"

        if expose_samsara_together == True:
            "Rocky is able to punch the zombie's head off and shoulder charge his way through a crowd without a scratch!"
            jump office_floor_2
        elif rocky_has_gun == True:
            "They fire their gun and make it out safely!"
            $ ammo -= 1
        else:

            menu:

                "I tell Rocky to use his crowbar!" if crowbar_collected == True:
                    play sound "audio/sfx/zombie huh.ogg"
                    queue sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/zombie what.ogg"
                    r "EAT THIS YOU WALKING BAG OF SHIT!!!"
                    "Rocky is able to get away!"   
                    jump office_floor_2                

                "I tell Norman to shoot the zombies!" if norman_has_gun == True:
                    play sound "audio/sfx/zombie moan.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    $ ammo -=1
                    r "Thanks Norman!"
                    n "No problem!"                    
                    jump office_floor_2   

                "I tell Norman to save Rocky" if norman_has_gun == False:
                    play sound "audio/sfx/zombie huh.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    "Norman charges the zombie but gets hurt in return!"
                    r "Holy fuck thanks!!!{w=.3} Are you gonna be ok!?"    
                    n "R-{w=.3} Run!!"
                    jump office_floor_2

                "I tell Vinnie to save Rocky" if vinnie_dead == False and vinnies_knife == False:
                    play sound "audio/sfx/zombie crowd.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    $ vinnie_health -=2
                    "Vinnie charges forwards but gets their body ravaged by the zombies in return!"
                    r "VINNIE NO!!!{w=.3} ARE YOU OKAY!"
                    v "C- {w=.3}carry me..."   
                    "Rocky carries Vinnie in their arms"                 
                    jump office_floor_2

                "I tell Vinnie to stab the zombies" if vinnie_dead == False and vinnies_knife == True and vinnie_has_gun == False:
                    play sound "audio/sfx/stab.ogg"
                    queue sound "audio/sfx/zombie crowd.ogg"
                    $ vinnie_health -=1
                    $ vinnies_knife == False

                    "Vinnie charges forwards and stabs the zombies! They get hurt in return and the knife is lost in the zombie's head!"
                    r "VINNIE NO!!!{w=.3} ARE YOU OKAY!"
                    v "C-carry{w=.3} me..."   
                    "Rocky carries Vinnie in their arms"                 
                    jump office_floor_2

                "I tell Vinnie to shoot the zombies!" if vinnie_dead == False and vinnie_has_gun == True:
                    play sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/zombie groan.ogg"

                    $ ammo -=1

                    v "Duck bitch!!!"
                    r "Huh?! HOLY FUCK!"
                    queue sound "audio/sfx/cock.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/zombie attack.ogg"
                    "Vinnie panics and shoots wildly, they don't hear the zombie behind them and get hurt in return!"

                    $ vinnie_health -=1
                    $ ammo -=1

                    v "*huff*{w=.3} *huff*{w=.3} I JUST SAVED YOUR ASS I EXPECT TO GET THE HOLIEST SLOPPY IN RETURN FOR THIS!!!"
                    jump office_floor_2  

                "I knock the zombie's block off!":
                    play sound "audio/sfx/punch.ogg"
                    queue sound "audio/sfx/m zombie moan.ogg"
                    $ sage_health -= 1
                    "I was able to save Rocky but got my fists banged up by the zombies in return!"
                    r "Thanks [pov]!"
                    jump office_floor_2

                "I shoot the zombies!" if sage_has_gun == True:
                    play sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/zombie what.ogg"
                    $ ammo -= 1
                    "I was able to save Rocky with no error!"
                    r "Thanks [pov]!"                    
                    jump office_floor_2
                    
                "I run away and abandon Rocky!":
                    if vinnie_dead == False and vinnie_has_gun == True:
                        play sound "audio/sfx/zombie groan.ogg"
                        queue sound "audio/sfx/shoot.ogg"
                        $ insanity_level += 1
                        v "Duck bitch!!!"
                        r "Huh?! HOLY FUCK!"
                        $ vinnie_health -=1
                        play sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/shoot.ogg"
                        queue sound "audio/sfx/zombie attack.ogg"
                        $ ammo -= 3

                        "Vinnie panics and shoots wildly,{w=.3} they don't hear the zombie behind them and get hurt in return!"
                        v "*huff*{w=.3} *huff*{w=.3} I JUST SAVED YOUR ASS I EXPECT TO GET THE HOLIEST SLOPPY IN RETURN FOR THIS!!!"   
                        jump office_floor_2

                    if vinnie_dead == False and vinnies_knife == True:
                        play sound "audio/sfx/stabwd.ogg"
                        queue sound "audio/sfx/zombie crowd.ogg"
                        $ insanity_level += 1
                        v "I'LL SAVE YOU ROCKY!!"
                        "Vinnie charges forwards and stabs the zombies!{w=.3} They get hurt in return and the knife is lost in the zombie's head!"
                        $ vinnie_health -=2
                        $ vinnies_knife = False
                        r "OH MY GOD ARE YOU GONNA BE OKAY?!?!"
                        v "C- {w=.3}carry me..."   
                        "Rocky carries Vinnie in their arms" 
                        jump office_floor_2

                    if vinnie_dead == False and vinnies_knife == False:
                        $ vinnie_health -=3
                        $ vinnie_dead = True
                        $ insanity_level += 1

                        play sound "audio/sfx/zombie crowd.ogg"
                        v "I'LL SAVE YOU ROCKY EVEN IF IT COST MY LIFE!!!"
                        "Vinnie charges forwards and gets lost in the horde in return... {w=.3}I hear chewing noises before Rocky yanks Vinnie out of there into their arms..."
                        r "VINNIE NO!!! ARE YOU OKAY! SPEAK TO ME!! YOU'RE NOT DEAD! YOU'RE NOT!!!!"
                        v "I... {w=.3}really.. {w=.3}l-{w=.3}l-{w=.3} liked our time together...{w=.3} please don- t be... {w=.3}worry ...{w=.3} haha...haaa {w=.3}*cough*"
                        v "D- {w=.3}don't push yourself... {w=.3}when you have people like... {w=.3}me... {w=.3}who do care..."
                        v "Don't... {w=.4}be... {w=.4}a... {w=.4}stranger... {w=.5}ha... {w=.5}haaaaa"
                        "Rocky carries Vinnie in their arms as they run towards the elevator"
                        $ vinnie_body_carried 
                        jump office_floor_2

                    else:
                        play sound "audio/sfx/zombie crowd.ogg"
                        queue sound "audio/sfx/eat.ogg"
                        $ insanity_level += 1
                        $ rocky_health -=5
                        $ rocky_dead == True
                        r "OH YEAH?!?! I-{w=.1} I'LL BEAT YOU ALL TO DEATH JUST YOU WAT-{w=.2} ARGGGHHHHH!!!"
                        "I hear chewing noises and the zombies moaning as I run further away..."
                        jump office_floor_2
                        
"We all run towards the elevator!"
pause 0.5
scene black with dissolve
return


    