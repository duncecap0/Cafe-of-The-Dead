

## PROFANITY FILTER BY https://lemmasoft.renai.us/forums/viewtopic.php?t=47064
#bad word list 1 by https://www.cs.cmu.edu/~biglou/resources/bad-words.txt
#bad word list 2 by https://github.com/zacanger/profane-words
#bad word list 2 by https://github.com/dsojevic/profanity-list
init python:
    import collections
    
    def ContainsBadWord(name):
        #Get list of bad words from text file, each word on a separate line
        rude_words_file = [line.rstrip('\n') for line in open(renpy.loader.transfn('rude_words.txt'), 'r')]
        
        #Check if the name contains a bad word
        for badWord in rude_words_file:
            if (badWord in name):
                return True

#CHARACTER DEATH STATUS
default rocky_dead = False
default vinnie_dead = False
default norman_dead = False

default rocky_cafe_death = False

#gun rounds aka bullets

#should irl be 15 but lets just ignore that...
default norman_has_gun = True
default ammo = 3

#CHARACTER HEALTH
default rocky_health = 4
default vinnie_health = 3
default norman_health = 4
default sage_health = 3
default pov = "Sage"

#SAGE STATS

default norman_affection = 0

default insanity_level = 0


#Zombie lives
default first_zombie_attacker_dead = False




label cafe_floor_0:
    $ norman_has_gun = False
    play music "audio/music/Morning_Joe.mp3"
    scene cafe outer with dissolve
    
    "It's October and college was finally almost over for my new group of friends, so it's about time to wind back and enjoy ourselves!"
    "We decided after class we should visit our friend at his new job as a barista."
    "He's employed in the lobby café of a skyscraper belonging to a massive company called \"Samsara Enterprises\"."
    "Although the first floor is much more of a recreational area for the general public to show off the other businesses sponsoring them."
    "There's even an indoor park and shopping district! The other floors were locked to business associates and office workers."
    "I've never really gone in there before since it's always full of white collars and bigwigs."
    "We came in from the subway transit, it was a nightmare trying to navigate our way through the swarm of civilians."

    show v 1 at center with moveinright
    show v at hop_loop
    v 1"HEY! GUYS OVER HERE!!!{w=.3} HAHA!!"
    v "HURRY UP!!! I{w=.3} {i}NEED{/i} {w=.3}TO SEE ROCKY AT HIS NEW STUPID LITTLE JOB HAHAHAHAHA!!!"
    "Here comes Vinnie,{w=.3} being their boisterous self as usual."
    "They were the one who really pushed for us to visit Rocky after class, {w=.3}Now that I think about it... Vinnie was {w=.3}{i}always{/i}{w=.3} the one who initiated the group hangouts."
    show n 2 at right with moveinright
    n "OK OK RELAX WE'RE ALMOST THERE!"
    n "You're really excited for this aren't you?"
    "Oh,{w=.3} hey Norman, {w=.3}He's being as patient as usual trying to humor Vinnie."
    "He was seen as the \"mom\" friend in the group,{w=.3} always responsible with keeping us from killing ourselves with our antics,{w=.3} well, {w=.3}mainly just Vinnie to be honest..."
    show c 13 at right with moveinright
    play sound "audio/sfx/short run.ogg"
    show v 4 at hop
    show n 6 at hop
    s "Pardon."
    show n at shiver with move
    show v 4 at hop
    show n 6 at hop
    n 5"Ough!" with hpunch
    "A stranger, Pine Marten, wearing a coat bumps into Norman as he marches into the skyscraper lobby."
    show c 13 at offscreen_left with move
    play sound "audio/sfx/short run.ogg"
    "I try to catch Norman as he recoils in response."
    show v 2 at hop
    v 2"Hey! {w=.3}Not cool man!{w=.3} That was totally on purpose!"
    hide c 13
    show n 6 at right with move
    n "Just drop it,{w=.3} I'm not hurt;{w=.3} while I appreciate it, {w=.3}let's not start anything unnecessary alright?{w=.3} It's all about Rocky's new job today!"
    v 12"...{w=.3}Ok if you say so..."
    v 8"If you change your mind... I'll use this epic butterfly knife I got from the gas station! Ha!"
    show v at shiver
    "Vinnie twists the knife around on their fingers. I wanted to say how dumb they look but,  {w=.3}I gotta admit that {w=.3}{i}is{/i} a neat trick."
    n 1"...Are you sure gas station knives are made of the best quality? It'll probably snap if you try using it..."
    v 5"Nuh-uh! The guy at the store said he got it from a good vendor!"
    n 2"Wouldn't the person trying to sell you something be the one who brags about how great it is?"
    show v at hop_loop
    v "Well, then I'll beat that guy down with my fists of fury! {w=.3}Haha!"
    show v at hop
    v 17"Just kidding,{w=.3} my arms are noodles..."
    show v at hop_loop
    v 3"Instead, {w=.3}I'll summon my attack dog! {w=.3}Rocky!{w=.3} Who will beat him down for me!"

    "Geez,{w=.3} why was that business guy in such a rush?{w=.3} Just another reason for why I never hung out around here..."
    show v at offscreen_left with move
    show n at offscreen_left with move
    pause 0.5
    scene cafe with Dissolve(0.2)
    play sound "audio/sfx/chime.ogg"
    show r 2 with Dissolve(0.2)
    r "Hello and welcome!{w=.3} What can I get you toda-"
    show r 8 at left1 with moveinleft
    r "Oh{w=.3},{i} oh no{w=.5} please dear lord no...{/i}"
    show r at left with move 
    show v 2 4 with Dissolve(0.2)
    show v 2 4 at shiver_loop
    v "HAHAHAHAHAHAHAHAHAHAHA!!!!{w=.3} STOP!!!!{w=.3} STOP IT!!!!{w=.3} I- {w=.3}I CAN'T BELIEVE IT!!!" 
    "Seeing the hulking figure of Rocky sell such cute pastries in a pastel café is enough to make anyone laugh."
    "Even I have to stifle a laugh when it sets in, {w=.4}hehe."
    v "BAHAHAHAHAHAHAHA!!!!!!!!"
    "We move past Vinnie who is currently laughing up a storm while leaning on a table for stability."
    show v at hop
    hide v with Dissolve(0.2)
    show n 1 with Dissolve(0.2)
    show n 1 at hop
    n "Hey Rocky! Nice to see you at your new post! {w=.3}Where's your co-worker?"
    r 1"She got a call from a family member, {w=.3}something about a medical emergency..."
    n 5"Woah! That sounds really serious! Are they gonna be ok?"
    r "Honestly, {w=.3}I'm not sure. She sounded real rattled when she heard the news, must've been serious."
    "Rocky,{w=.3} being the eldest of the group, {w=.3}always seemed like he had an avalanche of responsibilities to attend to."
    "I suppose Vinnie is only a year younger than him but still,{w=.3} that's just how Vinnie is."
    "I'm relatively new to friend group yet I still know the others more than Rocky since he often misses our hangouts."
    "I recall Norman mentioning how Rocky doesn't have a place to call home, so he bounces job to job to make ends meet."
    n 1"Well,{w=.3} we could cheer her up next time we visit you at work!{w=.3} We're gonna be regular customers so she's bound to get to know us eventually, right?"
    r 6"You'd really be willing to sacrifice so much of your time for {w=.4}{i}me?{/i}"
    "He suddenly shakes his head as if to push the thought away"    
    r 2"Ugh,{w=.3} speaking of... {w=.3}You guys aren't gonna make this weird or anything? Remember I have to keep this job so don't scre-"
    hide n with Dissolve(0.2)
    show v 5 with Dissolve(0.2)
    v "Oh!{w=.3} We're definitely making things weird!"
    v 9"Hello sir!{size=*0.8} {w=.3}Write this down because it's gonna be a long one,{/size}{w=.3} I would like to order:"
    v "A half caffeine quad venti at two-hundred degrees with half soy, no foam with foam steamed with cinnamon, crosshatched caramel hazelnut swirl drizzling, pulled ristretto, sugar-free sugar, and a cherry on top please!"
    v "And my friends here would like an eggnog flat white and a unicorn frappe with a whole unpeeled banana in it, also make sure to use sugar-free replacements!!"
    v "What do you mean it's out of season and you don't accept hundreds? I want to speak with the regional manager!!!"
    show r 3a at hop
    r 3a"{w=.3}Suck actual fat fucking cock."
    show v at hop
    v 2 4"BAHAHAHAHAHAHAHAHAHA!!!"
    show r at center with move
    show v at right with move
    "Rocky lunges forward to shut Vinnie's snout."
    hide v with Dissolve(0.2)
    hide r with Dissolve(0.2)
    show n 2 with Dissolve(0.2)
    show n 2 at hop
    n 7"Hahahahaha!"
    n 2"Hey, we had our fun how about we settle this down!"
    "Norman locks eyes with me and gently guides my arm towards the register."
    n 2"You go on ahead and order from Rocky since you two haven't had many chances to talk!"
    hide n with Dissolve(0.2)
    show v 15 at right with Dissolve(0.2)
    show r 3a with Dissolve(0.2) 
    "I walk up to Rocky,{w=.3} currently holding Vinnie's snout closed while shaking them back and forth;{w=.3} ignoring Vinnie's muffled protests."
    "Rocky stops what he's doing when he sees me."
    hide v 15 with Dissolve(0.2)
    show r 10 at hop
    if renpy.variant("pc"):
        $ rude_words_file = [line.rstrip('\n') for line in open(renpy.loader.transfn('rude_words.txt'), 'r')]
    r "Oh, that's right...{w=.3} I'm so sorry,{w=.3} but I'm having trouble remembering your name..."
    $ renpy.notify("Use the keyboard to type!")
 
    $ pov = renpy.input("It's fine, my name is", length=10).strip().lower().title() or "Sage"    

    if pov == "Bigvin":
        show v 2 4 at rightBIGG with Dissolve(0.2):
            zoom 2.0
        show r 2 at left with move:
            linear 0.5 zoom 0.5           
        "VINNIE HAS TRANSFORMED!!!!!!!!!!!!!!!"
        r 3a"GODDAMMIT VIN!"
        show v 2 4 at centerBIGG with move
        v "RAAAAAAAWWRRRR!!!!!!"
        with hpunch
        r "JUST FUCKING RESET THE SCENE ALREADY I HATE THIS EASTER EGG!"
        n "..."
        p 7"..."
        scene meme
        play sound "audio/sfx/mic.ogg"
        queue sound "audio/sfx/wrong beep.ogg"
        $ renpy.music.set_pause(True, channel="music")
        show static_anim
        centered "{size=+100}WE'LL BE BACK, RIGHT AFTER THESE MESSAGES{/size}"
        play sound "audio/sfx/start.ogg"
        scene cafe
        $ renpy.music.set_pause(False, channel="music")
        
    elif pov == "Sage":
        r "[pov]?{w=.3} You look like a [pov]... {w=.3}it fits..."

    elif pov in ["Breadley", "Bradley", "B0redbradley", "Boredbradley", "Breadly"]:
        "Huh?{w=.3}{w=.3} Shouldn't you be sleeping?"

    elif pov in ["Duncecap", "Dunce"]:
        "What the hell kind of name is that?{w=.3} GET A JOB BOZO! FATHERLESS BEHAVIOR!"

    elif pov == "Chris":
        "Shouldn't you be pushing boulders or something?"

    elif pov == "Leon":
        "*gasp* {w=.3}Where's baby eagle???{w=.3} also your hair's really nice."

    elif pov == "Claire":
        "When are you getting another game?"        

    elif pov == "Jill":
        "OMG NEMESIS IS BEHIND YOU!!!"

    elif pov == "Nemesis":
        "OMG NEMESIS IS BEHIND YOU!!!"

    elif pov in ["Tyrant", "Mr. X"]:
        "OMG NEMESIS IS BEHIND YOU!!!"  

    elif pov == "Ada":
        "Stop playing with my heart..."  

    elif pov in ["Ashley", "Babyeagle", "Baby Eagle", "Baby-Eagle", "Baby-eagle"]:
        "Remember to stick with Leon babe..."

    elif pov == "James":
        "Where's Mary?"  

    elif pov == "Mary":
        "{cps=*0.4}James...{w=.3} I'm in a beautiful place now...{/cps}"   

    elif pov == "Heather":
        "Hmm shouldn't you be avoiding a cult or something?"

    elif pov == "Harry":
        "When are you getting the remaster?{w=.5} (This dates this so horrible once it DOES come out...)"

    elif pov in ["Dinnerbone", "Grumm"]:
        "WOAH YOU'RE UPSIDE DOWN NOW!!!"

    elif pov == "James":
        "Where's Mary?" 

    elif pov == "11037":
        "The sixteenth student, lying hidden somewhere in this school. The one they call the Ultimate Despair. Watch out for her." 

    elif pov == "Steve":
        "I.{w=.5} AM. {w=.5}STEVE." 

    elif pov == "Ram Ranch":
        "Eighteen naked cowboys in the showers at Ram Ranch!!!" 

    elif pov == "Egg":
        "Be a good egg now!"

    elif pov == "Yuri":
        "I JUST WANT TO PULL YOUR SKIN OPEN AND CRAWL INSIDE OF YOU!!!"

    elif pov == "Natsuki":
        "Why don't you find some coins under the vending machine or something?"
        
    elif pov == "Monika":
        play sound "audio/sfx/static.ogg"
        "Just Monika."
        menu:
            "Just Monika."
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
            "Just Monika.":
                pass
        label monikaloop:
        
        play sound "audio/sfx/static.ogg"
        call screen confirm(message=" Just Monika. ", yes_action=Return(), no_action=Jump("monikaloop"))

    elif pov == "Sayori":
        "I want breakfast."

    elif pov == ["MC", "Protag", "Y/n", "Yn", "Pov", "Player", "P", 'Your Name', 'Mc', '']:
        "Not very creative now...."

    elif pov in ["Todd Howard", "Todd"]:
        "Please release TES6..."

    elif pov == ["William Afton", "William", "Afton", "Springtrap", "Will", "Scraptrap"]:
        "The Man Behind The Slaughter"

    elif pov == "Chara":
        "the true name"

    elif pov in ["gaster", "Gaster", "WDGaster", "W.D.Gaster"]:
        $ MainMenu(confirm=False)()
        
    elif pov in ["ToddHoward", "Todd"]:
        "Please release TES6..."

    elif pov == "Luke":
        "You're Luke Skywalker,{w=.3} you're here to rescue me!"

    elif pov in ["Colburn", "Maizie", "Wren", "Xochi", "Gwen", "IO", "August", "Cole", "Colby"]:
        "What a strange coincidence..."

    elif pov in ["Rocko", "Rocky"]:
        r "Woah that's crazy how we share the same name!"

    elif pov in["Vinny", "Vinnie", "Vin", "Norm", "Norman"]:
        r "Oh! I better make sure I don't confuse you with one of my friends then!"

    elif pov in ["Mom", "Mommy", "Mother", "Mama"]:
        show v 2 4 at right with Dissolve(0.2)
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE!{w=.3} I SHOULD HAVE THOUGHT OF THAT! YOU FETISHIZER!"
        hide v 2 4 at right with Dissolve(0.2)
        "I guess I'll let you get away with it..."

    elif pov in ["Dad", "Daddy", "Father", "Papa"]:
        show v 2 4 at right with Dissolve(0.2)
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! {w=.3}I SHOULD HAVE THOUGHT OF THAT! YOU THIRSTY THOT!"
        hide v 2 4 at right with Dissolve(0.2)
        "I guess I'll let you get away with it..."
    if renpy.variant("mobile"):
        if pov in ["Cunt", "Whore", "Fuck", "Fucker", "Ass", "Thot","Fuckface", "Fart", "Poop", "Shit", "Penis", "Cock", "Titty", "Cock", "Damn", "Dammit", "Boobs", "Tit", "Boob", "damm", "d4mm", "dick", "bastard", "blowjob", "turd", "anus", "bitch", "hoe", "ho", "booty", "butt"]:
            "Very mature but I'll let it slide..." 
    else:
        if (ContainsBadWord(pov)):
            "Very mature but I'll let it slide..."

    show r 10
    r 10"Duh!{w=.2} Of course, I remember your name! {w=.3}Ok [pov], {w=.3}what would you like?"
    show r at hop
    r 1"Wait a sec..."
    show r at hop_loop
    r 2"Dammit! Vinnie stop trying to steal the cake pops!{w=.3} I'm not giving any more handouts like back then!!!"
    show v 5 at right with Dissolve(0.2)
    show r at hop
    v "Aww c'mon man you used to do that for me all the time! {w=.3}You used to be cool Rocko! {w=.3}What happened?!?!"
    r 1"Well, {w=.3}{i}SOME{/i} {w=.3}people change and actually {w=.3}{i}MATURE{/i}{w=.3} overtime."
    r "{i}Something you'll never do apparently...{/i}"
    pause 0.5
    scene cafe with dissolve
    show v 1 at right with Dissolve(0.2)
    show n 1 with Dissolve(0.2)
    show r 1 at left with Dissolve(0.2)
    "Time passes,{w=.3} as we all take a seat and talk idly about what we've done recently."
    n 1"Ha, {w=.3}the professor really just threw that assignment out of nowhere, right?"
    r 1"Real smart of him considering half the class wasn't even done with the last one yet..."
    p 1"Does he really have to give us another one?{w=.3} I felt the group presentation was enough..."
    v 6"Meh, {w=.3}you guys are just coping with the fact I'm actually the smartest,{w=.3} prettiest, {w=.3}AND most talented out of any and every class!{w=.3} I have NO problems with assignments or tests~"
    r 2"Gee,{w=.3} I'm gonna have to deflate your head with a coffee straw just so it's able to get out the front door,{w=.3} med student!"
    v 3"Awww don't be jealous I have perfect straight A's!"
    r 4a"I have nothing to worry about considering you're absent half the time and are about to get dropped if you don't shape up!"
    v 5"Shut it dropout! {w=.3}You only just started school!"
    r 2"Are you kidding!?!{w=.3} You're only a year younger!{w=.3} I was at least working! {w=.3}You were busy getting arrested or whatever the hell overgrown street rats like you do! "    
    n 2"Hmmm it is sort of true though!{w=.3} You have to admit Vinnie is pretty smart!"
    p 15"\"Have to admit?\",{w=.3} as in, {w=.3}you didn't expect Vinnie to be this smart?"
    r 10"Hahaha! {w=.3}Serves you right if {i}Norman{/i} of all people thinks that less of you!"
    v 2 3"Norman! H{w=.3}-how could y{w=.3}-you... {w=.3}I THOUGHT WE WERE FRIENDS!!!"
    show v 9 at right
    "Vinnie pretends to bawl and stuffs their face into their hands."
    n 7"Hey! {w=.3}I never said that!"
    show black with Dissolve(0.5):
        alpha.5
    "These are the people I choose to spend my time with,{w=.3} truthfully,{w=.3} I didn't have anyone else in my life."
    "I don't have the best relationship with my relatives, {w=.3}so I prefer staying out of their way,{w=.3} I was never the sociable type in school;{w=.3} or life in general."
    "It's because {w=.3}{i}I know I'm a social vacuum compared to others.{/i}{w=.3} People seem to know this friend thing right off the bat but for me it's such a chore..."
    "I attempted to join in the crowd when I was much younger."
    hide r with Dissolve(0.5)
    show black with Dissolve(0.5):
        alpha.6    
    "But playground insults like my formal tone of voice and lack of awareness in social cues repelled them from me."
    "Not to mention being shoved around and having food thrown at me when I'm turned the other way."
    "I felt it would be a wasted effort to try again, {w=.3}since it's not an off and on switch. {w=.3}Why give people the opportunity to mock when you could remove yourself from the scenario altogether?"
    "It was worse when faculty took notice and started to coddle and infantilize me. {w=.3}{i}I hate patronization.{/i}{w=.3} I'm being treated as lesser."
    "As if I were just some bug in the air people should learn to tolerate.{w=.3} Except, {w=.3}I don't want to be just tolerated."
    hide v with Dissolve(0.5)
    show black with Dissolve(0.5):
        alpha.7    
    "I want to be accepted."
    "I want to be a person."
    "Why is that so hard for me to do?{w=.3} Why can't I follow such simple instructions? {w=.3}Are normal people not meant to question this because it's meant to be hardcoded into our brains?"
    "Well, {w=.3}if it's not hardcoded into {i}my{/i} brain {w=.5}then what does that make me?"
    "..."
    hide n with Dissolve(1.)
    show black with Dissolve(1.):
        alpha.8    
    "I'm normal... {w=.5}right?"
    "..."
    "I just want to be normal... {w=.3}That's all I've ever really wanted..."
    "..."
    pause 0.5
    show black with Dissolve(1.):
        alpha.6    
    "I've never spent this much time with anyone before;{w=.3} I was simply minding my business in class one day when Norman offered to join him at the park."
    "He slowly introduced me to the rest of his circle. {w=.3}I'm very grateful to have people I can talk to and actually listen to me."
    "Rocky's dependable nature, always lending a hand when he can;{w=.3} Vinnie's good-nature and levity; {w=.3}They're always able to brighten up a tough day."
    "And Norman,{w=.3} he's always there to cheer me on; {w=.3}I don't think he's ever rejected a chance to talk with me either,{w=.3} so he must enjoy my presence as much as I enjoy his."
    "I suppose I never properly thanked him for this opportunity... {w=.3}I have to remember to do that soon..."
    hide black with Dissolve(0.2)
    show v 4 at right with Dissolve(0.2)
    show v at hop
    v 4"EARTH TO [pov!u] EARTH TO [pov!u], HEY SPACE CADET YA THERE!?!?" with hpunch
    p 1"Ah, {w=.3}I apologize I wasn't paying attention."
    play music "audio/sfx/crowd panic.ogg" fadein 1.0
    v "You see this shit?!?! {w=.3}There're people screaming like crazy!"
    v 10"I didn't know the pride parade was coming THIS early!"
    show r 3 with Dissolve(0.2)
    r 3"Vin, {w=.3}shut up. Now isn't the time for your stupid jokes, it's serious."
    show v 11 at sink
    "Rocky snaps back at Vinnie who slumps back in their chair with a face I've never quite seen on them before."
    hide v with Dissolve(0.2)
    "I don't think I've ever seen Rocky be this fed up with Vinnie, {w=.3}sure he got annoyed,{w=.3} but never actually meant it until now."
    "I shoot my head upwards and see Rocky with Norman; both glued to the window."
    show n 3a at right with Dissolve(0.2)
    n "I'm trying to see what they're running from but no luck..."
    r 7"They just keep pouring out!{w=.3} What could have caused this?"
    scene cafe window with Dissolve(0.2)
    show r 7 with moveinleft
    show n 8 at right with moveinright
    show v 11 at left with moveinleft
    "I mutually stand up and stare out the window."
    "There're hundreds of people packing the street,{w=.3} all running as fast as they can."
    play sound "audio/sfx/window smash.ogg"
    "Some people take advantage of the chaos and smash open miscellaneous store windows to rob them."
    play sound "audio/sfx/ambulance.ogg"
    "Amongst the ocean of deafening screams are various cries for help."
    npc "JUST KEEP RUNNING!!!"
    npc "Get away from me, this is mine!!!"
    npc "Has anyone seen my husband?!?"
    npc "SAMANTHA WHERE ARE YOU!!!"
    npc "OH MY GOD THEY'RE COMING FOR US! RUN!!"
    show v at left with Dissolve(0.2)
    v 12"This is almost too much to look at... {w=.3}I-{w=.3} I don't want to see..."
    show v at sink
    hide v with Dissolve(0.2)
    r 1"I'm heading out shop, {w=.3}I need to see what's up..."
    show n at hop
    n 5"Wait!{w=.3} You can't! {w=.3}Look at how many people are out there!"
    n "You see a bunch of people running from something and choose to head straight into it?"
    r 1a"Relax, {w=.3}I'm just gonna sneak a peek outside then quickly run back in."

    #menu:
    #    "Rocky's right, I'm too curious to not go outside but, should someone else go?"
    #    "Only Rocky and I will go outside":
    #       jump first_zombie_investigation

    #    "Only Vinnie and I will go outside":
    #        jump first_zombie_investigation

    #    "Only Norman and I will go outside":
    #        jump first_zombie_investigation

    #    "I'll go alone":
    #        jump first_zombie_investigation
            
    #    "Let's all go out together":
    #        jump first_zombie_investigation

    
    #label first_zombie_investigation:

    n "I-"
    show r at offscreen_right with move
    show n at center with move
    "Before Norman can say any more Rocky rushes out."
    "I chose to go out with him."
    show n at hop
    n "Are you two serious?!?!"
    
    scene cafe outer with Dissolve(0.2)
    pause 0.5
    show r 1 with Dissolve(0.2)
    r 1"Oh, you decided to come with,{w=.3} here follow me I just want a glance at the cause of this..."
    npc "GET AWAY FROM ME!!! {w=.3}GET AWAY!!!"
    p 4"Is someone being attacked?"
    r 2"Jesus!{w=.3} T- {w=.3}those screams! {w=.3}Let's hurry! {w=.3}He could be in trouble!"
    r 4a"Let's take a closer look he could be in trouble!"
    show r at offscreen_right
    scene black with fade
    scene cafe outer with Dissolve(0.2)
    stop music fadeout 5.0
    play audio "audio/sfx/Wind.ogg"
    show r 1 with moveinleft
    "We go further up ahead to the source of the noise, the panicking crowd thinned out and is nowhere near as big as before."
    play music "audio/music/live or die intro.ogg"
    queue music "audio/music/live or die.ogg"
    npc "HELP ME!!!{w=.3} PLEASE SOMEBODY HELP ME!!!"
    r 4a"Over there!"
    "Our pace quickens until we come across a man attacking another man!{w=.3} He pinned him to the ground and clawing his neck!"
    show r at hop
    r 2"You goddamn freak get off him!"
    show r at hop
    "Rocky strikes the back of the attacker's head; {w=.3}the pain doesn't appear to register with him..."
    "Rocky grapples the back of him,{w=.3} attempting to restrain his arms."
    play sound "audio/sfx/zombie talk.ogg"
    "The attacker finally notices Rocky and tries clawing his face,{w=.3} he makes the most unpleasant noise I've ever heard..."
    "I didn't even know anyone was capable of evoking such a groan,{w=.3} almost like he wasn't even alive..."
    r 3a"What the hell are you?!?!"
    play sound "audio/sfx/zombie (2).ogg"
    show bigzom at shiver_loop with moveinright
    "The attacker is able to twist himself backward and faces Rocky directly when tussling with him."
    "He's trying to bite Rocky's neck, but his restrained arms prevent that."
    show r at shiver_loop
    p 7"Don't worry, I got this!"
    play sound "audio/sfx/hit13.ogg"
    "I jump to throw a punch to the side of his jaw; {w=.3}a couple teeth fall out!"
    with hpunch
    play sound "audio/sfx/hit12.ogg"
    "Rocky throws him down to the ground and pins his face the other way with his boot."
    with vpunch
    show bigzom at sink with moveinright
    show r at hop
    "The attacker protests intensely,{w=.3} flailing around like a dead cockroach in an attempt to get back up."
    play sound "audio/sfx/zombie moan.ogg"
    "There's that awful noise again..."
    "Now that I'm closer I'm able to see just how monstrous he is..."
    "He's dyed in blood, with milky white eyes,{w=.3} and evokes an odor so pungent it stings my eyes..."
    r 2"[pov!u]!{w=.3} Check out the guy he jumped to see if he's ok!"
    p 4"Got it!"
    hide r with Dissolve(0.2)
    hide bigzom with Dissolve(0.2)
    "I jog ahead to see that the victim is lying motionless on the floor..."
    "Blood pools beneath him as I see large gashes on his throat."
    p 7"Are you ok?!?!"
    "I check the pulse on his neck to see if he's still with us."
    "There's nothing."
    
    show r 3 with Dissolve(0.2)
    show r at hop

    r 3"Hey! {w=.3}[pov]!{w=.3} He alright!?!?"
    "I turn back to see a panicked Rocky still pinning down the attacker."
    p 7"We need to call an ambulance his neck is-"
    show bluzom at offscreen_bottom
    play sound "audio/sfx/Zombie_03.ogg"
    show bluzom at left with move
    "I turn one-eighty and see the previously dead man about to lunge at me!"
    with hpunch
    show bluzom at shiver_loop_left
    p 7"How are you alive!?" with vpunch
    r 3a"[pov!u]! Don't worry! I'll get to you!"
    show r at sink
    "Rocky sprints towards me but his leg gets grabbed by the person he was restraining, {w=.3}he face-plants into the curb."
    with vpunch
    show bigzom at right with moveinright
    show bigzom at shiver_loop_right
    r 2a"JESUS! {w=.3}GET IT OFF!{w=.3} GET IT OFF!"
    show r at sink_rise
    show r at shiver_loop

    show screen character_stats with Dissolve(0.2)

    menu rocky_first_death_choice:
        "What do I do now?"

        "Kick zombie attacking me in the knees" if first_zombie_attacker_dead == False:
            $ first_zombie_attacker_dead = True
            play sound "audio/sfx/hit.ogg"
            with hpunch
            queue sound "audio/sfx/zombie huh.ogg"
            show bluzom at offscreen_bottom with move
            hide bluzom
            queue sound "audio/sfx/zombie (2).ogg"
            "I use my smaller stature to my advantage and was able to knock the zombie over; It's down but not dead, now's my chance!"
            jump rocky_first_death_choice

        "Push off zombie attacking Rocky":
            if first_zombie_attacker_dead == True:
                "My horns are definitely pointy enough to cause some damage if use them!"
                play sound "audio/sfx/short run.ogg"
                queue sound "audio/sfx/punch.ogg"
                queue sound "audio/sfx/zombie huh.ogg"
                "I charge forward and knock off the zombie attacking Rocky" with vpunch
                show bigzom at offscreen_bottom with move
                hide bigzom
                show r 2 at sink_rise
                r "Wow!{w=.3} You saved my ass [pov]! {w=.3}Thank you!"
                p 13"Don't mention it!"
                jump norman_protects_rocky

            elif sage_health == 0:
                label sage_first_death:
                show black with Dissolve(0.2):
                    alpha .7
                play sound "audio/sfx/zombie attack.ogg"
                queue sound "audio/sfx/eat.ogg"
                "The zombie was able to fully grab onto my arm and bite into my neck." with hpunch
                "I was too weak to fight back... {w=.3}I feel... {w=.5}lighter..."
                jump death_screen

            elif first_zombie_attacker_dead == False:
                label sage_being_pulled_back:
                $ sage_health -= 1
                $ addRockyhealth(-1) 
                play sound "audio/sfx/zombie-19.ogg"
                "I tried running as fast as possible but the zombie lunging at me pulled my arm back." with vpunch
                if sage_health == 0:
                    jump sage_first_death
                "Didn't this exact thing happen to Rocky?{w=.3} I feel sharp nails dig into my arm,{w=.3} but was able to struggle out of it."
                "Damn that hurt... I see the other zombie similarly dig into Rocky's wrists."
                if rocky_health == 0:
                    extend "; his-"
                    jump rocky_dead_norman_rescue_sage
                else:
                    extend "; better be careful this time..."
                    jump rocky_first_death_choice

        "Call for help":
            $ addRockyhealth(-1) 
            p 7"NORMAN! VINNIE! ANYONE OUT THERE PLEASE HELP US!" with hpunch
            play sound "audio/sfx/zombie attack.ogg"
            r "AGH!" with vpunch
            "Shit...{w=.3} looks like Rocky just got a piece of his wrist dug up...{w=.3} I need to do something!"
            if rocky_health == 0:
                "Is he even..."
                jump rocky_dead_norman_rescue_sage
            else:
                jump rocky_first_death_choice
           

        "Abandon Rocky":

            if first_zombie_attacker_dead == True:
                $ addInsanity_level(3)
                show static_anim with Dissolve(0.2)
                camera:
                    perspective True
                    easein_bounce 0.54 zpos -20
                play sound "audio/sfx/short run.ogg"
                queue sound "audio/sfx/zombie talk.ogg"
                queue sound "audio/sfx/eat.ogg"
                camera:
                    reset
                scene black with Dissolve(0.2)
                "I ran as fast as my legs could carry me all the way to the café, in the distance I could hear a shriek and chewing noises."
                r "No!{w=.3} No!{w=.3} Get off me you fucks! {w=.3}AGGGGGGGHHHH!!!"
                $ addRockyhealth(-6) 
                pause 0.4
                scene cafe with Dissolve(0.2)
                show v 11 at right with Dissolve(0.2)
                show n 6 with Dissolve(0.2)
                v 11"I don't know what the hell they were thinking going outside..."
                n 1a"I'll take care of it don-"
                show n 2 at hop
                n 2"[pov]!?"
                show v 2 at hop
                v 2 "Where's Rocky?!?! {w=.3}He isn't with you?!?!"
                show n 8
                p 7"He's being attacked come with me!"
                v 2 1"And you just fucking left him there!?!"
                show v 21 at offscreen_left with move
                show n 8 at offscreen_right with move
                "Vinnie shouts as we all run out the café."
                scene cafe outer with Dissolve(0.2)
                "When we arrived outside, we see two of those monsters on top of Rocky, must've both have gone after him after I ran off..."
                jump rocky_dead_norman_rescue_sage
            else:
                jump sage_being_pulled_back
    
    label rocky_dead_norman_rescue_sage:
    $ rocky_cafe_death = True
    $ rocky_dead = True
    scene cafe outer with Dissolve(0.2)
    stop music fadeout 1.0
    play sound "audio/sfx/cock.ogg"
    pause 0.5
    queue sound "audio/sfx/shoot.ogg"
    $ norman_has_gun = True
    "Out of nowhere Norman whips a gun from inside his jacket to fire at the creatures!"
    "They drop dead with a hard thud and bounce as the bullet meets their brain."
    "Except,{w=.5} Rocky still hasn't gotten up..."
    show v 2 1 with moveinleft
    v 2 1"Rocky!{w=.3} Get up!{w=.3} Wake up!"
    "I've never seen Vinnie so distraught before..."
    v "Nonono...{w=.3} NO!!! GET UP YOU TOUGH SUNUVA BITCH!"
    v "GET UP!{w=.3} STOP JUST LAYING THERE!"
    "Vinnie kneels as they proceed to cradle Rocky's motionless body, looks like his neck and stomach have been torn open..."
    "Norman's paralyzed as if he had just seen a ghost."
    v 2 2"THIS ISN'T HAPPENING! SOMEONE CALL THE POLICE!{w=.3} HE ISN'T THAT HURT!{w=.5} STOP JUST STANDING THERE!!!"
    p 2"Vinnie... {w=.4}his neck..."
    show v 2 1 at hop
    v 2 1"SHUT UP!{w=.3} SHUT THE FUCK UP!{w=.3} HE'S FINE!"
    "Vinnie tries to shut Rocky's neck wound close as if it were that simple..."
    show n 5 at left with Dissolve(0.2)
    n 5"We have to get out of here! {w=.3}Look over there!{w=.3} More of them are coming!"
    "Norman seems to have snapped out of his trance to pull Vinnie away from Rocky,{w=.3} I help when I see Vinnie resist."
    show v 2 2 at shiver_loop
    v 2 2"Stop it! {w=.3}Are you crazy? {w=.3}We can't just leave him here! {w=.3}Look he's gonna be ok!"
    v "LET GO OF ME!!!{w=.3} ROCKY NEEDS ME!!!"
    "Vinnie keeps protesting as we struggle with dragging them all the way back to the café."
    jump cafe_aftermath

    label norman_protects_rocky:
    stop music
    play sound "audio/sfx/cock.ogg"
    pause 0.5
    queue sound "audio/sfx/shoot.ogg"
    "A gunshot rings out as one zombie gets its brains blown out."
    r 4a"Wha-"
    play sound "audio/sfx/shoot.ogg"
    "Another bullet flies right by me into the zombie near me."
    "The blood explodes from his face onto mine as he drops dead on the street."
    p 4"Who?"
    show n 14 at left with moveinleft
    $ norman_has_gun = True
    n "I told you it wasn't safe out here..."
    r 8"Y{w=.3}-you...{w=.3} YOU JUST KILLED TWO PEOPLE!"
    "Norman points towards the chest of the person who attacked Rocky"
    n "No, {w=.3}look at this injury of this one...{w=.3} I only fired once so why does he already have another gunshot wound?"
    r "I- {w=.3}I-..."
    n "No one can survive a gunshot to the heart and live.{w=.2} Think about it."
    n "C'mon we need to take cover; {w=.3}it isn't safe being exposed like this."
    show v 10 at right with moveinright
    v 10"Uh guys?{w=.3} You really shouldn't have left us behind lik-"
    v 16"..."
    show v 2 3 at hop
    v 2 3"{w=.3} HOLY FUCKING SHIT."
    show v at hop
    v "OH MY GOD, I'M GONNA BE SICK WHAT THE FUCK HAPPENED HERE?!?!"
    n "No time to explain we gotta get back!"
    "Norman ushers a silent Rocky and panicked Vinnie back to the café."

    label cafe_aftermath:
    hide screen character_stats with Dissolve(0.2)
    scene cafe with Dissolve(0.2)
    pause 1.0
    show v 11 at right with Dissolve(0.2)
    show n 8 with Dissolve(0.2)
    if rocky_dead == False:
        show r 7 at left with Dissolve(0.2)
    stop music fadeout 0.5
    play music "audio/sfx/EAS.ogg"
    tv "ALL CIVILIANS ARE TO TAKE COVER IN ANY SHELTER, {w=.3}DO NOT EXIT UNDER ANY CIRCUMSTANCES, {w=.3}BARRICADE ANY OPENINGS AS MUCH AS POSSIBLE,{w=.3} AVOID THE INFECTED AT ALL COSTS."
    tv "A PANDEMIC HAS OCCURRED;{w=.3} THE GOVERNMENT IS WORKING TO REMEDY THE SITUATION."
    tv "FROM WHAT WE KNOW THE ABNORMAL PATHOGEN INFECTS ITS VICTIMS MAKING THEM ACT HIGHLY AGGRESSIVE {w=.3}BE-{w=.4} O-"
    tv "The broadcast starts breaking up."
    if rocky_dead == False:
        r 3"C'mon work you stupid thing!"
    tv "{w=.3}-I---- {w=.3}A- {w=.3}P---- {w=.5}MAY GOD HAVE MERCY ON OUR SOULS-"
    play sound "audio/sfx/zap.ogg"
    stop music fadeout 0.5
    pause 1.0
    scene cafe with Dissolve(0.2) 
    show black with Dissolve(0.2):
        alpha.6
    pause 1.0
    "The power goes out as we all sit in silence..."
    if rocky_dead == False:
        "Rocky and Norman already barricaded the windows with chairs and crates from the backrooms."
    else:
        "Norman and I already barricaded the windows with chairs and crates from the backrooms."
        "Vinnie hasn't moved or talked since we dragged them in,{w=.3} I think Rocky's passing finally set in..."
    "The screams from outside turned from cries of help to shuffling feet and a cacophony of moans... {w=.3}Don't think it's safe to go out anytime soon..."
    "We all traveled here by the underground train system,{w=.3} so I doubt that's the safest option to go from here..."
    "Vinnie could try hot-wiring one of the cars from outside but what if we ran into a huge horde of those things from outside?{w=.3} We'll be surrounded..."
    if rocky_dead == True:
        "I also don't think they're in a very...{w=.3} {i}active{/i} state right now..."
    "We decided to just wait it out in here for the past hour... {w=.3}The broadcast advised us all to stay where we are...{w=.3} Someone's bound to rescue us right?"
    "There isn't much else for us to do so why eve-"
    hide black with Dissolve(0.2)
    show n 6 with Dissolve(0.2)
    n "We're gonna make it through this."
    "...?"
    show v 11 at right with Dissolve(0.2)
    if rocky_dead == False:
        show r 7 at left with Dissolve(0.2)
    "We perk up at Norman."
    n "We're gonna make it out of here I can assure you all."
    if rocky_dead == False:
        r 8"What are you talking about?{w=.3} It's practically hell on earth right now!"
        r 1"We're stuck in here and who knows what our families are going through."
        "I could see Vinnie visibly wince at that."
        r 3"It'll be a tragedy when they find one of those things outside..."
        r 8"Or worse, {w=.3}they're already gone."
        r 7"There are people {w=.3}{i}eating{/i}{w=.3} one another and you think we have a chance at this?!"
        n 6"Stop that"
        n "I remember when I was practically broke and about to live on the streets when all of a sudden you offered me a place to live."
        n 8"Even though you could barely afford it and got kicked out soon after for having another tenant without letting the landlord know."
        n 6"You still chose to help me out afterwards even though I ruined your life."
        n "What chance did we have then?{w=.3} But you still took it to help me out..."
        r 8"Norman, {w=.3}you never ruined anything I already told yo-"
        n 6"I know{w=.5}, I never forgot"
        v 12"That's how you lost your home?{w=.3} I never knew that part..."
        v 11"I- {w=.3}I don't know...{w=.3} about this guys... {w=.3}what really CAN we do besides just get ourselves k-{w=.3}killed..."
        n "Vinnie,{w=.3} listen, {w=.3}you're the smartest person I know so with your brains we're bound to come across a way to escape!"
        n 2"As long as we all got each other and stay careful it can't go wrong!"
        v 12"...!"
        r 1"What are you getting at?"
        n 6"I'm saying that my friends are amazing people that don't deserve to be trapped like this."
        n 3a"Stuck in here,{w=.3} twiddling our thumbs,{w=.3} hoping for the best."
        n 1"We can call for help and reach a safe zone somewhere!"
        n "Think about it! {w=.3}The government is bound to have set up some contained perimeter;{w=.3} all we have to do is come in contact with them and let them know there are survivors here!"
        r 1"Didn't you just say it was best to take cover?"
        n "I know what I said...{w=.3} but look outside... {w=.3}If they find us, we'll be completely trapped in here and... {w=.3}They'll eventually starve us out."
        v 2"Yeah, I don't think we could survive off frappes and cake pops forever..."
    else:
        v 2 2"Rocky got torn open, and you expect us to have a chance?"
        "Vinnie speaks in a somber tone from the corner of the room for the first time in a while"

        label vinnie_reaction_rocky_death:
        show v 2 2 with Dissolve(0.2)
        v "If someone as capable of Rocky didn't make it then we're gonna die here just like him..."
        v "It doesn't matter if you wave that gun around,{w=.3} there's no chance of survival...{w=.3} might as well just point it at me..."
        v "Rocky's family is going to be heartbroken when they find out,{w=.3} the son that took care of them...{w=.3} worked his ass of for their wellbeing gone{w=.3}, just like that"
        v "If they're even alive that is,{w=.3} they could be dead for all we know,{w=.3} all ours could be,{w=.3} so what's the point of it all? Die out there or starve to death in here... {w=.3} sort of a hail mary even..."
        v "The \"Best\" case scenario is if the national guard comes in here to rescue us...{w=.3} even then,{w=.3} is it even worth living a life without the people who care about you..."
        if norman_dead == False:
            show v 2 2 at right with move
            show n 8 with Dissolve(0.2)
            n 8"..."
            n "I remember when I was about to live on the streets,{w=.3} Rocky saved me,{w=.3} he welcomed me into his home and took care of me."
            n "I made him get kicked out his own apartment from housing an extra tenant and he still chose to be my friend, {w=.3}said he would do it all over again too if it meant I was safe."
            n "Rocky loved all of us, {w=.3}he always talked about how you came into his life and saved him, so he returns the favor to everyone he meets to give them that same experience."
            n "He told me life is about taking the losses and accepting the opportunity it grants you; {w=.3}because a life without loss...{w=.3} means nothing to gain..."
            n 6"\"What's a life worth without the people you care for?\"{w=.3} An opportunity to bring in people who may think the same..."
            n "You and Rocky were so close and you extended that to me...{w=.3} You two made me feel like I was a part of that and worthy of being loved..."
            n "We did the same with [pov] who had no one else in their life...{w=.3} You and Rocky saved us... {w=.3}he would still want that"
            n "So please, don't give up, {w=.3}because Rocky never did, {w=.3}just because he's..." 
            n 8"..."
            n 6"Doesn't mean he's not in our hearts, {w=.3}what do you think he would do right now?{w=.3} Shouldn't it be our responsibility to respect that?"
        v 12"..."
        v 11"...{w=.3} Rocky would kick my ass if he saw me moping...{w=.3} Say how it's just like me to sit and be a lazy sack of shit who feels nothing but self-pity..."
        v 10"Then he would,{w=.3} quite literally,{w=.3} lift me up and force me to keep going...{w=.3} just like how he did years ago when I gave up..."
       
        menu:

            "It's my fault he's dead...":
                $ addInsanity_level(-1)
                v 2"Oh!{w=.3} Don't you start now!{w=.3} Rocky would beat the shit out of you if he heard that!"
                v 12"Listen,{w=.3} I would have pussied out way worse than you did and taken out,{w=.3} like,{w=.3} you two {w=.5}PLUS the whole city if given the same dilemma."
                v "It's not something we really control...{w=.3} just sort of a flight or fight moment where we let our nerves get the better of us... {w=.3}guess we both need to work on that..."
                v "So don't beat yourself up...{w=.5} or else I'll do it for you in Rocky's spirit!"
                v 18"But... {w=.3}thanks...{w=.3} we appreciate that...{w=.3} truly...{w=.3} I'm sorry for making you think it was your fault when it's actually those FUCKING monsters outside!"

            "...":
                show static_anim with Dissolve(0.2)
                camera:
                    perspective True
                    easein_bounce 0.54 zpos -20
                $ addInsanity_level(1)
                hide static_anim with Dissolve(0.2)
                camera:
                    reset  
                pass

        if norman_dead == False and rocky_cafe_death == True:
            n 3a"It's going to be hard Vinnie...{w=.3} but you're a smart cookie!{w=.3} You know the government would set up safety perimeters somewhere,{w=.3} and that we need to make an effort to reach them..."
            n "It can be anything really!{w=.3} From a hospital they've safeguarded.{w=.3} Or a blocked off neighborhood....{w=.3} The problem right now is that the streets are just too crowded... {w=.3}Unless...?"
            n "There's someone in here that can help us?"

        if rocky_cafe_death == True:
            jump cafe_aftermath_2_electric_boogaloo
        else:
            return

    label cafe_aftermath_2_electric_boogaloo:
    menu:
        
        "I can't just stay silent;{w=.3} I need to let Norman know where I stand."

        "We can do this guys!":
            $ norman_affection += 1
            $ addInsanity_level(-1)
            n 2"Really?! {w=.3}I knew I could count on you [pov]!"
            if rocky_dead == False:
                    r 1"[pov]..."
            v 2 3"[pov]!?"
            p 14"Think about it! This building is huge! There are definitely more survivors out there!{w=.3} The bigger the group the stronger we are!"
            n "[pov] is so right!{w=.3} Hear me out on this!"

        "It's hopeless,{w=.3} might as well just wait for help":
            $ addInsanity_level(1)
            show static_anim with Dissolve(0.2)
            camera:
                perspective True
                easein_bounce 0.54 zpos -20
            n 8"[pov]..."
            hide static_anim with Dissolve(0.2)
            camera:
                reset
            if rocky_dead == False:
                r 1"I agree with [pov]... {w=.3}what's the point in trying? {w=.3}We'll just be getting ourselves killed."
                r "I have firsthand experience with how strong those things are,{w=.3} It's a death sentence to even try..."
            v 10"Yeah... {w=.3}I want to get out of here as much as the next guy, but it is pretty dangerous..."
            n 6"...I know it's scary guys, {w=.3}but we could do it!{w=.3} I think I have a plan..."
    play music "audio/music/Morning_Joe.mp3"
    n 2"We're already in a pretty big building right? {w=.3}That means it's an easy to find land marker for any nearby helicopters to land on!"
    n "Skyscrapers like this usually have their own antennae on top!{w=.3} Which means there has to be a way for us to reset it and contact someone!"
    v 25"I'm pretty sure the people that work here are trying to already do that...{w=.3}I mean,{w=.3} what are civilians meant to even do?"

    if rocky_dead == False:
        r 1"..."
        r 3"They gave me a safety plan map to the building in case something goes wrong..."
        show r 3 at offscreen_left with move
        pause 0.5
        "Rocky goes to the backroom and retrieves a hefty binder."
        show r 1 at left with moveinleft
        r 1"Here it is..."
    else:
        v 2"Corporate usually give employees safety plans maps... {w=.3}let me look in the backroom for it..."
        show v 2 at offscreen_left with move
        pause 0.5
        "Vinnie goes to the backroom and retrieves a hefty binder."
        show v 2 2 at right with move
        v 2 2"Oh Rocky...{w=.3} you're still helping us out even when you're gone..."

    n 2"Yeah, this is a great start!"
    "We all gather around the skyscraper map."
    v 1"Hey look here,{w=.3} it says there's a mechanical floor on the tenth..."
    v "If the power is off and the people here are having trouble activating it...{w=.3} we could do it ourselves from here..."

    if insanity_level >= 1:
        show static_anim with Dissolve(0.2)
        camera:
            perspective True
            easein_bounce 0.54 zpos -20 
        pause 0.3
        hide static_anim with Dissolve(0.2)
        camera:
            reset
        "Is this even worth the effort?"
    else:
        p 1"Also, I doubt the zombies would have made it that far up,{w=.3} I mean it's a pretty closed off building how far could the plague have spread?"

    if rocky_dead == False:
        n 2"You guys!{w=.3} This is perfect!{w=.3} C'mon Rocky what do you say?"
        r 1"..."
        r 2"I say it's worth a shot..."
        r "I guess I would just go crazy in here if I didn't even TRY escaping."
    else:
        n 2"You see?! {w=.3}We're real lucky to have you Vinnie!"
        
    n 2"That's the spirit we need to make it through this thing!"
    "Norman motions for a hug."
    
    if rocky_dead == True:
        "Vinnie drunkenly steps forwards before wrapping Norman in a tight embrace,{w=.3} lifting him off the ground with the sheer height difference."
        v 2 2"I can't believe he's dead man!"
        n 8"Shhh It's ok...{w=.3} just let it out..."
        "Vinnie sobs into Norman's shoulders for a moment...{w=.3} before stepping backwards and wiping their face..."
    else:
        if insanity_level == 0:
            p 13"Who can turn down a hug from NORMAN of all people!"
            "We all rush forwards to give Norman a hug!"
            "Rocky pretty much just lifted Norman and I off the ground from how strong he is...{w=.3} guess he really needed that hug...{w=.3}...{w=.3} I did too..."
        else:
            "They rush forward to give Norman a hug."
        if insanity_level == 0:
            p "I feel invincible already!"
        else:
            "I'm just a stranger compared to them... {w=.3}what right do I have?"
        
    v 3"The power of friendship guides me!"

    if rocky_dead == False:
        r 9"I'll kill you all if any of you die on me..."
        if insanity_level == 0:
            show r 2
            extend " also, Vinnie, were you caressing my hair?"
            v 23"Wait, {w=.3}I only did that because I thought you were the one poking my stomach!"
            p 3"Sorry, {w=.3}that was my horn..."

    n 7"Hahahaha!"

    n "We can do it guys!"

    if rocky_dead == False:
        r 10"YEAH!!!"
    v 6"YEAH!!!!!!!"
    if insanity_level == 0:
        p 13"Yeah!"

    pause 1.0
    $ renpy.music.set_pause(True, channel="music")
    v 2 4"Ok, so I didn't want to say anything earlier because I was honestly afraid to...{w=.3} but...{w=.3} do you always carry a loaded fucking handgun on you?!?!"
    $ renpy.music.set_pause(False, channel="music") 
    n 11"I have a license for it, and it is fully within my legal boundaries to wield it for self-defense,{w=.3} never know when trouble strikes!"

    n 13"Why do you think I always go with you on your late-night romps in the alleyways?"

    v 23"...{w=5}I am both flattered and seduced that you would be willing to put a bullet in someone's skull for me..."

    v 16"...{w=.3}But seriously do you carry that during class and stuff?"

    n 11"Let's just say it's not within OTHER people's legal boundaries...."

    v "..."
    v 10"...{w=.3} Norman...{w=.4} when did you have to use...{w=.5} the gun?"
    n 13"..."
    "..."
    "Norman is not one to be trifled with..."
    if rocky_dead == False:
        r 10"Well, you saved our asses earlier,{w=.3} thanks....{w=.3} you're clearly capable enough with it."
        p 13"Yeah! Thank you, Norman!"
        v 6"No!{w=.3} The bullet shots were actually me throwing my knife straight into that zombie's head!"
        v 5"If I recall correctly...{w=.3} Norman was freaking out the whole time while I valiantly saved you both!"
        show r 1a at hop
        r "Shut up Vinnie that was totally you!"
        show r 1a at offscreen_right with moveinleft
        show n 11 at offscreen_right with moveinleft
        show v 5 at offscreen_left with moveinleft
        "Rocky blurts out as we make our way to the staircase..."
    else:
        "I think as we me make our way to the staircase..."
    play sound "audio/sfx/short run.ogg"
    scene black with Dissolve(0.2)
    pause 0.5

    return


