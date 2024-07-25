def is_greater_than_5(numbers: list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''
    return [num > 5 for num in numbers]

def filter_less_than_5(numbers: list) -> list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''
    return [num for num in numbers if num < 5]

def sum_of_two_digit_numbers(numbers: list):
    '''Given a list of numbers find the sum of all two_digit_numbers.'''
    return sum(num for num in numbers if 10 <= num <= 99)

def is_all_has_a(words: list) -> bool:
    '''Given a list of words check if all words has the letter a(case insensitive) in it.'''
    return all('a' in word.lower() for word in words)

def print_with_numbering(items): 
    '''
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    '''
    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")

def make_dict(keys, values):
    '''Create a dict with keys and values'''
    return dict(zip(keys, values))

def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).'''
    return [i for i, word in enumerate(words) if len(word) > 5]

def decode_rle(chars: str, repeats: list) -> str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 
    Note rle refers to Run-length encoding
    '''
    return ''.join(char * repeat for char, repeat in zip(chars, repeats))