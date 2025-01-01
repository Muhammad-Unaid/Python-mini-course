# """
# Write a program that takes a string as input
# and removes all the consonants from it
# """

# word = input("enter a word: ")
# new_word = ''

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# for i in word:
#     if i in vowels:
#         new_word += i
#     else:
#         continue

# print(new_word)


"""
Write a program that takes an input and removes 
the digits (0 to 9) from it
"""
input_string = input("Enter a string input: ")
output_string = ''
digits = ['0','1','2','3','4','5','6','7','8','9']

for i in input_string:
    if i not in digits:
        output_string += i

print(output_string)


