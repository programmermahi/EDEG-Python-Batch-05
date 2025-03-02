sentence = input("Enter a sentence: ")
num_characters = len(sentence)
print(f"Total number of characters: {num_characters}")

if not sentence.isupper():
    sentence = sentence.upper()
    print("Converted to uppercase:")
print(sentence)
