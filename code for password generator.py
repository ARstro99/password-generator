import random
import array
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

max_len = 12

numbers = []
for number in digits:
    numbers.append(number)

ascii_lower_case = []
for lower_case in ascii_lowercase:
    ascii_lower_case.append(lower_case)
 
ascii_upper_case = []
for upper_case in ascii_uppercase:
    ascii_upper_case.append(upper_case)

symbols = []
for signs in punctuation:
    symbols.append(signs)

combined_lists = numbers + ascii_lower_case + ascii_upper_case + symbols

rand_digits = random.choice(numbers)
rand_upper = random.choice(ascii_upper_case)
rand_lower = random.choice(ascii_lower_case)
rand_symbol = random.choice(symbols)

temp_pass = rand_digits + rand_upper + rand_lower + rand_symbol

for x in range(max_len - 4):
    temp_pass = temp_pass + random.choice(combiined_lists)
    
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ''
for x in temp_pass_list:
    password = password + x
print(password)
