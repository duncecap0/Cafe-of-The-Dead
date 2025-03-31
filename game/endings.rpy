label endings:
    scene rooftop with flash
    "The door slides open to reveal an ashen cityscape,{w=.3} this is the first time I've felt the outside air since we started... {w=.3}I see the chopper circle around in the air,{w=.3} it's bound to notice if I call attention"
    if vinnie_dead == False or rocky_dead == False or norman_dead == False or tara == True:
        "We wave our hands in the air, {w=.3}signalling the copter to land..."
    if insanity_level >=1 and vinnie_dead and rocky_dead and norman_dead == True and tara == False:
        if norman_secret_death == True:
            stop music fadeout 0.5
            play sound "audio/sfx/Wind.ogg"
            play music "audio/music/hail.ogg"
            omg "Did you think you could kill me?"
            "I hear a familiar voice as I turn around and see..."
            show n 5a with Dissolve(1.)
            n "..."
            if norman_has_gun == True:
                show n 2a
                "He pulled his gun on me..."
            else:
                show n 1a with dissolve
            "Doesn't seem too happy..."
            n "...[pov]... {w=.3}I thought I knew you..."
            n 8"I really thought you were my friend... you seemed so kind... so trustworthy... so dependable..."
            n 1a"...{w=.3}But the way you've acted...{w=.3} is no different than the monsters..."
            n "Only focusing on yourself,{w=.3} letting your {w=.3}\"friends\"{w=.3} die so you would live? Your lack of compassion...{w=.3} is mortifying..."
            n "You did it, you killed everyone. {w=.3}Was it worth it [pov]? Was it worth seeing the people who only wanted to help you die gruesome deaths?"
            n 8"Vinnie...{w=.3} Rocky...{w=.3} They're dead because of you..."
            if closet_broken == True and tara == False:
                n 1a"Is that why you wanted us to leave the girl behind? Not because we didn't have the supplies...{w=.3} but because she would hinder your survival!?!"
            n 1a"You tricked me! {w=.3}You used me!{w=.3} You...{w=.3} you...{w=.9} {i}fucking{/i}{w=.5} freak..."
            p 17"Hmm? Is that right? {w=.3}As I recall, {w=.3}you thought quite highly of me before... {w=.3}are you by chance regretting it? {w=.3}I can't quite tell..."
            n "I can't believe I ever thought highly of such a demented creature..."
            n "Did you think you could just walk away? {w=.3}Think again... {w=.3}I'm not letting you get away...{w=.3} not this time..."
            if sage_has_gun == True:
                "I could just shoot him...{w=.3} but no... {w=.3}I have something else in mind..."
            if norman_has_gun == True:
                "Norman is about to pull the trigger right before..."
            "I run as fast as my legs could carry me, headfirst into Norman's chest. {w=.3}My horns puncture him as he starts bleeding out"
            if norman_has_gun == True:
                "He dropped his gun, I don't need it though.{w=.3} I have something else in mind..."
            show n 15 at shiver_loop
            p 16"You couldn't save Vinnie,{w=.3} Rocky, or yourself!"
            "I say as I start strangling Norman, {w=.3}He clocks me in the side of the head before I bite down on his arm"
            "We start wrestling for a bit, {w=.3}each of us trying to surmount the other; I always find a way to stay on top, {w=.3}even if it means fighting dirty"
            if norman_affection >= 3:
                p 17"Aww what happened Norman?{w=.3} Not the type of wrestling with me you had in mind with me? Hahaha!"
                "He grimaces"
            if norman_has_gun == True:
                "Norman kept trying to crawl for the gun; I kept pulling him back by his ears and smashing his face into the ground"
            if sage_has_gun == True:
                "Norman kept trying to reach for the gun in my pocket but I make sure to keep it juuuuuuusst out of reach..."
            "We keep fighting until we get to the ledge of the rooftop...{w=.3} he was closer and I was a bit further away..."
            "As he was catching his breath,{w=.3} I charged into him with my arms pushed outwards"
            "He was sent over!{w=.3} But grabbed onto the ledge,{w=.3} I started stomping out his fingers"
            n "I. {w=.3}KNOW.{w=.3} WHAT.{w=.3} YOU. {w=.5}DID!"
            show n at offscreen_bottom with move
            show black with Dissolve(1.):
                alpha.6
            "Were his last words before dropping into the ocean of zombies down below..."
            "Good riddance..."
            show side p 17 with dissolve
            "..."
            "I did it, {w=.3}I killed everyone who stood in my path."
        scene black with fade
        p 17"Life,{w=.3} death, {w=.3}love, {w=.3}hate,{w=.3} creation, {w=.3}destruction,{w=.3} war, {w=.3}and peace. {w=.3}All meaningless in the end when it comes to it..."
        p 17"What matters is the fact that {i}I{/i} am the one who controls it. {w=.3}{i}I{/i} am the one the world revolves around. {w=.3}{i}I{/i} decide who is worthy."
        p 17"It doesn't matter if you don't agree with it,{w=.3} because the decision is up to me in the end"
        p 16"\"How could you?{w=.3} How would like it if someone else was in control?\" Exactly, {w=.8}{i}they aren't.{/i}"
        p 17"Prepare for the second coming."
        pause 1.0
        stop music fadeout 1.0
        "Hail."
        window hide diss
        jump insane_screen
    play sound "audio/sfx/chopper.ogg" fadein 2.0
    scene black with dissolve
    "..."
    "About a week has passed since then, {w=.3}the government called the national guard and quarantined the city and nearby areas.{w=.3} Fortunately, {w=.3}the virus was contained and the rest of the country remains unaffected"
    if vinnie_dead == False and rocky_dead == False and norman_dead == False:
        v "IT'S A PARTY GUYS!!!!{w=.3} EVERYONE!! BREAK DANCE NOW!!!"
        n "I thought we would be goners for a second there!"
        r "Those zombies were no match for us!"
        if tara == True:
            w "We outsmarted those brainless dorks!"
        p "Let's hangout! {w=.3}In fact!{w=.3} Why don't we all get an apartment together?!?"
        r "I already pretty much am Vinnie's babysitter so that sounds good to me! I'm in!"
        v "YAY!{w=.3} I AM GOING TO THE BEST ROOMIE EVER! I CALL DIBS ON THE DOGHOUSE!!! I already have six siblings so I'm used to living with a LOT of people!"
        n "Of course! I love you guys so much! I wouldn't miss out on it for anything! Haha!"
        if tara == True:
            w "...Does that offer extend to me..."
            w "I... {w=.3}don't really have anyone anymore... {w=.3}everyone I know is dead..."
            p "Yep! You're stuck with us!"
            w "Really?!{w=.3} I- {w=.3}I've never had real friends before, {w=.3}only co-workers, {w=.3}THIS IS SO EXCITING!!"
        p "Great! {w=.3}We're almost like a real family now!"
        v "Oo!{w=.3} Oo!{w=.3} I am simultaneously the smexy smexy house wife and man of the house!"
        v "Rocky is the hen-pecked husband who obeys my commands!"
        v "Norman is are our daughter too good to be born to us!"
        v "[pov] is the homeless person who rifles through our trash that we let in!"
        if tara == True:
            v "And Tara is the person we kidnapped for ransom!"
        r "I would rather be eaten by the zombies then be married to you..."
        if norman_affection >= 5:
            n "I was swooned by the homeless person!"
        n "Umm wait- {w=.3}how did you two even birth me????"
        v "Mitosis."

        if tara == True:
            w "You'll all fare better than the last people who held me for ransom! Haha!"

        p "...{w=.3}What about me says I'm homeless?..."
        window hide diss
        pause 1.0
        if expose_samsara_together and expose_samsara_together_2 and expose_samsara_together_3:
            show side p 4 with dissolve
            "The surviving board members of Samsara and it's associates were held accountable in the court of law and arrested for crimes against society,{w=.3} thanks to us exposing them!"
        show side p 8 with dissolve
        "We did it,{w=.3} we all lived.{w=.3} A lot of innocent people died in the city but we will never forget them..."
        show side p 13 with dissolve
        p "My friends are the best thing to have happened to me. {w=.3}Finally a family that accepts and loves me. I'm going to like it here!"
        show black with dissolve
        show side p 13
        show n 2 at left1  with dissolve
        show r 11 at left with dissolve
        show v 1 at right with dissolve
        if tara == True:
            show w 4 at right2 with dissolve
            pause 1.0
        "{size=*2}TRUE END{/size}" with dissolve
        "{size=*2}Thanks for playing!{/size}"
    
    if vinnie_dead == True or norman_dead == True or rocky_dead == True:
        if vinnie_dead == False:
            "Vinnie never quite recovered from that day,{w=.3} they've been very isolated and haven't been communicating as they usually do"
            "Their funny quirks and quips are gone,{w=.3} replaced with quiet chuckles and longing stares at the floor"
            if rocky_dead == True:
                "They visited Rocky's parents to say how much Rocky meant to them and how he sacrificed himself so they could live"
            if norman_dead == True:
                "They visited Norman's family to apologize for failing to protect their son..."
            "I've only seen them once since then..."
        if rocky_dead == False:
                "Rocky isn't the same,{w=.3} I don't think he even works anymore. {w=.3}Just drinks his days away at some run down bar..."
                if vinnie_dead == True:
                    "They visited Vinnie's family to tell them what an inspiration Vinnie was to him and that their death is his fault..."
                if norman_dead == True:
                    "They went to Norman's family to beg them to press charges for murder since he feels like he should be locked up for letting Norman die..."
        if norman_dead == False:
                "Norman regularly meets up and starts the hangouts now, he seems much more jumpy and scared than back then"
                "He often checks in to see if everything is alright and if there's anything he could do"
                if rocky_dead == True or vinnie_dead == True:
                    "They keep a picture of all of us together in their jacket at all times..."
                if norman_affection >= 5 and insanity_level == 0:
                    "He lives we me now in a small apartment. I'm doing the best I can to support him and make him comfortable..."
        if tara == True:
            "Tara has been kept in confinement from the government for being related to the CEO, {w=.3}she isn't arrested but might as well be..."
            "She sends letters saying how grateful she is and that she'll visit as soon as possible"
        if insanity_level >= 1:
            "Something inside me changed too... {w=.3}I don't feel the same anymore..."
        elif insanity >= 2:
            "I've definitely noticed a gear shift inside my brain.{w=.3} I can't understand emotions as well...{w=.3} I feel broken..."
        if norman_affection >= 4 and insanity_level >= 1 and norman_dead == False:
            "I feel like Norman wanted to start something with me but I can't reciprocate... {w=.3}I'm different now...{w=.5} empty..."
        "We've been trying to stay friends but it gets hard when we notice the missing space..."
        "It really makes me think...{w=.3} I wonder if there was anything I could've done differently?"
    window hide diss
    jump win_screen
return

