
define flash =Fade(2.0, 1.0, 2.0, color="#fff")

define left1 = Position(xalign=0.3)

define right2 = Position(xalign=0.7)

define rightBIGG = Position(xalign=2.0, yalign=0.5)
define centerBIGG = Position(xalign=1.0, yalign=0.5)

image static_anim:
    "images/static1.webp"
    alpha 0.2
    pause 0.1
    "images/static2.webp"
    alpha 0.3
    pause 0.1
    "images/static3.webp"
    alpha 0.4
    pause 0.1
    "images/static4.webp"
    alpha 0.3
    pause 0.1
    "images/static5.webp"
    alpha 0.2
    pause 0.1
    repeat

image breadly:
    yalign 1.0
    "images/breadly.webp"

image dunce:
    "images/dunce.webp"

image bigzom:
    "images/z 1.webp"

image bluzom:
    xalign 0.0
    "images/z 2.webp"

image orangzom:
    yalign 1.0
    "images/z 3.webp"

image jug = "images/naut.webp"
image jug2 = "images/naut 2.webp"

image black ="#000000"

image click_to_continue:
    xpos 5
    ypos -12
    "gui/click_to_continue0.png"
    0.5
    linear 0.5 alpha 0.5
    0.5
    linear 0.5 alpha 1.0
    repeat

## TormentedStudios button scale https://www.reddit.com/r/RenPy/comments/yvz8x8/increase_the_size_of_a_button_when_hovered_over/

transform buttonScale: 
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0

transform buttonScale_sticker: 
    on hover:
        linear 0.1 zoom 1.0
    on idle:
        linear 0.1 zoom 0.9

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