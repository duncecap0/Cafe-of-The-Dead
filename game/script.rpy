label splashscreen:
   play sound "audio/sfx/start.ogg"

   $ rand_splash_text = renpy.random.choice(['Baby you light up my world like nobody else!~', 'Just Monika.', 'This game is not suitable for those who are easily dismembered', 'NEWGROUNDS IS G'
   , 'Omae wa mou shindeiru!', 'WE LIFE FORTNITE WE LIKE FORTNITE', 'Aisheteru~', 'meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow!'
   , 'Jenna and TJ best boy/girl', 'TOKO FUKAWA STAN', 'Stess', 'JACORB', 'Hey you, Youre finally awake', 'AAAAAND THIS IS GAME GRUMPS', 'At age 6 I was born without a face...', 'Jennifer Dumped me...', 'S-enpai!'
   , 'sub 2 Jay from Kubs Scouts', 'BRAT', 'FRIDAY NIGHT FUNKIN BABY', ' houtouts to tom fulp lmao', 'HATSUNE MIKU AND TETO KASANE BEST GRILLS!!!!', 'IM NOT A FURRY', 'PLEASE DO NOT KILL ME JACOB I HAVE A FAMILY', 'God is dead, we killed him'
   , 'Meow!', 'Hello, its me I was wondering if after all these years youd like to meet', 'ITS ME', 'MAURADER SHIELDS', 'Garrus best boi', 'BAzinga!!', 'Stop! You have violated the law!', 'Garrus my beloved'
   ,'shoot the zambies!!', 'VINNIE WUZ HERE'])

   scene black with dissolve
   with Pause(1)

   show text  "[rand_splash_text]" with dissolve
   with Pause(1)
   hide text with dissolve

   show text  "Dunce Cap Industries Presents... {w=.9}LOLL LIKE IM THAT OFFICIAL" with dissolve
   with Pause(1)
   hide text with dissolve

   show text "Cafe of The Dead" with dissolve
   with Pause(1)
   hide text with dissolve

   show text "{color=#f00}WARNING: THIS GAME CONTAINS: Foul Language, Dead Bodies, Jumpscares, Guns, Haunting Imagery, Violence, Zombies!!!{/color}" with dissolve
   with Pause(3)

   hide text with dissolve
   with Pause(1)

   return

label start:
   
   call cafeintro from _call_cafeintro


return

