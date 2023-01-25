print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



choice1 = input("You wake up in a dark room where you hear a mysterious growl, do you run or stay still?\n").lower()

if (choice1 == "stay still") or (choice1 == "stay"):
  choice2 = input("You wait patiently until the growling recedes. You begin to feel against the wall until you finally reach a door and open it. It leads you to a hallway that is dimly lit. \nWill you go left or right? ").lower()
  if choice2 == "left":
    choice3 = input("You continue down the hall and as you round a corner you see light from a hole in the wall. You step out of the dungeon and on to a path towards some docks. You approach the docks and see a island in the distance. You believe you can swim to it but you also see a boat floating towards the docks. Do you swim to the island or wait for the boat?\n").lower()
    if (choice3 == "wait for boat") or (choice3 == "wait"):
      choice4 = input("As the sun begins to set the boat finally reachs the shore, you pull it towards the dock and sit down. As you take inventory you see an oar, a piece of parcel, and some food. You deem the food safe to eat and chow down while you examine the parcel. It's a map titled 'Treasure Island'. You see a larger island persumably where you are and the smaller island marked with an X. Do you row to the island or stay put?").lower()
      if (choice4 == "row to the island") or (choice4 == "row"): 
        choice5 = input("You row across the water to the smaller island, as you hit the shower and step onto the hot sand you see 3 paths.\n The first leads to a dark cave entrance.\n The second leads to a small cottage on a hill. \n The third and final path leads to a small weeping willow tree. \nWill you walk down the first path, the second path, or the third path? ").lower()
        if (choice5 == "the first path") or (choice5 =="first path") or (choice5 == 1) or (choice5 == "the first"):
          print("You approach the cave and look into it. Without a light you can't see much but you still brave the dark abyss. As you walk deeper you find your footsteps are softer but your feet feel heavy. As you reach down to feel your feet you feel a sticky webby substance. Your heart races and you begin to hear chittering from all sides. You look up and facing you is a giant black widow. She looks hungry... and you seem to be on the menu...\n GAME OVER")
        elif (choice5 == "the second path") or (choice5 =="the second") or (choice5 =="second path") or (choice5 ==2):
          print("As you approach the cottage you smell something sweet in the air. You notice the house is made of candy. The door to the cottage slowly opens as if to beckon you in. You can't seem to resist... what is that smell?! You walk into the cottage and the nice old lady is there pulling a freshly baked pie out of the oven. She looks up at you and smiles. 'You can have a slice of pie if you like, but before you do can you please pull that last pie out of the oven. It's in the back'. A strange request but who can resist a good pie. You put some mittens on and reach into the oven. Odd... You never realized how big this oven is, matter fact where is the pie. The realization dawns on you but not fast enough as the now cackling old lady shoves you in and shuts the door.\n GAME OVER...(\Hmm sounds like a old children's story but hey maybe the pie would've been worth it.)")
        elif (choice5 == "the third path") or (choice5 =="the third") or (choice5 =="third path") or (choice5 ==3):
          print("You hike up to the weeping willow, gratefully accepting its shade and all... OWW you stub your toe on the convientely placed shovel. You look down and see a patch of soil with no grass. Intuition and curiousity take over as you begin to dig the spot up. It isn't long before you hear the clank of metal on metal.\n You've done it, all the gold and jewels you could ever dream of are now yours. Spend them wisely.\n")
          print('''
                           '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
              . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
    ''')
        else:
          print("Game Over.Try again")
      else:  
        print("Well some say freedom is a treasure in itself. You bask in the sunlight... no physical treasure but hey that was enough adventuring for the day...\n GAME OVER")
      
    else: 
      print("You vigorously swim towards the island, as you approach the halfway mark you realize this part of the water is darker than all the rest. You look directly below you and see a large formation of rocks that seem to be moving towards you... or wait are those teeth?!?!?\n GAME OVER")
    
  else:   
    print("You wander down the hall when suddenly you step into nothingness.\n GAME OVER")
else: 
  print("You mad dash away from the growling and suddenly you hear fast foot steps chasing after you before you can react you are tackled and feel hot breath on your face.\n GAME OVER")





