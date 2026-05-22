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
    
    "It's October and college was finally almost over for me and my group of friends.{w=.3} It's about time we wind back and enjoy ourselves!"
    "We decided after class we should visit our friend at his new job as a barista."
    "He's employed in the lobby café of a skyscraper belonging to a massive company called{w=.3} \"Samsara\"."
    "The higher floors are for... {w=.3}whatever it is that business people do I guess?"
    "However, the first floor is much more of a recreational area for the general public."
    "There's even an indoor park and shopping district!"
    "It's mainly there to show off the businesses sponsoring them,{w=.3} but don't let consumerism ruin the moment."
    "I myself have never really gone in there before.{w=.3} I always assumed it'd be full of jaded business workers on their way to work."
    "I wonder if they're annoyed from seeing us lowly NPCs in the way?"
    "My friends and I came in from the subway transit.{w=.3} It was a nightmare trying to navigate our way through..."

    show v 1 at center with moveinright
    show v at hop_loop
    v 1"HEEEEEEEYY! GUUUUUUUYS!!! OVER HEEEREEEEE!!!{w=.3} HAHAHAHA!!"
    v "HURRY UP!!! I{w=.3} {i}NEED{/i} {w=.3}TO SEE ROCKY AT HIS NEW STUPID LITTLE JOB HAHAHAHAHA!!!"
    "Here comes Vinnie,{w=.3} being their boisterous self as usual."
    "They were the one who really pushed for us to visit Rocky after class. {w=.3}Now that I think about it..."
    "Vinnie was {w=.3}{i}always{/i}{w=.3} the one who initiated the group hangouts."
    show n 2 at right with moveinright
    n "OK! {w=.3}OK!{w=.3} SLOW DOWN WE'RE ALMOST THERE!"
    n "You're really excited for this aren't you?"
    "Oh,{w=.3} hey Norman. {w=.3}He's being as warmhearted as usual. Trying his best to keep up with Vinnie."
    "He was seen as the \"mom\" friend in the group.{w=.3} Always responsible with keeping us from killing ourselves with our antics."
    "Well, {w=.3}mainly just Vinnie to be honest..."
    show c 13 at right with moveinright
    with vpunch
    play sound "audio/sfx/short run.ogg"
    queue sound "audio/sfx/punch_4.ogg"
    show v 4 at hop
    show n 6 at hop
    s "Pardon."
    show n at shiver with move
    show v 4 at hop
    show n 6 at hop
    n 5"Ough!" with hpunch
    "A stranger Pine Marten bumps into Norman as he determinedly marches into the skyscraper's front entrance."
    show c 13 at offscreen_left with move
    play sound "audio/sfx/short run.ogg"
    "Vinnie and I steady Norman as he stumbles."
    show v 2 at hop
    v 2"Hey! {w=.3}Not cool man!{w=.3} That was totally on purpose!"
    hide c 13
    show n 6 at right with move
    n "Let's drop it,{w=.3} I'm not hurt.{w=.3} While I appreciate it..."
    n "Let's not start anything unnecessary alright?{w=.3} It's all about Rocky today!"
    v 12"...{w=.3}Ok if you say soooo."
    v 8"But if you change your mind...{w=.3} I'll just use this EPIC butterfly knife I got from the gas station!{w=.3} Haha!"
    show v at shiver
    "Vinnie twirls the knife around on their fingers. {w=.3}I wanted to say how silly they look, but I gotta admit that {w=.3}{i}is{/i} a cool trick..."
    n 1"Are you sure gas station knives are of the best quality? It'll probably break if you try using it..."
    v 5"Nuh-uh!{w=.3} The guy at the store said he gets them from a good source!"
    n 2"Wouldn't the person trying to sell you something be the one who brags about how great it is?"
    show v at hop_loop
    v "Well,{w=.3} then I'll beat that guy down with my fists of fury! {w=.3}Haha!"
    show v at hop
    v 17"Just kidding,{w=.3} my arms are noodles..."
    show v at hop_loop
    v 3"Instead, {w=.3}I'll summon my attack dog! {w=.3}Rocky!{w=.3} Who will beat him down for me!"
    n "Hmm,{w=.3} I guess it's ok. Since you didn't actually waste money. {w=.3}Yes,{w=.3} I {i}know{/i} you stole it."
    v 5"Heeheehee!"
    "Geez,{w=.3} why was that business guy in such a rush?{w=.3} Guess my assumption was correct..."
    show v at offscreen_left with move
    show n at offscreen_left with move
    pause 0.5
    scene cafe with Dissolve(0.2)
    play sound "audio/sfx/chime.ogg"
    show r 2 with Dissolve(0.2)
    r "Hello and welcome!{w=.3} What can I get you toda-"
    show r 8 at left1 with moveinleft
    r "Oh,{w=.3}{i} oh no.{w=.5} Please dear lord no...{/i}"
    show r at left with move 
    show v 2 4 with Dissolve(0.2)
    show v 2 4 at shiver_loop
    v "HAHAHAHAHAHAHAHAHAHAHA!!!!{w=.3} STOP!!!!{w=.3} STOP IT!!!!{w=.3} I- {w=.3}I CAN'T BELIEVE IT!!!" 
    "Seeing the hulking figure of Rocky sell such cute pastries in a pastel café is enough to make anyone laugh."
    "Even I have to stifle a laugh when it sets in, {w=.4}hehe."
    v "BAHAHAHAHAHAHAHA!!!!!!!!"
    "We move past Vinnie, currently laughing up a storm while leaning on a table for stability."
    show v at hop
    hide v with Dissolve(0.2)
    show n 1 with Dissolve(0.2)
    show n 1 at hop
    n "Hey Rocky! Nice to see you at your new post! {w=.3}Where's your co-worker?"
    r 1"She got a call from a family member. {w=.3}Something about a medical emergency..."
    n 5"Woah! {w=.3}That sounds really serious! {w=.3}Are they gonna be ok?"
    r "Honestly, {w=.3}I'm not sure.{w=.3} She sounded real rattled when she heard the news, {w=.3}must've been serious."
    "Rocky,{w=.3} being the eldest of the group, {w=.3}always seemed like he had an mountain of responsibilities to attend to."
    "I suppose Vinnie is only a year younger than him, but still,{w=.3} that's just how Vinnie is."
    "I'm somewhat new to the friend group, {w=.3}I think? {w=.3}"
    "Yet, I still know the others more than Rocky since his schedule prevents frequent hangouts."
    "I recall Norman mentioning how Rocky doesn't have a place to call home, so he bounces job to job to make ends meet."
    n 1"Well,{w=.3} we could cheer her up next time we visit you at work!"
    n "We're gonna be regular customers so she's bound to get to know us eventually, right?"
    r 6"You'd really be willing to sacrifice so much of your time for {w=.4}{i}me?{/i}"
    "He shakes his head, as if to swat the thought away."    
    r 2"Ugh,{w=.3} speaking of... {w=.3}You guys aren't gonna make this weird or anything? Remember I have to keep this job so don't screw-"
    hide n with Dissolve(0.2)
    show v 5 with Dissolve(0.2)
    v "Oh!{w=.3} We're definitely making things weird!"
    v 9"Hello sir!{size=*0.8} {w=.3}Write this down because it's gonna be a long one,{/size}{w=.3} I would like to order:"
    v "A half caffeine quad venti at two-hundred degrees with half soy, no foam with foam steamed with cinnamon, crosshatched caramel hazelnut swirl drizzling, pulled ristretto, sugar-free sugar, and a cherry on top please!"
    v "And my friends here would like an eggnog flat white and a unicorn frappe with a whole unpeeled banana in it, also make sure to use sugar-free replacements!!"
    v "What do you mean it's out of season and you don't accept hundreds? I want to speak with the regional manager!!!"
    show r 3a at hop
    r 3a"{w=.5}Suck actual fat fucking cock."
    show v at hop
    v 2 4"BAHAHAHAHAHAHAHAHAHA!!!"
    show r at center with move
    show v at right with move
    "Rocky rushes forward to shut Vinnie's muzzle."
    hide v with Dissolve(0.2)
    hide r with Dissolve(0.2)
    show n 2 with Dissolve(0.2)
    show n 2 at hop
    n 7"Hahahahaha!"
    n 2"Hey, we had our fun! How about we settle this down?"
    "Norman locks eyes with me and gently guides my arm towards the register."
    n 2"You go on ahead and order from Rocky since you two should talk more! {w=.3}Break the ice y'know?"
    hide n with Dissolve(0.2)
    show v 15 at right with Dissolve(0.2)
    show r 3a with Dissolve(0.2) 
    "I walk up to Rocky,{w=.3} currently holding Vinnie's muzzle closed while shaking them back and forth."
    "I think I can hear Vinnie's muffled cries for help as I get closer."
    "Rocky lets go of Vinnie when he sees me awkwardly staring at him."
    hide v 15 with Dissolve(0.2)
    show r 10 at hop

    r "Oh, that's right...{w=.3} I'm so sorry,{w=.3} but I'm having trouble remembering how to spell your name..."
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
        r "[pov]?{w=.3} You look like a [pov]... {w=.3}It fits..."

    elif pov in ["Breadley", "Bradley", "B0redbradley", "Boredbradley", "Breadly", 'Breadman']:
        "GO TO SLEEP ALREADY!!!!!!!"

    elif pov in ["Duncecap", "Dunce", "Dunce cap"]:
        "What the hell kind of name is that? Idiot!"

    elif pov in ["Bix", "Bixarre"]:
        "Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. Dolion. Gabriel. "

    elif pov == "Chris":
        "Shouldn't you be pushing boulders or something?"

    elif pov == "Leon":
        "*gasp* {w=.3}Where's baby eagle???{w=.3} Also your hair's really nice."

    elif pov == "Claire":
        "When are you getting another game?"        

    elif pov == "Jill":
        "OMG! NEMESIS IS BEHIND YOU!!!"

    elif pov == "Nemesis":
        "YOU WERE ACTUALLY SCARY IN THE OG!"

    elif pov in ["Tyrant", "Mr. X"]:
        "X GON' GIVE IT TO YA!"  

    elif pov == "Ada":
        "Stop playing with Leon's heart..."  

    elif pov in ["Ashley", "Babyeagle", "Baby Eagle", "Baby-Eagle", "Baby-eagle"]:
        "Remember to stick with Leon babe..."

    elif pov == "James":
        "Where's Mary?"  

    elif pov == "Mary":
        "{cps=*0.4}In my restless dream, I see that town. Silent Hill. You promised you'd take me there again someday. But you never did. Well, I'm alone there now, in our \"special place\". Waiting for you.{/cps}"   

    elif pov == "Heather":
        "Hmm,{w=.3} shouldn't you be avoiding a cult or something?"

    elif pov == "Harry":
        "REMAKE CONFIRMED! REMAKE CONFIRMED! GIMME THE SH1!!!!!!!)"

    elif pov in ["Dinnerbone", "Grumm"]:
        "WOAH! YOU'RE UPSIDE DOWN NOW!!!"

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

    elif pov == ["MC", "Protag", "Y/n", "Yn", "Pov", "Player", "P", 'Your Name', 'Mc']:
        "Not very creative now...."

    elif pov in ["Todd Howard", "Todd"]:
        "Please release TES6..."

    elif pov == ["William Afton", "Williamafton", "WilliamAfton", "Afton", "Springtrap", "Scraptrap"]:
        "The Man Behind The Slaughter"

    elif pov == "Chara":
        "the true name"

    elif pov in ["gaster", "Gaster", "WDGaster", "W.D.Gaster"]:
        $ MainMenu(confirm=False)()
        
    elif pov in ["ToddHoward", "Todd", "Todd Howard",]:
        "Please release TES6..."

    elif pov == "Luke":
        "You're Luke Skywalker,{w=.3} you're here to rescue me!"

    elif pov in ["Colburn", "Maizie", "Wren", "Xochi", "Gwen", "IO", "August", "Cole", "Colby", "Tara", "Taran", "Coburn", "Eilis", "Malachy"]:
        "What a strange coincidence..."

    elif pov in ["Frank", "Frank West"]:
        "But where's the scoop?"

    elif pov in ["Rocko", "Rocky"]:
        r "Woah, {w=.3}that's crazy how we share the same name!{w=.3} Two rocks versus the world!{w=.3} Hahahaha!"

    elif pov == "Rock":
        r "Wow!{w=.3} Almost like my name huh?{w=.3} We're two rocks against the world!{w=.3} Hahaha!"

    elif pov in ["Vinny", "Vinnie", "Vin", "Norm", "Norman"]:
        r "Oh!{w=.3} I better make sure I don't confuse you with one of our friends then!"

    elif pov in ["Mom", "Mommy", "Mother", "Mama"]:
        show v 2 4 at right with Dissolve(0.2)
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE!{w=.3} I SHOULD HAVE THOUGHT OF THAT! YOU HORN DOG!"
        hide v 2 4 at right with Dissolve(0.2)
        "I was born for the role of mother apparently..."

    elif pov in ["Dad", "Daddy", "Father", "Papa"]:
        show v 2 4 at right with Dissolve(0.2)
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! {w=.3}I SHOULD HAVE THOUGHT OF THAT! YOU THIRSTY THOT!"
        hide v 2 4 at right with Dissolve(0.2)
        "I was born for the role of father apparently..."

    elif pov in ["Douche", "Cunt", 'Fag', 'Faggit', 'Faggot', "Faglord", "Fagpipe", "Whore", "Fuck", "Fucker", "Ass", "Thot","Fuckface", "Fart", "Poop", "Shit", "Penis", "Cock", "Titty", "Cock", "Damn", "Dammit", "Boobs", "Tit", "Boob", "damm", "d4mm", "dick", "bastard", "blowjob", "turd", "anus", "bitch", "hoe", "ho", "booty", "butt", "cum"]:
        "I'll let it slide..."

    show r 10
    r 10"Duh!{w=.2} Of course I remember your name!{w=.3} I was just making sure!{w=.3} Ok [pov], {w=.3}what would you like?"
    n "Don't worry [pov]... Rocky knew your name. He really did want to just double check..."
    "Norman whispered into my ear. I hope he meant that..."
    show r at hop
    r 1"Wait a sec..."
    show r at hop_loop
    r 2"Dammit Vinnie! Stop trying to steal the cake pops!{w=.3} I'm not giving any more handouts like back then!!!"
    show v 5 at right with Dissolve(0.2)
    show r at hop
    v "Awwwww, c'mon man you used to do that for me all the time! {w=.3}You used to be cool Rocko! {w=.3}What happened?!?!"
    r 1"Well, {w=.3}{i}SOME{/i}{w=.3} people change and actually {w=.3}{i}MATURE{/i}{w=.3} overtime."
    r "{i}Something you'll never do apparently...{/i}"
    pause 0.5
    show r 11 at hop
    pause 0.5
    show r 11 at right with move
    play audio "audio/sfx/step_lth2.ogg"
    queue audio "audio/sfx/punch_4.ogg"
    pause 0.7
    show r 10 at hop
    pause 0.1
    show v 2 3 at shiver_loop_right
    pause 0.5
    show v 2 3 at hop_loop
    pause 0.5
    show r 11 at center with move
    v 2 3"YEOWCH!!! DID YOU JUST YANK MY TAIL ASSHOLE!"
    show v at hop
    r "Hmmmm, must've been the wind..."
    show v 5 at hop
    pause 0.4
    show v 5 at center with move
    play audio "audio/sfx/step_lth2.ogg"
    pause 0.2
    show v at hop
    play audio "audio/sfx/punch_4.ogg"
    show r 9 at shiver_loop
    pause 0.3
    show v 5 at right with move
    show r 9 at shiver_loop
    pause 0.3
    v 5 "GOTCHA!"
    show r 9 at hop_loop
    r "Asshat!{w=.3} I'll get you back!"
    show v at hop_loop
    v 6"You're gonna have to chase me, hehehehe!!!!"
    play audio "audio/sfx/step_lth2.ogg"
    show v at offscreen_left with move
    show r at offscreen_left with move
    play audio "audio/sfx/step_lth2.ogg"
    "Rocky chases Vinnie around the café for a bit...{w=.4} Norman laughs hysterically at their antics..."
    play audio "audio/sfx/step_lth2.ogg"
    pause 0.3
    "Wow, {w=.3}they're really booking it huh?{w=.3} I always forget just {w=.3}{i}how{/i}{w=.3} fast Vinnie is at running!"
    pause 0.5
    scene cafe with fade
    show v 1 at right with Dissolve(0.2)
    show n 1 with Dissolve(0.2)
    show r 1 at left with Dissolve(0.2)
    "Time passes,{w=.3} as we all take a seat and talk idly about what we've done recently."
    n 1"Ha, {w=.3}the professor really just threw that assignment out of nowhere, right?"
    r 1"Real smart of him considering half the class wasn't done with the last one yet..."
    p 1"Does he really have to give us another one?{w=.3} I felt the group presentation was enough..."
    v 6"Meh, {w=.3}you guys are just coping with the fact I'm actually the smartest,{w=.3} prettiest, {w=.3}{i}and{/i} most talented doctor in the making!"
    r 2"Ego much? Don't make me deflate your head with a coffee straw!{w=.3} Typical med student!"
    v 3"Awww, don't be jealous I have perfect straight A's!"
    r 4a"I have nothing to worry about considering you're late all the time and gonna get DROPPED if you don't shape up!"
    v 5"Shut it dropout! {w=.3}You only just started school!"
    r 2"Are you kidding?!?!{w=.3} We started a year apart! I was at least working!!" 
    # r "You were busy getting arrested or whatever the hell street rats like you do."   
    n 2"Hmmm, Vinnie's sort of right !{w=.3} They have pretty consistent marks!"
    p 15"\"Have to admit?\",{w=.3} as in, {w=.3}you didn't expect Vinnie to be this smart?"
    r 10"Hahaha! {w=.3}Serves you right if {i}Norman{/i} of all people thinks that less of you!"
    v 2 3"Norman! H-{w=.3}how could y-{w=.3}you... {w=.3}I THOUGHT WE WERE FRIENDS!!!"
    show v 9 at right
    "Vinnie pretends to bawl as they stuff their face into their hands."
    n 7"Hey! {w=.3}I never said that!"

    #########################################################################################
    ################################ WORKSHOP THIS MONOLOGUE ################################
    #########################################################################################

    show black with Dissolve(0.5):
        alpha.5
    "These are the people I choose to spend my time with,{w=.3} truthfully,{w=.3} I didn't have anyone else in my life."
    "I don't have the best relationship with my relatives, {w=.3}so I prefer staying out of their way.{w=.3} I was never the sociable type in school;{w=.3} or life in general."
    "It's because I know... {w=.5}that I'm a social vacuum. {w=.3}People seem to know this friend thing right off the bat, but for me it's such a chore..."
    "I attempted to join in the crowd when I was much younger."
    hide r with Dissolve(0.5)
    show black with Dissolve(0.5):
        alpha.6    
    "But playground insults like teasing my quietness and tone of voice repelled them from me."
    "Not to mention being shoved around and having food thrown at me when I'm turned the other way."
    "I felt it would be a wasted effort to try again, {w=.3}since that's not really an off and on switch..."
    "Why give people the opportunity to mock. When you could remove yourself from the scenario altogether?"
    "It got worse when adults took notice and started to coddle me. {w=.3}{i}I hate being patronized.{/i}{w=.3} It's like I'm being treated as lesser."
    "As if I were just some annoying noise people should learn to tolerate.{w=.3} Except, {w=.3}I don't want to be just tolerated."
    hide v with Dissolve(0.5)
    show black with Dissolve(0.5):
        alpha.7    
    "I want to be accepted."
    "I want to be a person."
    "Why is that so hard for me to do?{w=.3} Why can't I follow such simple instructions? {w=.3}Are normal people not meant to question this because it's hardcoded into their brains?"
    "Well, {w=.3}if it's not hardcoded into {i}my{/i} brain {w=.5}then what does that make me?"
    "..."
    hide n with Dissolve(1.)
    show black with Dissolve(1.):
        alpha.8    
    "I'm normal... {w=.5}right?"
    "..."
    "I just want to make friends... {w=.3}That's all I've ever really wanted... {w=.3}To feel like I'm not as much as an alien as people make me out to be."
    "Like I can actually be apart of the world instead of hiding from it."
    "..."
    pause 0.5
    show black with Dissolve(1.):
        alpha.6    
    "I've never spent this much time with anyone before.{w=.3} I was simply minding my business in class until one day..."
    "Norman offered to join him at the park."
    "He slowly introduced me to the rest of the circle. {w=.3}I'm very grateful to have people I can talk to and actually listen to me."
    "Rocky's dependable nature; always lending a hand when he can.{w=.3} Vinnie's good-nature and levity. {w=.3}They're always able to brighten up a tough day."
    "And Norman,{w=.3} he's always there to cheer me on. {w=.3}I don't think he's ever rejected a chance to talk with me either"
    "So he must enjoy my presence as much as I enjoy his..."
    "I suppose I never properly thanked him for this opportunity... {w=.3}I have to remember to do that soon..."
    hide black with Dissolve(0.2)
    
    #########################################################################################

    show v 4 at right with Dissolve(0.2)
    show v at hop
    v 4"EARTH TO [pov!u] EARTH TO [pov!u], HEY SPACE CADET YA THERE!?!?" with hpunch
    p 1"Ah, {w=.3}apologies.{w=.3} I wasn't paying attention."
    play music "audio/sfx/crowd panic.ogg" fadein 1.0
    v "You see this shit?!?! {w=.3}There's people screaming like crazy!"
    v 10"I didn't know the pride parade was coming {i}this{/i} early! Hahahahaha!!!"
    show r 3 with Dissolve(0.2)
    r 3"Vin, {w=.3}stop. Now isn't the time for your jokes, it's serious."
    show v 11 at sink
    "Rocky snaps back at Vinnie who slumped back in their chair with a defeated expression."
    hide v with Dissolve(0.2)
    "I've never heard Rocky's voice in that tone before with Vinnie"
    "Sure he got annoyed,{w=.3} but never actually meant it."
    "I shoot my head upwards and see Rocky with Norman; glued to the window."
    show n 3a at right with Dissolve(0.2)
    n "I'm trying to see what they're running from, but no luck..."
    r 7"They just keep pouring out!{w=.3} What could have caused this?"
    scene cafe window with Dissolve(0.2)
    show r 7 with moveinleft
    show n 8 at right with moveinright
    show v 11 at left with moveinleft
    "We stare out the window. Trying to pick out a source of the commotion."
    "There's hundreds of people packing the street.{w=.3} All running as fast as they can."
    play sound "audio/sfx/window smash.ogg"
    "Some people take advantage of the chaos and smash open miscellaneous store windows to rob them."
    play sound "audio/sfx/ambulance.ogg"
    "I can just barely make out some voices from the uproar."
    npc "JUST KEEP RUNNING!!!"
    npc "Get away from me,{w=.3} this is mine!!!"
    npc "Has anyone seen my husband?!?"
    # npc "HONEY, WHERE ARE YOU!?!?"
    npc "OH MY GOD! THEY'RE COMING FOR US! {w=.3}RUN!!"
    show v at left with Dissolve(0.2)
    v 12"This is too much to look at... {w=.3}I-{w=.3}I don't want to watch anymore..."
    show v at sink
    hide v with Dissolve(0.2)
    r 1"I'm heading out shop, {w=.3}I need to see what's up..."
    show n at hop
    n 5"Wait!{w=.3} You can't! {w=.3}Look at how many people are out there!"
    n "You see a bunch of people running from something and head straight into it?"
    r 1a"Relax, {w=.3}I'm just gonna sneak a peek then rush back in."

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
    "Before Norman can say any more. Rocky rushes out."
    "I choose to go out with him."
    show n at hop
    n "Are you two serious?!?!"
    
    scene cafe outer with Dissolve(0.2)
    show r 1 at right with Dissolve(0.2)
    pause 1.0
    show r 1 at center with move
    r 1"Oh,{w=.3} Hey [pov]!{w=.3} You followed me?{w=.3} Stay close, ok? I just wanna make out what's happening..."
    "Rocky and I crane our heads, trying to peek over the crowd."
    npc "Move it!"
    with hpunch
    p "Ough!"
    "A civilian shoulders me out of the way."
    r "HEY! Why don't you watch it, dick!"
    r "Sorry [pov], I dunno what's gotten into them! I'll have your back though!"
    "Before I can open my mouth, distant shrieking turns our heads."
    pause 0.5
    npc "GET AWAY FROM ME!!! {w=.3}GET AWAAAAAAY!!!"
    with hpunch
    p 4"Is someone being attacked?"
    r 2"Jesus!{w=.3} T-{w=.3}that shouting! {w=.3}Let's hurry! {w=.3}He sounds like he's in trouble!"
    r 4a"Don't worry! We'll help you!"
    show r at offscreen_right
    scene black with fade
    scene cafe outer with Dissolve(0.2)
    stop music fadeout 5.0
    play audio "audio/sfx/Wind.ogg"
    show r 1 with moveinleft
    "We rush towards the direction of the man's yelling.{w=.3} The panicking crowd thinned out and is nowhere near as big as before."
    play music "audio/music/live or die intro.ogg"
    queue music "audio/music/live or die.ogg"
    npc "HELP ME!!!{w=.3} PLEASE SOMEBODY HELP ME!!!"
    r 4a"Over there!"
    "We quicken our pace until we come across a man attacking another man!{w=.3} He's pinned him to the ground and mauling his neck!"
    show r at hop
    r 2"You goddamn freak! Get off him!"
    show r at hop
    with vpunch
    "Rocky strikes the back of the attacker's head. {w=.3}He doesn't seem to register the punch at all.."
    "Rocky grapples the back of him,{w=.3} attempting to restrain his arms."
    play sound "audio/sfx/zombie talk.ogg"
    "The attacker finally notices Rocky and tries clawing at him.{w=.3} A grotesque growl came along with it."
    "I didn't even know anyone was capable of evoking such a noise,{w=.3} almost like he wasn't even alive..."
    r 3a"What the hell are you?!?!"
    play sound "audio/sfx/zombie (2).ogg"
    show bigzom at shiver_loop with moveinright
    "The attacker is able to twist himself backwards and faces Rocky directly when tussling with him."
    "He's trying to bite Rocky's neck, but his restricted arms keep him at bay."
    show r at shiver_loop
    p 7"Don't worry, I got this!"
    play sound "audio/sfx/hit13.ogg"
    "I throw a punch at his jaw. {w=.3}I think I saw a tooth fly out!"
    with hpunch
    play sound "audio/sfx/hit12.ogg"
    "Rocky throws him to the ground and pins his face down with his boot."
    with vpunch
    show bigzom at sink with moveinright
    show r at hop
    "The attacker protests intensely.{w=.3} Like that of a flailing cockroach sprayed with poison."
    play sound "audio/sfx/zombie moan.ogg"
    "There's that awful noise again..."
    "Now that I'm closer I'm able to make out just how monstrous he is..."
    "He has milky white eyes and is dyed in blood. {w=.3}He conjures an odor so pungent it stings..."
    r 2"[pov!u]!{w=.3} Check out the guy he jumped to see if he's ok!"
    p 4"Got it!"
    hide r with Dissolve(0.2)
    hide bigzom with Dissolve(0.2)
    "I jog ahead to see the victim, motionless on the floor..."
    "Blood pools beneath him as I scrutinize the large gashes across his throat."
    p 7"Are you ok?!?!"
    "I check for a pulse, {w=.3}or any signs of breathing."
    pause 1.0
    "There's nothing."
    show r 3 with Dissolve(0.2)
    show r at hop

    r 3"Hey! {w=.3}[pov]!{w=.3} He alright!?!?"
    "I turn back to see a panicked Rocky still pinning down the attacker."
    p 7"Rocky! We need to call an ambulance his neck is-"
    pause 0.5
    show bluzom at offscreen_bottom
    play sound "audio/sfx/Zombie_03.ogg"
    show bluzom at left with move
    "I turn one-eighty and see the previously motionless man lurch at me!"
    "I try to hold his wrists in place when he grabs at me. I don't think I can fend him off for much longer!"
    with hpunch
    show bluzom at shiver_loop_left
    p 7"How are you alive!?" with vpunch
    r 3a"[pov!u]! Don't worry! I'll get to you!"
    show r at sink
    play sound "audio/sfx/hit13.ogg"
    queue sound "audio/sfx/zombie-22.ogg"
    "Rocky sprints towards me, but his foot gets grabbed by the person he was confining. {w=.3}He face-plants into the curb with a hard thud."
    with vpunch
    show bigzom at right with moveinright
    show bigzom at shiver_loop_right
    r 2a"JESUS! {w=.3}GET IT OFF!{w=.3} GET IT OFF!"
    show r at sink_rise
    show r at shiver_loop

    show screen character_stats with Dissolve(0.2)

    menu rocky_first_death_choice:
        "What should I do?"

        "Kick zombie attacking me in the knees" if first_zombie_attacker_dead == False:
            $ first_zombie_attacker_dead = True
            play sound "audio/sfx/hit.ogg"
            with hpunch
            queue sound "audio/sfx/zombie huh.ogg"
            show bluzom at offscreen_bottom with move
            hide bluzom
            queue sound "audio/sfx/zombie (2).ogg"
            "I use my smaller stature to my advantage and aim for it's knees!"
            "I was sucessfully able to tumble him over.{w=.3} It's down, but not dead. Now's my chance!"
            jump rocky_first_death_choice

        "Push off zombie attacking Rocky":
            if first_zombie_attacker_dead == True:
                "My horns are definitely sharp enough to cause some damage if use them! I've never done that before, but those clips online portrayed them as pretty deadly!"
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
                "The zombie was able to fully dig onto my arm and bite into my neck." with hpunch
                "I was too weak to fight back... {w=.3}I feel... {w=.5}lighter..."
                jump death_screen

            elif first_zombie_attacker_dead == False:
                label sage_being_pulled_back:
                $ sage_health -= 1
                $ addRockyhealth(-1) 
                play sound "audio/sfx/zombie-19.ogg"
                "I tried running as fast as possible, but the zombie nearest to me pulled my arm back." with vpunch
                if sage_health == 0:
                    jump sage_first_death
                "Didn't the exact thing happen to Rocky?{w=.3} I feel sharp nails dig into my arm,{w=.3} but was able to struggle out of it."
                "Damn that hurt... I see the other zombie similarly dig into Rocky's leg."
                if rocky_health == 0:
                    extend " His-"
                    jump rocky_dead_norman_rescue_sage
                else:
                    extend " Better be careful this time..."
                    jump rocky_first_death_choice

        "Call for help":
            $ addRockyhealth(-1) 
            p 7"NORMAN! VINNIE! ANYONE OUT THERE PLEASE HELP US!" with hpunch
            play sound "audio/sfx/zombie attack.ogg"
            r "AAGH!" with vpunch
            "Shit...{w=.3} Looks like Rocky just got a piece of his leg dug up...{w=.3} I need to do something!"
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
                "I run as fast as my legs could carry me to the café. In the distance, I could hear loud shrieking and gnawing noises."
                r "No!{w=.3} Noooo!{w=.3} Get off me you fucks! {w=.3}AAAAAGGHHHH!!!"
                $ addRockyhealth(-6) 
                pause 1.0
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
                pause 1.0
                "I guide them all the way to where Rocky and I got attacked."
                "We suddenly stop when we see-"
                "Two of those zombies on top of him, ripping out his insides.{w=.3} Must've both gone after him after I ran off..."
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
    "Out of nowhere, Norman whips a gun from inside his jacket to fire at the creatures!"
    "They drop dead with a hard thud as the bullet meets their brains."
    "Except,{w=.5} Rocky still hasn't gotten up..."
    show v 2 1 with moveinleft
    v 2 1"Rocky!{w=.3} Get up!{w=.3} Wake up!"
    "I've never seen Vinnie so distraught before..."
    v "Nonono...{w=.3} NO!!! NOOOO!!! GET UP YOU TOUGH SUNUVA GUN!"
    v "GET UP!{w=.3} STOP JUST LAYING THERE!"
    "Vinnie kneels as they cradle Rocky's lifeless body. His neck and stomach have been completely torn open..."
    "Norman's paralyzed; as pale as a ghost."
    v 2 2"THIS ISN'T HAPPENING! SOMEONE CALL THE POLICE!{w=.3} HE ISN'T THAT HURT!{w=.5} STOP JUST STANDING THERE!!!"
    p 2"Vinnie... {w=.4}His neck..."
    show v 2 1 at hop
    v 2 1"SHUT UP!{w=.3} SHUT THE FUCK UP!{w=.3} HE'S FINE!"
    "Vinnie tries to put back together Rocky's shredded neck.{w=.3} If only it were that simple..."
    show n 5 at left with Dissolve(0.2)
    n 5"We have to get out of here! {w=.3}Look over there!{w=.3} More of them are coming!"
    "Norman seemed to have snapped out of his trance.{w=.3} They try to pull Vinnie away from Rocky, but Vinnie resists."
    "I help when I see the zombies in the distance shuffle towards us."
    show v 2 2 at shiver_loop
    v 2 2"Stop it! {w=.3}Are you crazy? {w=.3}We can't just leave him here! {w=.3}Look, he's gonna be ok!"
    v "LET GO OF ME!!!{w=.3} ROCKY NEEDS MEEEEEEE!!!"
    "Vinnie sobs as we drag them back to the café."
    jump cafe_aftermath

    label norman_protects_rocky:
    stop music
    play sound "audio/sfx/cock.ogg"
    pause 0.5
    queue sound "audio/sfx/shoot.ogg"
    "A gunshot rings out as one zombie gets its brains blown out."
    r 4a"Wha-"
    play sound "audio/sfx/shoot.ogg"
    "A bullet flies straight into the zombie next to me."
    "The blood explodes from his head and splashes onto mine as he collapses."
    p 4"Who?"
    show n 2a at left with moveinleft
    $ norman_has_gun = True
    n "I told you it wasn't safe out here..."
    r 8"Y-{w=.3}you...{w=.3} YOU JUST KILLED TWO PEOPLE!?!?"
    show n 14 at left with moveinleft
    "Norman points at the chest of the thing that attacked Rocky."
    n "No, {w=.3}look at the injury of this one...{w=.3} I only fired once, so why does he already have another gunshot wound?"
    r "I-{w=.3}I-..."
    n "No one can survive a shot to the heart and live.{w=.3} Think about it."
    pause 1.0
    n "C'mon we need to take cover. {w=.3}It isn't safe being exposed like this."
    show v 10 at right with moveinright
    v 10"Uh guys?{w=.3} You really shouldn't have left us behind lik-"
    v 16"..."
    pause 1.0
    show v 2 3 at hop
    v 2 3"{w=.3} HOLY FUCKING SHIT!"
    show v at hop
    v "OH MY GOD! I'M GONNA BE SICK! WHAT THE FUCK HAPPENED HERE?!?!"
    n "No time to explain! We gotta get back!"
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
    tv "ALL CIVILIANS ARE EXPECTED TO STAY IN YOUR SHELTERS. {w=.3}DO NOT EXIT UNDER ANY CIRCUMSTANCES."
    tv "BARRICADE ALL OPENINGS WITH ANY FURNITURE OR OBJECTS NEAREST TO YOU.{w=.3} AVOID THE INFECTED AT ALL COSTS."
    tv "AN EPIDEMIC HAS OCCURRED.{w=.3} THE GOVERNMENT IS WORKING FOR A SOLUTION TO SITUATION.{w=.3} PLEASE STANDBY."
    tv "FROM WHAT WE KNOW THE ABNORMAL PATHOGEN SPREADS THROUGH INFECTING THE LIVING WITH- REACTIVATING- MAKING- ACT- HIGHLY AGGRESSIVE {w=.3}BE-{w=.4} C-"
    "The broadcast starts breaking up."
    if rocky_dead == False:
        r 3"C'mon, work you stupid thing!"
    tv "{w=.3}-I---- {w=.3}A- {w=.3}P---- {w=.5}MAY GOD HAVE MERCY ON OUR SOULS-"
    play sound "audio/sfx/zap.ogg"
    stop music fadeout 0.5
    pause 1.0
    scene cafe with Dissolve(0.2) 
    show black with Dissolve(0.2):
        alpha.6
    pause 1.0
    "The power goes out and we're left in silence..."
    pause 1.0
    "..."
    pause 1.0
    if rocky_dead == False:
        "Rocky and Norman barricaded the windows with chairs and crates from the backroom."
    else:
        "Norman and I already barricaded the windows with chairs and crates from the backroom."
        "Vinnie hasn't moved or talked since we dragged them in.{w=.3} I think Rocky's passing finally set in..."
    "I hear a cacophony of moans and shuffling feet from outside. {w=.3}I don't think it's safe to leave anytime soon..."
    "Even if we were to leave... Where would we go?"
    "We came here from using the subway.{w=.3} I doubt a cramped, underground area is worth the risk of travel.."
    "Vinnie could try hot-wiring one of the cars from outside, but what if we run into a huge horde of those things?{w=.3} We'd be surrounded..."
    if rocky_dead == True:
        "I also don't think they're in a very...{w=.3} {i}active{/i} state right now..."
    "We decided to just wait it out in here for the past couple hours... {w=.3}The broadcast advised us all to stay where we are..."
    "Someone's bound to rescue us, right?"
    "..."
    "There isn't much else for us to do so why eve-"
    hide black with Dissolve(0.2)
    show n 6 with Dissolve(0.2)
    n "We're gonna make it through this."
    "...?"
    show v 11 at right with Dissolve(0.2)
    if rocky_dead == False:
        show r 7 at left with Dissolve(0.2)
    "We perk up at Norman."
    n "We're gonna make it out of here. I can assure you all."
    if rocky_dead == False:
        r 8"What are you talking about?{w=.3} It's practically hell on earth right now!"
        r 1"We're stuck in here and God knows what our families are going through."
        "I could see Vinnie visibly wince at that."
        r 3"It'd be a tragedy if they came across those things. We can only hope they're also hiding."
        r 8"Or worse, {w=.3}they're already gone."
        r 7"There are people {w=.3}{i}eating{/i}{w=.3} one another and you think we have a chance at this?!"
        n 6"Stop that."
        n "I remember when I was practically broke and about to live on the streets, when all of the sudden... You offered me a place to live."
        n 8"Even though you could barely afford it.{w=.3} You still risked it.{w=.6} And then you got evicted for having a tenant without the landlord's consent."
        n 6"You still chose to be my friend. Even though I ruined your life."
        n "What chance did we have then?{w=.3} But, you still took it to help me out..."
        r 8"Norman, {w=.3}you never ruined anything I already told you-"
        n 6"I know,{w=.5} I never forgot."
        v 12"That's how you lost your place?{w=.3} I never knew that part..."
        v 11"I-{w=.3}I don't know...{w=.3} about this guys... {w=.3}What really can we do besides just get ourselves k-{w=.3}killed..."
        n "Vinnie,{w=.3} listen, {w=.3}you're the smartest person I know. With your brains we're fated to find a way to escape!"
        n 2"As long as we all got each other and stay careful. It can't go wrong!"
        v 12"...!"
        r 1"What are you getting at?"
        n 6"I'm saying that my friends are amazing people. That don't deserve to be trapped like this."
        n 3a"Stuck in here,{w=.3} twiddling our thumbs.{w=.3} Hoping for the best."
        n 1"We can call for help and reach a safe zone somewhere!"
        n "Think about it! {w=.3}The government had to have set up a perimeter somewhere;{w=.3} all we have to do is come in contact with them and let them know we're here!"
        r 1"Didn't you just say it was best to take cover?"
        n 3a"I know what I said...{w=.3} But, look outside... {w=.3}If they find us, we'd be completely trapped in here and...{w=.3} and..."
        n 8"..."
        n 6"They'll eventually starve us out if we don't leave soon. Might as well try to look around, right?"
        v 2"Yeah, I don't think we could survive off frappes and cake pops forever..."
        n 2"We can always bunker here again if we don't find anything!"
    else:
        v 2 2"Rocky was ripped into pieces and you expect us to have a chance?"
        "Vinnie said in a somber tone from the corner of the room.{w=.3} For the first time in a long while"

        label vinnie_reaction_rocky_death:
        show v 2 2 with Dissolve(0.2)
        v "If someone as capable of Rocky didn't make it then we're gonna die here just like him..."
        v "It doesn't matter if you wave that gun around.{w=.3} There's no chance of survival...{w=.3} Might as well just point it at me..."
        v "Rocky's family is gonna be heartbroken when they find out.{w=.3}That the son that took care of them...{w=.3} Worked his ass of for their wellbeing is gone.{w=.3} Just like that"
        v "If they're even alive that is.{w=.3} They could be dead for all we know,{w=.3} all ours could be,{w=.3} so what's the point of it all? Die out there or wither away in here..."
        v "Starvation is a Hail Mary at this point..."
        v "The \"Best\" case scenario is if the national guard comes in here to rescue us...{w=.3} Even then,{w=.3} is it even worth living a life without the people who care about you..."
        if norman_dead == False:
            show v 2 2 at right with move
            show n 8 with Dissolve(0.2)
            n 8"..."
            n "I remember when I was about to live on the streets.{w=.3} Rocky saved me,{w=.3} he welcomed me into his home and took care of me."
            n "Housing an extra tenant got him evicted.{w=.3} Yet,{w=.3} he still kept being my friend. {w=.3}He said he'd do it all over again too if it meant I was safe."
            n "Rocky loved all of us. {w=.3}He always talked about how you came into his life and saved him, so he returns the favor to everyone he knows. To give them that same experience."
            n "He told me life is about taking the losses and accepting the opportunity it grants you; {w=.3}because a life without loss...{w=.3} Means nothing to gain..."
            n 6"\"What's a life worth living without the people who care about you?\".{w=.3} An opportunity to bring in people who are just as lonely..."
            n "You and Rocky were so close and you extended that to me...{w=.3} You two made me feel like I was a part of that and worthy of being loved..."
            n "We did the same with [pov]. Who had no one else in their life...{w=.3} You and Rocky saved us... {w=.3}He'd still want that."
            n "So please, don't give up. {w=.3}Because Rocky never did, {w=.3}just because he's..." 
            n 8"..."
            n 6"Doesn't mean he's not in our hearts. {w=.3}What do you think he would do right now?{w=.3} Shouldn't it be our responsibility to respect that?"
        v 12"..."
        v 11"...{w=.3} Rocky would kick my ass if he saw me moping..."
        v "Say how it's just like me to give up and be a lazy sack of shit who feels nothing but self-pity..."
        v 10"Then he would,{w=.3} quite literally,{w=.3} lift me up and force me to keep going... {w=.3}Just like how he did years ago when I gave up..."
       
        menu:

            "It's my fault he's dead...":
                $ addInsanity_level(-1)
                v 2"Oh!{w=.3} Don't you start now!{w=.3} Rocky would beat the shit out of you if he heard that!"
                v 12"Listen,{w=.3} I would have wimped out way worse than you did."
                v "And taken out,{w=.3} like,{w=.3} you two. {w=.5}PLUS the whole city if put in that position."
                v "It's not something we really control...{w=.3} Just sort of a flight or fight moment where we let our nerves get the better of us..."
                v "Guess we both need to work on that..."
                v "So don't beat yourself up...{w=.5} Or else I will! {w=.3}In Rocky's spirit!"
                v 18"But... {w=.3}thanks...{w=.3} We appreciate it...{w=.3} Truly...{w=.3} I'm sorry for making you think it was your fault."
                v "When it's actually those FUCKING monsters outside!"
                n "Everything will be ok. Learn from past mistakes and take the steps for a better future..."
                "I see Norman wipe a tear from his eye. Vinnie gently pats his back..."

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
            n 3a"It's going to be hard Vinnie...{w=.3} But you're a smart cookie!"
            n "You know the government would set up safety perimeters somewhere. All we need to do is make an effort to reach them..."
            n "It can be anything really!{w=.3} From a hospital they've safeguarded.{w=.3} Or a blocked off neighborhood..."
            n "The problem right now is that the streets are just too crowded... {w=.3}Unless...?"
            n "There's something or, someone, in here that can help us?"

        if rocky_cafe_death == True:
            jump cafe_aftermath_2_electric_boogaloo
        else:
            return

    label cafe_aftermath_2_electric_boogaloo:
    menu:
        
        "I can't just stay silent.{w=.3} I need to let them know where I stand."

        "We can do this guys!":
            $ norman_affection += 1
            $ addInsanity_level(-1)
            n 2"Really?! {w=.3}I knew I could count on you [pov]!"
            if rocky_dead == False:
                    r 1"[pov]..."
            v 2 3"[pov]!?"
            p 14"Think about it! This building is huge!{w=.3} There are definitely more survivors out there!{w=.3} The bigger the group, the stronger we are!"
            n "[pov] is so right!{w=.3} Hear me out on this!"

        "It's hopeless...":
            $ addInsanity_level(1)
            show static_anim with Dissolve(0.2)
            camera:
                perspective True
                easein_bounce 0.54 zpos -20
            n 8"[pov]..."
            hide static_anim with Dissolve(0.2)
            camera:
                reset
            "I release the breath I didn't know I was holding. I think I felt a blood vessel pop?"
            if rocky_dead == False:
                r 1"I agree with [pov]... {w=.3}What's the point in trying? {w=.3}We'll just be getting ourselves killed."
                r "I have firsthand experience with how strong those things are,{w=.3} It's a death sentence to even try..."
            v 10"Yeah... {w=.3}I want to get out of here as much as the next guy, but it is pretty dangerous..."
            n 6"...I know it's scary guys, {w=.3}but we could do it!{w=.3} I think I have a plan..."

    play music "audio/music/Morning_Joe.mp3"
    n 2"We're already in a pretty big building right? {w=.3}That means it's an easy to find land marker for any nearby helicopters!"
    n "Skyscrapers like this usually have their own comms system! {w=.3}We could use it to contact someone!"
    v 25"I'm pretty sure the people that work here are already trying to do that...{w=.3}I mean,{w=.3} what are civilians meant to even do?"

    if rocky_dead == False:
        r 1"..."
        r 3"They gave me a safety plan map to the building in case something goes wrong..."
        show r 3 at offscreen_left with move
        pause 0.5
        "Rocky goes to the backroom and retrieves a hefty binder."
        show r 1 at left with moveinleft
        r 1"Here it is..."
    else:
        v 2"Corporate usually give employees safety plans maps... {w=.3}Let me look in the backroom for it..."
        v "Rocky gave me an extra key if I ever needed a safe place to bum off in..."
        show v 2 at offscreen_left with move
        pause 0.5
        "Vinnie goes to the backroom and retrieves a hefty binder."
        show v 2 2 at right with move
        v 2 2"Oh...{w=.3} You're still helping us out even when you're gone..."

    n 2"Yeah... {w=.3}Yeah!{w=.3} This is a great start!"
    "We all gather around the skyscraper map."
    v 1"Hey, look here.{w=.3} It says there's a mechanical floor on the tenth floor..."
    v "If the power is off and the people here are having trouble reactivating it...{w=.3} We could do it ourselves from there!"

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
        p 1"I also doubt that the zombies made it that far up.{w=.3} I mean, it's a pretty closed off building. How fast could the plague have spread?"

    if rocky_dead == False:
        n 2"You guys!{w=.3} This is perfect!{w=.3} C'mon Rocky what do you say?"
        r 1"..."
        r 2"I say it's worth a shot..."
        r "I guess I would just go crazy in here if I didn't even{w=.3} TRY {w=.3} escaping."
    else:
        n 2"You see?! {w=.3}We're real lucky to have you Vinnie!"
        
    n 2"That's the spirit we need to make it through this thing!"
    "Norman motions for a hug."
    # PENIS
    if rocky_dead == True:
        "Vinnie drunkenly steps forwards before wrapping Norman in a tight embrace.{w=.3} Lifting him off the ground with the sheer height difference."
        v 2 2"I can't believe he's dead man!"
        n 8"Shhh, it's ok...{w=.3} Just let it out..."
        "Vinnie sobs onto Norman for a moment...{w=.3} Before taking a step back and wiping their face..."
    else:
        if insanity_level == 0:
            p 13"Who can turn down a hug from NORMAN of all people!"
            "We all rush forwards to give Norman a hug!"
            "Rocky pretty much just lifted Norman and I off the ground from how strong he is...{w=.3} Guess he really needed that hug...{w=.3} I did too..."
        else:
            "They rush forward to give Norman a hug."
        if insanity_level == 0:
            p "I feel invincible already!"
        else:
            "I'm just a stranger compared to them... {w=.3}What right do I have?"
        
    v 3"The power of friendship guides me!"

    if rocky_dead == False:
        r 9"I'll kill you all if any of you die on me!"
        if insanity_level == 0:
            show r 2
            extend " Also, Vinnie. Were you caressing my hair?"
            v 23"Wait, {w=.3}I only did that because I thought you were the one poking my stomach!"
            p 3"Sorry, {w=.3}that was my horn..."

    n 7"Hahahaha!"

    n "We can do this guys!"

    if rocky_dead == False:
        r 10"YEAH!!!"
    v 6"YEAH!!!!!!!"
    if insanity_level == 0:
        p 13"Yeah!"

    pause 2.0
    $ renpy.music.set_pause(True, channel="music")
    v 10"Ok, so I didn't want to say anything earlier because I was honestly afraid to...{w=.3} But...{w=.3} do you always carry a loaded fucking handgun on you?!?!"
    $ renpy.music.set_pause(False, channel="music") 
    n 11"I have a license for it, and it is fully within my legal boundaries to wield it for self-defense.{w=.3} Never know when you might need it!"

    n 13"Why do you think I always go with you on your late-night vandalism projects?"

    v 23"...{w=5}I am both honored and seduced that you would be willing to put a bullet in someone's skull for me."

    v 16"Do you seriously carry that during class and stuff?"

    n 11"Let's just say... It's not within {i}OTHER{/i} people's legal boundaries...."

    v "..."
    v 10"...{w=.3} Norman...{w=.4} When did you have to use...{w=.5} the gun?"
    n 13"..."
    "..."
    "Norman is not one to be trifled with..."
    if rocky_dead == False:
        r 10"Well, you saved our asses earlier.{w=.3} Thank you!....{w=.3} You're clearly capable enough with it."
        p 13"Yeah! Thank you, Norman!"
        v 6"No!{w=.3} The bullet shots were actually me throwing my knife straight into that zombie's head!"
        v 5"If I recall correctly...{w=.3} Norman was freaking out the whole time while I valiantly saved you both!"
        show r 1a at hop
        r "Shut up Vinnie! That was totally you!"
        show r 1a at offscreen_right with moveinleft
        show n 11 at offscreen_right with moveinleft
        show v 5 at offscreen_left with moveinleft
        "Rocky blurts out as we make our way to the mechanical floor staircase..."
    else:
        "I think as we me make our way to the mechanical floor staircase..."
    play sound "audio/sfx/short run.ogg"
    scene black with Dissolve(0.2)
    pause 0.5

    return


