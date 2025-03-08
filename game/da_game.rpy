default rocky_dead = False
default viv_dead = False
default norman_dead = False
default health = 100
default insanity_level = 0
default friendship_level = 0


label cafeintro:
    $ pov="Sage"

    play music "audio/music/mixkit-positive-energy-973- Michael Ramir C.ogg" fadein 1
    scene cafe outer with dissolve
    "Today is the first day of October, college was finally almost over for my new group of friends and I so It was as good as any other time to wind back and enjoy ourselves"
    "We decided after class we should visit our friend at his new job as a barista"
    "He's employed on the first floor of a skyscraper belonging to a biotechnology company called \"Samsara Enterprises\""
    "I've never really gone in here before since it's always full of white collars and bigiwgs"
    "Although the first floor is much more of a recreational area for the general public to show off the other businesses sponsoring \"Samsara\""
    "There's even an indoor park and shopping district! The other floors were locked to the business associates and office workers of Samsara"
    "We came in from the underground railway, {w=.3}it was a nightmare trying to navigate our way through hordes of people"

    show vinnie with dissolve
    v "HEY! GUYS OVER HERE!!!{w=.3} HAHA!!"
    show vinnie at hop
    v "HURRY UP!!! I {i}NEED{/i} TO SEE ROCKY IN HIS NEW STUPID LITTLE APRON HAHAHAHAHA!!!"
    "This was Vinnie,{w=.3} my gender diverse Opossum friend, being their boisterous self per usual"
    "They were the one who really pushed for us to visit Rocky after class, Vinnie was always the one who initiated the group hangouts"
    show norman at right with dissolve
    n "OK OK RELAX WE'RE ALMOST THERE!"
    n "You're really excited for this aren't you?"
    "Here's Norman,{w=.3} my compassionate Golden Retriever buddy, as caring as ever trying to humor Vinnie"
    "They were seen as the \"mom\" friend in the group,{w=.3} always responsible with keeping us from killing ourselves with our antics {w=.5}{i}well mainly just Vinnie to be honest...{/i}"
    npc "Hey watch it buddy!"
    n "Ough!" with hpunch
    "A stranger in a business suit and briefcase bumped into Norman on his way to the upper floor elevator"
    v "Hey! {w=.3}Not cool man!{w=.3} That was totally on purpose!"
    n "Just drop it,{w=.3} I'm not hurt; {w=.3}let's not start anything unneccessary alright?{w=.3} It's all about Rocky's new job today!"
    v "...{w=.3}Ok if you say so..."
    v "If you change your mind... I'll use this epic butterfly knife I got from the gas station! Ha!"
    "Vinnie twists the knife around on his fingers..."
    n "...I don't think gas station knives are the best quality though...{w=.3} It'll probably snap if you actually try to stab something with it..."
    v "Nuh-uh! the guy at the store said he got it from a good vendor!"
    n "Wouldn't the person trying to sell you something be the one who brags how great it is?"
    v "Well then I'll beat that guy down with my fists of fury! {w=.3}Haha!"
    v "Just kidding my arms are noodles... {w=.3}I'll summon my attack dog, {w=.3}Rocky,{w=.3} who will beat him down for me!"

    "Geez why was that business guy in such a rush?{w=.3} Just another reason for why I never hung out around here..."
    hide norman with dissolve
    hide vinnie with dissolve
    pause 0.5
    scene cafe with dissolve
    play sound "audio/sfx/chime.ogg"
    r "Hello and welcome!{w=.3} What can I get you toda-"
    show rocky with dissolve
    r "Oh{w=.3}{i} oh no{w=.5} please god no...{/i}"
    show rocky at left with move 
    show vinnie with dissolve
    show vinnie at rattle
    v "HAHAHAHAHAHAHAHAHAHAHA!!!!{w=.3} STOP!!!!{w=.3} STOP IT!!!!{w=.3} I- {w=.3}I CAN'T BELIEVE IT!!!" 
    show vinnie at rattle
    v "HAHAHAHAHAHAHA"
    "We move past Vinnie who is currently laughing up a storm while leaning on a table for stability"
    show vinnie at hop
    hide vinnie with dissolve
    show norman with dissolve
    show norman at hop
    n "Hey Rocky nice to see you at your new post! {w=.3}Where's your co-workers?"
    r "She got a call from a family member, {w=.3}something about a medical emergency..."
    n "Woah! That sounds really serious are they gonna be okay?"
    r "Honestly, {w=.3}I'm not sure she sounded real rattled when she heard the news, must've been real serious"
    "Rocky was the eldest of the group,{w=.3} a jaded Maned Wolf,{w=.3} he always seemed so grumpy with his place in life no matter where he was"
    "I'm relatively new to friend group yet I still know the others more than Rocky since he often misses our hangouts"
    "I recall Norman mentioning how Rocky doesn't have a place to call home so he bounces job to job to make ends meet"
    n "Well,{w=.3} we could cheer her up next time we visit you at work!{w=.3} We're gonna be regular customers so she's bound to get to us know eventually right?"
    r "Ugh,{w=.3} speaking of... {w=.3}You guys aren't gonna make this weird or anything? Remember I have to keep this job so don't scre-"
    hide norman with dissolve
    show vinnie with dissolve
    v "Oh!{w=.3} We're definently making things weird!"
    v "Hello sir!{size=*0.5} {w=.3}write this down because it's gonna be a long one{/size}{w=.3} I would like to order:"
    v "A half caffeine quad venti at 200 degrees with half soy, no foam with foam steamed with cinnamon, crosshatched caramel hazelnut swirl drizzling, pulled ristretto, sugar-free sugar, and a cherry on top please!"
    v "And my friends here would like an eggnog flat white and a unicorn frappe with a whole unpeeled banana in it, also make sure to use sugar-free replacements!"
    v "What do you mean it's out of season and you don't accept $100s? I want to speak with the regional manager!!!"
    r "{w=.3}Suck actual fucking cock"
    v "BAHAHAHAHAHAHAHAHAHA!!!"
    show rocky at center with move
    show vinnie at right with move
    "Rocky lunges forward to shut Vinnie's snout"
    hide vinnie with dissolve
    hide rocky with dissolve
    show norman with dissolve
    show norman at hop
    n "Hey we had our fun how about we settle this down!"
    n "Why don't we get actual drinks here to relax?{w=.3} You go on ahead and order from Rocky since you two haven't had many chances to talk!"
    hide norman with dissolve
    show vinnie at right with dissolve
    show rocky with dissolve 
    "I walk up to Rocky,{w=.3} currently holding Vinnie's snout closed while pushing him back and forth"
    "Rocky stops what he's doing when he sees me at the register"
    hide vinnie with dissolve
    "Oh that's right...{w=.3} I'm so sorry,{w=.3} but I'm having trouble remembering your name..."

    $ pov = renpy.input("It's fine, my name is", length=10).strip() or "Sage"    

    if pov == "Sage":
        r "[pov]? You look like a [pov]... it fits..."

    elif pov == "sage":
        r "[pov]? You look like a [pov]... it fits..."

    elif pov == "Breadley":
        "Huh?{w=.3} Shouldn't you be sleeping?"

    elif pov == "Bradley":
        "Huh?{w=.3} Shouldn't you be sleeping?"

    elif pov == "B0red Bradley":
        "Huh?{w=.3} Shouldn't you be sleeping?"

    elif pov == "Bored Bradley":
        "Huh?{w=.3} Shouldn't you be sleeping?"

    elif pov == "Dunce Cap":
        "What the hell kind of name is that?{w=.3} GET A JOB BOZO! FATHERLESS BEHAVIOR!"

    elif pov == "dunce cap":
        "What the hell kind of name is that? {w=.3}GET A JOB BOZO! FATHERLESS BEHAVIOR!"

    elif pov == "Chris":
        "Shouldn't you be pushing boulders or something?"

    elif pov == "Leon":
        "*gasp* {w=.3}Where's baby eagle???{w=.3} also your hair's really nice"

    elif pov == "Claire":
        "When are you getting another game?"        

    elif pov == "Chris":
        "Shouldn't you be pushing boulders or something?"

    elif pov == "Jill":
        "OMG NEMESIS IS BEHIND YOU!!!"

    elif pov == "Ashley":
        "Remember to stick with Leon babe..."

    elif pov == "Baby Eagle":
        "Remember to stick with Leon babe..." 

    elif pov == "Dinnerbone":
        "WOAH YOU'RE UPSIDE DOWN NOW!!!"

    elif pov == "Grumm":
        "WOAH YOU'RE UPSIDE DOWN NOW!!!"

    elif pov == "Chara":
        "the true name"

    elif pov == "Todd":
        "Please release TES6..."

    elif pov == "Luke":
        "You're Luke Skywalker, You're here to rescue me!"

    elif pov == "Cunt":
        "Very mature but I'll let it slide..."

    elif pov == "Whore":
        "Very mature but I'll let it slide..."

    elif pov == "Fuck":
        "Very mature but I'll let it slide..."

    elif pov == "Fucker":
        "Very mature but I'll let it slide..."

    elif pov == "Ass":
        "Very mature but I'll let it slide..."

    elif pov == "Fuckface":
        "Very mature but I'll let it slide..."

    elif pov == "Fart":
        "Very mature but I'll let it slide..."

    elif pov == "Poop":
        "Very mature but I'll let it slide..."

    elif pov == "Shit":
        "Very mature but I'll let it slide..."

    elif pov == "Faggot":
        "Very mature but I'll let it slide..."

    elif pov == "Penis":
        "Very mature but I'll let it slide..."

    elif pov == "Cock":
        "Very mature but I'll let it slide..."

    elif pov == "Titty":
        "Very mature but I'll let it slide..."

    elif pov == "Fag":
        "Very mature but I'll let it slide..."

    elif pov == "Penis":
        "Very mature but I'll let it slide..."

    elif pov == "Cock":
        "Very mature but I'll let it slide..."

    elif pov == "Titty":
        "Very mature but I'll let it slide..."

    elif pov == "Damn":
        "Very mature but I'll let it slide..."

    elif pov == "Dammit":
        "Very mature but I'll let it slide..."

    elif pov == "God dammit":
        "Very mature but I'll let it slide..."

    elif pov == "Boobs":
        "Very mature but I'll let it slide..."

    elif pov == "Boob":
        "Very mature but I'll let it slide..."

    elif pov == "Vinny":
        "What a strange coincidence..."

    elif pov == "Vinnie":
        "What a strange coincidence..."

    elif pov == "Vivi":
        "What a strange coincidence..."

    elif pov == "Vincent":
        "What a strange coincidence..."

    elif pov == "Vin":
        "What a strange coincidence..."

    elif pov == "Rocko":
        "What a strange coincidence..."

    elif pov == "Rocky":
        "What a strange coincidence..."

    elif pov == "Norm":
        "What a strange coincidence..."

    elif pov == "Norman":
        "What a strange coincidence..."

    elif pov == "Colburn":
        "What a strange coincidence..."

    elif pov == "Maizie":
        "What a strange coincidence..."

    elif pov == "Wren":
        "What a strange coincidence..."

    elif pov == "Gwen":
        "What a strange coincidence..."

    elif pov == "Xochi":
        "What a strange coincidence..."

    elif pov == "IO":
        "What a strange coincidence..."

    elif pov == "August":
        "What a strange coincidence..."

    elif pov == "Cole":
        "What a strange coincidence..."

    elif pov == "Colby":
        "What a strange coincidence..."

    elif pov == "Mom":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE!{w=.3} I SHOULD HAVE THOUGHT OF THAT!"

    elif pov == "Mother":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE! {w=.3}I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Mommy":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE! {w=.3}I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Dad":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! {w=.3}I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Daddy":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE!{w=.3} I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Father":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE!{w=.3} I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Papa":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE!{w=.3} I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Mama":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE! {w=.3}I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    else:

        pass

    r "Okay [pov], {w=.3}what would you like?"

    hide rocky with dissolve
    pause 0.5
    scene black with dissolve
    scene cafe with dissolve
    show vinnie at right with dissolve
    show norman with dissolve
    show rocky at left with dissolve
    "Time passes,{w=.3} as we all take a seat and talk idly about what we've done recently"
    n "Ha, {w=.3}the professor really just threw that assignment out of nowhere right?"
    r "Real smart of him considering half the class wasn't even done with last one yet..."
    p "Does he really have to give us another one?{w=.3} I felt the slides presentation was enough about this..."
    v "Meh, {w=.3}you guys are just coping with the fact I'm actually the smartest,{w=.3} prettiest, {w=.3}AND most talented of the class!{w=.3} I have NO problems with submitting any assignments or tests~"
    r "Gee I'm gonna have to deflate your head with a coffee straw just so it's able to get out the front door"
    v "Awwww don't be jealous I have perfect straight A's!"
    r "I have nothing to worry about considering the fact you're absent half the time and most likely gonna get dropped if you don't shape up"
    n "Hmmm it is sort of true though!{w=.3} You have to admit Vinnie is pretty smart with math!"
    p "\"Have to admit?\",{w=.3}as in, {w=.3}you didn't expect Vinnie to be this smart?"
    r "Hahaha! {w=.3}Serves you right if {i}Norman{/i} of all people thinks that less of you!"
    v "Norman! H{w=.3}-how could y{w=.3}-you... {w=.3}I THOUGHT WE WERE FRIENDS!!!"
    "Vinnie pretends to bawl and stuffs their face in their hands"
    n "Hey! {w=.3}I didn't say any of that!"
    show black with Dissolve(1.):
        alpha.6
    "These were the people I chose to spend my time with, {w=.3}truthfully,{w=.3} I didn't have anyone else in my life"
    "I don't have the best relationship with my family so I'd prefer staying away from them"
    "I've never spent this much time with anyone before,{w=.3} I was simply minding my business in class when Norman offered me to join him one day at the park"
    "He slowly introduced me to the rest of his circle, {w=.3}I'm very grateful to have people I can talk to and actually listen to me"
    "Rocky's dependable nature, {w=.3}always lending a hand when he can; {w=.3}Vinnie's good-nature and levity; {w=.3}They're always able to brighten a tough day"
    "And Norman, {w=.3}he's always there to cheer me on;{w=.3} I don't think he's ever rejected a chance to talk with me either so he must enjoy my presence as much as I enjoy his"
    "I suppose I never properly thanked him for this opportunity... {w=.3}I have to remember to do that soon..."
    hide black with dissolve
    hide rocky with dissolve
    hide norman with dissolve
    show vinnie at hop
    v "EARTH TO [pov!u] EARTH TO [pov!u], HEY SPACE CADET YA THERE!?!?" with hpunch
    p "Ah, {w=.3}I apologize I wasn't paying attention"
    play music "audio/sfx/crowd panic.ogg" fadein 1.0
    v "You see this shit?!?! {w=.3}There's people screaming like crazy!"
    v "I didn't know the pride parade was coming THIS early!"
    show rocky with dissolve
    r "Vin, {w=.3}shut up now isn't the time for your stupid jokes it's serious"
    show vinnie at sink
    "Rocky snaps back at Vinnie who slumps back in their chair with a sad face I've never seen on them before"
    hide vinnie with dissolve
    "I don't think Rocky has ever been this serious with Vinnie, {w=.3}sure he got mad,{w=.3} but he never actually meant it until now"
    "I shoot my head towards the window and see Rocky with Norman standing up glued to the window"
    show norman at right with dissolve
    n "I'm trying to see what they're running from but no luck..."
    r "They just keep pouring out!{w=.3} What could have caused this?"
    scene cafe window
    "I stand up and stare out the window"
    "There's hundreds of people packing the street, {w=.3}all running as fast as they can"
    "I see a mother holding a baby and her daughter huddling on top of a car, {w=.3}most likely to avoid being stampeded"
    "There's an older man who clearly lost his cane trying to get up but,{w=.3} keeps getting pushed back down to the ground by everyone else"
    play sound "audio/sfx/window smash.ogg"
    "There's some people taking advantage of the chaos and smashing open miscellaneous store windows to rob them"
    play sound "audio/sfx/car alarm.ogg"
    npc "Get the hell away from this is mine!"
    npc "Has anyone seen my husband?!?"
    npc "SAMANTHA WHERE ARE YOU!!!"
    npc "OH MY GOD THEY'RE COMING FOR US! RUN!!"
    "Amongst the ocean of deafening screams are various cries of anguish"
    show vinnie at left with dissolve
    v "This is almost too much to look at..."
    show vinnie at sink
    play sound "audio/sfx/ambulance.ogg"
    r "I'm heading out shop, {w=.3}I need to see what's up..."
    show norman at hop
    n "Wait!{w=.3} You can't! {w=.3}Look at how many people are out there!"
    n "You see a bunch of people running from something and choose to head straight into it?"
    r "Relax, {w=.3}I'm just gonna take a peek outside then quickly run back in"
    n "I-"
    show rocky at farright with move
    "Before Norman can say more Rocky rushes out"
    "I chose to go out with him"
    show norman at hop
    n "Are you serious?!?!"
    hide norman with dissolve
    hide vinnie with dissolve

    scene cafe outer
    play music "audio/music/mixkit-fright-night-871-Michael Ramir C.ogg"
    show rocky with dissolve
    r "Oh you decided to come with,{w=.3} here follow I just want a glance at the cause of this..."
    npc "GET AWAY FROM ME!!! {w=.3}GET AWAY!!!"
    p "Is someone being attacked?"
    r "Let's get a closer look he could be in trouble!"
    show rocky at farright with move
    scene black with fade
    scene cafe outer with dissolve
    show rocky at center with move
    "We go further up on ahead to the source of the noise, the crowd thinned out and is nowhere near as big as before"
    npc "HELP ME!!!{w=.3} PLEASE SOMEBODY HELP ME!!!"
    r "Over there!"
    "Our pace quickens until we come across a man attacking another man! He's pinned him to the ground and appears to be clawing at his neck!"
    show rocky at hop
    r "You goddamn freak get off him!"
    show rocky at hop
    "Rocky strikes the attacker at the back of the head who didn't appear to even notice..."
    "Rocky grapples the back of him,{w=.3} attempting to restrain his arms"
    play sound "audio/sfx/zombie talk.ogg"
    "The attacker finally notices Rocky and tries clawing at his face,{w=.3} he makes the most unpleasant noise I have ever heard from someone..."
    "I didn't even know anyone was capable of evoking such a groan,{w=.3} it's almost like he wasn't even alive..."
    r "What the hell are you?!?!"
    "The attacker is able to twist himself backwards and is facing Rocky directly when tussling with him"
    "He's trying to bite at Rocky's neck while his arms are restrained"
    s "Don't worry I got this!"
    "I run up ahead and punch him at back of the head"
    "Rocky throws him down to the ground and pins him face down with foot"
    "The attacker protests intensely, {w=.3}he's shifting around like a dead cockroach and is trying to get back up"
    play sound "audio/sfx/zombie moan.ogg"
    "There's that god awful noise again... {w=.3}I didn't even know anyone was capable of evoking anything like it"
    "Now that I'm closer I'm able to see just how disgusting looking he is..."
    "His fur is coming off with patches, {w=.3}his eyes are milky white, the odor is so pungent it stinks my eyes..."
    r "[pov!u]!{w=.3} Check out the guy he jumped to see if he's okay!"
    p "Got it!"
    "I walk up ahead to see that the victim is laying motionless on the floor..."
    "Blood pools beneath him as I see gashes across his throat"
    p "Are you okay?!?!"
    "I check the pulse on his neck to see if he's still with us"
    "There's nothing"
    r "Hey! {w=.3}[pov]!{w=.3} He alright!?!?"
    "I look back to see a panicked Rocky still pinning down the attacker"
    p "We need to call an ambulance his neck is-"
    play sound "audio/sfx/zombie attack.ogg"
    p "AHH NO! HE'S ON ME!"
    r "[pov!u]! I'll get to you!"
    "Rocky sprints towards me but his leg gets grabbed by the person he was restraining,{w=.3} he faceplants into the curb"
    r "JESUS! {w=.3}GET IT OFF!{w=.3} GET IT OFF!"
    play sound "audio/sfx/cock.ogg"
    pause 0.1
    queue sound "audio/sfx/shoot.ogg"
    "A shoot rings out as the person mounting Rocky drops dead"
    r "Wha-"
    play sound "audio/sfx/shoot.ogg"
    "A bullet flies past right by me into my attacker's head"
    "The blood explodes from his face onto mine as he drops dead on the street"
    p "Who?"
    show norman with dissolve
    n "I told you it wasn't safe out here..."
    r "Y{w=.3}-you...{w=.3} YOU JUST KILLED TWO PEOPLE!"
    "Norman points towards the chest of the person who attacked Rocky"
    n "No, {w=.3}look at this injury of this one...{w=.3} I only fired once so why does he already have another gun shot wound?"
    r "I- {w=.3}I-..."
    n "No one can survive a gun shot to the heart and live"
    n "C'mon we need to take cover, {w=.3}it isn't safe being exposed like this"
    show vinnie at left with dissolve
    v "Uh guys?"
    v "You really shouldn't have left us behind lik-{w=.3} HOLY FUCKING SHIT"
    show vinnie at hop
    v "OH MY GOD I'M GONNA BE SICK WHAT THE FUCK HAPPENED HERE?!?!"
    n "No time to explain we gotta get back!"
    "Norman ushers a silent Rocky and panicked Vinnie back to the cafe"
    scene cafe with dissolve
    pause 1.0
    show vinnie at right with dissolve
    show norman with dissolve
    show rocky at left with dissolve
    stop music fadeout 0.5
    play music "audio/sfx/EAS.ogg"
    tv "ALL CIVILIANS ARE TO TAKE COVER IN YOUR OWN HOMES, DO NOT EXIT UNDER ANY CIRCUMSTANCES, {w=.3}BARRICADE ANY OPENINGS AS MUCH AS POSSIBLE, {w=.3}AVOID THE INFECTED AT ALL COSTS"
    tv "A PANDEMIC HAS OCCURRED,{w=.3} ALL GOVERNMENTS ARE WORKING TOGETHER TO DISCOVER A REMEDY TO THE SITUATION"
    tv "FROM WHAT WE KNOW THE ABNORMAL PATHOGEN INFECTS IT'S VICTIMS MAKING THEM ACT HIGHLY AGGRESSIVE {w=.3}BE-{w=.3} O-"
    "The broadcast starts breaking up"
    r "C'mon work you stupid thing!"
    tv "{w=.3}-I---- {w=.3}A- {w=.3}P---- {w=.5}MAY GOD HAVE MERCY ON OUR SOULS-"
    stop music
    "The power goes out..."
    "We all sit in silence for a moment..."
    "Rocky and Norman already barricaded the windows with chairs and boxes from the backrooms"
    "We all traveled here by the underground train system so I doubt that's the safest option to go from here..."
    "Vinnie could try hotwiring one of the cars from outside but, what if we run into a huge horde of those things from outside? We'll be surrounded!"
    "We all decided to just wait it out in here... {w=.3}The broadcast advised us all to stay in place... {w=.3}Someone's bound to rescue us right?"
    "There isn't much else for us to do so why eve-"
    show norman with dissolve
    n "We're gonna make it through this"
    "...?"
    "Everyone perks up at Norman"
    n "We're gonna make it out of here alive I can assure you all"
    show rocky at right with dissolve
    r "What are you talking about?{w=.3} It's practically hell on earth right now!"
    r "We're stuck in here and god knows what our families are going through"
    "I could see Vinnie visibly flinch at that"
    r "It'll be a tragedy when they find as one of those things outside..."
    r "Or worse, {w=.3}they're already gone."
    r "There are people {i}eating{/i} one another and you think we have a chance at this?!"

    n "Stop that"
    n "I remember when I was practically broke and about to live on the streets when all of the sudden you offered me a place to live"
    n "Even though you could barely afford it and got kicked out soon after for having another tenant without letting the landlord know"
    n "You still chose to help me out afterwards even though I ruined your life"
    n "What chance did we have then?{w=.3} But you still took it to help me out..."
    r "Norman, {w=.3}you never ruined anything I already told yo-"
    n "I know,{w=.3} I never forgot"
    show vinnie at left with dissolve
    v "That's how you lost your home?{w=.3} I never knew that part..."
    v "I- {w=.3}I don't know...{w=.3} about this guys... {w=.3}what really CAN we do besides just getting ourselves k-{w=.3}killed..."
    n "Vinnie,{w=.3} listen, {w=.3}you're the smartest person I know so with your brains we're bound to come across a way to escape!"
    n "As long as we all got each other and stay careful it can't go wrong!"
    v "..!"
    p "What are you getting at?"
    n "I'm saying that my friends are amazing people that don't deserve to be trapped like this"
    n "Stuck in here,{w=.3} twiddling our thumbs hoping for the best"
    n "We can call for help and reach a safe-zone somewhere!"
    n "Think about it! {w=.3}The government is bound to have set up some contained perimeter; all we have to do is come in contact with them and let them know there are survivors here!"
    p "Weren't you the one who said it was best to take cover?"
    n "I know what I said...{w=.3} but look outside... {w=.3}if they find us we'll be completely trapped in here and... {w=.3}they'll eventually starve us out"
    v "Yeah I don't think we could survive off frappes and cake pops forever..."
    menu:
        
        "I can't just stay silent,{w=.3} I need to let Norman know where I stand"

        "We can do this guys!":
            $ renpy.notify("You feel a weight off your chest lighten...")
            n "Really?! {w=.3}I knew I could count on you [pov]!"
            r "[pov]..."
            v "[pov]!"
            p "Think about it! This building is huge there are definitely more survivors out there!{w=.3} The bigger the group the stronger we are!"
            n "[pov] is so right! {w=.3}I already have a plan!"
            pass 
                

        "It's hopeless,{w=.3} might as well just wait for help":
            $ insanity_level += 1
            $ renpy.notify("You feel your stomach sink when the realization sets in...")
            n "[pov]..."
            r "I agree with [pov]... {w=.3}what's the point in trying? {w=.3}We'll just be getting ourselves killed"
            r "I have firsthand experience with how strong those things are,{w=.3} It's a death sentence to even try..."
            v "Yeah... {w=.3}I want to get out here as much as the next guy but it is pretty dangerous..."
            n "...I know it's scary guys, {w=.3}but we could do it I already have a plan..."
            pass

    n "We're already in a pretty big building right? That means it's an easy to find land marker for any nearby helicopters to land on!"
    n "Skyscrapers like this usually have their own antennae on top! Which means there has to be a way for us to reset it and contact someone!"
    v "I'm pretty sure the people that work here are trying to already do that...{w=.3}I mean, what are civilians meant to even do?"
    n "Well,{w=.3} Rocky technically works here as coffee employee so he could use his keycard to get us upstairs!"
    r "..."
    r "They actually gave me schematics to this place for the safety plan if anything goes wrong..."
    hide rocky at right with dissolve
    "Rocky goes to the backroom and retrieves a hefty binder"
    show rocky at right with dissolve
    r "Here it is..."
    n "Yeah this is a great start!"
    "We all gather around the schematics"
    v "Hey look here, it says there's a mechanical room on the 10th floor..."
    v "If the power is off and the people here are having trouble activating it...{w=.3} we could do it ourselves from there..."
    if insanity_level >= 0:
        p "Also, I doubt the zombies would have made it that far up,{w=.3} I mean it's a pretty closed off building how far could the plague have spread?"
    elif:
        pass
    n "You guys!{w=.3} This is perfect!{w=.3} C'mon Rocky what do you say?"
    r "..."
    r "I say it's worth a shot..."
    r "I guess I would just go crazy in here if I didn't even TRY escaping"
    n "That's the spirit!"
    "Norman motions for a group hug"
    if insanity_level >= 0:
        "Vinnie and Rocky gingerly step forwards before rushing in to hug Norman back"
        "They all exchange gentle smiles at one another"
    elif:
        p "Who can turn down a hug from NORMAN of all people!"
        "We all rush forwards to give Norman a hug!"
        "Rocky pretty much just lifted Norman and I off the ground from how strong he is...{w=.3} guess he really needed that hug...{w=.3}... I did too..."
        p "I feel invincible already!"
        v "The power of friendship guides me!"
        r "I'll kill you all if any of you die on me...{w=.3} also Vinnie were you caressing my hair?"
        v "Wait, {w=.3}I did that because I thought you were the one poking my stomach!"
        p "Sorry, {w=.3}that was my horn..."
        n "Hahahaha!"
    n "We can do it guys!"

    if insanity_level >= 0:
        all "YEAH!!!"
    elif:
        allnosage "Yeah!"

    pause 0.5
    v "Ok,{w=.3} so I didn't want to say anything earlier because I was honestly afraid to...{w=.3} but...{w=.3} do you always carry a loaded ducking handgun on you at all times???"

    n "I have a license for it and it is fully within my legal boundaries to wield it for self defense,{w=.3} never know when trouble is afoot!"

    n "Why do you think I always go with you on your late-night romps in the alleyways? "

    v "...{w=.3}I am both flattered and seduced that you would be willing to put a bullet in someone's in skull for me..."

    v "...{w=.3}But seriously do you carry that during class and stuff?"

    n "Let's just say it's not within OTHER people's legal boundaries...."

    "..."
    "Norman is not one to be trifled with..."
    r "Well you saved our asses earlier,{w=.3} thanks....{w=.3} you're clearly capable enough with it"
    p "Yeah! Thank you Norman!"
    v "No!{w=.3} The bullet shots were actually me throwing my knife straight into that zombie's head!"
    v "If I recall correctly...{w=.3} Norman was throwing up the whole time while I valiantly saved you both!"
    r "Shut up Vinnie."
    "Rocky blurts out as we make our way to the staircase"


