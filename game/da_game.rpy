default rocky_dead = False
default viv_dead = False
default norman_dead = False
default health = 100

label cafeintro:
    $ pov="Sage"
    $ renpy.notify("Remember to save often...")
    $ health += 5

    play music "audio/music/mixkit-positive-energy-973- Michael Ramir C.ogg" fadein 1
    scene cafe outer with dissolve
    "Today is the first day of October, college was finally almost over for my new group of friends and I so It was as good as any other time to wind back and enjoy ourselves"
    "We decided after class we should visit our friend at his new job as a barista"
    show vinnie with dissolve
    v "HEY! GUYS OVER HERE!!! HAHA!!"
    show vinnie at hop
    v "HURRY UP!!! I {i}NEED{/i} TO SEE ROCKY IN HIS NEW STUPID LITTLE APRON HAHAHAHAHA!!!"
    "This was Vinnie, my gender diverse Oppussum friend, being their boisterous self per usual"
    "They were the one who really pushed for us to visit Rocky after class, Vinnie was always the one who initiated the group hangouts"
    hide vinnie with dissolve
    show norman with dissolve
    n "OK OK RELAX WE'RE ALMOST THERE!"
    n "You're really excited for this aren't you?"
    "Here's Norman, my compassionate Golden Retriever buddy, as caring as ever trying to humor Vinnie"
    "They were seen as the \"mom\" friend in the group, always responsible with keeping us from killing ourselves with our antics {w=.5}{i}well mainly just Vinnie to be honest...{/i}"
    hide norman with dissolve
    pause 0.5
    scene cafe with dissolve
    play sound "audio/sfx/chime.ogg"
    r "Hello and welcome! What can I get you toda-"
    show rocky with dissolve
    r "Oh{w=.3}{i} oh no{w=.5} please god no...{/i}"
    show rocky at left with move 
    show vinnie with dissolve
    show vinnie at rattle
    v "HAHAHAHAHAHAHAHAHAHAHA!!!! STOP!!!! STOP IT!!!! I- I CAN'T BELIEVE IT!!!" 
    show vinnie at rattle
    v "HAHAHAHAHAHAHA"
    "We move past Vinnie who is currently laughing up a storm while leaning on a table for stability"
    show vinnie at hop
    hide vinnie with dissolve
    show norman with dissolve
    show norman at hop
    n "Hey Rocky nice to see you at your new post! Where's your co-workers?"
    r "She got a call from a family member, something about a medical emergency..."
    n "Woah that sounds really serious are they gonna be okay?"
    r "Honestly, {w=.3}I'm not sure she sounded real rattled when she heard the news, must've been real serious"
    "Rocky was the eldest of the group, a jaded Maned Wolf, he always seemed so grumpy with his place in life no matter where he was"
    "I'm relatively new to friend group yet I still know the others more than Rocky since he often misses our hangouts"
    "I recall Norman mentioning how Rocky doesn't have a place to call home so he bounces job to job to make ends meet"
    n "Well, we could cheer her up next time we visit you at work! We're gonna be regular customers so she's bound to get to us know eventually right?"
    r "Ugh,{w=.3} speaking of... You guys aren't gonna make this weird or anything? Remember I have to keep this job so don't scre-"
    hide norman with dissolve
    show vinnie with dissolve
    v "Oh! We're definently making things weird!"
    v "Hello sir!{size=*0.5} write this down because it's gonna be a long one{/size} I would like to order:"
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
        "Huh? Shouldn't you be sleeping?"

    elif pov == "Bradley":
        "Huh? Shouldn't you be sleeping?"

    elif pov == "B0red Bradley":
        "Huh? Shouldn't you be sleeping?"

    elif pov == "Bored Bradley":
        "Huh? Shouldn't you be sleeping?"

    elif pov == "Dunce Cap":
        "What the hell kind of name is that? GET A JOB BOZO! FATHERLESS BEHAVIOR!"

    elif pov == "dunce cap":
        "What the hell kind of name is that? GET A JOB BOZO! FATHERLESS BEHAVIOR!"

    elif pov == "Chris":
        "Shouldn't you be pushing boulders or something?"

    elif pov == "Leon":
        "*gasp* Where's baby eagle??? also your hair's really nice"

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
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"

    elif pov == "Mother":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Mommy":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Dad":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Daddy":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Father":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Papa":
        show vinnie at right with dissolve
        v "HAHAHAHA OK DADDY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    elif pov == "Mama":
        show vinnie at right with dissolve
        v "HAHAHAHA OK MOMMY HAHAHAHAHA"
        v "GOOD ONE! I SHOULD HAVE THOUGHT OF THAT!"
        hide vinnie with dissolve

    else:

        pass

    r "Okay [pov], what would you like?"

    hide rocky with dissolve
    pause 0.5
    scene black with dissolve
    scene cafe with dissolve
    show vinnie at right with dissolve
    show norman with dissolve
    show rocky at left with dissolve
    "Time passes, as we all take a seat and talk idly about what we've done recently"
    n "Ha, the professor really just threw that assignment out of nowhere right?"
    r "Real smart of him considering half the class wasn't even done with last one yet..."
    v "Meh, you guys are just coping with the fact I'm actually the smartest, prettiest, AND most talented of the class! I have NO problems with submitting any assignments or tests~"
    p "It's true though, Vinnie is pretrty"




    

label death_screen:
    play sound "audio/sfx/stinger.ogg"
    play music "audio/music/mixkit-feedback-dreams-588- Eugenio Mininni.ogg"
    scene black with pixellate
    show text "{size=+90}{b}{color=#f00}YOU HAVE PERISHED{/color}{/b}{/size}"

    call screen death_nav

return

    

    
