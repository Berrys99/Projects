"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Beránek
email: tomas.malehorky@seznam.cz
discord: Tomáš B. Berrys#6258
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrated_users = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'
}
print('Welcome in the text analyzator program, to continue please')

logged_username = input('type your registrated username: ')
    
for names in registrated_users.keys():
    if logged_username in names:
        login = logged_username
        logged_password = input('type your registrated password: ')
        if logged_password == registrated_users[login]:
            print('---------------------------')
            break
        else:
            exit('wrong password, terminating the program..')
    else:
        continue

if logged_username not in names:
    exit('unregistered user, terminating the program..')

print('Welcome to the app', (logged_username))

print('We have 3 text to be analyzed.')
print('---------------------------')
selected_text_index = input('Enter a number btw. 1 and 3 to select: ')
print('---------------------------')

if selected_text_index.isnumeric():
    selected_text_index = int(selected_text_index)
    if selected_text_index < 1 or selected_text_index > 3:
        exit('out of range, terminating program..')    
else:
    exit('unsupported character, terminating program..')

selected_text = TEXTS[selected_text_index - 1] 

prepared_text = list()
selected_text = selected_text.replace(',', ' ').replace('.', ' ').replace("-", " ").replace("\n", " ")
selected_text = selected_text.split(" ")

for word in selected_text:
    if word.isalnum():
        prepared_text.append(word)

numbers = list()

word_type_map = {'num_of_words': len(prepared_text),
                 'num_of_titlecase_words': 0,
                 'num_of_uppercase_words': 0,
                 'num_of_lowercase_words': 0,
                 'num_of_numeric_strings': 0}

for word in prepared_text:
    if word.istitle():
        word_type_map.update({'num_of_titlecase_words': word_type_map ['num_of_titlecase_words'] + 1})
    elif word.isupper() and word.isalpha():
        word_type_map.update({'num_of_uppercase_words': word_type_map ['num_of_uppercase_words'] + 1})
    elif word.islower():
        word_type_map.update({'num_of_lowercase_words': word_type_map ['num_of_lowercase_words'] + 1})
    elif word.isnumeric():
        word_type_map.update({'num_of_numeric_strings': word_type_map ['num_of_numeric_strings'] + 1})
        numbers.append(int(word))

sum_of_all_the_numbers = sum(numbers)

word_letter_count_map = {}

for word in prepared_text:
    word_length = len(word)
    if word_length not in word_letter_count_map:
        word_letter_count_map.update({word_length: 0})
    word_letter_count_map.update({word_length: word_letter_count_map[word_length] + 1})

sorted_word_letter_count_map = dict(sorted(word_letter_count_map.items()))

for word_types, occurrence in word_type_map.items():
    word_types = word_types.replace('_', ' ').replace('num of', '')
    if occurrence == 1:
        print('There is ', f'{occurrence:2}', word_types.rstrip('s'))
    else:
        print('There are', f'{occurrence:2}', word_types)

print('The sum of all the numbers', sum_of_all_the_numbers)

print('----------------------------------------')
print(f'{'LEN|' : <10}' + f'{'OCCURENCES' : ^10}' + f'{'|NR.': >10}' )
print('----------------------------------------')

for lenght, number_of_ocur in sorted_word_letter_count_map.items():
    print(f'{lenght:3}''|' f'{'*'* number_of_ocur:21}', '|', number_of_ocur)
