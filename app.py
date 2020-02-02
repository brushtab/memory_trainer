import random
import sys
from collections import OrderedDict
filename = 'memory_map.txt'
memory_dict = OrderedDict()
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        number, memory_point = line.split('.')
        memory_dict[number] = memory_point.strip()
last_memory_point = int(list(memory_dict.keys())[-1])
score = 0
print("Welcome to memory trainer!")
max_training_number = int(sys.argv[1])
correct_anwser = False
while True:
    random_memory_point = random.randint(0, max_training_number)
    #print(f"Your score is {score}")
    if correct_anwser:
        user_number_guess = input(f"+{score} How number {random_memory_point} looks? ")
    else:
        user_number_guess = input(f"-{score} How number {random_memory_point} looks? ")
    if user_number_guess.lower() == memory_dict[str(random_memory_point)].lower():
        #print(f"You're right! {random_memory_point} is {user_number_guess}")
        score += 1
        correct_anwser = True
        #print(f"{score}")
    else:
        #print("You're wrong!")
        correct_anwser = False
        score -= 1
        print(f"{random_memory_point} is {memory_dict[str(random_memory_point)].lower()}")
    

