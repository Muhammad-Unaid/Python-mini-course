"""
Write a program that takes a string as input, removes
vowels (a,e,i,o,u) from it and prints the string without 
vowels
"""
# word = input("Enter a word: ")
# new_word = ''

# for i in word:
#     if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
#         continue
#     else:
#         new_word = new_word + i

# print(new_word)

word = input("enter a word: ")
new_word = ''

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in word:
    if i in vowels:
        continue
    else:
        new_word += i

print(new_word)