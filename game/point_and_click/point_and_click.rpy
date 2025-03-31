########## DEVIL SPIδεR'S POINT'n'CLICK PLUGIN ##########
# This plugin implements a modular point'n'click feature to make gameplay more interactive
# Currently supported features:
#   - Conditional interaction - make interactions available only when a certain condition is met
#   - Perspective switching - make segments take place in multiple rooms or angles
#   - Multiple ways to start or end one point'n'click segment - it's all a matter of jumping in and out of the segment

## Parameters ##
# There are numerous occasions where I list out a format for parameters. If the argument is in quotation marks in the format (like "this")
# the argument should also be in quotation marks

## Images ##
# There should an arbitrary amount of image pairs in game/point_and_click/image:
# the pair should consist of images in the filename format of X_idle.png and X_hover.png, where X is a word or a phrase
# this will be needed later in the plugin.

# This is the code that renders the point'n'click elements to the player

# To see steps necessary outside the PnC segments that initialize them, see the demo game's script.rpy file
# If you don't have the demo script, the rundown is that you have to set the current_room variable correctly and start the segment like this:
#   $ current_room = "example" # this value can be changed
#   jump pnc_loop

init -3:
    default current_room = None # This variable controls what list to get buttons from
    default pnc_flags = {} # This variable controls various creator-defined flags that control the state of a given point'n'click segment

screen pnc_screen(room="left"):

    style_prefix "pnc"

    for i in eval(f"{room}_buttons"):
        if (i[3] is None) or (eval(i[3])):
            imagebutton auto "point_and_click/image/" + str(i[0]) + "_%s.png" pos i[1] action Return(i[2])

style pnc_image_button:
    anchor (0.5, 0.5)

define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause


# This label handles showing the screen to the player.
label pnc_loop:
    $ quick_menu = False
    window hide diss
    call screen pnc_screen(current_room)
    window show diss
    $ quick_menu = True
    jump expression _return


### INTERACTION LISTS ###
# The plugin supports creation of an unlimited amount of so-called interaction lists, which are Python lists of tuples of a given format:
# (("image_name"),(x_coordinate, y_coordinate),"label_name", condition),
# - image_name represents a string that will determine the button's appearance. To demonstrate with an example, if this parameter was "dog",
# then the plug-in expects dog_idle.png and dog_hover.png to exist in game/point_and_click/image.
# - x_coordinate and y_coordinate correspond to the position of the button in the screen, relative to the button's center.
# - label_name represents the label that triggers when that button is pressed.
# - conditions corresponds to either:
# -- a string containing Python expression that determines the button's visibility - it shows when the condition is True
# -- the None value - making the button visible at all times
# The lists should end in _buttons

########## OG STUFF
define left_buttons = [
    (("look"),(530, 430),"left_frame", None),
    (("look"),(1140, 550),"left_door", None),
    (("move"),(1140, 650),"escape", "pnc_flags.get('door_unlocked') == True"), # Condition. The way it's written ensures that the game doesn't throw an error if the "door_unlocked" key isn't in the dictionary
    (("move"),(1720, 540),"to_right", None),
]

define right_buttons = [
    (("look"),(1390, 430), "right_frame", None),
    (("move"),(200, 540), "to_left", None),
]

#MECHANICAL FLOOR BUTTONS
define mech_floor_main_room_1_buttons = [
    (("look"),(330, 130),"mech_crowbar", "crowbar_collected == False"), 
    (("look"),(500, 420), "hvac", "examined_HVAC_machine == False"),
    (("look"),(865, 480),"mech_ladder", "crowbar_collected == False"), # Condition. The way it's written ensures that the game doesn't throw an error if the "door_unlocked" key isn't in the dictionary
    (("move"),(1030, 530),"mech_floor_main_room_2", None),
    (("move"),(130, 530),"mech_floor_main_room_2", None),
    (("move"),(1200, 450), "mech_hallway", None),
]

define mech_floor_main_room_2_buttons = [
    (("look"),(500, 600), "mech_corpse", "worker_journal_3_collect == False"),
    (("look"),(70, 390), "mech_electric_door", None),
    (("look"),(1170, 390),"mech_elevator", None),
    (("move"),(150, 600),"mech_vent", "pnc_flags.get('vent_unlocked') == True"), # Condition. The way it's written ensures that the game doesn't throw an error if the "door_unlocked" key isn't in the dictionary
    (("move"),(650, 700),"mech_floor_main_room_1", None),

]

define mech_hallway_buttons= [
    (("look"),(720, 400), "mech_desk", "worker_journal_1_collect == False"),
    (("move"),(640, 700),"mech_floor_main_room_1", None), #this will return you the hallway loop
    (("move"),(270, 400),"mech_hallway_left", None),
    (("move"),(1020, 400),"mech_hallway_right", None),
]

define mech_hallway_left_buttons= [
    (("look"),(330, 430), "mech_left_hall_jacket", "worker_key_collect == False"),
    (("move"),(650, 700),"mech_hallway", None), #this will return you the hallway loop
]

define mech_hallway_right_buttons= [
    (("look"),(400, 580),"mech_right_hall_bed", "worker_journal_2_collect == False"),
    (("move"),(650, 700),"mech_hallway", None), #this will return you the hallway loop
]



###OFFICE FLOOR BUTTONS
define office_start_buttons = [
    (("look"),(650, 370), "office_window", "examined_window == False"),
    (("look"),(550, 600), "office_corpse", None),

    (("move"),(1140, 430),"office_desks", None),
    (("move"),(60, 430),"office_hall", None), 
]

define office_hall_buttons = [
    (("look"),(650, 400),"secret_elevator", None),

    (("move"),(1030, 430),"office_restroom", None),

    (("move"),(290, 430),"blocked_closet", None),
    #(("move"),(290, 430),"office_closet", None),
    
    (("move"),(650, 700),"office_start", None), 
]

define office_restroom_buttons = [
    (("look"),(670, 500), "toilets", "morphine_used == False"),
    (("move"),(650, 700),"office_hall", None), 
]

define office_closet_buttons = [
    (("look"),(650, 500), "injured_woman_closet", None),
    (("move"),(650, 700),"office_hall", None), 
]

define office_desks_buttons= [
    (("look"),(750, 500),"worker_diary", None),

    (("move"),(1180, 440),"office_breakroom", None), 
    (("move"),(90, 430),"office_boardroom", None),

    (("move"),(650, 700),"office_start", None), 
]

define office_breakroom_buttons= [
    (("look"),(590, 260),"worker_memo", None),
    (("look"),(280, 150),"medkit_choice", "medkit_used == False"),

    (("move"),(650, 700),"office_desks", None), 
]

define office_boardroom_buttons= [
    (("look"),(720, 390),"worker_email", None),

    (("move"),(130, 300),"office_computerdesk", None), 
    (("move"),(650, 700),"office_desks", None), 
]

define office_computerdesk_buttons= [
    (("look"),(430, 370),"word_puzzle", None),

    (("move"),(650, 700),"office_boardroom", None), 
]



### LAB FLOOR START DOWNSTAIRS BUTTONS
define lab_start_buttons = [
    (("move"),(780, 300),"lab_upstairs", None),
    (("move"),(510, 300),"lab_upstairs", None),


    (("move"),(650, 480),"lab_puzzle_b_room", None),

    (("move"),(1190, 430),"lab_tanks_room", None),
    (("move"),(100, 430),"lab_radio", None), 
]

define lab_puzzle_b_room_buttons = [
    (("look"),(650, 500),"piece_puzzle_b", None),
    
    (("move"),(650, 700),"lab_start", None), 
]

define lab_radio_buttons = [
    (("look"),(300, 510), "radio", None),
    (("look"),(1100, 600), "pills", "pills == False"),

    (("move"),(650, 700),"lab_start", None), 
]

# TANK ROOM BUTTONS

define lab_tanks_room_buttons = [
    (("look"),(800, 650), "bullets", "lab_ammo_2_collected == False"),
    (("look"),(700, 420), "keycard_slider", "keycard_accepted == False"),
    (("look"),(100, 350), "bioreactor", None),

    (("move"),(700, 420),"lab_downstairs_hall", "keycard_accepted == True"),
    (("move"),(650, 700),"lab_start", None), 

]

define lab_downstairs_hall_buttons= [

    (("move"),(630, 400),"lab_puzzle_piece_a_collect_room", None), 
    (("move"),(650, 700),"lab_tanks_room", None), 
]

define lab_puzzle_piece_a_collect_room_buttons= [
    (("look"),(400, 660),"puzzle_piece_a_collect", "puzzle_piece_a_collect == False"),

    (("move"),(650, 700),"lab_downstairs_hall", None), 
]

#LAB UPSTAIRS BUTTONS

define lab_upstairs_buttons= [
    (("look"),(650, 400), "locked_master_door", None),

    (("move"),(60, 430),"lab_upstairs_left_hall", None), 
    (("move"),(1200, 430),"lab_upstairs_right_hall", None), 

    (("move"),(650, 700),"lab_start", None), 
]

#LAB UPSTAIRS LEFT HALL BUTTONS

define lab_upstairs_left_hall_buttons= [

    (("move"),(650, 400),"lab_closet_room", None), 
    (("move"),(1070, 450),"lab_puzzle_a_room", None), 
    (("move"),(200, 450),"lab_puzzle_piece_b_collect_room", None), 
    (("move"),(650, 700),"lab_upstairs", None), 
]


define lab_puzzle_a_room_buttons= [
    (("look"),(650, 500),"piece_puzzle_a", None),
    (("look"),(350, 650),"drawer_key", "drawer_key_collected == False"),

    (("move"),(650, 700),"lab_upstairs_left_hall", None), 
]

define lab_puzzle_piece_b_collect_room_buttons= [

    (("look"),(900, 670),"puzzle_piece_b_collect", "puzzle_piece_b_collect == False"),
    
    (("move"),(650, 700),"lab_upstairs_left_hall", None), 
]

define lab_closet_room_buttons= [
    (("look"),(1010, 670),"lab_note_2", None),

    (("move"),(650, 700),"lab_upstairs_left_hall", None), 
]

#LAB UPSTAIRS RIGHT HALL BUTTONS

define lab_upstairs_right_hall_buttons= [

    (("move"),(720, 400),"lab_upstairs_rightmost_hall", None), 


    (("move"),(600, 400),"lab_tara_tank", None), 

    (("move"),(450, 430),"lab_desk", None), 
    (("move"),(780, 430),"lab_upstairs_test_room", None), 

    (("move"),(650, 700),"lab_upstairs", None), 
]


define lab_desk_buttons = [
    (("look"),(850, 300), "lab_note_1", None),

    (("move"),(650, 700),"lab_upstairs_right_hall", None), 
]

define lab_upstairs_test_room_buttons = [

    (("look"),(800, 620), "bullet", "lab_ammo_1_collected == False"),

    (("move"),(650, 700),"lab_upstairs_right_hall", None), 
]

define lab_tara_tank_buttons = [

    (("look"),(490, 440),"lab_note_3", None),

    (("move"),(650, 700),"lab_upstairs_right_hall", None), 
]

#LAB UPSTAIRS RIGHTMOST HALL BUTTONS

define lab_upstairs_rightmost_hall_buttons = [

    (("move"),(630, 400),"lab_keycard_room", None), 

    (("move"),(650, 700),"lab_upstairs_right_hall", None), 
]


define lab_keycard_room_buttons = [
    (("look"),(200, 450), "keycard", "keycard == False"),
    (("look"),(920, 490), "lab_note_4", None),

    (("move"),(650, 700),"lab_upstairs_rightmost_hall", None), 
]


########## OG STUFF

### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.

### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.

#label left_frame:
    #"An empty frame."
    #"Nothing special."
    #jump pnc_loop

#label right_frame:
    #"An empty frame."
    #"Nothing special."
    #extend " Except for the fact that when you touch it, you hear a click."
    #$ pnc_flags["door_unlocked"] = True # this adds a key-value pair into the pnc_flags dictionary.
    #jump pnc_loop

#label left_door:
    #"A door."
    #if pnc_flags.get("door_unlocked") == True: # This ensures that the game doesn't throw an error if the value isn't in the dictionary
    #    "It's unlocked, so there's nothing stopping you from leaving."
    #else:
    #    "It's locked."
    #jump pnc_loop # this throws the player out from the point'n'click segment

#label escape:
    #"You open the door."
    #jump end

# The following is an example of interactions that move the player or change perspective.
# They change the background and set the room variable so that the correct set of buttons is displayed

#label to_left:
    #window hide diss
    #scene room_left with dissolve
    #$ current_room = "left"
    #jump pnc_loop

#label to_right:
    #window hide diss
    #scene room_right with dissolve
    #$ current_room = "right"
    #jump pnc_loop
