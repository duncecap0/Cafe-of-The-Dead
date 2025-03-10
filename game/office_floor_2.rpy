
#variables
default morphine = False
default closet_broken = False
default medkit = False

#password
define password = "password"
define password_input = ""

#REMEMBER TO ADD TARA TO EPILOGUE ENDING
default save_tara_1 = False
default save_tara_2 = False


label office_floor_2:

    scene black with dissolve
    stop sound
    stop music
    pause 1.0
    scene elevator with dissolve
    "We all sit in silence for a good while, just trying to take it all in..."
    "Norman already pressed the button for us to go into the office space, we think survivors are in there..."
    ##NORMAN GETS DEPRESSED DIALOGUE TREE
    if rocky_dead == True or vinnie_dead == True:
        "The elevator's music is playing as if it were mocking our losses..."
    if vinnie_body_carried == True:
        "Rocky has Vinnie's lifeless body's head resting on his lap, eyes closed as if they were sleeping; Rocky seemed to be lost in them..."
        "Rocky hasn't spoken a word since it happened, the rest of us are too afraid to speak until-"
        n "..."
    if insanity_level <= 1:
        if norman_affection >= 1:
            n "We've gotten pretty far now haven't we?"
            if rocky_dead == True or vinnie_dead == True:
                n "I know we've had some losses on the way... things won't be the same without them..."
                if rocky_dead == True:
                    n "Rocky's protectiveness, bravery, and caring nature... always making sure everyone was happy even if it hurt him... he was my first best friend you know... I still can't grasp he's..."
                if vinnie_dead == True:
                    n "Vinnie's charm, love, and acceptance.... always trying to get people to not wallow in misery for too long... they wanted this friend group to exist more than anything...."
                n "Ah! Look at me getting emotional... we have work to do no? Haha..."
                menu:
                        "I'm sorry for your losses":
                            $ norman_affection +=1
                            n "...!"
                            n "They're your losses to you know... just because you're the newest member doesn't mean that your worth less... especially to me..."
                            p "They're your friends, our friends, how can you not be sad? It's ok to let it out Norman... to feel pain is to be alive..."
                            n "..."
                            if vinnie_dead == False and rocky_dead == True:
                                v "I miss him too Norman... I don't think I'll ever be able to live like how he wanted me to, but if you having nothing to lose you have nothing to gain? Remember his words you told me?"
                            if rocky_dead == False and vinnie_dead == True:
                                r "I miss them too Norman... I'll never be able to laugh like how they made me, but if you having nothing to lose you have nothing to gain!"
                            if vinnie_body_carried == True:
                                "Rocky set Vinnie's body down with their arms folded over their chests as he said this"
                            if rocky_dead == False or vinnie_dead == False:
                                n "Guys... I... I c-can't..."
                                "Norman begins sobbing uncontrollably before leaping into our arms... we all hug until we hear sniffling die down... I don't even know if it's from Norman or not..."
                            else:
                                n "[pov]... I... I c-an't..."
                                "Norman begins sobbing uncontrollably before leaping into my arms... we hug until I hear the sniffling die down..."
                            "I don't want to let go..."
                            pause 0.5
                            n "Thank you... I needed that..."
                            "A minute passes before everyone goes back to their respective part of the elevator, until Norman sidles up next to me again"

                        "Don't get sappy.":
                            $ norman_affection -=2
                            $ insanity_level +=1
                            n "{w=.3}...Oh... I suppose you're... right..."
                            "Norman looks as if I had just slapped him, not my fault someone isn't focusing on the fact we could die at any minute..."
                            jump office_floor_2_survivor_banter
            else:
                n "We haven't had any losses yet! Go team us!"

            n "[pov]... I'm so proud of you... you're like a natural born leader...."
            n "That's one of the things I've always admired about you... so dead-set on their beliefs and willing to speak out! You may seem quiet to the naked eye but that's because people don't look hard enough!"
            n "You're able to speak louder than a million people with just a single sentence. You can accomplish what people only dream of doing; that's not an easy skill, I can assure you that..."

            menu:
                "Thanks":
                    n "No Problem [pov]!"
                    jump office_floor_2_survivor_banter

                "I admire you too Norman":
                    if vinnie_dead == False:
                        n "[pov]...? D-don't say stuff like that out loud! Vinnie would NEVER let me hear the end of it.."
                    else:
                        n "[pov]...? D-don't say stuff like that out loud! What if someone hears that?"
                    p "It's true though, strength and responsibility like Rocky, smarts and charm as Vinnie... and you say I'm the skillful one but I could only dream of being like you"
                    "Norman has been staring down at the ground the whole time, I think I see his cheeks blush red..."
                    n "[pov]... thank you... truly..."
                    p "Don't mention it, I'll never forget it."
                    if vinnie_dead == False:
                        "I'm pretty sure I caught Vinnie sneaking peeks at us; I don't care, let them watch..."
                    if rocky_dead == False and vinnie_body_carried == False:
                        "Rocky has been staring at his watch for far too long to be unsuspecting; as if he were trying to give us room, good."
                    jump office_floor_2_survivor_banter

label office_floor_2_survivor_banter:

    if rocky_has_gun == True:

        if vinnie_body_carried == True:
            r "Your gun..."
        else:
            r "Here! Take your gun back Norman!"

    if vinnie_has_gun:
            v "TAKE THIS GUN AWAY FROM ME PLEASE NORM-NORM!!! I'm not a good shot at all..."

    if sage_has_gun:
            p "Also, I believe this gun belongs to you?"

    if insanity_level <=1:
        n "Hmm how about you keep it from now on [pov]! You proved yourself capable today!"
        p "You sure? I'm not a marksman or have the training that you do..."
        n "Says the one that doesn't panic at a moment's notice! Haha! Just take it you goof!"
        $ sage_has_gun == True
    else:
        n "Thanks! Good thing I never leave home without it!"
        $ norman_has_gun == True

    if rocky_dead == False and vinnie_dead == False:
        r "That battle was intense! Glad we made it through alright!"
        v "Yeah that was ass up in shit's creek! Thanks to [pov]'s star spangling advice we got out there"
        r "Don't forget it was {i}my{/i} battle expertise that saved you all..."
        v "CALM YOU'RE DOUBLE D TIG OL BITTIES WOMAN! I'm not trying to accuse anyone of anything just saying that {i}I{/i} think some people pulled their weight more than others..."
        r "...That's exactly what a fucking accusation is you dumb slut..."
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
            p "Hey Vinnie? It's gonna be ok bud... I didn't know you guys for too long but I can tell Rocky loved you... remember that we're here for you if you need anything got that?"
            v "..."
            v "...Thank you...[pov]... he was like family to me... I..."
            v "..."
            v "You and Norman are my family as well. Got it?"
            if norman_affection >=0:
                p "...Norman especially is like a-"
            p "...I'm so grat-"
    if rocky_dead == False and vinnie_dead == True:
        "I hear Rocky muttering something under his breath... I think it's some type of religious prayer?"
        if vinnie_body_carried == True:
            "He's now standing with Vinnie's body in his arms, bridal position"
        if insanity_level == 0:
            "I reach out to touch Rocky's back who says nothing in response"
            p "Hey Rocky? It's gonna be ok big guy... I didn't know you guys for too long but I can tell Vinnie loved you... remember that we're here for you if you need anything got that?"
            r "..."
            r "...Thank you...[pov]... they were like family to me... maybe even a...."
            r "God, I wonder what mom and pa are up to right now... hope their safe..."
            r "..."
            r "You and Norman are my family too? Got it?"
            if norman_affection >=0:
                p "...Norman especially is like a-"
            p "...I'm so grat-"
    if insanity_level >=1:
        "..."
        "..."
        "The air feels like it's flexing as awkward silence fills the room"
        "I couldn't help but notice Norman staring intensely at my back when he thinks I'm looking away, what's he so wary of? He's treating me as if I were one of the monsters..."
        "..."
    "The elevator comes to a screeching stop as the doors slide open"

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


label office_window:
    scene city view with dissolve
    "The city is destroyed, buildings on fire and hordes of zombies roam, I don't even see any civilians walking around anymore..."
    jump pnc_loop

label toilets:
    "What did I expect to get out of a toilet?"
    if vinnie_dead == False:
        v "Office workers usually do drug deals in here, hang on let me check behind one..."
        $ renpy.notify("Morphine was added to inventory!")
        menu:
            "Who should we use it on?"

            "Me":
                $ sage_health +=2
            "Norman" if norman_dead == False:
                $ norman_health +=2
                n "Never done drugs before..."
            "Rocky" if rocky_dead == False:
                $ rocky_health +=2
                r "Reminds me of when I broke my back at the warehouse..."

            "Vinnie" if vinnie_dead == False:
                $ vinnie_health +=2
                v "I hope I don't get addicted to these things again...."
            
            "Save it for Injured Woman" if closet_broken == True: 
                $ morphine == True
            
    jump pnc_loop

label projector:
    "The projector plays a broken reel of an \"immortality\" project..."
    jump pnc_loop

label injured_woman_closet:
    scene office window with dissolve
    $ w_name = "Injured Woman"

    w "..."
    "A bloody woman lies on the floor, she's breathing very slowly and won't respond back"
    "We're gonna need some medical supplies for this..."
    if morphine == True or medkit == True:
        menu try_save_woman:

            "Give Medkit":
                $ save_tara_1 = True
                w "...rearrange... words... days.. of week..."
                "She's a little better, but not fully healed... she won't last long without further treatment, I wonder if there's anything else to give her?"
                jump try_save_woman

            "Give Morphine":
                $ save_tara_2 = True
                w "You... must go to... higher floor... only way out..."
                "She's a little better, but not fully healed... she won't last long without further treatment, I wonder if there's anything else to give her?"
                jump try_save_woman

            "Leave":
                jump pnc_loop
    elif save_tara_1 and save_tara_2 == True:
        w "T-thank you.. I won't forget this..."
        $ w_name = "Tara"
        "My name is Tara"
        "She reveals lore #remember to add this dunce cap...."
        w "... don't let the word die out..."
    else:
        "We have none..."
    
    jump pnc_loop

label medkit:
        "I find a medkit in one of the top cabinets"
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
            
            "Save it for Injured Woman" if closet_broken == True: 
                $ medkit == True
        
        jump pnc_loop

label blocked_closet:
    "This room is boarded up too well to enter"
    if crowbar_collected == True:
        $ closet_broken == True
        "I use the crowbar to break down the boards"
        jump injured_woman_closet
    elif crowbar_collected == True and rocky_dead == False:
        $ closet_broken == True
        "Fortunately, Rocky uses the crowbar to break down the boards"
        jump injured_woman_closet
    elif vinnies_knife == True and vinnie_dead == False:
        $ closet_broken == True
        "Fortunately, Vinnie uses their knife to slowly wear away the boards over time"
        jump injured_woman_closet
    else:
        pass
    jump pnc_loop

label word_puzzle:
    scene computer with dissolve
    $ renpy.notify("Use the keyboard to type the password...")
    "We need to solve this word puzzle to be able to access the higher floors"
    #TO DO FIX
    jump get_password
return

label worker_diary:
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Halogen.ttf}I want to quit but can't because I'm under contract to work until next month... I hope I can go home soon.{/font}"
    centered "{font=Halogen.ttf}I don't even know what we're working on anymore, before they said It was for medical research but, now it seems like something for extending lifespans...{/font}"
    centered "{font=Halogen.ttf}The sick people being brought from the hospitals never come out of the higher floors...{/font}"
    centered "{font=Halogen.ttf}I'm gonna blow the lid off this place and see what's going on up there, I programmed an exploit to open up those doors. You have to rearrange the words. I'm gonna see what's up there no matter what.{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"
    jump pnc_loop

label worker_memo:
    play sound "audio/sfx/page turn.ogg"
    show black with Dissolve(1.):
            alpha.6
    centered "{font=Halogen.ttf}Remember guys! Boss said security is gonna be tighter these days so the higher floors will now be restricted to those with authorization{/font}"
    hide black with dissolve
    play sound "audio/sfx/page turn.ogg"
    jump pnc_loop

label office_corpses:
    scene office window with dissolve
    "Various corpses are strewn about, some seem to have been eaten while a few are shredded with bullet holes. I don't understand how they were able to die if they had access to machine guns..."
    "... Where even are the people with machine guns if they're not dead in here?"
    jump pnc_loop


label office_floor_ending:
    s "...Stop what you're doing."
    "The speakers make my eardrums ring, I see "
    "An explosion happens what do I do?"
    
    menu:
        "Protect":
            "PROTECT"
            jump lab_floor_3

#INPUT PASSWORD SHENANIGANS

label get_password:
    $ password_input = renpy.input("What's the password?", length = 8)

    if password_input == password:
        jump correct_password
    else:
        jump wrong_password
    return

label correct_password:
    play sound "audio/sfx/correct beep.ogg"
    "That was it!"
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