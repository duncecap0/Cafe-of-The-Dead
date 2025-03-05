screen sage_status: 
    imagebutton:
        pos (500, 300) 
        idle "arrow_down"
        hover "arrow_down_glow"
        action [Hide("displayTextScreen"), Jump("digicode_room")]

        hovered Show("displayTextScreen", 
            displayText = "Go Downstairs?") 
        unhovered Hide("displayTextScreen")

screen rocky_status: 
    imagebutton:
        pos (500, 300) 


        if rocky_dead:
            idle "arrow_down"
            hover "arrow_down_glow"
        else:
            idle "arrow_down"
            hover "arrow_down_glow"    

        action [Hide("displayTextScreen"), Jump("digicode_room")]

        hovered Show("displayTextScreen", 
            displayText = "Go Downstairs?") 
        unhovered Hide("displayTextScreen")

screen vivi_codex: 
    imagebutton:
        pos (500, 300) 
        idle "arrow_down"
        hover "arrow_down_glow"
        action [Hide("displayTextScreen"), Jump("digicode_room")]

        hovered Show("displayTextScreen", 
            displayText = "Go Downstairs?") 
        unhovered Hide("displayTextScreen")

screen norman_codex: 
    imagebutton:
        pos (500, 300) 
        idle "arrow_down"
        hover "arrow_down_glow"
        action [Hide("displayTextScreen"), Jump("digicode_room")]

        hovered Show("displayTextScreen", 
            displayText = "Go Downstairs?") 
        unhovered Hide("displayTextScreen")





screen down_arrow_vault_digicode: 
    imagebutton:
        pos (500, 300) 
        idle "arrow_down"
        hover "arrow_down_glow"
        action [Hide("displayTextScreen"), Jump("digicode_room")]

        hovered Show("displayTextScreen", 
            displayText = "Go Downstairs?") 
        unhovered Hide("displayTextScreen")

screen vault_brick_collect: 
    imagebutton:
        pos (200, 500) 
        idle "brick"
        hover "brick"
        action [ToggleScreen("vault_brick_collect"), Hide("displayTextScreen"), Jump("vault_brick")]

        hovered Show("displayTextScreen", 
            displayText = "Collect Brick?") 
        unhovered Hide("displayTextScreen")