# ===== Question 4 =====

print("\n===== Question 4 =====")

import string

# a) Given paragraph
text = """
Python is a high-level programming language. Python is easy to learn and easy to use.
Python is used for web development, data science, and automation.
"""

# b) Convert to lowercase and remove punctuation
text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

print("\nCleaned Text:")
print(text)

# c) Count word frequency using dictionary and get()

word_frequency = {}

words = text.split()

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")

# d) Print top 5 most frequent words

print("\nTop 5 Most Frequent Words:")

top_words = sorted(
    word_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in top_words[:5]:
    print(f"{word}: {count}")

# e) Print words appearing exactly once

print("\nWords Appearing Exactly Once:")

for word, count in word_frequency.items():
    if count == 1:
        print(word)

# f) Dictionary comprehension for words appearing 2+ times

filtered_dict = {
    word: count
    for word, count in word_frequency.items()
    if count >= 2
}

print("\nWords Appearing 2+ Times:")
print(filtered_dict)
