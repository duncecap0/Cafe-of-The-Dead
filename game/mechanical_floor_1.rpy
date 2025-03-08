label mechanical_floor_staircase:
    scene elevator ride with dissolve
    "My heart beats as I march upwards, {w=.3}would we really be able to restore the power?{w=.3} Are the people here even okay?{w=.3} Would we really make it out of here?"
    n "Hey [pov]..."
    "Norman is speaking quietly with me as he lagged behind the others..."
    if insanity_level >= 0:
        n "I know you're not 100% on board with this but,{w=.3} please trust in us..."
        n "I'm just as afraid of you...{w=.3} I just put on a front because I don't want the others seeing how weak I really am..."
        n "Please...{w=.3} I- {w=.3}WE- won't let anything bad happen to you...{w=.3} I promise..."
        n "\"Your true family is the one who choose and accept one another\"...{w=.3} That's what you said right?"
        "Norman remembered my poem from class on the presentation day..."
        p "..."

    elif:
        n "Thank you for backing me up earlier [pov]..."
        n "To  be honest, {w=.3}I'm not sure about this myself, {w=.3}I'm glad to know I have someone to rely on..."
        n "You're someone I can trust... {w=.3}I love Vinnie and Rocky but, {w=.3} sometimes it feels like I can't really open up to them since they're dealing with so much as is..."
        n "I can't them know that... {w=.3}I-{w=.3} don't really know what I'm doing..."
        n "Don't get it wrong! I'm always glad to help them out it's like someone needs me... {w=.3}and hears me..."
        n "But, {w=.3}it's nice to have someone like that for me too..."
        n "\"Your true family is the one who choose and accept one another\"...{w=.3} That's what you said right?"
        "Norman remembered my poem from class on the presentation day..."
        p "..."
        p "Norman, {w=.3}of course I'll be there..."
        p "Don't worry, {w=.3}we ALL got your back on this..."
        p "Just look how far you've gotten us already..."
        n "...!"
        "Norman turns his head away sharply... {w=.3}I've never seen him this flustered... {w=.3}like he said,{w=.3} he always has to put on a perfect front..."
        "I swear Norman I'll ease your burdens... {w=.3}I'll let everyone else know so we can all be there for each other... {w=.3}In, {w=.3}fact we're already on the first step..."

label mechanical_floor_elevator:
    $ renpy.notify("Remember to save often...")
    "Here we are, the room is lined with pipes and exposed machinery, it feels humid and I can almost taste the dust in the air... why would they not have windows here?"
    n "It's hard to see..."
    p "That's right Golden Retrievers can't see as well in the dark"
    r "Better be careful, hang on to someone so they can guide you better..."
    v "Pfft, sounds like a skill issue! I can see perfectly!"
    p "Hey, goats and maned wolves' night vision isn't {i}that{/i} bad compared to yours"
    n "If your vision is so good! Wanna be in charge of the gun for now?"
    v "...! Uhhhh"
    v "Why doesn't [pov] take it... Pygmy Goat's vision ain't that bad either!"
    r "Why not me?"
    v "I told you once that it's apart of Opossum culture to eat the smallest of their young and you believed me..."
    v "Why would I trust someone like that with a loaded weapon?"
    r "I uh,{w=.3} didn't want to judge cultures..."
    v "Exactly another reason if you think eating children is a valid thing to just do... {w=.3}Take the dang thing [pov]!"
    n "Here! Just flick this here to release the safety, remember to breathe slowly to aim for the head better, and press here to shoot!"
    p "Thanks, I'll put this to use"
    $ renpy.notify("You recieved Norman's Gun!")
    
    #Examine Staircase where you came from
        "Just the fire exit from where we came from..."
        r "Really,{w=.3} you wanna go back already?"
        v "Jeez!{w=.3} Don't just give up now! {w=.3}Look at me!{w=.3} If I can handle it so can y-{w=.3}you!"
        "Vinnie says as they shiver uncontrollably"
        n "It's okay [pov]... {w=.3}remember what I told you?"

    #Examine locked ladder to upper ramp
    #toggable image button
    if  worker_key_collect == True
        "The key fits perfectly as the padlock falls off"
        p "Hmm I'm the smallest so my weight shouldn't mess with the under constructed platform as much"
        v "Hey! You actually should be thankful for being as light as a feather for once!"
        r "You're one to talk string bean..."
        "I steady myself on top of the elevated platform and reach out for the crowbar"
        p "Got it!"
        n "Yay! Good Job [pov]!"
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
            n "...Haaaaa..."
            "Rocky sets me down as we continue our search"
    else:
        p "The ladder is locked behind a padlock..."
        r "Workers usually have a key to this type of stuff if only we could find someone with it..."

    #examine under construction upper ramp crowbar
    #toggable image button when you get worker key
        if examined_upper_ramp:
            "That crowbar would be great at smashing stuff in..."
        else:
            p "Hey check out that crowbar on that upper ramp! {w=.3}Could be useful in breaking stuff open!"
            r "Looks like they were installing a higher level here. {w=.3}They never got the chance to finish it..."
            v "Woah it seem's pretty flimsy dunno about going up there or not... "
    
    #examine HVAC machine
        if examined_HVAC_machine:
            r "This here is an HVAC, stands, for heating, ventilation, and air conditioning. {w=.3}Used to work on them back when I worked odd jobs for neighbors..."
            r "Looks like it's not on right now...{w=.3} I don't know what that means for long term but for now we should be fine"
            v "Looks like you're blue collarness background has finally come to use!"
            r "You've never worked a day in your life{w=.3} {i}trust fund baby{/i}"
            v "But I'm {i}your{/i} trust fund baby...{w=.3} I can be your sugar daddy too with all that supposed trust fund if you want!"
            show rocky blush
            R "...!"
        else:
            "Just an HVAC, nothing of use..."
    

    #examine work desk
    ## make this a toggleable imagebutton
        "Looks like a personal journal, {w=.3}some of the pages have been ripped out..."
        $ worker_journal_1_collect = True
        play sound "audio/sfx/page turn.ogg"
        show bblack with Dissolve(1.):
                alpha.6
        centered "{font=Gargle Rg.otf}PROPERTY OF: Luis Garcia{/font}"
        centered "{font=Gargle Rg.otf}August 27-  When I first started working here in Lucian's tower I was but a wee lad o' 17 that came here with nothin but the clothes on me and a dime. Now that damn "Samara" (Samsara?) business bought up the place and renamed it under their company name.{/font}"
        centered "{font=Gargle Rg.otf}The younger workers nowadays don't even know the original name! They just assumin' they always owned the place. Samsara made this fine building that kickstarted beginning businesses into just another one of their extravagant advertisements!{/font}"
        centered "{font=Gargle Rg.otf}Those kids even dismiss the fact that Samsara make local hospitals gouge their prices, steal their resources, and give out their patient medical records to them. I wonder who made that seem like a hoax to all the common folk? I have no idea what they want with medical records of all things... {/font}"
        centered "{font=Gargle Rg.otf}What resource could you want from a hospital besides medical equipement anyways?!?! The company is all types of wrong if they could do that and get away with it, must have some deal with the government to let them do that...{/font}"
        centered "{font=Gargle Rg.otf}They bring in the wrong crowds now... Before it was fresh faced people who wanted to change the world for the betta! Now it somthing 'bout \"biotech\" or whateva the hell they call it. Sounds like a load of horseshit from me!(YEAH YOU HEARD ME CORPORATE){/font}"
        centered "{font=Gargle Rg.otf}They had us expand the tower immensely for their more private businesses when they first bought the place out; had me sign an NDA and everything! Didn't let us know what exactly the floors were for damn do they take a helluva lot electricity.{/font}"
        centered "{font=Gargle Rg.otf}Those bastards took the money required to power them out of our paychecks! Not to mention they treat us like trash! I've been working here for 47 damn years! Like hell am I gonna let them get away with this! I been starting a union with us mistreated workers... I'll teach them to mess with us...{/font}"
        #centered "{font=Gargle Rg.otf}{color=#f00}{u}color and underline{/u}{/color}{/font}"
        hide bblack with dissolve
        play sound "audio/sfx/page turn.ogg"
        r "This is horrible, just fucking disgusting. My MOM'S been forced into paying for those ridiculous prices!"
        r "I've sacrificed my entire LIFE into paying them! I've never been able to enjoy affording something because the guilt of my mom not being able to kills me as well"
        r "My dad worked my entire childhood just to keep her alive! Imagine that! Being forced to give out all your money to keep your loved one trapped in a fucking chamber where they DIE if you can't pay"
        r "No freetime for us, no family trips, no nice clothing, barely enough food to have enoug energy to work the rest of the day!"
        r "We're still working our asses of! He never got to enjoy retirement! My family and others sacrificed all for a CEO's 47th trip to the Bahamas!"
        v "Rocky..."
        n "..."
        menu:
            "Now's your chance to fix it"
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
                
            "Let's keep searching"
                r "..."
                r "Fine..."
                r "{w=.3}I hope every person who allowed this was devoured alive by those monsters..."

            "..."
            v "Rocky...{w=.3} I'm so sorry... I-{w=.3}... {w=.3}It's my fault for...{w=.3} making you care for my immature ass..."
            v "If I wasn't so stupid back then... {w=.3}I could have worked as well to help you out... "
            v "All those damn pranks I pulled on people and police... {w=.3}and the times of me making you do some dumbass shit with me for fun... {w=.3}All just for my selfishness..."
            r "..."
            r "...{w=.3}Don't say that.... {w=.3}you're one of the few people who {i}have{/i} been helping me out... {w=.3}my whole life..."
            r "The few chances I did get of free time. {w=.3}I didn't even know how to relax properly without thinking of a missed opportunity for working..."
            r "You made me think of something besides my own failures...{w=.3} I felt... {w=.3}alive for those moments with you..."
            r "Like I actually existed for something that wasn't a job..."
            v "...!"
            "Vinnie looks aways,{w=.3} I think I spot a tear?{w=.3} Hard to tell in the dark..."
            if expose_samsara_together == True:
                r "Norman. {w=.3}[pov], {w=.3}that goes for you too. {w=.3}I love you guys..."
            r "Anways, {w=.3}let's stop sulking,{w=.3} we got a job to do!"
            "Rocky steps further away by himself as Vinnie waits around in the hallway stares at his back"
            n "I never knew how deep Rocky's money problems went...{w=.3} I don't think Vinnie and him spoke like that in a while as well..."
            n "They were childhood friends you know...{w=.3} They had some type of falling and didn't meet again til college,{w=.3} I was the who convinced Rocky to see his childhood friend again"
            n "At the time I didn't know Vinnie...{w=.3} but I'm glad I did that... {w=.3}they seem good for eachother{w=.3} right?"
            menu:
                "I'm glad to have you"
            $ insanity_level -= 1
                $ norman_affection += 1
                    show norman blush
                    n "...!"
                    n "[pov]... {w=.3}I'm glad to have you too..."
                    n "You're a good friend [pov],{w=.3} that means something...{w=.3} remember?"
                    p "I never forgot."
                    n "..."
                "You're a good friend to them"
                    n "Awww don't forget you're my friend too!"
                    if insanity_level >= 0:
                        p "..."
                        n "...?"
                    else:
                        p "Thank you.{w=.3} Sometimes I just feel like an outsider..."
                        n "You're no outsider... {w=.3}to me..."

        #$ renpy.notify("Worker's Journal Entry #1 has been added to Notes!")
    

    #worker key hidden in worker's coat
    #toggable imagebutton
        "Looks like a large worn out worker's jacket,{w=.3} I check the pockets to see if there's anything..."
        "...! {w=.3}I feel a key in one of the pockets!"
        $ worker_key_collect = True
        p "Guys look!"
        r "That's a padlock key,{w=.3} you can tell from how small it is and the notches"
        n "Impressive! {w=.3}How did you know that!"
        r "Used to work in a warehouse and they had me lock up all sorts of stuff similar to this..."
        $ renpy.notify("Padlock key has been added to inventory!")
    

    #worker journal scrap 2
    ## make this a toggleable imagebutton
    "I pick up the loose paper scrap on the floor"
        $ worker_journal_2_collect = True
        play sound "audio/sfx/page turn.ogg"
        show bblack with Dissolve(1.):
                alpha.6
        centered "{font=Gargle Rg.otf}September 2- Well, the union idea was a complete failure. The posse I gathered up marched straight to the head office demanding a raise and to be respected.{/font}"
        centered "{font=Gargle Rg.otf}When we listed off all our demands we were met with a full minute of deafening silence, then try to trick thinkin' I'm so starry-eyed youngin' with their \"Thank you for being honest with us, your concerns will be met accordingly\" B.S.!{/font}"
        centered "{font=Gargle Rg.otf}I've been working longer than you've been wiping your own ass boy! Don't toy with me! The workers and I rioted outside with signs in the main lobby until shouting and exposing our mistreatment until...{/font}"
        centered "{font=Gargle Rg.otf}Some... men in black body armour showed up, evacuated all civilians from the premises and set up a mile wide perimeter preventing anyone from seeing us... and then started just... beating us with riot batons and pepper spray{/font}"
        centered "{font=Gargle Rg.otf}Even when we surrendered they just kept going. I blacked out and when I woke up, I was in a bed. Some person in a suit said that I was under law to stay in these quarters and be restricted to this buildiong for the forseeable future{/font}"
        centered "{font=Gargle Rg.otf}They implemented some new system where employees are rewarded now for reporting any sign of dissatisfaction with their job and disciplined for not doing so... God, I still don't where some of my long time friends are for refusing to surrender...{/font}"
        centered "{font=Gargle Rg.otf}I'm scared to even write anymore... What if someone finds it? I have to get out here...{/font}"
        hide bblack with dissolve
        play sound "audio/sfx/page turn.ogg"
        r "How could they mistreat their workers like that?!?{w=.3} Don't they know how hard it is for some people?"
        v "Yeah, pretty fucked up how the sytem's just stacked against lower wage workers, {w=.3}people who claim there isn't a class system are total dumbasses when shit like this happens..."

    #blood stained water boiler
    r "This looks like a boiler meant for central heating, cooking, warm water..."
    v "Rocky the handyman!"
    extend "Hol up is that blood?"
    p "This is why we stick together,{w=.3} never know what's out there in the dark"
    n "Hold that gun tight [pov]..."

    #Elevator imagebutton
    r "This is the elevator, won't turn on unless the power's on..."
    n "This is why we practice the fire safety drill people!"
    v "NEERRRDD!!!!"
    if norman_affection >= 0:
        p "He's my nerd..."
        v "...?"
        p "...!"
        p "OUR nerd..."
        "I'm pretty sure Norman was out of earshot for that one... too busy guiding himself on the walls..."
    else:
        p "He's our nerd..."
        v "Meh, I GUESS we'll keep him..."
    

    #corpse with note
    v "OH MY FUCKING GOD IT'S A DEAD BODY! SHOOT IT! IT MIGHT BE A ZOMBIE!!!"
    "I aim my gun at it as Rocky starts guarding Norman and Vinnie..."
    n "...{w=.3}I'm preeeeeetty sure he isn't coming back... {w=.3}wouldn't he have been roaming around here?"
    p "Hmm, {w=.3}true..."
    "I step forward and start rummaging through the bodies pockets..."
    if insanity_level >= 0:
        "Useless pile of meat..."
    else: 
        pass
    v "DUUUUUDEE YOU CAN'T MAKE THIS SHIT UP!!!!!"
    r "You're braver than I thought..."
    n "Now that's what I call thorough!"
    "I find a hastily written scrap of paper undeneath his hand"
    $ worker_journal_3_collect = True
    play sound "audio/sfx/page turn.ogg"
        show bblack with Dissolve(1.):
                alpha.6
        centered "{font=Gargle Rg.otf}October(?) something...- Been here for who knows how long... They keep me cooped up here to set an example for the others...{/font}"
        centered "{font=Gargle Rg.otf}Conditions only got worse... it's a dog-eat-dog world out here now... men selling out their friend for a raise... never thought I'd see the day...{/font}"
        centered "{font=Gargle Rg.otf}The kids here turned from desperate for a job to pirahnna overnight... never thought I'd miss their smartass mouths until now...{/font}"
        centered "{font=Gargle Rg.otf}The workers have been getting taken more and more frequently... It's just me and a skeleton crew now... this one kid... early 20's maybe? Named Lucas been scaring me...{/font}"
        centered "{font=Gargle Rg.otf}He was a chef here... got called higher up to deliver private foood to a V.I.P and I guess he saw something he wasn't supposed to see... forced him to be locked up here like me... I gave him my quarters while I sleep on the desk...{/font}"
        centered "{font=Gargle Rg.otf}Keeps ranting and raving about some monster... they must'a knocked his head up real bad to do this... he locked himself in the electric generator... said monsters can't get him there...{/font}"
        centered "{font=Gargle Rg.otf}Hasn't eaten in days... I try to force him to but he locked me out. I'm trying to break my way in there but I don't know if I have the strength anymore. He honestly might be better off in there. No one to force him to do his required hours{/font}"
        centered "{font=Gargle Rg.otf}I'm gonna save us kid. Ol' Luis will get ya outta here Lucas! And everyone else too, you're just being forced to by a broken system...{/font}"
        hide bblack with dissolve
        play sound "audio/sfx/page turn.ogg"
        
    "..."
    "Norman approaches the body closer with me and notices something..."
    n "...The back of his head... {w=.3}It already has a bullet hole in it? {w=.3}Who did... {w=.3}that..."
    p "Some people just can't handle it maybe... {w=.3}he... {w=.3}you know..."
    v "Or the one crazy guy he was talking about..."
    r "Luis was a good man,{w=.3} I bet he would have gotten everyone out if he had more time..."
    if expose_samsara_together == True:
        r "We already decided on exposing this place! We'll pick up where you left off Luis!"
    v "Big thankies Luis!~ I will make you internet famous so the world will remember your name!"
    n "We won't let your wish be in vain Luis!"
    if insanity_level >= 0:
        "...{w=.3}how hopeless"
    else: 
        p "I won't forget you Luis."

    #ELECTRIC GENERATOR VENT
    #toggable image buttons that only appears if you got the worker journal 3
    if worker_journal_3_collect == True:
        p "This vent has to be the alternative path the note was talking about"
        v "How do we get in though?"
        n "It seems real small... {w=.3}I think [pov] might be the only one who fits..."
        if expose_samsara_together == True:
        r "I got this! Watch and learn!{w=.3} I'll get us all outta here!"
            if crowbar == True:
                "Rocky enthusiastically bashes the vent in repeatedly"
            else:
            "Rocky enthusiastically kicks the vent in repeatedly"
            if insanity_level >= 0:
                v "Woo Woo! You got this Rocky!"
                n "You can do it!"
                jump mechanical_floor_escape
            else:
                p "You're mom is waiting on us! She's chilling in her room just knowing that Rocky the great is on his way!"
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
                if crowbar == True:
                    "With one final overzealous crowbar bashing, he opens the vent"
                else:
                    "With one final overzealous kick, he opens the vent"
                if crowbar == True:
                    r "I'M GONNA KICK YOU DOWN NEXT RETRIEVER!"
                else:
                    r "I'M GONNA BASH YOU WITH THE CROWBAR NEXT RETRIEVER!"
                jump mechanical_floor_escape
        else crowbar:
            p "You can use the crowbar to smash open the vent, I think Rocky is most suitable for the task"
            r "Got it!"
            "*Thud* Thud* Thud*" with hpunch
            v "C'mon Rocky... You got this..."
            n "Give it your all!"
            jump mechanical_floor_escape
        
label mechanical_floor_escape:

    if expose_samsara_together == True:
        "[pov!u] IT'S UP TO YOU NOW!"
    else:
        "After a while, Rocky is able to crack the vent open"
        r "*huff* {w=.3}phew- {w=.3}Well-{w=.3} You can go in now [pov]!"
    "I make my way through the vent"
    scene electric switch
    "The body in this cramped space creates a foul humid odor..."
    n "IS EVERYTHING GOOD IN THERE [pov!u]"
    p "Yeah! It's safe just real musty!"
    p "Ah, here's the switch..."
    "I can feel the walls vibrate while the building itself feels like it's booting up"
    v "THE LIGHTS ARE ON!!! I CAN SEE CLEARLY NOW!~"
    n "Ahh much better!"
    play sound "audio/sfx/zombie crowd.ogg"
    "A cacophony of stomping and groaning echoes throughout the room as if a "
    r "What the hell is that?!?"
    n "Oh no they must have heard the vent racket and the generator starting up!"
    ""





            


               

        



    #ELECTRIC GENERATOR DOOR
    if worker_journal_3_collect == True:
        "I peek through the metal window and see a decomposing corpse in front of what looks like a machine, that must be Lucas"
        r "That has to be the electric generator switch, didn't the note say there was another way in?"
    elif crowbar == True: 
        v "This door is locked! Hey meathead! Use your muscle gut for something good with the crowbar!"
        r "...I'll just pretend the door is your face!"
        "Rocky tries smashing the window and door handle but it won't budge..."
        r "*huff* *huff*"
        n "Well, it was a good effort!"
        if worker_journal_3_collect == True:
            n "Didn't the note say there was another way in?"
        jump 
    else:
        "I peek through the window and see a decomposing corpse in front of what looks like a machine"
        r "That has to be the electric generator switch, How do we get in?"
    


    
