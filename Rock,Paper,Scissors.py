#!/usr/bin/env Python3

import random #import module so that computer will generate random choice

print('''                                                                                                                                                                                          
88888888ba                        88           88888888ba                                                   ad88888ba             88                                                       
88      "8b                       88           88      "8b                                                 d8"     "8b            ""                                                       
88      ,8P                       88           88      ,8P                                                 Y8,                                                                             
88aaaaaa8P' ,adPPYba,   ,adPPYba, 88   ,d8     88aaaaaa8P' ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,    `Y8aaaaa,    ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
88""""88'  a8"     "8a a8"     "" 88 ,a8"      88""""""'   ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8      `"""""8b, a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
88    `8b  8b       d8 8b         8888[        88          ,adPPPPP88 88       d8 8PP""""""" 88                    `8b 8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
88     `8b "8a,   ,a8" "8a,   ,aa 88`"Yba,     88          88,    ,88 88b,   ,a8" "8b,   ,aa 88            Y8a     a8P "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
88      `8b `"YbbdP"'   `"Ybbd8"' 88   `Y8a    88          `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88             "Y88888P"   `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                      88                                                                                                                   
                                                                      88                                                                                            
      ''')
print("\nA DaRoc Production\n")

# Game images variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors] #Variable puts the ASCII art in a list

user_choice = int(input("Rock, Paper, Scissors Shoot! 1.Rock 2.Paper 3.Scissors\n"))

if user_choice >= 3 or user_choice <0: #This if statement will print "You lose" if the user inputs an invalid choice.
  print("You typyed and invalid number, You lose!")
else:
  print(game_images[user_choice]) #When user choices a number, this prints a ASCII image

  computer_choice = random.randint(0, 2) #Here causes the computer to pick a random number between 0 - 2.
  print(f"Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("\nYou win!")
  elif computer_choice == 0 and user_choice ==2:
    print("You lose!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif computer_choice == user_choice:
    print("It's a draw")
  elif user_choice > computer_choice:
    print("You win!")
