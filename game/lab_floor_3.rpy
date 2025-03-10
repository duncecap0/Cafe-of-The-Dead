


#EVENTS

default zombie_large_attack = True

#ITEMS

default keycard = False
default pills = False

#PIECE PUZZLE

default puzzle_piece_b_collect = False
default puzzle_piece_a_collect = False

default piece_puzzle_b = False
default piece_puzzle_a = False




label lab_floor_3:
    scene black with dissolve
    stop sound
    stop music
    pause 1.0
    scene elevator with dissolve
    #HAVE DIALOGUE BRANCH WITH SURVIVORS
    $ current_room = "lab_start" # this initializes the point'n'click segment to display the correct set of buttons.
    scene lab main room with dissolve
    "Well here we are in the lab"
    jump pnc_loop



##LAB ROOMS
## YES THERE ARE A LOT ;(

##LAB DOWNSTAIRS HUB
label lab_start:
    scene lab main room with dissolve
    $ current_room = "lab_start" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS CENTER BOTTOM ROOM

label lab_puzzle_b_room:
    scene lab main room with dissolve
    $ current_room = "lab_puzzle_b_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS LEFT ROOMs

label lab_radio:
    scene lab radio with dissolve
    $ current_room = "lab_radio" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

## LAB DOWNSTAIRS RIGHT ROOMS
label lab_test_room:
    scene lab test with dissolve
    $ current_room = "lab_test_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_downstairs_hall:
    scene lab hall with dissolve
    $ current_room = "lab_downstairs_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_puzzle_piece_a_collect_room:
    scene lab storage with dissolve
    $ current_room = "lab_puzzle_piece_a_collect_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

#UPSTAIRS !!!!!!!

label lab_upstairs:
    scene lab upstairs main room with dissolve
    $ current_room = "lab_upstairs" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#UPSTAIRS LEFT ROOMS !!!!!!!

label lab_upstairs_left_hall:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_left_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


label lab_puzzle_a_room:
    scene lab puzzle with dissolve
    $ current_room = "lab_puzzle_a_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_puzzle_piece_b_collect_room:
    scene lab storage with dissolve
    $ current_room = "lab_puzzle_piece_b_collect_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#UPSTAIRS RIGHT ROOMS DONT CONFUSE FOR RIGHT-MOST ROOMS !!!!!!!
##### RIGHT !!!!!!!!!!!!!!!!

label lab_upstairs_right_hall:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_right_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_desk:
    scene lab desk with dissolve
    $ current_room = "lab_desk" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_upstairs_test_room:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_test_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop



#UPSTAIRS RIGHT-MOST ROOMS DONT CONFUSE FOR RIGHT ROOMS !!!!!!!
##### RIGHT-MOST !!!!!!!!!!!!!!!!

label lab_upstairs_rightmost_hall:
    scene lab hall with dissolve
    $ current_room = "lab_upstairs_rightmost_hall" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_keycard_room:
    scene lab keycard room with dissolve
    $ current_room = "lab_keycard_room" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_tanks:
    scene lab tanks with dissolve
    $ current_room = "lab_tanks" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label lab_boss_room:
    scene lab tanks with dissolve
    $ current_room = "lab_tanks" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop


#LAB POINT AND CLICK LABELS

label dead_soldiers:
    "That's a lot of dead people in body armour... this has to be who the employees were referring to, they don't seem very threatening right now"
    jump pnc_loop

label radio:
    
    "Most other telecommunications in this room seem to be malfunctioning... the radios being no exception..."

    if save_tara_1 and save_tara_2:
        "Until an ear-splitting static voice fills the empty dullness of the room"
        w "Hello?"
        "I rush over to pick up the radio"
        p "[w_name]? You're ok?"
    jump pnc_loop

label bullets:
    "Looks like two bullets are on the floor..."
    if norman_has_gun:
        $ ammo += 2
        "Norman stuffs them into his pocket"
    else:
        $ ammo += 2
        "I stuff them into my hoodie"
    jump pnc_loop    
#PENIS
label puzzle_piece_a_collect:
    $ puzzle_piece_a_collect == True
    "I collect puzzle piece A"
    jump pnc_loop

label pills:
    "There's some pill capsules on the floor"
    if vinnie_dead == False:
        v "Those look like painkillers, you can tell from the coloring and shape"
        menu pill_choose:
            "Who should I heal?"

            "Me":
                $ sage_health +=1
                $ pills == True

            "Norman":
                if sage_health <= 4:
                    n "Awww thank you [pov]!!! But, I think you should take them... you don't look so good..."
                else:
                    $ norman_health +=1
                    $ pills == True
                    n "Thanks [pov]! I feel better already!"

            "Vinnie":
                $ vinnie_health +=1
                $ pills == True
                v "Wow, I am just a PERUSER today!!!"

            "Rocky":
                $ pills == True
                $ rocky_health +=1
                r "I've never been more thankful for random floor pills before in my life..."
    
    else:
        menu pill_risk:
            "Should I risk using them? It may be useful..."
            
            "Me":
                $ sage_health +=1
                $ pills == True

            "Norman":
                if norman_affection >= 0:
                    $ norman_health +=1
                    $ pills == True
                    n "I trust you with my life[pov]! I'm sure it'll be fine!"
                    jump pnc_loop    
                else:
                    n "Don't take this the wrong way [pov]... but I don't trust it..."
                    jump pill_risk

            "Vinnie":
                if insanity >= 0:
                    $ vinnie_health +=1
                    $ pills == True
                    v "No"
                    v "I'm not just gonna be eating random shit off the floor, I worked too hard to get back in to that again..."
                    jump pill_risk
                else:
                    v "..."
                    v "Ok, I'll trust you..."
                    jump pnc_loop

            "Rocky":
                $ rocky_health +=1
                $ pills == True

                r "I'm a big guy, so if it IS something bad it won't hit too hard... right?"
            
    jump pnc_loop    

label keycard_slider:
    if keycard == False:
        "This needs some type of identification key to get through..."
    else:
        play sound "audio/sfx/correct beep.ogg"
        "I slide the keycard through and loud beep confirms it!"
    jump pnc_loop   

label plague_note:
    $ puzzle_piece_a == True
    "I collect puzzle piece A"
    jump pnc_loop

label zombies_large_attack:
    if zombie_large_attack:
        show screen kill_zombie
        "They dropped some ammo"
        $ ammo +=3
        $ zombie_large_attack == False
    else:
        "Nothing else here"
    jump pnc_loop

label keycard:
    $ keycard == True
    "I look around the drawers and find an employee keycard!"
    jump pnc_loop

label bullet:
    "Looks like a single bullet...."
    if norman_has_gun:
        $ ammo += 1
        "Norman put it into the gun"
    else:
        $ ammo += 1
        "I put it in the gun"
    jump pnc_loop

label puzzle_piece_b_collect:
    $ puzzle_piece_b_collect == True
    "I collect puzzle piece B"
    jump pnc_loop

label locked_master_door:
    if piece_puzzle_a and piece_puzzle_b:
        "I enter through the door"
        jump boss_battle
    else:
        "This door won't open unless we activate something around here..."
    jump pnc_loop


label piece_puzzle_a:
    if puzzle_piece_a_collect:
        $ piece_puzzle_a == True
        "I solve it"
    else:
        "This needs it's respective piece to open..."
    jump pnc_loop

label piece_puzzle_b:
    if puzzle_piece_b_collect == True:
        $ piece_puzzle_b == True
        "I solve it"
    else:
        "This needs it's respective piece to open..."
    jump pnc_loop




##LAB BOSS BATTLE ENDING
label boss_battle:
    p "fuck you"
    s "ow"
    "He dies"
#jump rooftop:

return



