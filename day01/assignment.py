sentence = input("Enter the sentence: ")


num_characters = len(sentence)
print("Number of characters:", num_characters)


words = sentence.split()
num_words = len(words)
print("Number of words:", num_words)


vowels = "aeiouAEIOU"
num_vowels = 0

for ch in sentence:
    if ch in vowels:
        num_vowels += 1

print("Number of vowels:", num_vowels)
