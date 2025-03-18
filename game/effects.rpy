
define flash =Fade(2.0, 1.0, 2.0, color="#fff")

image black ="#000000"

image click_to_continue:
    xpos 5
    ypos -5
    "gui/click_to_continue0.png"
    linear 0.5 alpha 0.2
    pause(1.0)
    linear 0.5 alpha 0.3
    pause(0.5)
    linear 0.5 alpha 0.4
    pause(0.5)
    linear 0.5 alpha 0.3
    "gui/click_to_continue1.png"
    repeat

screen item_shit_UI:
    frame:
        #add "UI/bg_FUCK.png":
            #xsize 500
            #ysize 500    
        add Solid ("#3b3b3b")
        xsize 500
        ysize 500
        xalign 1.0
        yalign 0.5
        text "Item Acquired!"
        #hbox:
            #spacing 20
            #text "Item Acquired!"

style item_shit_UI:
    size 40
    #color "#f00"

transform sink:
        ypos 710 
        linear 0.43 ypos 822 
        0.53
        ypos 822 

transform sink_rise:
        ypos 822 
        linear 0.43 ypos 710 
        0.53
        ypos 710

transform hop:
        ypos 730 
        easein_bounce 0.24 ypos 720 
        0.34
        ypos 720

transform hop_loop:
        ypos 730 
        easein_bounce 0.24 ypos 720 
        0.34
        ypos 720
        repeat

transform big_hop:
        ypos 650 
        easein_bounce 0.24 ypos 720 
        0.34
        ypos 720 

transform big_hop_loop:
        ypos 650 
        easein_bounce 0.24 ypos 720 
        0.34
        ypos 720 
        repeat

transform shiver:
        xpos 630 
        easein_bounce 0.18 xpos 650 
        easein 0.15 xpos 640 
        0.43
        xpos 640 

transform shiver_loop:
        xpos 630 
        easein_bounce 0.18 xpos 650 
        easein 0.15 xpos 640 
        0.43
        xpos 640
        repeat

transform slow_r2l_loop:
        xpos 500 
        linear 0.18 xpos 500 
        linear 0.15 xpos 700 
        2.0
        xpos 700
        repeat

transform offscreen_right:
        linear 0.75 xpos 1500 

transform offscreen_left:
        linear 0.75 xpos -1500 

return