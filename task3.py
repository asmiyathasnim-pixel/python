# Sentence Checker 
# Write a program that takes a sentence from the user. 
# The program should show a small part of the sentence. 
# It should also check whether a given word is present in the sentence and print a message.

a = input('Write a sentence:')
print(a[:6])


word = input('Enter the word: ')
if word in a:
    print(f'the word {word} is present in this sentence')

else:
    print(f'the word {word} is not present in this sentence')