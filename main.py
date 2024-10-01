# Up Down Left Right - Practice Program
# Required Internet on this Branch (gTTS)
# CopyRight by Panupong Utvichai

import random
from gtts import gTTS
import os
import pyttsx3
import time

def draw_final_answer(total_command):
  block = [
    ["L0 R0", "L0 R0", "L0 R0", "L0 R0"],
    ["L0 R0", "L0 R0", "L0 R0", "L0 R0"],
    ["L0 R0", "L0 R0", "L0 R0", "L0 R0"],
    ["L0 R0", "L0 R0", "L0 R0", "L0 R0"]
  ]

#   block = [
#     ["00", "01", "02", "03"],
#     ["10", "11", "12", "13"],
#     ["20", "21", "22", "23"],
#     ["30", "31", "32", "33"]
#   ]

  for command in total_command:
    compute_answer(command, block)

  count = 0
  print()
  print("======================ANSWER======================\n")
  while count < 4:
     print(block[count])
     print()
     count += 1

def compute_answer(command, answer_block):
   # Command come as "UDLRL"
   x_value = 0
   y_value = 0

   # BASED on Main Direction (1st Alphabet)
   if command[0] in {"U", "D"}:
      # Start Vertically
      if (command[0] == "U"):
         x_value = 0
      else:
         x_value = 3

      if (command[1] == command[0]):
         x_value += 0
      elif (command[0] == "U" and command[1] == "D"):
         x_value += 1
      else:
         x_value -= 1

      # Next Horizontally
      if (command[2] == "L"):
         y_value = 0
      else:
         y_value = 3

      if (command[3] == command[2]):
         y_value += 0
      elif (command[2] == "L" and command[3] == "R"):
         y_value += 1
      else:
         y_value -= 1

   else:
      # Start Horizontally
      if (command[0] == "L"):
         y_value = 0
      else:
         y_value = 3

      if (command[1] == command[0]):
         y_value += 0
      elif (command[0] == "L" and command[1] == "R"):
         y_value += 1
      else:
         y_value -= 1

      # Next Vertically
      if (command[2] == "U"):
         x_value = 0
      else:
         x_value = 3

      if (command[3] == command[2]):
         x_value += 0
      elif (command[2] == "U" and command[3] == "D"):
         x_value += 1
      else:
         x_value -= 1
   
   # print("XY: " + str(x_value) + str(y_value) + " | L/R: " + str(command[4].upper()))

   target_block = answer_block[x_value][y_value]
   hand_to_write = command[4]
   split_left_right_count = target_block.split(" ")
   left_count = int(split_left_right_count[0][1])
   right_count = int(split_left_right_count[1][1])
   if hand_to_write == "L":
       left_count += 1
   else:
       right_count += 1
   answer_block[x_value][y_value] = "L" + str(left_count) + " R" + str(right_count)

def read_out_load(command_list):
   total_number_to_ask = random.randint(2,5)
   print("Total num to ask: " + str(total_number_to_ask))
   total_command_count = len(command_list)

   list_of_position_to_ask = set()
   while len(list_of_position_to_ask) < total_number_to_ask:
      position_to_ask = random.randint(1, total_command_count)
      list_of_position_to_ask.add(position_to_ask)
      
   print("list of position to ask: ")
   print(list_of_position_to_ask)
   replacement_map = {'R': 'Right', 'L': 'Left', 'U': 'Up', 'D': 'Down'}
   final_string = "UDLR Five Four Three Two One "

   count_command = 1
   for command in command_list:
      final_string += " | "
      for char in command:
         final_string += replacement_map[char]
      if count_command in list_of_position_to_ask:
         final_string += " "
         math_question = str(random.randint(-9,9))
         final_string += math_question
         math_question_list.append(math_question)
      count_command += 1
   print("Math Question List: ")
   print(math_question_list)
   # print("final_string = ")
   # print(final_string)
   tts = gTTS(text=final_string, lang='en')
   tts.save("udlr_output.mp3")
   os.system("start udlr_output.mp3")

def ending_math_game(list_of_numbers):
   question_list = [
    "How many numbers in the list are prime numbers?",
    "Find the sum of all numbers.",
    "Find the sum of all even numbers.",
    "Find the sum of all odd numbers.",
    "Find the sum of all negative numbers.",
    "Find the sum of all positive numbers.",
    "Find the product of all numbers."
]
   
   ending_question_set = set()
   ending_question_set.add("How many numbers are there?")
   i = 1
   while i <= 4 : # Number of question here.
      randomed_question = random.choice(question_list)
      if randomed_question not in ending_question_set:
         ending_question_set.add(randomed_question)
         i += 1

   time.sleep(60) # Waiting for commands to finish

   for question in ending_question_set:
      print(question)
      engine.say(question)
      engine.runAndWait()
      time.sleep(5)

# START
engine = pyttsx3.init()

# voice sound
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# voice speed -- Default 200 wpm
newVoiceRate = 130
volume = 0.9
engine.setProperty('volume', volume)
engine.setProperty('rate', newVoiceRate)

choices_start_direction = ["updown", "leftright"]
choices_up_down = ["U", "D"]
choices_left_right = ["L", "R"]
math_question_list = []

print("START ULDR")

total_command = []
x = 1
while x <= 20: # Change Total Commands here
    start_direction = random.choices(choices_start_direction)
    if (start_direction[0] == "updown") :
        alphabet1 = random.choice(choices_up_down)
        alphabet2 = random.choice(choices_up_down)
        alphabet3 = random.choice(choices_left_right)
        alphabet4 = random.choice(choices_left_right)
        alphabet5 = random.choice(choices_left_right)
    else:
        alphabet1 = random.choice(choices_left_right)
        alphabet2 = random.choice(choices_left_right)
        alphabet3 = random.choice(choices_up_down)
        alphabet4 = random.choice(choices_up_down)
        alphabet5 = random.choice(choices_left_right)
    command = alphabet1[0]+alphabet2[0]+alphabet3[0]+alphabet4[0]+alphabet5[0]
    total_command.append(command)
    x += 1
    
print(total_command)
counter = 1
for com in total_command:
   print(str(counter) + ': ' + com)
   counter += 1

print("Total Command: " + str(len(total_command)))
read_out_load(total_command)
draw_final_answer(total_command)
ending_math_game(math_question_list)
input("Press Enter to exit...")