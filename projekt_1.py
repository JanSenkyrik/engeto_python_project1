"""
projekt_1.py: First project for Engeto Python Academy

author: Jan Senkyrik
email: jansenkyrik@email.cz
discord: Honza Š.#8749
"""

# Define the texts
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
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

delimiter = "-" * 40

# User credentials
credentials = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}


# Get user credentials
username = input('username: ')
password = input('password: ')
print(delimiter)

# Check if user exists and password is correct
if username in credentials and credentials[username] == password:
    print(f'Welcome to the app, {username}')
    print('We have 3 texts to be analyzed.')
    print(delimiter)

    # Get the selected text
    while True:
        selection = input('Enter a number btw. 1 and 3 to select: ')
        if selection.isdigit() and 1 <= int(selection) <= 3:
            selected_text = TEXTS[int(selection) - 1]
            break
        else:
            print('Invalid input. Exiting..')
            exit()

    # Analyze the selected text
    words = selected_text.split()
    word_count = len(words)
    titlecase_words = 0
    uppercase_words = 0
    lowercase_words = 0
    numeric_strings = 0
    numeric_sum = 0
    word_lengths_count = {}

    for word in words:
        if word.istitle():
            titlecase_words += 1
        if word.isupper():
            uppercase_words += 1
        if word.islower():
            lowercase_words += 1
        if word.isnumeric():
            numeric_strings += 1
            numeric_sum += int(word)
        length = len(word.strip('.,'))
        if length in word_lengths_count:
            word_lengths_count[length] += 1
        else:
            word_lengths_count[length] = 1

    # Print the analysis results
    print(f'There are {word_count} words in the selected text.')
    print(f'There are {titlecase_words} titlecase words.')
    print(f'There are {uppercase_words} uppercase words.')
    print(f'There are {lowercase_words} lowercase words.')
    print(f'There are {numeric_strings} numeric strings.')
    print(f'The sum of all the numbers {numeric_sum}')
    print(delimiter)
    print('LEN|     OCCURENCES     |NR.')
    print(delimiter)
    sorted_lengths = sorted(word_lengths_count.keys())
    for length in sorted_lengths:
        count = word_lengths_count[length]
        bar = '*' * count
        print(f'{length:2} |{bar:20}|{count}')


else:
    print(f'Username {username} does not exist or the password is not correct. Exiting..')
    print(delimiter)

