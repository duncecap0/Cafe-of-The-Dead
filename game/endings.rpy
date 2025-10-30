label endings:
    scene rooftop with flash
    "The elevator door slides open to reveal an ashen cityscape.{w=.3} I haven't felt outside air since everything began..."
    "I see the chopper circle around in the sky."
    if vinnie_dead == False or rocky_dead == False or norman_dead == False or tara == True:
        "We wave our hands in the air, {w=.3}signaling for the copter to land..."
    if insanity_level >=1 and vinnie_dead == True and rocky_dead == True and norman_dead == True and tara == False:
        if norman_secret_death == True:
            show static_anim with dissolve
            play audio "audio/sfx/static.ogg"
            camera:
                perspective True
                easein_bounce 0.54 zpos -20
            pause 0.3 
            hide static_anim with dissolve
            camera:
                reset
            stop music fadeout 0.5
            play sound "audio/sfx/Wind.ogg"
            play music "audio/music/hail.ogg"
            omg2 "Did you think you could kill me?"
            "I hear a familiar voice as I turn around to see..."
            show n 5a with dissolve
            n "..."
            if norman_has_gun == True:
                show n 2a
                "He pointed his gun at me..."
            else:
                show n 1a with dissolve
            "They don't seem so happy..."
            n "[pov]... {w=.3}I thought I knew you..."
            n 8"I really thought you were my friend...{w=.3} You seemed so kind...{w=.3} So trustworthy...{w=.3} So dependable..."
            n 1a"{w=.3}But the way you've acted...{w=.3} is no different than the monsters..."
            n "Only focusing on yourself,{w=.3} letting your {w=.3}\"friends\"{w=.3} die so you could live? Your lack of compassion...{w=.5} is mortifying..."
            n "You did it, {w=.3}you killed everyone. {w=.3}Was it worth it [pov]?{w=.3} Was it worth seeing the people who only wanted to help you. Die such gruesome deaths?"
            n 8"Vinnie...{w=.3} Rocky...{w=.3} They're dead because of you..."
            if closet_broken == True and tara == False:
                n 1a"Is that why you wanted us to leave the girl behind?{w=.3} Not because we didn't have the supplies...{w=.3} But because she would hinder your survival!?!"
                p 17"Don't play coy. You did the exact same."
            n 1a"You tricked me! {w=.3}You used me!{w=.3} You...{w=.3} you...{w=.9} {i}fucking{/i}{w=.5} freak..."
            p 17"Hmm? Is that right? {w=.3}As I recall, {w=.3}you thought quite highly of me before... {w=.3}Are you by chance regretting it? {w=.3}I can't quite tell..."
            n "I can't believe I ever thought highly of such a demented creature..."
            n "Did you think you could just walk away? {w=.3}Think again... {w=.3}I'm not letting you get away...{w=.3} Not this time..."
            if sage_has_gun == True:
                "I could just shoot him...{w=.3} But no... {w=.3}I have something else in mind..."
            if norman_has_gun == True:
                "Norman is about to pull the trigger right before..."
            "I run as fast as my legs could carry me. Headfirst into Norman's chest. {w=.3}My horns puncture him as he starts bleeding out."
            if norman_has_gun == True:
                "He dropped his gun; I don't need it though.{w=.3} I have something else in mind..."
            show n 15 at shiver_loop

            if closet_broken == True and tara == False:
                p 16"You couldn't save Vinnie,{w=.3} Rocky, that girl, or yourself!"
            else:
                p 16"You couldn't save Vinnie,{w=.3} Rocky, or yourself!"

            "I say as I start strangling Norman, {w=.3}He clocks me in the side of the head."
            "I bite down on his arm in response."
            "We start wrestling for a bit, {w=.3}each of us trying to surmount the other. I always find a way to stay on top, {w=.3}even if it means fighting dirty."
            if norman_affection >= 3:
                p 17"Awww, what happened Norman?{w=.3} Not the type of wrestling you had in mind with me?{w=.3} Hahahaha!"
                "He grimaces."
            if norman_has_gun == True:
                "Norman kept trying to crawl for the gun.{w=.3} I pulled him back by his ears and smashed his face into the ground."
            if sage_has_gun == True:
                "Norman kept trying to reach for the gun in my pocket, {w=.3}but I make sure to keep it juuuuuuusst out of reach..."
            "We keep fighting until we get to the edge of the rooftop.{w=.3} He was closer, and I was a bit further away..."
            "As he was catching his breath.{w=.3} I charged into him with my arms pushed outwards."
            "He was sent over.{w=.3} But grabbed onto the edge."
            "I started stomping out his fingers."
            n "I. {w=.5}KNOW.{w=.5} WHAT.{w=.5} YOU. {w=.5}DID!"
            p 17"Until you meet the pavement."
            show n at offscreen_bottom with move
            with vpunch
            show black with Dissolve(1.):
                alpha.6
            pause 5.0
            "Those were his last words before dropping into the ocean of zombies below..."
            "Good riddance."
            show side p 17 with dissolve
            "..."
            pause 1.0
            "I did it, {w=.3}I killed everyone who stood in my path."
            "They hindered my survival. Some people aren't meant for the apocalypse."
            pause 1.0
        scene black with fade
        p 17"Life,{w=.3} death, {w=.3}love, {w=.3}hate,{w=.3} creation, {w=.3}destruction,{w=.3} war, {w=.3}and peace. {w=.3}All meaningless in the end when it comes to it..."
        p 17"What matters is the fact that {i}I{/i} am the one who controls it. {w=.3}{i}I{/i} am the one the world revolves around. {w=.3}{i}I{/i} decide who is worthy."
        p 17"It doesn't matter if you don't agree with it,{w=.3} because the decision is up to me in the end."
        p 17"I've learned a great many things."
        p 17"Number one being that friendship is overrated."
        p 17"It didn't save anyone, now did it?"
        p 16"\"How could you?{w=.3} How would you like it if someone else was in control?\"{w=.3} Exactly, {w=.8}{i}they aren't.{/i}"
        pause 1.0
        stop music fadeout 1.0
        window hide diss
        if norman_secret_death == True:
            p 17"Prepare for the second coming."
            "Hail."
            $ notices.append("Ending Unlocked: Hail.")
            $ persistent.hailending = True
            $ config.window_title = _("Hail.")
            if norman_dead == True:
                $ notices.append("Achievement Unlocked: Taking The Dog Out Back")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.killnorman = True
            if vinnie_dead == True:
                $ notices.append("Achievement Unlocked: Roadkill After All")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.killvin = True
            if rocky_dead == True:
                $ notices.append("Achievement Unlocked: Wolf or Fox? Now We Will Never Know...")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.killrocky = True
            if tara == True:
                $ notices.append("Achievement Unlocked: Coming Out The Closet")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.savetara = True
            if tara_against_dad == True:
                $ notices.append("Achievement Unlocked: Escaping the Mad House")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.tara_against_dad = True
            if ammo >= 3:
                $ notices.append("Achievement Unlocked: I Don't Need No Dang Gun!")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.dontusebullets = True
            #if medkit_used == False and morphine_used == False and crowbar_collected == True and vinnies_knife == True and ammo == 3 and pills == False:
                #$ notices.append("Achievement Unlocked: Bad MotherFucker!")
                #play audio "audio/sfx/achievement.ogg"
                #$ persistent.dontuseitems = True
            if insanity_level == 0:
                $ notices.append("Achievement Unlocked: Coffee AU")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.nosanityloss = True
            if norman_affection >= 5:
                $ notices.append("Achievement Unlocked: Dog Boyfriend")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.romancenorman = True
            if expose_samsara_together == True and expose_samsara_together_2 == True and expose_samsara_together_3 == True:
                $ notices.append("Achievement Unlocked: Samsara's End")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.motivatefriends = True
            $ notify_me("and so it ends...")
            jump insane_screen
        else:
            if norman_dead == True:
                $ notices.append("Achievement Unlocked: Taking The Dog Out Back")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.killnorman = True
            if vinnie_dead == True:
                $ notices.append("Achievement Unlocked: Roadkill After All")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.killvin = True
            if rocky_dead == True:
                $ notices.append("Achievement Unlocked: Wolf or Fox? Now We Will Never Know...")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.killrocky = True
            if tara == True:
                $ notices.append("Achievement Unlocked: Coming Out The Closet")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.savetara = True
            if tara_against_dad == True:
                $ notices.append("Achievement Unlocked: Escaping the Mad House")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.tara_against_dad = True
            if ammo >= 3:
                $ notices.append("Achievement Unlocked: I Don't Need No Dang Gun!")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.dontusebullets = True
            #if medkit_used == False and morphine_used == False and crowbar_collected == True and vinnies_knife == True and ammo == 3 and pills == False:
                #$ notices.append("Achievement Unlocked: Bad MotherFucker!")
                #play audio "audio/sfx/achievement.ogg"
                #$ persistent.dontuseitems = True
            if insanity_level == 0:
                $ notices.append("Achievement Unlocked: Coffee AU")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.nosanityloss = True
            if norman_affection >= 5:
                $ notices.append("Achievement Unlocked: Dog Boyfriend")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.romancenorman = True
            if expose_samsara_together == True and expose_samsara_together_2 == True and expose_samsara_together_3 == True:
                $ notices.append("Achievement Unlocked: Samsara's End")
                play audio "audio/sfx/achievement.ogg"
                $ persistent.motivatefriends = True
            $ notify_me("and so it ends...")
            jump sad_screen

    play sound "audio/sfx/chopper.ogg" fadein 2.0
    scene black with dissolve
    "..."
    "About a week has passed since then.{w=.3} The government called the national guard and quarantined the city and nearby areas." 
    "Fortunately, {w=.3}the virus was contained. {w=.3}The rest of the country remains largely unaffected."
    if vinnie_dead == False and rocky_dead == False and norman_dead == False:
        v "IT'S A PARTY GUYS!!!!{w=.3} EVERYONE!!! BREAK DANCE NOW!!!"
        n "I thought we were goners for a second there!"
        r "Those zombies were no match for us!"
        if tara == True:
            w "We outsmarted those brainless dorks!"
        p "Let's hangout! {w=.3}In fact!{w=.3} Why don't we all get an apartment together?!?!"
        r "I'm already your babysitter. So that sounds good to me! I'm in!"
        v "YAY!{w=.3} I AM GOING TO THE BEST ROOMIE EVER! I CALL DIBS ON THE DOGHOUSE!!! I already have six siblings, so I'm used to living with a LOT of people!"
        n "Of course! I love you guys so much! I wouldn't miss out on it for anything! Haha!"
        if tara == True:
            w "...{w=.3}Does that offer extend to me."
            w "I... {w=.3}Don't really have anyone anymore..."
            p "Yep! You're stuck with us!"
            w "Really?! Finally! I get to hang out with the proletariat! {w=.3}THIS IS SO EXCITING!!!"
            w "Kidding! Kidding! Hahahaha!"
        p "Great! {w=.3}We're almost like a real family now!"
        v "Oo!{w=.3} Oo!{w=.3} I am simultaneously the smexy smexy housewife and man of the house!"
        v "Rocky is the hen-pecked husband who obeys my commands!"
        v "Norman is our daughter too good to be born to us!"
        v "[pov] is the homeless person who rifles through our trash that we let in!"
        if tara == True:
            v "And Tara is the person we kidnapped for ransom!"
        r "I would rather be eaten by the zombies than be married to you..."
        if norman_affection >= 5:
            n "Why did I get with the homeless person?!?!"
            if tara == True:
                w "You like the rugged vibe,{w=.3} right?"
        n "Ummm,{w=.3} wait- {w=.3}How are you two my parents if we're almost the same age?!?!"
        v "Asexual reproduction."

        if tara == True:
            w "You'll all fare better than the last people who held me for ransom! Haha!"

        p "...{w=.3}What about me says I'm homeless?"
        window hide diss
        pause 1.0
        if expose_samsara_together and expose_samsara_together_2 and expose_samsara_together_3:
            show side p 4 with dissolve
            "The surviving board members of Samsara and its associates were sent to court. They were arrested for their crimes against society."
            "All thanks for us exposing them!"
            "There's still some free remnants out there but not for long!"
        show side p 8 with dissolve
        "We did it,{w=.3} we all lived.{w=.3} A lot of innocent people died in the city, but we will never forget them..."
        show side p 13 with dissolve
        p "My friends are the best thing to have happened to me. {w=.3}Finally, a family that accepts and loves me. I'm going to like it here!"
        show black with dissolve
        show side p 13
        show n 2 at left1  with dissolve
        show r 11 at left with dissolve
        show v 1 at right with dissolve
        if tara == True:
            show w 4 at right2 with dissolve
        pause 1.0
        if tara == True:
            "{size=*2}TRUE END{/size}" with dissolve
            $ persistent.trueending = True
        else:
            "{size=*2}GOOD END{/size}" with dissolve
        "{size=*2}Thanks for playing!{/size}"
        
    if vinnie_dead == True or norman_dead == True or rocky_dead == True:
        if vinnie_dead == False:
            "Vinnie never quite recovered from that day.{w=.3} They've been very isolated and haven't been communicating as they used to do."
            "Their funny quirks and quips are gone.{w=.3} Replaced with quiet chuckles and longing stares at the floor."
            if rocky_dead == True:
                "They visited Rocky's parents to say how much Rocky meant to them."
                "How he sacrificed himself so they could live."
            if norman_dead == True:
                "They visited Norman's family to apologize for failing to protect their son..."
            "I've only seen them once since then..."
        if rocky_dead == False:
                "Rocky isn't the same,{w=.3} I don't think he even works anymore. {w=.3}Just drinks his days away at some run-down bar..."
                if vinnie_dead == True:
                    "He visited Vinnie's family to tell them what an inspiration Vinnie was to him."
                    "That their death is his fault..."
                if norman_dead == True:
                    "He went to Norman's family to beg for them to press charges for murder." 
                    "Since he feels like he should be locked up for letting Norman die..."
        if norman_dead == False:
                "Norman starts the hangouts much more frequently."
                "Almost to an overbearingly degree..."
                "He's a lot more jumpier and fearful compared to back then."
                "He often checks in to see if everything is alright and if there's anything he could do."
                if rocky_dead == True or vinnie_dead == True:
                    "They always keep a picture of all of us together in their jacket..."
                if norman_affection >= 5 and insanity_level == 0:
                    "He lives with me now in a small apartment. I'm doing the best I can to support him and make him comfortable..."
        if tara == True:
            "Tara has been kept in confinement by the government for being related to the CEO. {w=.3}She isn't arrested but might as well be..."
            "She sends letters saying how grateful she is and that she'll visit us as soon as possible."
        if insanity_level >= 1:
            "Something inside me changed too... {w=.3}I don't feel the same anymore..."
        elif insanity_level >= 2:
            "I've definitely noticed a gear shift inside my brain.{w=.5} I feel broken..."
        if norman_affection >= 4 and insanity_level >= 1 and norman_dead == False:
            "I feel like Norman wanted to start something with me, but I can't reciprocate... {w=.3}I'm different now...{w=.5} Empty..."
        "We've been trying to stay friends, but it gets hard when we notice the missing space..."
        "It really makes me think...{w=.5} I wonder if there was anything else I could've done differently?"
    window hide diss
    if norman_dead == True:
        $ notices.append("Achievement Unlocked: Taking The Dog Out Back")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.killnorman = True
    if vinnie_dead == True:
        $ notices.append("Achievement Unlocked: Roadkill After All")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.killvin = True
    if rocky_dead == True:
        $ notices.append("Achievement Unlocked: Wolf or Fox? Now we will never know...")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.killrocky = True
    if tara == True:
        $ notices.append("Achievement Unlocked: Coming Out The Closet")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.savetara = True
    if tara_against_dad == True:
        $ notices.append("Achievement Unlocked: Escaping the Mad House")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.tara_against_dad = True
    if ammo >= 3:
        $ notices.append("Achievement Unlocked: I don't need no dang gun!")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.dontusebullets = True
    #if medkit_used == False and morphine_used == False and crowbar_collected == True and vinnies_knife == True and ammo == 3 and pills == False:
        #$ notices.append("Achievement Unlocked: Bad MotherFucker!")
        #play audio "audio/sfx/achievement.ogg"
        #$ persistent.dontuseitems = True
    if insanity_level == 0:
        $ notices.append("Achievement Unlocked: Coffee AU")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.nosanityloss = True
    if norman_affection >= 5:
        $ notices.append("Achievement Unlocked: Dog Boyfriend")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.romancenorman = True
    if expose_samsara_together == True and expose_samsara_together_2 == True and expose_samsara_together_3 == True:
        $ notices.append("Achievement Unlocked: Samsara's End")
        play audio "audio/sfx/achievement.ogg"
        $ persistent.motivatefriends = True
    $ notify_me("and so it ends...")
    jump win_screen

    label secret_tara_end_scene:
        if seen_tara_ending == False:        
            $ seen_tara_ending = True
            $ w_name = "Tara"
            play music "audio/music/successful failure.ogg"
            scene boss battle with fade
            show snow1
            show snow2 with dissolve
            pause 2.0
            "I'm about to enter the elevator to the rooftop until-"
            "Tara taps my shoulder and I turn around to face her."
            show w 14 with Dissolve(0.2)
            w "..."
            w 15"Hey..."
            w "He- {w=.3}He..."
            w "My fath-"
            w "Taran-"
            w "...The CEO."
            w "I... {w=.3}I know he was a horrible, {w=.3}{i}horrible{/i} person."
            w "I fully understand and recognize all the bad things he's done.{w=.3} All the people he hurt.{w=.3} But..."
            w "I...{w=.3} can't bring myself to fully hate him.{w=.3} I want to.{w=.3} I know I should."
            w "But it would feel like someone else's words in my mouth if I did."
            w 8"Am I a horrible person?"
            w 15"I am fully prepared to cleanse his sins against mankind.{w=.3} I'm not him after all."
            w "I like to think so anyways..."
            w 14"I want to heal everything that was destroyed and use my heritage and status for good instead of bad."
            w 7"I wish my dad never died.{w=.3} I wish my pseudo-family wasn't dead. {w=.3}They were my childhood.{w=.5} They're me."
            pause 1.0
            w 16"I miss them..."
            w 12"There were the typical corporate cronies and scientists. But-"
            w "These people in particular acted so friendly to me. They were different."
            w 13"School, {w=.3}birthdays, {w=.3}shows, and movies. {w=.3}They were there for all of those things."
            w 4"It felt like I had more then one parent."
            pause 1.0
            w 3"They've known my father for a long time. Since before Samsara. Before everything."
            w 2"I liked to think that they were special, different from the other people here. That they would change the world for the better."
            w "That the whole corporation and science experiments wasn't really them."
            w 15"Except, they were just as complicit."
            w 14"Everyone I grew up with is dead now. {w=.5}I'm all that's left."
            w "Is it wrong for me to mourn?"

            menu: 
                "You have no right.":
                    p 1"People died and you think you have the right to mourn?"
                    p 4"I want you to know the pain of losing your father and multiply that by thousands for all the people who lost theirs."
                    p 2"Next time you feel{w=.3} \"sad\"{w=.3} think about how it was your {w=.3}\"family\"{w=.3} that killed everyone else's."
                    w 14"..."
                    w 2"...{w=.3}The fact that your words ring true and it doesn't change me is what scares me most."
                    p 4"..."
                    p 1"Let's get out of here."
                    w 14"..."
                    w "I hope this doesn't lead to anything bad... I really don't..."
                    hide w with Dissolve(0.2)
                    pause 1.0

                "You selfish brat.":
                    show w 14
                    stop music fadeout 3.0
                    p 14"People died and you think you have the right to mourn? {w=.3}Shut the fuck up.{w=.3} Everyone is dead."
                    p "There are people outside who lost so much more then you did. {w=.3}The key difference is that they weren't evil sacks of shit who deserved a fate worse then dying."
                    p "Nobody needs a spoiled princess crying for attention.{w=.3} You have no right to feel bad."
                    p "Next time you want to feel \"sad\" think about how actual innocents were hurt from your \"family\"."
                    w 15"..."
                    w 2"...{w=.3}The fact that everything you said is true but... I don't agree with it. Is what makes me feel like..."
                    w 14 "What changed?"
                    w "What was fixed?{w=.3} What was harmed? {w=.3}What can we do?{w=.3} Everything is just so fucked."
                    w 2"What {i}can{/i} change? {w=.3}I want to answer it. {w=.3}But I'm afraid I've been blinded by a truth nobody else can see."
                    w "So much more happened here then you realize... {w=.3}A lot more you're gonna learn soon..."
                    w "A lot more about yourself. {w=.3}How you're no different from the people you judge."
                    pause 1.0
                    w 14"That's something I know all about."
                    w "..."
                    w 2"Nothing ever really goes away... {w=.3}It's all one big cycle we can never escape. {w=.3}This didn't end anything..."
                    w "I wish we had the choice to dissapear like they did..."
                    w "..."
                    w 14"Let's just get out of here already."
                    w "..."
                    p 4"..."
                    hide w with Dissolve(0.2)
                    pause 1.0

                "No, it isn't.":
                    $ addInsanity_level(1)
                    p 2"Listen...{w=.5} as long as you promise not to repeat or downplay their crimes.{w=.3} And understand none of it was good. {w=.3}I would say.... {w=.3}no.{w=.3} You could cry without guilt."
                    p 1"All those memories you had of his love had to mean something..."
                    p "Think very carefully about what exactly it was that made you so attached in the first place.{w=.3} And extend that to other people."
                    p 4"People died Tara... {w=.3}He wasn't soley to blame, true.{w=.3} A lot more were involved. {w=.3}But he isn't a good person."
                    p 1"...{w=.3}I'm sorry he betrayed your love for him. {w=.3}He failed. {w=.3}But you won't. Right?"
                    w 7"*hic* {w=.3}*hic*{w=.3} I-{w=.3}I miss them so much! I want them to come back but it won't be how I remembered them! {w=.3}I wish everything could go back to how it used to be..."
                    w 16"I'm so tired of all this... {w=.3}I've been working against them for so long and now! {w=.3}It's finally over!{w=.3} I get peace! {w=.3}I get peace in the fact I can know what went wrong and mourn the losses!"
                    p 2"It's ok Tara...{w=.3} just... {w=.3}This must be a lot for you to deal with right now."
                    p "Let't talk more about it when we get out of here alright?"
                    w 13"Thank you... {w=.3}Thank you!"
                    w 7"*hic* {w=.3}*sob*{w=.3} God I miss them so much... {w=.3}*sob*"
                    "I give Tara a pat on the back. She hugs me back."
                    p 15"It's ok to cry.{w=.3} We have all the time we need now..."
                    show w 7
                    pause 1.0

                    w 13"...Haaahaaa...{w=.3} Let's get out of here. {w=.3}These fumes can't be healthy,{w=.3} right?{w=.3} Haahaa..."
                    w 4"I have a lot of work to do! {w=.3}A lot of mistakes to be fixed! {w=.3}A lot of people who need my help!"
                    p 13"Right! {w=.3}Let's leave! {w=.3}Together!"
                    hide w with Dissolve(0.2)
                    pause 1.0

            "..."
            jump secret_dev_message_scene
        elif seen_tara_ending == True:
            pass
        jump secret_dev_message_scene

    label secret_dev_message_scene:
        if seen_dev_message == False:
            $ seen_dev_message = True
            scene elevator with fade
            play music "audio/music/Going_Up.mp3"
            "Thank you so much for playing the crap out of our game!"
            "I know it must've been rough going through everything."
            "Playing through the game. Multiple times over."
            "Some characters that you may or may not like going through some things you may or not want."
            "It's difficult to find the right balance between \"Is this too much?\" or \"Is this too little?\"."
            "I want every player to get at least some type of enjoyment from the game..."
            "If you spent this much time. That means you liked it, at least a little bit."
            "Right?"
            "So much that you wanted to play it again. Even after getting every achievement."
            "If you're that player. (You are since you're reading this). Type \"#TOILETGANG\" in a review."
            "Then I'll know that there's some epic gamers."
            "Hopefully, on the scale of \"This is cringe\" to \"This is OK\". It was somewhere positive."
            "Even if it wasn't exactly positive... I still appreciate any type of thought. So thank you!"
            "More games are coming out soon. Perhaps not of the \"Cafe of The Dead\" world. (I can see two more games in that world). But still, watch out for them!"
            "Remember to love yourself! And the people who love you! Because there is always someone. Even if they don't come to mind right now."
            "Because I will always be one of those people <3."
            "Now let's get back to the game!"
        elif seen_dev_message == True:
            pass
        jump cafe_floor_0
return

