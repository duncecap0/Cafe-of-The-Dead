
## change music code after persistent ending https://lemmasoft.renai.us/forums/viewtopic.php?t=69574
init python:
   def replace_music(filename):
      if filename == config.main_menu_music and persistent.hailending == True:
         return "audio/music/hail.ogg"
      elif filename == config.main_menu_music and persistent.trueending == True:
         return "audio/music/Morning_Joe.mp3"
      return filename

define config.audio_filename_callback = replace_music

## endings
default persistent.trueending = False

default persistent.hailending = False

## achievements
default persistent.killnorman = False
default persistent.killvin = False
default persistent.killrocky = False
default persistent.savetara = False
default persistent.dontuseitems = False
default persistent.petty_sage = False

default persistent.nosanityloss = False

default persistent.touchtoilet5times = False
default persistent.dontusebullets = False
default persistent.motivatefriends = False
default persistent.romancenorman = False

default persistent.tara_against_dad = False

## secrets
default seen_dev_message = False
default seen_tara_ending = False

label splashscreen:
   play sound "audio/sfx/start.ogg"
   $ rand_splash_text = renpy.random.choice(['Baby you light up my world like nobody else!~', 'Death is the only cure for madness','How many of you do I have to kill to save your lives.', 'Coin-user!', 'PLEASE STOP HITTING ME WITH A METAL PIPE!!!', 'THEY/THEM? I AM CLEARLY OUTNUMBERED', 'Task failed successfully', 'Blessed Lamb...', 'Are you there? Can you hear me?', 'Hasta la vista!', 'HE WAS A SKATER BOY!', 'TRANS RIGHTS!', 'YURI!', 'CORAL!', 'You were almost a Jill sandwich', 'Seven minutes. Seven minutes is all I can spare to play with you', 'You dont need to save the world to find meaning in life. Sometimes all you need is something simple, like someone to take care of.', 'Find my 8 pages...', 'There is no "I" in team, but there is an "I" in pie.','Go to the Inner Sanctum... Find Alexander and kill him', 'Monsters...? They look like monsters to you?', 'Its Frank. Frank West. Remember that name cause the whole worlds gonna know it in three days when I get the scoop.', 'You two are the biggest morons ever! I swear, if I have to spend one more second with you guys Ill go crazy!', 'WUBUBUBUBUBU!', 'Did i ever tell you bout the time my buddy Keith', 'Good riddance. Always giving to others instead of to yourself. Why did you live like that? What was the point? What a load of crap.', 'I was weak, I needed someone to punish me for my sins' 'Just Monika.', 'The world is quieter now.','The Mad House of Taran is coming soon...','The beginning of madness... or end?' 'This game is not suitable for those who are easily dismembered', 'NEWGROUNDS IS DA G', 'Omae wa mou shindeiru!', 'WE LIKE FORTNITE WE LIKE FORTNITE', 'Aisheteru~', 'meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow!', 'Stess', 'JACORB', 'Hey you, Youre finally awake', 'At age 6 I was born without a face...', 'S-senpai!', 'Malachy and Taran sitting in a tree!', 'Eilis is kicking ass rn...', 'My lord!! My lord Taran!! Im here to save you from across time and space!!!', 'BRAT', 'FRIDAY NIGHT FUNKIN BABY', 'shoutouts to tom fulp lmao', 'HATSUNE MIKU AND TETO KASANE BEST GRILLS!!!!', 'IM NOT A FURRY', 'PLEASE DO NOT KILL ME JACOB I HAVE A FAMILY', 'God is dead, we killed him', 'Meow!', 'Hello, its me I was wondering if after all these years youd like to meet', 'ITS ME', 'MAURADER SHIELDS', 'Garrus best boi', 'BAzinga!!', 'Stop! You have violated the law!', 'Garrus my beloved', 'shoot the zambies!!', 'VINNIE WUZ HERE', 'I stole a mothers cellphone and a 10 year old boys wallet', 'A GAME THEORY', 'callibrating', 'Reticulating splines', 'It was just a prank Han!', 'WE NEED TO FIND A BOAT!!', '28 STAB WOUNDS!!!', 'He dun wan it!', 'Daniel hear my voice...', 'Dont forget, Im with you in the dark', 'Its still you', 'NEVER SHOULD HAVE COME HERE','ADHD POWERS ACTIVATE', 'PSYCHO 1998 REMAKE', 'she took the kids', 'Successfully Deleted System 32', 'The devils eyes', 'When in hell, only the devil can you hear you out', 'Live or Die, your choice', 'Only want you gone', 'Still alive', 'STILL. NOT. BITTEN.', 'COOOOORAAALLLLLL!!!', 'respect the wahmen!', 'This game contains 0 LGBT', 'There are no furries in this game', 'I cant make this choice! No, youre the only one who can...', 'In my way.', 'The cake is a lie', 'CUT MY LIFE INTO PIECES', 'FUNNY! ISNT IT?!', 'NWAH!', 'KHAJIIT NO EQUAL FURRY PLS', 'LEON WE NEED TO GET THE HERBS', 'STOP WITH THE FUCKING TANK CONTROLS JILL!!!', 'Do you like scary movies?', 'I LOVE FIT GIRLS','ULTRAKILL DIDNT INSPIRE DOLION', 'GIALLO MY BELOVED', 'SPRUCE MY BELOVED','Caution is coming soon!', 'LIVE BENNETT REACTION', 'CUT MY LIFE INTO PIECES', 'WAKE ME UP INSIDE', 'HELLA', 'HIIII', 'ZESTY','HEART. LUNG. LIVER. NERVES.', 'Now with somewhat betterer grammar!', 'stess', 'YA I GOT PAPERS HYAHYAHYAHYA!!!', 'I TAKE A POTATO CHIP AND EAT IT', 'I SWEAR I REALLY TRIED FOR THIS TO BE GOOD WE HAD A TIGHT SCHEDULE!!!', '11037', 'Mukuro Ikusaba. The sixteenth student, lying hidden somewhere in this school. The one they call the Ultimate Despair. Watch out for her.','Eighteen naked cowboys in the showers at Ram Ranch', 'What the fuck did you just fucking say about me you little cumslut? Ill have you know I graduated top of my class in the Navy Seals'])
   
   scene black with dissolve
   with Pause(1)

   show text  "[rand_splash_text]" with dissolve
   with Pause(1)
   hide text with dissolve

   show text "Cafe of The Dead" with dissolve
   with Pause(1)
   hide text with dissolve

   show text "{color=#f00}WARNING: THIS GAME CONTAINS: Zombies, Foul Language, Haunting Imagery, Jump scares, Knives, Guns, Violence, Drug Abuse, Drug Overdose, Mental Illness, Corpses, and Suicide{/color}" with dissolve
   with Pause(3)
   show text "{color=#f00}Characters will perform rudimentary medical practices.  It is highly recommended to NOT COPY these character's actions as neither the developers or characters are medically certified. It also suggested to not follow any extreme actions demonstrated by some characters as they can give problematic advice.{/color}" with dissolve
   with Pause(5)
   hide text with dissolve
   with Pause(1)

   return
               
label start:

   #if persistent.trueending == True and persistent.touchtoilet5times == True and persistent.killnorman == True and persistent.killvin == True and persistent.killrocky == True and persistent.savetara == True and persistent.tara_against_dad == True and persistent.dontusebullets == True and persistent.nosanityloss == True and persistent.romancenorman == True and persistent.petty_sage == True and persistent.motivatefriends == True and persistent.hailending == True: 
   #   play sound "audio/sfx/start.ogg"
   #   show text "Congrats on getting every achievement!" with dissolve
   #   with Pause(2)
   #   hide text with dissolve
   #   show text "{color=#f00}Secret scenes unlocked!{/color}" with dissolve
   #   with Pause(1)
   #   hide text with dissolve
   #   call secret_tara_end_scene from _call_secret_tara_end_scene

   call cafe_floor_0 from _call_cafe_floor_0
   
   call mechanical_floor_1 from _call_mechanical_floor_1

   call office_floor_2 from _call_office_floor_2

   call lab_floor_3 from _call_lab_floor_3

   call endings from _call_endings

return

