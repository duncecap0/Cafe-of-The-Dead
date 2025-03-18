label endings:
    stop sound
    stop music
    # play music "audio/music/"
    scene rooftop with flash
    "The door slides open to reveal an ashen cityscape, this is the first I've felt the outside air since the beginning of all this. I see the chopper circle around in the air, it's bound to notice if I call attention"
    if insanity_level >=1 and vinnie_dead and rocky_dead and norman_dead == True and tara == False:
        if norman_secret_death == True:
            omg "Did you think you could kill me?"
            "I hear a familiar voice as I turn around and see..."
            n '...'
            if norman_has_gun == True:
                "He pulled his gun on me..."
            "Doesn't seem too happy..."
            n "...[pov]... I thought I knew you..."
            n "..But the way you've acted... is no different than the monsters..."
            n "Only focusing on yourself, letting your \"friends\" die so you would live? Your lack of compassion... is mortifying..."
            n "You did it, you killed everyone. Was it worth it [pov]? Was it worth seeing the people who only wanted to help you die gruesome deaths?"
            n "Vinnie... Rocky... They're dead because of you..."
            if closet_broken == True and tara == False:
                n "Is that why you wanted us to leave the girl behind? Not because we didn't have the supplies.... but because she would hinder your survival!?!"
            n "You tricked me! You used me! You... you... {i}fucking{/i} freak..."
            p "Hmm? Is that right? As I recall, you thought quite highly of me before... are you by chance regretting it? I can't quite tell..."\
            n "I can't believe I ever thought highly of such a demented creature..."
            n "Did you think you could just walk away? Think again... I'm not letting you get away... not this time..."
            if sage_has_gun == True:
                "I could just shoot him... but no... I have something else in mind..."
            if norman_has_gun == True:
                "Norman is about to pull the trigger right before..."
            "I run as fast as my legs could carry me, headfirst into Norman's chest. My horns puncture him as he starts bleeding out"
            if norman_has_gun == True:
                "He dropped his gun out of reach, I don't need it though. I have something else in mind for him..."
            p "You couldn't save Vinnie, Rocky, or yourself!"
            "I say as I start strangling Norman, He clocks me in the side of the head before I bite down on his arm"
            "We start wrestling for a bit, each of us trying to surmount the other until I always find a way to stay on top, even if it means fighting dirty"
            if norman_affection >= 3:
                p "Aww what happened Norman? Not the type of wrestling with me you had in mind? Hahaha!"
                "He grimacess"
            if norman_has_gun == True:
                "Norman kept trying to crawl for his gun but I kept pulling him back by the ears and smashing his face into the ground"
            if sage_has_gun == True:
                "Norman kept trying to reach for the gun in my pocket but I always out of reach for him to grab it"
            "We kept fighting until we got the ledge of the rooftop... he was closer and I was a bit further away..."
            "As he was catching his breath, I charged into him with my arms pushed outwards"
            "He was sent over! But grabbed onto the ledge, I started stomping out his fingers"
            n "I. KNOW. WHAT. YOU. DID!"
            "Were his last words before dropping into the ocean of zombies down below..."
            "Good riddance..."
            "..."
            "I did it, I killed everyone who stood in my path."
        "Life, death, love, hate, creation, destruction, war, and peace. All meaningless in the end when it comes to it..."
        "What matters is the fact that {i}I{/i} am the one who controls it. {i}I{/i} am the one the world revolves around. {i}I{/i} decide who is worthy."
        "It doesn't matter if you don't agree with it, because the decision is up to me in the end"
        "\"How could you? How would like it if someone else was in control?\"{i} Exactly,{/i} you aren't."
        "Hail."
        return
    scene chopper with flash
    #play sound "audio/sfx/"
    scene black with dissolve
    "..."
    "About a week has passed since then, the government called the national guard and quarantined the city and nearby areas. Fortunately the virus was contained and the rest of the country remains unaffected"
    if vinnie_dead and rocky_dead and norman_dead == False:
        v "IT'S A PARTY GUYS!!!! EVERYONE!! BREAK DANCE NOW!!!"
        n "I thought we would be goners for a second there!"
        r "Those zombies were no match for us!"
        if tara == True:
            "We outsmarted those brainless dorks!"
        p "Let's hangout! In fact! Why don't we all get an apartment together?!?"
        r "I already pretty much am Vinnie's babysitter so that sounds good to me! I'm in!"
        v "YAY! I AM GOING TO THE BEST ROOMIE EVER! I CALL DIBS ON THE DOGHOUSE!!!"
        n "Of course! I love you guys so much! I wouldn't miss out on it for anything! Haha!"
        if tara == True:
            w "...Does that offer extend to me..."
            p "Yep! You're stuck with us!"
            w "Really?! I- I've never had friends before, only co-workers, THIS IS SO EXCITING!!"
        p "Great! We're almost like a real family now!"
        v "Oo! Oo! I am simutaneously the smexy smexy house wife and man of the house!"
        v "Rocky is the hen-pecked husband who obeys my commands!"
        v "Norman is are our daughter too good to be born to us!"
        v "[pov] is the homeless person who rifles through our trash that we let in!"
        if tara == True:
            v "And Tara is the person we kidnapped for ransom!"
        r "I would rather be eaten by the zombies then be married to you..."
        if norman_affection >=3:
            n "I was swooned by the homeless person!"
        else:
            n "Umm how did you two even birth me????"
            v "Mitosis."
        if tara == True:
            w "You'll all fare better than the last people who held me for ransom! Haha!"
        p "...What about me says I'm homeless?..."
        if expose_samsara_together and expose_samsara_together_2 and expose_samsara_together_3:
            "The surviving board members of Samsara and it's associates were held accountable in the court of law and arrested for crimes against society, thanks to us exposing them!"              
        "We did it, we all lived. A lot of innocent people died in the city but we will never forget them..."
        "My friends are the best thing to have happened to me. Finally a family that accepts and loves me. I'm going to like it here!"    
    
    if vinnie_dead or norman_dead or rocky_dead == True:
        if vinnie_dead == False:
            "Vinnie never quite recovered from that day, they've been very isolated and haven't been communicating as they usually do"
            "Their funny quirks and quips are gone, replaced with quiet chuckles and longing stares at the floor"
            if rocky_dead == True:
                "They visited Rocky's parents to say how much Rocky meant to them and how he sacrificed himself so they could live"
            if norman_dead == True:
                "They visited Norman's family to apologize for failing to protect their son..."
            "I've only seen them once since then..."
        if rocky_dead == False:
                "Rocky isn't the same, I don't think he even works anymore. Just drinks his days away at some run down bar..."
                if vinnie_dead == True:
                    "They visited Vinnie's family to tell them what an inspiration Vinnie was to him and their death was his fault..."
                if norman_dead == True:
                    "They went to Norman's family to beg them to press charges for murder since he feels like he should be locked up for letting Norman die..."
        if norman_dead == False:
                "Norman is the only one who regularly meets up and starts the hangouts now, he seems much more jumpy and scared than back then"
                "He often checks in to see if everything is alright and if there's anything he could do"
                if rocky_dead or vinnie_dead == True:
                    "They keep a picture of all of us together in their jacket at all times..."
        if tara == True:
            "Tara has been kept in confinement from the government for being related to the CEO, she isn't arrested but might as well be..."
            "She sends letters saying how grateful she is and that she'll visit as soon as possible"
        "We've been trying to stay friends but it gets hard when we notice the people who are missing..."
        "It really makes me think... I wonder if there was anything I could've done differently?"

return

