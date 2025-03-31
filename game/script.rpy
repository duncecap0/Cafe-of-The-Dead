label splashscreen:
   play sound "audio/sfx/start.ogg"

   $ rand_splash_text = renpy.random.choice(['Baby you light up my world like nobody else!~', 'Just Monika.', 'This game is not suitable for those who are easily dismembered', 'NEWGROUNDS IS G'
   , 'Omae wa mou shindeiru!', 'WE LIKE FORTNITE WE LIKE FORTNITE', 'Aisheteru~', 'meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow!'
   , 'Jenna and TJ best boy/girl', 'TOKO FUKAWA STAN', 'Stess', 'JACORB', 'Hey you, Youre finally awake', 'At age 6 I was born without a face...', 'S-enpai!'
   , 'sub 2 Jay from Kubs Scouts', 'BRAT', 'FRIDAY NIGHT FUNKIN BABY', 'shoutouts to tom fulp lmao', 'HATSUNE MIKU AND TETO KASANE BEST GRILLS!!!!', 'IM NOT A FURRY', 'PLEASE DO NOT KILL ME JACOB I HAVE A FAMILY', 'God is dead, we killed him'
   , 'Meow!', 'Hello, its me I was wondering if after all these years youd like to meet', 'ITS ME', 'MAURADER SHIELDS', 'Garrus best boi', 'BAzinga!!', 'Stop! You have violated the law!', 'Garrus my beloved'
   ,'shoot the zambies!!', 'VINNIE WUZ HERE'])

   scene black with dissolve
   with Pause(1)

   show text  "[rand_splash_text]" with dissolve
   with Pause(1)
   hide text with dissolve

   show text "Cafe of The Dead" with dissolve
   with Pause(1)
   hide text with dissolve

   show text "{color=#f00}WARNING: THIS GAME CONTAINS: Foul Language, Dead Bodies, Jumpscares, Guns, Haunting Imagery, Suicide, Violence, Zombies!!!{/color}" with dissolve
   with Pause(3)

   hide text with dissolve
   with Pause(1)

   return

label start:
   
   call cafe_floor_0 from _call_cafe_floor_0
   
   call mechanical_floor_1 from _call_mechanical_floor_1

   call office_floor_2 from _call_office_floor_2

   call lab_floor_3 from _call_lab_floor_3

   call endings from _call_endings

return

