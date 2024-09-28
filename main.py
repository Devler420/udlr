# Up Down Left Right - Practice Program

#TODO: Voice Engine + Math Interuption

import random
import pyttsx3

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
      elif (command[2] == "U" and command[1] == "D"):
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

def read_out_loud(command_list):
   for command in command_list:
      string_to_read = "".join(transform_to_full_letter(letter) for letter in command)
      engine.say(string_to_read)
      engine.runAndWait()

def transform_to_full_letter(single_string):
   if (single_string == "U"):
      single_string = "Up"
      return single_string
   elif (single_string == "D"):
      single_string = "Down"
      return single_string
   elif (single_string == "L"):
      single_string = "Left"
      return single_string
   elif (single_string == "R"):
      single_string = "Right"
      return single_string
   else:
      return "Invalid String"

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

print("START ULDR")

total_command = []
x = 1
while x <= 20:
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
print(len(total_command))
read_out_loud(total_command)
draw_final_answer(total_command)
