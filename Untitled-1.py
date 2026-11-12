paragraph = input("Enter a paragraph: ")

paragraph = paragraph.lower()

for char in ",.!":
    paragraph = paragraph.replace(char, "")

words = paragraph.split()

total_words = len(words)

unique_words = set(words)

unique_count = len(unique_words)

repeated_words = sorted(set(word for word in words if words.count(word) > 1))

print("Total words:", total_words)
print("Unique words:", unique_count)
print("Repeated words:", repeated_words)

print("Unique words alphabetically:")

for word in sorted(unique_words):
    print(word)