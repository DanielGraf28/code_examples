# Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.

import math
r = float(input("Enter radian: "))
converted_amount = r*180/math.pi
print(converted_amount)

# Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.

def sorted_numbers(numbers, order):
  if order == 'asc':
    return sorted(numbers)
  elif order == ' desc':
    return sorted(numbers, reverse=True)
  elif order == 'none':
    return numbers
  else:
    print('Invalid parameter entered')
  print(numbers)

# Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.

number = int(input('Enter a number '))
if number < 1024:
  print(bin(number))

# Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.

def vowel_counter(word):
  vowels = 'aeiouAEIOU'
  return sum(1 for char in word if char in vowels)
word = input('Enter word here ')
num_vowels = vowel_counter(word)
print('Number of vowels in ', word,' ',num_vowels)

# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent “4444444444444444”, then it should return “4444”.

def hide_card_num(nums):
  hid_nums = '*' * (len(nums)-4)
  show_nums = nums[-4:]
  return hid_nums + show_nums
nums = input('Enter credit card number ')
hide_card_num(nums)

# Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. It should then return a boolean value of either True or False.
# If the count of Xs and Os are equal, then the function should return True. If the count isn’t the same, it should return False. If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.

def count_xo(string):
  xs = string.lower().count('x')
  os = string.lower().count('o')
  return xs == os
string = input('Enter a string here ')
count_xo(string)

# Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.
# The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.

def calculator(int_1, func, int_2):
  if func == '+':
    ans = int_1 + int_2
    return ans
  elif func == '-':
    ans = int_1 - int_2
    return ans
  elif func == '/':
    ans = int_1 / int_2
    return ans
  elif func == '*':
    ans = int_1 * int_2
    return ans
int_1 = int(input('Enter integer '))
int_2 = int(input('Enter integer '))
func = input('Enter function ')
calculator(int_1, func, int_2)

# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def sale_price(price, discount):
  dis = discount / 100
  sale = 1 - dis
  new_price = price * sale
  return new_price
price = int(input('Enter full price '))
discount = (float(input('Enter percentage off ')))
sale_price(price, discount)

# Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.

def int_extractor(list):
  new_list = [item for item in list if item.isdigit()]
list = []
while True:
  item = input('Enter item of list. When done enter done ')
  list.append(item)
  if item.lower() == 'done':
    break
print(list)
int_extractor(list)

# Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.

def double_characters(string):
    double_string = ' '
    for char in string:
        double_string += char* 2
    return double_string
print(double_characters('hello'))
