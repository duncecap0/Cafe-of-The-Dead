
define flash =Fade(2.0, 1.0, 2.0, color="#fff")

define left1 = Position(xalign=0.3)

define right2 = Position(xalign=0.7)

image breadly:
    yalign 1.0
    "images/breadly.png"

image dunce:
    "images/dunce.png"

image bigzom:
    "images/z 1.png"

image bluzom:
    xalign 0.0
    "images/z 2.png"

image orangzom:
    yalign 1.0
    "images/z 3.png"

image jug = "images/naut.png"
image jug2 = "images/naut 2.png"

image black ="#000000"

image click_to_continue:
    xpos 5
    ypos -12
    "gui/click_to_continue0.png"
    0.5
    linear 0.5 alpha 0.5
    "gui/click_to_continue1.png"
    0.5
    linear 0.5 alpha 1.0
    repeat



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

transform sink_rise_little:
        ypos 822 
        linear 0.43 ypos 710 
        0.53
        ypos 710

transform offscreen_bottom:
        ypos 2000 
        linear 0.43 ypos 2000 
        0.53
        ypos 2000

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


transform shiver_loop_left:
        xpos -10 
        easein_bounce 0.18 xpos 10 
        easein 0.15 xpos 5 
        0.43
        xpos -5
        repeat

transform shiver_loop_right:
        xanchor 0.0
        xpos 830 
        easein_bounce 0.18 xpos 850 
        easein 0.15 xpos 840 
        0.43
        xpos 840
        repeat

transform shiver_loop:
        xpos 630 
        easein_bounce 0.18 xpos 650 
        easein 0.15 xpos 640 
        0.43
        xpos 640
        repeat

transform shiver_loop_center:
        xpos 430 
        easein_bounce 0.18 xpos 450 
        easein 0.15 xpos 440 
        0.43
        xpos 440
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