"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomáš Beránek
email: tomas.malehorky@seznam.cz
discord: Tomáš B. Berrys#6258
"""

import csv
import random
import time


print('Hi there!')
print('-----------------------------------------------')
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print('-----------------------------------------------')

unique_numbers = random.sample(range(0,10), 4)

while unique_numbers[0] == 0:
    unique_numbers = random.sample(range(0,10), 4)

number_for_game = f'{unique_numbers[0]}' + f'{unique_numbers[1]}' + f'{unique_numbers[2]}' + f'{unique_numbers[3]}'      
print(number_for_game)

print('-----------------------------------------------')
print('If you want to stop playing, type "exit"')

def input_check(checked_attempt):
    """
    Checking if the input is right
    """
    if not checked_attempt.isnumeric():
        return 'You have typed wrong characters, please type only numbers.'
    if not len(checked_attempt) == 4:
        return 'You have typed wrong number of characters.'
    if checked_attempt.startswith('0'):
        return 'Number cannot start with zero'
    if not len(splited_users_numbers_set) == 4:
        return 'Numbers cannot be duplicates'
    return None

def hints_updater(dict_name, dict_animal):
    """
    Updating hints in 'hints' dict
    """
    dict_name.update({dict_animal: dict_name[dict_animal]+1})

def hints_counter(numbers_list,random_numbers,index_for_numbers):
    """
    Counting how many numbers are correct in players input
    """
    for users_numbers in numbers_list:
            if users_numbers in random_numbers:
                hints_updater(hints, 'cows')
            if users_numbers == random_numbers[index_for_numbers]:
                hints_updater(hints, 'bulls')
            index_for_numbers += 1

def hints_printer(hints_dict):
    """
    Printing hints for the player
    """
    for animals, ocurence in hints_dict():
        if ocurence == 1:
            print(animals.rstrip('s'), ':', ocurence)
        else:
            print(animals, ':', ocurence)

attempts = 0
time_start = time.perf_counter()

while True:
    user_attempt = input('Enter a number: ')
    if user_attempt == 'exit':
        exit('Game has been closed')

    splited_users_numbers_set = set()
    splited_user_numbers_list = list()
    hints = {'cows': 0, 'bulls': 0}

    for one_number in user_attempt:
        splited_users_numbers_set.add(one_number)

    error_in_attempt = input_check(user_attempt)

    if error_in_attempt == None:
        attempts += 1
        for one_number in user_attempt:
            splited_user_numbers_list.append(int(one_number))
    
        hints_counter(splited_user_numbers_list,unique_numbers,0)

    else:
        print(error_in_attempt)
        continue
    
    hints.update({'cows': hints['cows'] - hints['bulls']})

    hints_printer(hints.items)

    print('-----------------------------------------------')
    if hints['bulls'] == 4:
        break

time_end = time.perf_counter()
time_value = time_end - time_start
minutes = int(time_value / 60) 
seconds = time_value % 60

attemps_informations = [['Attempts', ' Time'],
                        [attempts, f'{minutes:02}:{round(seconds):02}']]

file_path = 'results.csv'

try:
    with open(file_path, 'r+') as file:
        file.seek(0,2)
        writer = csv.writer(file, delimiter = '\t')
        writer.writerow(attemps_informations[1])
except FileNotFoundError:
    with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter = '\t')
        for row in attemps_informations:
            writer.writerow(row)


print('-----------------------------------------------')
print('---->', number_for_game, '<----')
print("Correct, you've guessed the right number\nin ",len(attempts), " guesses")
print(f'your time: {minutes:02}:{round(seconds):02}')
print('-----------------------------------------------')

