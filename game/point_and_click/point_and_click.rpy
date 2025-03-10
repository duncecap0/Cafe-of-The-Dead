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
    (("look"),(300, 100),"mech_crowbar", None), #HOW DO YOU MAKE THIS GO AWAY WHEN IT APPEARS??
    (("look"),(600, 440), "hvac", None),
    (("look"),(750, 300),"mech_ladder",  None), # Condition. The way it's written ensures that the game doesn't throw an error if the "door_unlocked" key isn't in the dictionary
    (("move"),(800, 100),"mech_floor_main_room_2", None),
    (("move"),(1140, 430), "mech_hallway", None),
]

define mech_floor_main_room_2_buttons = [
    (("look"),(650, 500), "mech_corpse", None),
    (("look"),(60, 300), "mech_electric_door", None),
    (("look"),(1220, 300),"mech_elevator", None),
    (("move"),(60, 500),"mech_vent", "pnc_flags.get('vent_unlocked') == True"), # Condition. The way it's written ensures that the game doesn't throw an error if the "door_unlocked" key isn't in the dictionary
    (("move"),(650, 700),"mech_floor_main_room_1", None),

]

define mech_hallway_buttons= [
    (("look"),(650, 400), "mech_desk", None),
    (("move"),(650, 700),"mech_floor_main_room_1", None), #this will return you the hallway loop
    (("move"),(90, 400),"mech_hallway_left", None),
    (("move"),(1200, 400),"mech_hallway_right", None),
]

define mech_hallway_left_buttons= [
    (("look"),(1200, 400), "mech_left_hall_jacket", None),
    (("move"),(650, 700),"mech_hallway", None), #this will return you the hallway loop
]

define mech_hallway_right_buttons= [
    (("look"),(200, 540),"mech_right_hall_bed", None),
    (("move"),(650, 700),"mech_hallway", None), #this will return you the hallway loop
]



###OFFICE FLOOR BUTTONS
define office_start_buttons = [
    (("look"),(650, 440), "office_window", None),

    (("move"),(1140, 430),"office_desks", None),
    (("move"),(60, 430),"office_hall", None), 
]

define office_hall_buttons = [
    (("move"),(1140, 430),"office_restroom", None),

    (("look"),(60, 430),"blocked_closet", None),
    (("move"),(60, 430),"office_closet", "pnc_flags.get('vent_unlocked') == True"),
    
    (("move"),(650, 700),"office_start", None), 
]

define office_restroom_buttons = [
    (("look"),(650, 500), "toilets", None),
    (("move"),(650, 700),"office_hall", None), 
]

define office_closet_buttons = [
    (("look"),(650, 500), "injured_woman_closet", None),
    (("move"),(650, 700),"office_hall", None), 
]

define office_desks_buttons= [
    (("look"),(900, 500),"worker_diary", None),
    (("look"),(650, 700),"office_corpse", None),

    (("move"),(60, 440),"office_breakroom", None), 
    (("move"),(1140, 430),"office_boardroom", None),

    (("move"),(650, 700),"office_start", None), 
]

define office_breakroom_buttons= [
    (("look"),(700, 440),"worker_memo", None),
    (("look"),(900, 500),"medkit", None),

    (("move"),(650, 700),"office_desks", None), 
]


define office_boardroom_buttons= [
    (("look"),(650, 400), "projector", None),
    (("look"),(900, 200),"worker_diary", None),

    (("move"),(60, 430),"office_computerdesk", None), 
    (("move"),(650, 700),"office_desks", None), 
]

define office_computerdesk_buttons= [
    (("look"),(650, 440),"word_puzzle", None),

    (("move"),(650, 700),"office_desks", None), 
]



### LAB FLOOR BUTTONS
define lab_start_buttons = [
    (("look"),(650, 440), "dead_soldiers", None),

    (("move"),(1140, 430),"lab_upstairs", None),
    (("move"),(60, 430),"lab_radio", None), 
]

define lab_puzzle_b_room_buttons = [
    (("look"),(60, 430),"piece_puzzle_b", None),
    
    (("move"),(650, 700),"office_start", None), 
]

define lab_radio_buttons = [
    (("look"),(650, 500), "radio", None),
    (("look"),(650, 300), "pills", None),

    (("move"),(650, 700),"lab_start", None), 
]

define lab_test_room_buttons = [
    (("look"),(650, 500), "bullets", None),
    (("look"),(650, 400), "keycard_slider", None),

    (("move"),(650, 300),"lab_downstairs_hall", None),
    (("move"),(650, 700),"lab_start", None), 

]

define lab_downstairs_hall_buttons= [

    (("move"),(650, 440),"lab_puzzle_piece_a_collect_room", None), 
    (("move"),(650, 700),"lab_test_room", None), 
]

define lab_puzzle_piece_a_collect_room_buttons= [
    (("look"),(700, 440),"piece_puzzle_a", None),

    (("move"),(650, 700),"lab_downstairs_hall", None), 
]

define lab_upstairs_buttons= [
    (("look"),(650, 400), "locked_master_door", None),

    (("move"),(60, 430),"lab_upstairs_left_hall", None), 
    (("move"),(1000, 700),"lab_upstairs_right_hall", None), 
    (("move"),(650, 700),"lab_start", None), 
]

define lab_upstairs_left_hall_buttons= [

    (("move"),(60, 430),"lab_puzzle_a_room", None), 
    (("move"),(1000, 700),"lab_puzzle_piece_b_collect_room", None), 
    (("move"),(650, 700),"lab_upstairs", None), 
]


define lab_puzzle_a_room_buttons= [
    (("look"),(650, 440),"piece_puzzle_a", None),

    (("move"),(650, 700),"lab_upstairs_left_hall", None), 
]

define lab_puzzle_piece_b_collect_room_buttons= [

    (("look"),(650, 430),"puzzle_piece_b_collect", None),
    
    (("move"),(650, 700),"lab_upstairs_left_hall", None), 
]

define lab_upstairs_right_hall_buttons= [

    (("move"),(60, 430),"lab_desk", None), 
    (("move"),(1000, 700),"lab_upstairs_test_room", None), 
    (("move"),(650, 700),"lab_upstairs", None), 
]

define lab_desk_buttons = [

    (("look"),(650, 500), "plague_note", None),
    (("move"),(650, 700),"lab_upstairs_right_hall", None), 
]


define lab_upstairs_rightmost_hall_buttons = [
    (("move"),(60, 500),"lab_keycard_room_buttons", None), 
    (("move"),(1000, 500),"lab_tanks_buttons", None), 

    (("move"),(650, 700),"lab_upstairs_rightmost_hall", None), 
]


define lab_keycard_room_buttons = [
    (("look"),(650, 400), "keycard", None),

    (("move"),(650, 700),"lab_upstairs_rightmost_hall", None), 
]

define lab_tanks_buttons = [

    (("look"),(650, 440),"zombie_large_attack", None),

    (("move"),(650, 700),"lab_upstairs_rightmost_hall", None), 
]

define lab_boss_room_buttons = [
    (("move"),(650, 700),"lab_upstairs", None), 
]

########## OG STUFF

### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.

### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.

label left_frame:
    "An empty frame."
    "Nothing special."
    jump pnc_loop

label right_frame:
    "An empty frame."
    "Nothing special."
    extend " Except for the fact that when you touch it, you hear a click."
    $ pnc_flags["door_unlocked"] = True # this adds a key-value pair into the pnc_flags dictionary.
    jump pnc_loop

label left_door:
    "A door."
    if pnc_flags.get("door_unlocked") == True: # This ensures that the game doesn't throw an error if the value isn't in the dictionary
        "It's unlocked, so there's nothing stopping you from leaving."
    else:
        "It's locked."
    jump pnc_loop # this throws the player out from the point'n'click segment

label escape:
    "You open the door."
    jump end

# The following is an example of interactions that move the player or change perspective.
# They change the background and set the room variable so that the correct set of buttons is displayed

label to_left:
    window hide diss
    scene room_left with dissolve
    $ current_room = "left"
    jump pnc_loop

label to_right:
    window hide diss
    scene room_right with dissolve
    $ current_room = "right"
    jump pnc_loop
