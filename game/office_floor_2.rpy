
#variables
default morphine = False
default closet_broken = False
default medkit = False
default scissors = False
default norman_secret_death = False
default examined_toilet = False


default norman_office_death = False
default vinnie_office_death = False
default rocky_office_death = False

 
#password
define password = "password"
define password_input = ""



# options being chosen
default t_o_1 = False
default t_o_2 = False

#relationships

default expose_samsara_together_2 = False


#REMEMBER TO ADD TARA TO EPILOGUE ENDING
default save_tara_1 = False
default save_tara_2 = False

default tara  = False

#Zombie lives
default juggernaut_zombie = True


label office_floor_2:

    scene black with dissolve
    stop sound
    stop music
    pause 1.0
    scene elevator with dissolve
    "We all sit in silence for a good while,{w=.3}  just trying to take it all in..."
    "Norman already pressed the button for us to go into the office space,{w=.3}  we think survivors are in there..."
    ##NORMAN GETS DEPRESSED DIALOGUE TREE
    if rocky_dead == True or vinnie_dead == True:
        "The elevator's music is playing as if it were mocking our losses..."
    if vinnie_dead == True:
        #"Rocky has Vinnie's lifeless body's head resting on his lap, {w=.3} eyes closed as if they were sleeping;{w=.3}  Rocky seemed to be lost in them..."
        "Rocky hasn't spoken a word since it happened, {w=.3} the rest of us are too afraid to speak until-"
    n "..."
    if insanity_level <= 1:
        if norman_affection >= 1:
            n "We've gotten pretty far now haven't we?"
            if rocky_dead == True or vinnie_dead == True:
                n "I know we've had some losses on the way... {w=.3} things won't be the same without them..."
                label norman_death_reaction:
                if rocky_dead == True:
                    n "Rocky's protectiveness,{w=.3} bravery, and caring nature... {w=.3} always making sure everyone was happy even if it hurt him... {w=.3} he was my first best friend you know... {w=.3} I still can't grasp he's..."
                if vinnie_dead == True:
                    n "Vinnie's charm, love, and acceptance....{w=.3} always trying to get people to not wallow in misery for too long... {w=.3} they wanted this friend group to exist more than anything...."
                n "Ah! {w=.3} Look at me getting emotional...{w=.3} we have work to do no? Haha..."
                menu:
                        "I'm sorry for your losses":
                            $ norman_affection +=1
                            n "...!"
                            n "They're your losses to you know... {w=.3} just because you're the newest member doesn't mean that your worth less...{w=.3}  especially to me..."
                            p "They're your friends, our friends, {w=.3} how can you not be sad?{w=.3}  It's ok to let it out Norman...{w=.3}  to feel pain is to be alive..."
                            n "..."
                            if vinnie_dead == False and rocky_dead == True:
                                v "I miss him too Norman...{w=.3}  I don't think I'll ever be able to live like how he wanted me to,{w=.3}  but if you having nothing to lose you have nothing to gain? Remember his words you told me?"
                            if rocky_dead == False and vinnie_dead == True:
                                r "I miss them too Norman...{w=.3}  I'll never be able to laugh like how they made me, {w=.3} but if you having nothing to lose you have nothing to gain!"
                            if rocky_dead == False or vinnie_dead == False:
                                n "Guys... {w=.3} I... {w=.3} I c-{w=.3} can't..."
                                "Norman begins sobbing uncontrollably before leaping into our arms...{w=.3}  we all hug until we hear sniffling die down... {w=.3} I don't even know if it's from Norman or not..."
                            else:
                                n "[pov]... {w=.3} I...{w=.3}  I c-{w=.3}can't..."
                                "Norman begins sobbing uncontrollably before leaping into my arms... {w=.3} we hug until I hear the sniffling die down..."
                            "I don't want to let go..."
                            pause 0.5
                            n "Thank you...{w=.3} I needed that..."
                            "A minute passes before everyone goes back to their respective part of the elevator, {w=.3} until Norman sidles up next to me again"

                        "Don't get sappy.":
                            $ norman_affection -=2
                            $ insanity_level +=1
                            n "{w=.3}...Oh...{w=.3}  I suppose you're... {w=.3} right..."
                            "Norman looks as if I had just slapped him,{w=.3}  not my fault someone isn't focusing on the fact we could die at any minute..."
                            jump office_floor_2_survivor_banter
            else:
                n "We haven't had any losses yet! Go team us!"

            n "[pov]... I'm so proud of you... {w=.3} you're like a natural born leader...."
            n "That's one of the things I've always admired about you... {w=.3} so dead-set on their beliefs and willing to speak out! You may seem quiet to the naked eye but that's because people don't look hard enough!"
            n "You're able to speak louder than a million people with just a single sentence. You can accomplish what people only dream of doing; that's not an easy skill, {w=.3}I can assure you that..."

            menu:
                "Thanks":
                    n "No Problem [pov]!"
                    jump office_floor_2_survivor_banter

                "I admire you too Norman":
                    if vinnie_dead == False:
                        n "[pov]...?{w=.3}  D-{w=.3} don't say stuff like that out loud! Vinnie would NEVER let me hear the end of it.."
                    else:
                        n "[pov]...? {w=.3} D-{w=.3} don't say stuff like that out loud! What if someone hears that?"
                    p "It's true though,{w=.3}  strength and responsibility like Rocky, {w=.3} smarts and charm as Vinnie...{w=.3}  and you say I'm the skillful one but I could only dream of being like you"
                    "Norman has been staring down at the ground the whole time,{w=.3}  I think I see his cheeks blush red..."
                    n "[pov]... {w=.3} thank you...{w=.3}  truly..."
                    p "Don't mention it,{w=.3}  I'll never forget it."
                    if vinnie_dead == False:
                        "I'm pretty sure I caught Vinnie sneaking peeks at us;{w=.2} I don't care,{w=.3} let them watch..."
                    if rocky_dead == False:
                        "Rocky has been staring at his watch for far too long to be unsuspecting; {w=.2} as if he were trying to give us room,{w=.3} good."
                    jump office_floor_2_survivor_banter

label office_floor_2_survivor_banter:

    if rocky_has_gun == True:

        if vinnie_body_carried == True:
            r "Your gun..."
        else:
            r "Here! {w=.3} Take your gun back Norman!"

    if vinnie_has_gun:
            v "TAKE THIS GUN AWAY FROM ME PLEASE NORM-NORM!!! I'm not a good shot at all..."

    if sage_has_gun:
            p "Also,{w=.3}  I believe this gun belongs to you?"

    if insanity_level <=1:
        n "Hmm how about you keep it from now on [pov]! {w=.3} You proved yourself capable today!"
        p "You sure?{w=.3}  I'm not a marksman or have the training that you do..."
        n "Says the one that doesn't panic at a moment's notice! Haha!{w=.3}  Just take it you goof!"
        $ sage_has_gun == True
    else:
        n "Thanks! {w=.3} Good thing I never leave home without it!"
        $ norman_has_gun == True

    if rocky_dead == False and vinnie_dead == False:
        r "That battle was intense! Glad we made it through alright!"
        v "Yeah that was ass up in shit's creek! Thanks to [pov]'s star spangling advice we got out there"
        r "Don't forget it was {i}my{/i} battle expertise that saved you all..."
        v "CALM YOU'RE DOUBLE D TIG OL BITTIES WOMAN! I'm not trying to accuse anyone of anything just saying that {i}I{/i} think some people pulled their weight more than others..."
        r "...{w=.3} That's exactly what a fucking accusation is you dumb slut..."
        v "EXCUSE ME, AM I THE ONE WHO THINKS THAT ALL ASSASSINATED PRESIDENTS FAKED THEIR DEATHS TO JOIN THE SHADOW COUNCIL AND PULL THE STRINGS WITHOUT US KNOWING?!?!"
        r "THAT SHOOTING WAS TOTALLY STAGED AND I CAN PROVE IT! WHY DO YOU THINK ALL THEIR FRIENDS JUST SO HAPPENED TO DIE THE FOLLOWING YEARS HUH?!?!"
        v "They died because they were old as fuck and all that coke from their younger years caught up to them!"
        r "YOU TAKE THAT BACK YOU SHEEPLE!!!"
        v "Correct term is \"Sherson\" {i}actually{i}..."
        n "Guys, isn't that word a little offensive to [pov]?"
        "They're too busy continuously shouting back and fourth about conspiracy theories and the Deep State to hear..."
    if rocky_dead == True and vinnie_dead == False:
        "I hear Vinnie chanting Rocky's name quietly under their breath as if it were a hastened prayer; I don't think they even noticed what they were doing..."
        if insanity_level == 0:
            "I reach out to squeeze Vinnie's shoulders who jumps in response"
            p "Hey Vinnie? {w=.3} It's gonna be ok bud... {w=.3} I didn't know you guys for too long but I can tell Rocky loved you... {w=.3} remember that we're here for you if you need anything got that?"
            v "..."
            v "...Thank you...{w=.3} [pov]... {w=.3} he was like family to me... I..."
            v "..."
            v "You and Norman are my family as well. Got it?"
            if norman_affection >=0:
                p "...{w=.3} Norman especially is like a-"
            p "...{w=.3} I'm so grat-"
    if rocky_dead == False and vinnie_dead == True:
        "I hear Rocky muttering something under his breath... {w=.3} I think it's some type of religious prayer?"
        if insanity_level == 0:
            "I reach out to touch Rocky's back who says nothing in response"
            p "Hey Rocky? {w=.3} It's gonna be ok big guy... {w=.3} I didn't know you guys for too long but I can tell Vinnie loved you... {w=.3} remember that we're here for you if you need anything got that?"
            r "..."
            r "...Thank you...[pov]...{w=.3}  they were like family to me... {w=.3} maybe even a...."
            r "God, {w=.3} I wonder what mom and pa are up to right now... {w=.3} hope their safe..."
            r "..."
            r "You and Norman are my family too?{w=.3}  Got it?"
            if norman_affection >=0:
                p "...{w=.3} Norman especially is like a-"
            p "...{w=.3} I'm so grat-"
    if insanity_level >=1:
        "..."
        "..."
        "The air feels like it's flexing as awkward silence fills the room"
        "I couldn't help but notice Norman staring intensely at my back when he thinks I'm looking away,{w=.3} what's he so wary of? He's treating me as if I were one of the monsters..."
        "..."
    "The elevator comes to a screeching stop as the doors slide open"

    n "Hello is anyone-"

    extend "What in the world happened here! It's nothing but dead bodies!"

    p "They're not as fortunate as we thought they would be, it's putrid in here..."
    
    if rocky_dead == True: 
        v "There goes another hope..."

    if rocky_dead == False: 
        v "I should have remembered those clamps I bought for rocky since those would be real useful in blocking my nose"

        r "Ugh the smell-"
        extend "Wait, what were you talking about?!?"

    n "Let's not give up there has to be someone alive here!"
    jump office_start


##OFFICE ROOMS

label office_start:
    scene office start with dissolve
    $ current_room = "office_start" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label office_hall:
    scene office hall with dissolve
    $ current_room = "office_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label office_restroom:
    scene office restroom with dissolve
    $ current_room = "office_restroom" 
    jump pnc_loop

label office_closet:
    scene office closet with dissolve
    $ current_room = "office_closet" 
    jump pnc_loop

label office_desks:
    scene office desks with dissolve
    $ current_room = "office_desks" 
    jump pnc_loop


label office_breakroom:
    scene office breakroom with dissolve
    $ current_room = "office_breakroom" 
    jump pnc_loop

label office_boardroom:
    scene office board room with dissolve
    $ current_room = "office_boardroom" 
    jump pnc_loop

label office_computerdesk:
    scene office computer with dissolve
    $ current_room = "office_computerdesk" 
    jump pnc_loop

### POINT'n'CLICK LABELS ###

label office_corpse_pile:

    "Various corpses are strewn about, some seem to have been eaten while a few are shredded with bullet holes. I don't understand how they were able to die if they had access to machine guns..."
    "... Where even are the people with machine guns if they're not dead in here?"
    if norman_dead == False:
        n "Doesn't this seem similar to how the people on the mechanical floor died?"
    jump pnc_loop


label office_window:
    scene city view with dissolve

    "The city looks abandoned, with only hordes of zombies shambling together flooding the streets, the sky is burning as smoke fills the air" 

    v "Things got worse since we last saw outside..."

    r "...{w=.3} I'll save you mom and dad,{w=.3} this will only take a bit longer"

    n "..."

    "He's staring blankly at the floor; as if he cant comprehend whats happening outside"

    menu:

        "It'll be okay Norman, don't worry":
            $ norman_affection += 1
            n "t-thank you" 
            "Norman blurts out while still staring downwards"
    
        "Don't get distracted":
            $ insanity_level +=1
            n "..."

    jump pnc_loop

label toilets:
    if examined_toilet:
        "Enough with the toilets!"
    else:
        "What did I expect to get out of a toilet?"
        if vinnie_dead == False:
            v "Office workers usually do drug deals in here, hang on let me check behind one..."
            if norman_dead == False:
                n "Wow! That's so smart!"
            if rocky_dead == False:
                r "Looks like your teen years weren't as useless as everyone though!"
                v "Shut it! NPC!"
            v "AHA! Found some morphine taped underneath this one? Who wants restroom drugs???"
            if norman_dead == False:
                "Hang on, do we have to use it right now? Let's save it for when really need it! Morphine isn't something to be played around with!"

            menu morphine_choice:
                "Who should we use it on?"

                "Me":
                    $ sage_health +=2

                "Norman" if norman_dead == False:

                    if closet_broken == False:
                        $ norman_health +=2
                        n "Never done drugs before..."

                    if closet_broken == True:
                        n "We should give it to the woman in the closet! Not ourselves!"

                        jump morphine_choice

                "Rocky" if rocky_dead == False:
                    $ rocky_health +=2
                    r "Reminds me of when I broke my back at the warehouse..."

                "Vinnie" if vinnie_dead == False:
                    $ vinnie_health +=2
                    v "I hope I don't get addicted to these things again...."

                "Leave for now it may be useful for later":
                    pass
                
                "Save it for injured woman" if closet_broken == True:
                    $ morphine == True
                    jump try_save_woman

    jump pnc_loop

label injured_woman_closet:
    scene office window with dissolve
    $ w_name = "Injured Woman"
    w "..."
    "A bloodied woman lies on the floor, her arm seems to be missing"
    p "Hello! Are you OK?"
    if rocky_dead == False:
        r "You're safe now! We're here for you! There {i}were{/i} other people here! Good thing we checked!"
    if vinnie_dead == False:
        v "There's so much blood!! How are you even still alive?!?!"
        v "Don't worry I'm a med student! I could get help you here I just need the supplies!"
    if norman_dead == False:
        n "Oh my god I'm so happy to know we're not alone! We need to save her!"

    menu try_save_woman:

        "That arm wound is brutal, how do I help with that?"

        "Use Med kit" if medkit == True and t_o_1 == False:
            $ t_o_1 == True
            $ save_tara_2 = True
            w "...rearrange... words... days.. of week..."
            "She's a little better, but not fully healed... she won't last long without further treatment, I wonder if there's anything else to give her?"
            if save_tara_1 and save_tara_2 == True:
                jump saved_tara
            else:
                jump try_save_woman

        "Have Vinnie help her in place of the med kit" if vinnie_dead and t_o_1 == False:
            $ t_o_1 == True
            $ save_tara_2 = True
            w "...rearrange... words... days.. of week..."
            "She's a little better, but not fully healed... she won't last long without further treatment, I wonder if there's anything else to give her?"
            if save_tara_1 and save_tara_2 == True:
                jump saved_tara
            else:
                jump try_save_woman

        "Use Morphine" if morphine == True and t_o_2 == False:
            $ t_o_2 == True
            $ save_tara_2 = True
            w "You... must go to... higher floor... only way out..."
            "She's a little better, but not fully healed... she won't last long without further treatment, I wonder if there's anything else to give her?"
            if save_tara_1 and save_tara_2 == True:
                jump saved_tara
            else:
                jump try_save_woman
                
        "Leave to look for stuff":
            p "I have nothing on me right now, maybe there's something else around?"
    
    jump pnc_loop

    label saved_tara:
        $ tara == True
        $ w_name = "Tara"
        w "T-thank you.. I won't forget this, My name is Tara, I'm an employee here and barricaded myself into this room to hide from the rampage outside. We were all called here today for an \"important\" meeting."
        w "We were all waiting, until people in black body armour showed up and started shooting everybody dead, all of the sudden the dead people rose back up again and started eating those who avoided being shot"
        
        if vinnie_dead == False:
            v "Sounds like you've been through a lot"

        if rocky_dead == False:
            r "I'm sorry to hear that"
            
        w "I've noticed that Samsara has been heading towards a dark path, so I investigated the company's records and found shady dealings with the local medical facilities around here"
        w "The upper floors HAVE to be involved, all of us on the lower floors wanted to leave when when they started cracking things down, I saw that they headed upwards by going through the express elevator right outside this room"
        w "It's locked up tight, you need to crack the code to be able to enter. I found out that the password input is hidden behind a false wall in the boardroom. We need to solve it!"
        if rocky_dead == False:
            r "No offense but, we're just trying to get out of here not solve a mystery"
            w "Heh, none taken"
        w "The upper floors have a comms room. We could signal for help and call in a chopper to save us"
        if norman == False:
            n "Ok [pov] let's check out the boardroom! Are you gonna be alright here Tara?"
        "Tara tries to get up but sits back down after feeling a pain in her arm"
        if vinnie_dead == False:
            v "Try not moving! You've already lost a lot of blood I'll take care of this alright?"
            "Vinnie spends a while dressing Tara's wound"
            v "Just stay here for now. Don't overwork yourself we've got it under control!"
        t "Alright, I trust you to handle this situation. I can't exactly get up, doctor's orders..."
        jump pnc_loop

label medkit:

        "I find a med kit in one of the top cabinets"

        menu:
            "Who should we use it on?"

            "Me":
                $ sage_health +=1
            "Norman" if norman_dead == False:
                $ norman_health +=1
                n "Never done drugs before..."
            "Rocky" if rocky_dead == False:
                $ rocky_health +=1
                r "Reminds me of when I broke my back at the warehouse..."

            "Vinnie" if vinnie_dead == False:
                $ vinnie_health +=1
                v "I hope I don't get addicted to these things again...."

            "Leave for now it may be useful for later":
                pass

            "Use for Injured Woman" if closet_broken == True:
                $ medkit == True
                jump try_save_woman
        
        jump pnc_loop

label blocked_closet:
    "The door to this room won't budge as if it were locked from the inside"

    if crowbar_collected and rocky_dead == True:
        $ closet_broken == True
        "I use the crowbar to break the handle"
        jump injured_woman_closet

    elif crowbar_collected == True and rocky_dead == False:
        $ closet_broken == True
        "Fortunately, Rocky uses the crowbar to break the handle"

        jump injured_woman_closet

    elif vinnies_knife == True and vinnie_dead == False:
        $ closet_broken == True
        "Fortunately, Vinnie uses their knife to slowly wear away the handle over time"
        jump injured_woman_closet

    elif vinnies_knife and crowbar_collected == False and vinnie_dead and rocky_dead and norman_dead == True:
        $ closet_broken == True
        "I have nothing to break the handle, should the gun be used?"
        
        menu:
                "Shoot 4 times to break open the door handle":
                    play sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    queue sound "audio/sfx/shoot.ogg"
                    pause 0.3
                    "The handle breaks and I'm able to enter"
                    jump injured_woman_closet

                "Find something else":
                    jump pnc_loop


label word_puzzle:
    scene computer with dissolve
    $ renpy.notify("Use the keyboard to type the password...")
    if tara == True:
        "This must be what Tara was talking about, we need to solve this word puzzle to be able to access the higher floors"
    else:
        "I'm not sure what this does but it must be important if it were hidden behind a wall"
    #TO DO FIX
    jump get_password
return


label secret_elevator:
    p "Looks like another elevator, it won't open no matter how many times I call for it"
    if norman_dead == False:
        n "This has to be the express elevator that leads to the higher floor! If the telecommunications isn't here it should be up there!"
    if tara == True:
        p "Tara said it should be accessible once I enter code the in the boardroom's false wall"
        


label worker_diary:
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Sandra Keyes- I'm not too sure what our goal is anymore. Before, it was leasing floors, then that coffee company took over and now we're cooperating with hospitals?{/font}"
    centered "{font=Dudu_Calligraphy.ttf}A lot of patient transfers and faculty being taken to the higher floors... some of them finally explained with the board meeting. SO many crazy words I've never even heard before!{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I thought it was a joke but no one was laughing. Its something about virology...? What the hell could they possibly be doing up there!{/font}"
    centered "{font=Dudu_Calligraphy.ttf}I'm talking to Ashley about this later and we're gonna have a word with the higher ups about this crazy talk!{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"

    p "Guess not even THESE employees knew what was going on"

    if rocky_dead == False:
        r "Why even expand to something else? You're a coffee business for crying out loud!"

    if vinnie_dead == False:
        v "There's always something going on behind the scenes... ask yourself what your favorite product is; then ask someone who worked on it; then you'll find out its all about the profit, never about the those who bring it to life..."
        v "Worker abuse takes place everywhere because people can get away with it. When was the last time you thought about your cashier's income and how their boss treats them? You don't do you? If we did we wouldn't be here now would we..."
    
    if norman_dead == False:
        n "Jobs should help people with their lives, not take them away..." 
    
    jump pnc_loop


label worker_email:
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf}Daniel Walsh- Jesus, things have gotten brutal the past few months. Everything's shifted to pure medical research with just a skeleton crew managing the coffee side of their business{/font}"
    centered "{font=Dudu_Calligraphy.ttf} Now there's a work quota we have to meet or else we get \"fired\". All of the sudden these riot gear guys started roaming around these halls like they're patrolling something{/font}"
    centered "{font=Dudu_Calligraphy.ttf}They’re holding way too overkill of equipment for simple security so what are they here for? They seem to particularly needed in the higher floors... {/font}"
    centered "{font=Dudu_Calligraphy.ttf}My buddy Charlie couldn't deal with all the changes so he quit. He never answer my calls anymore.{/font}"
    centered "{font=Dudu_Calligraphy.ttf}The CEO seemed so nice in passing... but how could he have let this happen? I don't want to work here anymore but I'm scared I'll find out what happen to Charlie if I do...{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"

    p "Armoured men? Disappearances? Work quota? Sounds like they didn't have much agency..."
    
    if vinnie_dead == False:
        v "Exactly why you never sign your soul away to a corporate entity. You become another cog in the endless wheel. The cruelest part is, even if you DO know what will happen you still have no choice but to submit"
        v "Most aren't fortunate enough to pick the job they want... \"why don't you just quit?\" Because theres never not strings attached, be it a strike on your record or no income"
    
    p "Welcome to hell, your work shift starts now"
   
    if rocky_dead == False:
        r "You may think the business you work with would never take advantage of you like others. But the truth is, money comes first. Whether it be demotions, firings, or write offs. You aren't safe with any type of mangament. They'll swap their models as they see fit. Profit comes first" 
   
    if norman_dead == False:
        n "Sounds like you've been through a lot...I- I've never really had to get a job..."

    if vinnie_dead and norman_dead == False:
        v "It's OK! We still love you, you trust fund baby!!!"

    jump pnc_loop    


label worker_memo:
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Dudu_Calligraphy.ttf} Ashley Cooper - Ethics Officer:REMINDER TO BELOVED SAMSARA ENTERPRISES EMPLOYEES:{/font}"
    centered "{font=Dudu_Calligraphy.ttf}We've heard your dissatisfaction with a particular conduct we practice here at Samsara!~ We're a big happy family all in this together so you're happiness is our number one priority! {/font}"
    centered "{font=Dudu_Calligraphy.ttf}I promise that we have heard you and we'll listen to your words! There will be representatives establishing some new changes around here on Friday so make sure to be here. No matter what. {/font}"
    centered "{font=Dudu_Calligraphy.ttf}:Failure to be appear will result in appropriate action:{/font}"

    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"

    p "I would NOT like to meet who wrote this in person, seems like a real piece of work"

    if rocky_dead == False:
        r "Honeyed words from a seasoned liar! That bitch!"

    if vinnie_dead == False:
        v "Ah yes the classic ol' \"we love you!\" manipulation tactic B.S."

    if norman_dead == False:
        n "The date they were supposed to meet was today! Is that related to how they're all..."
    if vinnie_dead == False:
        v "Man, it sucks how people take others for granted, her emotional exploitation on those she sees as \"lower\" than her because of her ranking just shows how insecure she is"
        v "People suffer all because of one person's much needed ego check, why is it that people like that are usually put in charge? Do you HAVE to be a scumbag to reach the top? Because the only way to climb that high is to step on the fingers of others?"
        v "I had teen parents and they had no idea how to take care of me and my siblings, we all fended for ourselves while our parents got fucked up at some random party. My older siblings are like our true parents"
        v "Why is it that the rest have to suffer from the sins of the few? As long as CPS sees that you're fed and clean they don't give a shit. Only reason we weren't was from OUR own efforts not our parents"
        v "Who came up with that system? They saw abused children and went on with their day. One less paper to fill out, is that all we are to them?"
        v "The water seeps through the cracks in the rules and drowns the rest of us... Why did those responsible not take better care of us?"
        v "My parents mellowed out when they got much older and apologized, but still, it's too little too late..."
        if norman_dead == False:
            n "I'm so sorry Vinnie...."
        menu:
            "It's our duty to point it out, you're on the right track" if insanity_level == 0:
                p "When you see something wrong, don't let them get away with it. It's how the cycle repeats over and over again. They do it because they can, but we won't let them. Right?"
                v "But why should it be our responsibility if someone else messes up?"
                p "It's our responsibility to call it out and make sure no one else suffers as much as we did. If we saw and kept silent, we would be complicit right? It's ok to take the time you need, but make sure it isn't too late"
                v "[pov]... That's... real clever actually... yeah... YEAH!!! Corruption only exists because we let it! Once I get home I'm suing everyone's asses for a drazillion dollars!!!"
                v "I'm gonna boycott this place and yell to this heavens how they mistreated their employees here! Once Samsara of all companies gets in trouble EVERYONE ELSE IS NEXT!!!"
                $ expose_samsara_together_2 == True
                if norman_dead == False:
                    "...!"

            "Relax, let's keep going":
                v "...Whatever"

        if rocky_dead == False:
            r "Fuck, I'm sorry man I wasn't there for you sooner. If I- I had known more about you I wouldn't have been so hard on you..."
            v "Dude, don't even. I was like a child and we didn't even know each other at the time, what were you gonna do as a 9 year old, suplex adults twice your size?"
            v "You couldn't have known plus you had your own shit you were dealing with at the time. You were right to call out my immaturity, I take it too far sometimes. You fixed me..."
            v "My {i}harmless{/i} pranks and antics landed me in jail... You convinced me to stop where I did... Who knows where I would be without you... thank you..."
            r "Vinnie..."
            "Rocky and Vinnie stare at each other before breaking away and taking a few steps in the opposite direction"
        if norman_dead == False:
            n "I- I'm in shock, Vinnie told me they had a bad childhood but I didn't know how bad it was"
            n "Vinnie... Rocky... they had such a hard life... I need to be there for them, It's the least I can do as their friend"
        menu:
            "People can be there for you too":
                $ norman_affection += 1
                n "[pov], you're such a good person... I mean that y'know... I'll make sure to let you know if I'm having any doubts... Thank you, for thinking about me"
            "Alright":
                "..."
    
    jump pnc_loop

label office_corpses:
    scene office window with dissolve
    "Various corpses are strewn about, some seem to have been eaten while a few are shredded with bullet holes. I don't understand how they were able to die if they had access to machine guns..."
    "... Where even are the people with machine guns if they're not dead in here?"
    jump pnc_loop


label office_floor_ending:
    pause 0.3
    scene office hall with dissolve
    if tara == True:
        if rocky_dead == False:
            "Rocky is carrying Tara on his back"
            w "Ah, apologies for the inconvenience"
            r "Are you kidding me?!?! You're arm is gone! What kind of person would I be if I left you on your own?"
            if vinnie_dead == False:
                v "Hey! Make sure to take care of my patient you blockhead! Don't yell at her!"
                r "I am LITERALLY carrying her right now how is this mistreatment???"
                v "She can smell the steak and beer on your breath from your late night binge sessions you mangy dog!"
                r "I haven't done that in years how are you still holding that against me?!?!"
                w "Hahaha! You have quite the friends here [pov]!"

        if rocky_dead == True and vinnie_dead == False:
            v "Are you ok? Can you stand?"
            "Vinnie has Tara lean on their shoulders"
            v "I had a friend who could of carried you better, he- he didn't make it..."
            w "Oh, I'm so sorry to hear that... I promise you we will hold whoever is responsible for this accountable"
            v "...thank you..."

        if rocky_dead and vinnie_dead == True:
            "Norman and I are standing Tara up side from side"
            w "Sorry, for slowing you two down.."

        n "Don't worry! Tara we're all in this together!" 
    if insanity_level == 0:
        p "I can't believe we've made it this for guys! We got this!"       
    if closet_broken == True:
        n "I feel bad for that woman in the closet but, she'll most likely bleed out if we stand her up right now... it's best to wait and we'll come back once we found something to help her" 
    pause 0.2
    s "...Stop what you're doing."
    "Out of nowhere a booming voice echoes from the speakers in the ceilings"
    
    if tara == True:
        w "F- Father?!?"
        
        if rocky_dead == False:
            "Rocky sets Tara behind a potted plant"
            r "Here girl, don't come out no matter what..."
            if vinnie_dead == False:
                v "Listen to him Tara, don't make a noise..."

        if rocky_dead == True and vinnie_dead == False:
            "Vinnie hides Tara behind a potted plant"
            v "Here! Don't make a peep!"

        if rocky_dead and vinnie_dead == True:
            "Norman and I set Tara down and hide her behind a potted plant"
            n "Don't make a sound Tara..."


    "I hear the express elevator rumbling as if it were currently in use, it eventually comes to a sudden stop and the doors slide open to reveal..."
    "A man in a black armour suit! He's carrying a stun baton and lunges at us!"
   
    if tara == True:
        
        if rocky_dead == False:
            "Rocky sets Tara behind a potted plant"
            r "Here girl, don't come out no matter what..."
            if vinnie_dead == False:
                v "Listen to him Tara, don't make a noise..."

        if rocky_dead == True and vinnie_dead == False:
            "Vinnie hides Tara behind a potted plant"
            v "Here! Don't make a peep!"

        if rocky_dead and vinnie_dead == True:
            "Norman and I set Tara down and hide her behind a potted plant"
            n "Don't make a sound Tara..."
    
    s "...Kill them all"

    if tara or closet_broken == True:
        s "...Get the girl once the rest are dispatched" 

    s "...Detonate the bomb afterwards"

    if norman_has_gun == True:
        play sound "audio/sfx/shoot.ogg"
        $ ammo -=1
        "He goes for Norman but the latter shoots a bullet straight at the man's face! His helmet protects him but Norman's gun makes it so that he goes for someone else instead!"
        jump vinnie_v_juggernaut
    else:
        menu:
            "What can I do to help Norman?"

            "I save myself and do nothing!":
                $ insanity_level += 1
                $ norman_health -=2
                play sound "audio/sfx/punch.ogg"
                if norman_health <= 1:
                    $ norman_office_death == True
                n "Unf!"
                "Norman is brought down to the floor from the stun baton and isn't getting up..."
                jump vinnie_v_juggernaut
                
            "Push Norman into danger" if insanity_level >= 1 and norman_affection <= 1 and tara == False and rocky_dead and vinnie_dead == True:
                $ norman_health -=5
                $ insanity == 100
                $ norman_secret_death == True
                $ norman_office_death == True
                $ norman_dead == True
                n "Unf!!"
                "I shove Norman so he falters to the ground as the man beats him down, Norman is brought down to the floor from the stun baton and isn't getting up..."
                jump vinnie_v_juggernaut

            "I tell Vinnie to stab the armored man with their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                v "Got it! I'll save you Norm!"
                "Vinnie rushes in front of Norman and penetrates the armored man's protected neck with their butterfly knife, the armored man yanks it out before crushing it with his hands"
                jump vinnie_v_juggernaut
           
            "I tell Vinnie to save Norman!" if vinnies_knife == False:
                if expose_samsara_together_2 == True:
                    v "I got you Norman!"
                    "Vinnie helps Norman with no issue"
                else:
                    $ vinnie_health -= 1
                    if vinnie_health <= 1:
                        $ vinnie_office_death == True
                    v "Got it! I'll save you Norm! OW!"
                    "Vinnie punches the man but gets punched back HARD in the face"
                jump vinnie_v_juggernaut

            "I headbutt the man with my horns!":
                if norman_affection >= 0:
                    play sound "audio/sfx/punch.ogg"
                    "He thinks he could attack Norman?!? I run forward headfirst and stab the man's chest with my horns, I don't care about the pain I need Norman safe!" with hpunch
                    jump vinnie_v_juggernaut
                else:
                    $ sage_health -= 1
                    play sound "audio/sfx/punch.ogg"
                    "I run forward headfirst and stab the man's chest with my horns, I feel my brain hit the roof of my skull as I deter the man off course" with hpunch
                    if sage_health <= 1:
                        jump death_screen             
                    jump vinnie_v_juggernaut
            
            "I shoot the man!" if sage_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I shoot the man right in his helmet! It blocks the bullet but at least it distracts him from Norman"
                jump vinnie_v_juggernaut
            
            "I crowbar the man!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/punch.ogg"
                $ crowbar_collected == False
                "I use my crowbar to hit the man over the head, he stumbles in response before grabbing it out of my arms and throwing it across the room"
                "The crowbar was lost in the scuffle but at least Norman was protected"
                jump vinnie_v_juggernaut

            "I tell Rocky to save Norman!" if rocky_dead == False:
                if expose_samsara_together:
                    play sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 1
                    if rocky_health <= 1:
                        $ rocky_office_death == True
                    "Rocky tries to bear hug the man but gets punched in the chest and knocked to the floor, he's able to recover slightly!"
                    r "*cough* *hack* *wheeze*"
                    jump vinnie_v_juggernaut
                elif crowbar_collected:
                    play sound "audio/sfx/punch.ogg"
                    "Rocky tries to bear hug the man but gets punched in the chest and knocked to the floor, he looks hurt..."
                    r "*cough* *hack* *wheeze* *wheeze*"
                    if rocky_health <= 1:
                        $ rocky_office_death == True
                    $ rocky_health -= 2
                    jump vinnie_v_juggernaut
                else:
                    play sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 3
                    if rocky_health <= 1:
                        $ rocky_office_death == True
                    "Rocky tries to bear hug the man but gets punched in the chest and knocked to the floor, he looks pretty hurt and even coughs up blood..."
                    r "*cough* *hack* *cough* *wheeze* *wheeze* *sputter*"
                    jump vinnie_v_juggernaut

label vinnie_v_juggernaut:
    if vinnie_dead == True:
        jump rocky_v_juggernaut
    else:
        v "HEY!!! DONUT PUNCHER OVER HERE!!!"
        "The armored man shoots his head toward Vinnie and makes a run for them!"
        menu:
            "What can I do to help Vinnie?"

            "I save myself and do nothing!":
                $ insanity_level += 1
                $ vinnie_health -=2
                if vinnie_health <= 1:
                    $ vinnie_office_death == True
                play sound "audio/sfx/punch.ogg"
                v "OW DAMN!!!"
                "Vinnie is brought down to the floor from the stun baton and isn't getting up..."
                jump rocky_v_juggernaut
                
            "I tell Vinnie to stab the armored man with their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                v "TAKE IT YOU FUGLY HO!!!"
                "Vinnie dashes forward and penetrates the armored man's protected neck with their butterfly knife, the armored man yanks it out before crushing it with his hands"
                jump rocky_v_juggernaut
           
            "I tell Norman to save Vinnie!":
                $ norman_health -= 1
                if norman_health <= 1:
                    $ norman_office_death == True
                n "AAAAAAAAAAAHHHHH!!!!" with hpunch
                "Norman blocks Vinnie with his body but takes the strike instead!"
                jump rocky_v_juggernaut

            "I tell Norman to shoot the man!" if norman_has_gun and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "Norman shoots him in the face, the man is stunned in return!"
                jump rocky_v_juggernaut

            "I headbutt the man with my horns!":
                if norman_affection >= 0:
                    play sound "audio/sfx/punch.ogg"
                    "He thinks he could attack Norman?!? I run forward headfirst and stab the man's chest with my horns, I don't care about the pain I need Norman safe!" with hpunch
                    jump rocky_v_juggernaut
                else:
                    $ sage_health -= 1
                    play sound "audio/sfx/punch.ogg"
                    "I run forward headfirst and stab the man's chest with my horns, I feel my brain hit the roof of my skull as I deter the man off course" with hpunch
                    if sage_health <= 1:
                        jump death_screen                    
                    jump rocky_v_juggernaut
            
            "I shoot the man!" if sage_has_gun == True and ammo >= 1:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I shoot the man right in his helmet! It blocks the bullet but at least it distracts him from attacking Vinnie"
                jump rocky_v_juggernaut

            "I crowbar the man!" if crowbar_collected and rocky_dead == True:
                play sound "audio/sfx/punch.ogg"
                $ crowbar_collected == False
                "I use my crowbar to hit the man over the head, he stumbles in response before grabbing it out of my arms and throwing it across the room"
                "The crowbar was lost in the scuffle but at least Vinnie was protected"
                jump rocky_v_juggernaut

            "I tell Rocky to save Vinnie!" if rocky_dead == False:
                if expose_samsara_together:
                    play sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 1
                    if rocky_health <= 1:
                        $ rocky_office_death == True
                    r "NOT IF I HAVE ANYTHING TO DO WITH IT YOU CUCK!!!"
                    "Rocky blocks the strike against Vinnie, shrugs it off, and even throws a return punch which knocks the man off guard!"
                    jump rocky_v_juggernaut
                elif crowbar_collected:
                    play sound "audio/sfx/punch.ogg"
                    "Rocky blocks the man's baton strike with the crowbar but it gets snapped in the process, the man kicks rocky in the groin!"
                    r "*wheeze*"
                    v "Rocky! No!"
                    $ rocky_health -= 2
                    jump rocky_v_juggernaut

                else:
                    play sound "audio/sfx/punch.ogg"
                    $ rocky_health -= 3
                    if rocky_health <= 1:
                        $ rocky_office_death == True
                    "Rocky grabs the man's baton strike with his bare hands and gets struck in the process, the man proceeds to strike Rocky over the head with the baton. Rocky's in a terrible state..."
                    r "Ugh... *cough* *hack*"
                    jump rocky_v_juggernaut

label rocky_v_juggernaut:
    if rocky_dead == True:
        jump juggernaut_zombie_aftermath
    else:
        r "YOU ROTTEN BASTARD WHY DON'T YOU PICK ON SOMEONE YOUR OWN SIZE? WHAT ARE YOU WAITING FOR!"
        menu:
            "While the man dashes furiously towards Rocky, must've really got under his skin, what can I do to help?"
             
            "I save myself and do nothing!":
                $ insanity_level += 1
                $ rocky_health -=3
                if rocky_health <= 1:
                    $ rocky_office_death == True
                play sound "audio/sfx/punch.ogg"
                r "*retches*"
                "Rocky is brought down to the floor from the stun baton and isn't getting back up at all... is he breathing?"
                jump juggernaut_zombie_aftermath

            "I tell Vinnie to stab the armored man with their knife!" if vinnies_knife == True:
                $ vinnies_knife = False
                v "DIE YOU DICK!!"
                "Vinnie dashes forward and penetrates the armored man's protected neck with their butterfly knife, the armored man yanks it out before crushing it with his hands"
                jump juggernaut_zombie_aftermath
            
            "I tell Norman to save Rocky!":
                $ norman_health -= 1
                if rocky_health <= 1:
                    $ rocky_office_death == True
                n "AAAAAAAAAAAHHHHH!!!!" with hpunch
                "Norman blocks Rocky with his body but takes the strike instead!"
                jump juggernaut_zombie_aftermath

            "I tell Norman to shoot the man!" if norman_has_gun:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "Norman shoots him in the face, the man is stunned in return!"
                jump juggernaut_zombie_aftermath

            "I headbutt the man with my horns!":
                $ sage_health -= 1
                play sound "audio/sfx/punch.ogg"
                "I run forward headfirst and stab the man's chest with my horns, I feel my brain hit the roof of my skull as I deter the man off course" with hpunch
                if rocky_health <= 1:
                    jump death_screen
                jump juggernaut_zombie_aftermath
            
            "I shoot the man!" if sage_has_gun == True:
                $ ammo -= 1
                play sound "audio/sfx/shoot.ogg"
                "I shoot the man right in his helmet! It blocks the bullet but at least it distracts him from attacking Vinnie"
                jump juggernaut_zombie_aftermath
            
            "I tell Rocky to crowbar the man!" if crowbar_collected == True:
                play sound "audio/sfx/punch.ogg"
                if expose_samsara_together_2 == True:
                    "Rocky bashes the man over the head with it, before the man could retaliate Rocky hits him again!"
                else:
                    $ crowbar_collected == False
                    "Rocky bashes the man over the head with it but the man grabs it and breaks it in response"
                jump juggernaut_zombie_aftermath

            "I tell Vinnie to save Rocky!" if vinnie_dead == False:
                play sound "audio/sfx/punch.ogg"
                if expose_samsara_together_2 == True:
                    v "SUCK ON THIS!!!"
                    "Vinnie runs to protect Rocky and does so without a hitch!"
                else:
                    $ vinnie_health -= 1
                    if vinnie_health <= 1:
                        $ vinnie_office_death == True
                    "As Vinnie runs to protect Rocky, the armored man grabs Vinnie by the neck before throwing him to the floor"
                    v "Unnhhhh..."

                jump juggernaut_zombie_aftermath

label juggernaut_zombie_aftermath:
    
        if tara == True:
            w "Leave them alone!"
            "Apparently Tara ran off to grab a desk lamp and clubbed the man over the head with it!"
        if rocky_health >= 1:
            r "HOW MUCH MORE CAN HE POSSIBLY TAKE?"                 

        "I've had enough of this, I jumped onto the man's back and straddled his back. I then removed his helmet which revealed..."
        "A completely decayed face not unlike the zombies! The man groaned in returned and tried reaching for his helmet"

        if tara == True:
            "Tara kicks it away far away from his grasp"

        if norman_health >= 1:
            n "He's more focused on his helmet more than us!"

        "He's dead set on grabbing that helmet and sprints to put it back on! When his back is turned I realized he's wearing an explosive belt and a detonator in his pocket"
        
        if tara == True:
            w "Now's our chance!"

        if vinnie_health >= 1:
            v "Take the detonator with you! You could explode his ass! {i}pause{/i}"        
        
        if tara == True or rocky_health >= 1 or norman_health >= 1 or vinnie_health >= 1:
            "I snatch the detonator away from his we all sprint inside the express elevator"
        else:
            "I snatch the detonator away from him as I sprint inside the express elevator"

        if vinnie_office_death == True:
            $ vinnie_dead = True
            "We're forced to leave Vinnie behind as they lay deceased on the floor"

        if rocky_office_death == True:
            $ rocky_dead = True
            "Rocky is left behind as they're no longer with us, he took quite the beating for us to escape..."
            
        if norman_office_death == True:
            $ norman_dead == True
            "Norman was killed in action, no time to carry him as I run"
            if norman_affection >= 1:
                "Norman, my Norman... no... I will avenge you..."
                "...I loved you..."
            elif insanity_level >= 1:
                "Oh well, no skin off my nose"
            if norman_has_gun:
                "I quickly snatch the gun he carried while on my way"

        ##THEY'RE IN THE ELEVATOR NOW!!!!!!
        scene black with dissolve
        pause 0.3
        scene elevator with dissolve

        if tara == True or rocky_health >= 1 or norman_health >= 1 or vinnie_health >= 1:
            "They urge me to press the button and as soon as I do-"
        else:
            "I press the button and as soon as I do-"
        play sound "audio/sfx/explode.ogg"
        "The elevator rumbles for a bit as is it explodes beneath us... I wonder if it took out the whole floor or not?" with vpunch
        "..."
        if insanity_level >= 0:
            p "What a pathetic creature..."
        else:
            p "That was certainly quite the experience"
        "It's deadly quiet for a while..."

        if vinnie_health <= 1 and rocky_health >= 1:
            "Rocky stares absentmindedly at the floor..., he must be thinking about Vinnie. I hear him whisper some, I think religious, chant under his breath"
            r "Vinnie... Vinnie... you- y- you can-'t be..."
            r "Dear god... what kind of world does this... who would do this? Why them... why me..."
            if norman_health >= 1:
                "Norman rubs circles on his back for a bit"
                n "It's ok... It's ok... I miss them too... it's ok to cry..."
                "..."
            r "Vinnie I-..."
            "Rocky's voice breaks before they quit their attempt at speaking and remain silent"
            if insanity_level >= 0:
                "Maybe they shouldn't have gotten themselves killed then..."
            else:
                "I'm gonna miss Vinnie, their humor, their voice, their spirit to keep us happy..."
            pause 0.3

        if rocky_health >= 1 and rocky_health <= 1:
            call vinnie_reaction_rocky_death
        
        if rocky_health <= 1 or rocky_health <= 1 or norman_health <= 1 and tara == True:
            w "I'm so sorry about what happened with..."

        if vinnie_health >= 1 and norman_dead and rocky_dead == False:
            v "WE WOOOOOOOOOON!!!!!!!!!!!! YIIIIIIIIIPIIIIIIIIIIIEEEEE!!!!"
            if rocky_health >= 1:
                v "KISS ME ON THE MOUTH ROCKY!!! CARRY ME BRIDAL STYLE!!!"
                if tara == True:
                    r "The hell?? I'm not carrying you!!! AND TARA!"
                    w "They look so excited though! Why don't we swap places?"
                    v "DOCTOR'S ORDERS THAT YOU LISTEN TO MY PATIENT'S EVERY DEMAND!!!"
                else:
                    r "The hell?? I'm not carrying you!!!"
                "Rocky grabs Vinnie's face cheeks and squishes them so Vinnie's tongue lolls out before shoving them across the elevator"

        if rocky_health >= 1 and norman_dead and vinnie_dead == False:
            r "Holy- I thought that was it for us, I didn't think we would make it"
        if tara == True or rocky_health >= 1 or norman_health >= 1 or vinnie_health >= 1:
            n "Great team effort everyone!"
            "Norman starts inspecting our wounds to see if anything could be done"
        
        if norman_dead == True:
            if vinnie_dead == False:
                v "Norman... no god no not Norman of all people..."
                if rocky_dead == True:
                    v "First Rocky now this?!?!"
                v "This is too much... I can't... I can't..."

            if rocky_dead == False:
                r "Norman... if you can hear this.. I- I failed you..."
                if vinnie_dead == True:
                    r "Couldn't protect Vinnie... couldn't protect you..."
                r "What kind of man am I? Why did I live..."

        if norman_health >= 1:
            n "Great effort! Great effort!"
            if norman_affection >= 1:
                "Norman inspects me to see if I'm ok"
                if sage_health <= 3:
                    n "Oh no, you look pretty banged up there [pov], are you ok?"
                    if insanity_level >= 1:
                        p "Quit fussing"
                    else:
                        p "I'm fine, thanks for asking"
                else:
                    n "Glad to see you're ok [pov]!"
                    if insanity_level >= 1:
                        p "..."
                    else:
                        p "Ditto Norman!"                    

        p "What even was that thing? It looked and acted a lot like one of the zombies"
        if tara == True:
            w "I- I have some explaining to do. It's the least I can do... From now on there will be 100 percent honesty from me"
            w "The CEO is my father... He's always been {i}off{/i}, doesn't think the same way regular people do. Imagine a child with a magnifying glass vs. an ant colony"
            w "The child has no comprehension over the significance of ending one's life. He sees the world revolved around him, and only him, everything else is seen as a prop or asset for him"
            w "The ants are his plaything and no one can convince him otherwise because ants ARE meaningless in the eyes of others"
            w "I suppose I was treated well enough, never directly hurt, just sort of... cast to the side. As if I was yet another prop that adds a nice \"family\" man flavor to him in his public persona"
            w "I noticed his true personality as I got older, I'm 22 now, it was only recently that I figured out the extent. When I confronted him about it, he put me on house arrest so I escaped and infiltrated my way here as an employee"
            w "My plan was to personally confront him in his office while working undercover but, I had no idea he has this plague in mind... I'm sorry for not being truthful, I was trying to figure out the right time to tell you"

            if insanity_level >= 0:
                "This bitch is hiding things from me, she can't be trusted"
            else:
                p "It's ok, I understand. What's important is that you're telling now" 
            if vinnie_health >= 1:
                v "Talk about daddy issues girl..."
            if rocky_health >= 1:
                r "No parent should treat their own family like that, what a degenerate. Keep close to us ok?"
            if norman_health >= 1:
                n "I'm so sorry to hear that, I can relate to a distant family like that"
            w "That \"thing\" was specifically sent to retrieve me and kill you, I don't want to endanger you..."
            if insanity_level >= 0:
                "Maybe you'd be better left behind but I can't exactly throw you out right now..."
            p "We're always in danger so it doesn't matter if you're gone or not you're staying with us"             
            if vinnie_health >= 1:
                v "MY PATIENT CAN'T LEAVE UNTIL YOU GET YOUR DOCTOR REFERRAL, STAY WITH US TARA!!!"
            if norman_health >= 1:
                n "Yeah!!! Join us!!"
            w "T- thank you..., the top floor should have access to the rooftop and we could flag a helicopter from there"
        p "Hmm the floor this elevator leads to is labelled as a \"laboratory\", well this should be fun..."
        "Time passes"
        pause 0.2
        if norman_health >= 1 and norman_affection >= 2:
            "Norman scoots very close next to me, almost leaning against my shoulder"
            n "Hey [pov]... I'm scared, so scared of dying..."
            if rocky_health >= 1:
                n "Rocky's dead..."
            if vinnie_health >= 1:
                n "Vinnie's dead..."
            if closet_broken == True:
                n "That girl we left behind in the closet is probably dead..."
            n "How much longer do {i}we{/i} have? I- I don't want to die or see anymore dead people... please help me..."
            n "I'm so afraid of being seen as weak... because pretending to have it under control is all I have... I can't EVER show myself because the people who rely on me will see me as the fraud I am..."
            menu:
                "You're no fraud {i}especially{/i} to {i}me{/i}":
                    $ norman_affection +=1
                    "I wrap Norman in a tight embrace and hold him closer"
                    n "[pov]... [pov]..."
                    "He only now starts hugging back, I think I can hear his tail wag"
                    n "Haahaa why can't this elevator last a little bit longer?"
                    p "I wish it did to"
                    pause 0.3 
                    "We eventually unwrap our arms around each other but continue to hold hands"
                    if vinnie_health >= 1 and rocky_health >= 1:
                        "Vinnie and Rocky are off in the corner pretending not to look at us while whispering into each other's ears"
                        v "*sniffle* *sniffle* Our lil' Normie and [pov] are becoming big grown muscular 6'9 men right before our very eyes... They grow up so fast I'M NOT READY TO LET THEM LEAVE THE NEST YET!! WAAAAAAA!!!! HOLD ME ROCKY!!!"
                        r "Stop it you're embarrassing them! If you don't shut your hag mouth you're gonna scare them from each other! I'm personally very glad to see Norman and [pov] so happy, I've never seen either so ecstatic before"
                        v "*hic* I am too..."
                    if vinnie_health <= 1 and rocky_health >= 1:
                        r "I'm proud of two, truly, you have my blessing for whatever that's worth. Vinnie also would be cool with it, learn from their and my mistakes..."
                    if vinnie_health >= 1 and rocky_health <= 1:
                        v "It warms my heart to see you two be together. Rocky also would approve, make sure never to let go of each other like we did..."
                    if tara == True:
                        "Tara gives a thumbs up and wink from across the elevator"
                        
                "Just forget about it":
                    n "...I guess it can't be a problem if It's not acknowledged..."

        jump lab_floor_3

label get_password:
    $ password_input = renpy.input("What's the password?", length = 8)

    if password_input == password:
        jump correct_password
    else:
        jump wrong_password
    return

label correct_password:
    play sound "audio/sfx/correct beep.ogg"
    "{size=*1}{color=#15ff00}EXPRESS ELEVATOR ACCESS GRANTED{/color}{/size}"
    p "That was it! That opened up another way for us to go!"
    if norman_dead == False:
        n "Great job team us! Woo Woo!"
    if vinnie_dead == False:
        v "Well that was tedious!"
    if rocky_dead == False:
        r "Yeah! We got this team! Nice job [pov]!"
    if tara == True:
        p "Let's go get Tara and be on our way"
    scene black with dissolve
    if norman_dead and vinnie_dead and rocky_dead == True:
        "I make my way towards the express elevator the computer said"
    else:
        "We make our way towards the express elevator the computer said"
    jump office_floor_ending
    return

label wrong_password:
    play sound "audio/sfx/wrong beep.ogg"
    "{size=*1}{color=#f00}PASSWORD INCORRECT{/color}{/size}"
    hide screen input_pw_button
    jump pnc_loop
    return

screen input_pw_button:
    textbutton "Click here to input the password.":
        align (0.5,0.5)
        text_color "#ff0000"
        action [Jump("get_password"), Return()]