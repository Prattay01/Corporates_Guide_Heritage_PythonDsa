# ===== Question 6 =====

print("\n===== Question 6 =====")

import string

# a) Define two paragraphs

paragraph1 = """
Python is a popular programming language. It is widely used for web development,
data analysis, automation, and machine learning. Python has a simple syntax and
a large community of developers.
"""

paragraph2 = """
Machine learning and data science often use Python. Python provides many useful
libraries for automation and analysis. Developers enjoy Python because it is
easy to learn and powerful.
"""

# b) Function to tokenize text and return unique lowercase words

def tokenize(text):
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, "")

    return set(text.split())

# Create sets of unique words

words1 = tokenize(paragraph1)
words2 = tokenize(paragraph2)

print("\nUnique Words in Paragraph 1:")
print(words1)

print("\nUnique Words in Paragraph 2:")
print(words2)

# c) Set Operations

print("\nWords Appearing in BOTH Paragraphs:")
print(words1.intersection(words2))

print("\nWords ONLY in Paragraph 1:")
print(words1.difference(words2))

print("\nWords ONLY in Paragraph 2:")
print(words2.difference(words1))

print("\nAll Unique Words Across Both Paragraphs:")
print(words1.union(words2))

print("\nWords in One Paragraph but Not the Other:")
print(words1.symmetric_difference(words2))

# d) Function to find common letters between two words

def common_letters(word1, word2):
    return set(word1.lower()).intersection(set(word2.lower()))

print("\nCommon Letters Examples:")

print("python & programming:")
print(common_letters("python", "programming"))

print("data & database:")
print(common_letters("data", "database"))

print("science & machine:")
print(common_letters("science", "machine"))

# e) Find the 5 most common words across both paragraphs

combined_text = paragraph1 + " " + paragraph2

combined_text = combined_text.lower()

for char in string.punctuation:
    combined_text = combined_text.replace(char, "")

frequency = {}

for word in combined_text.split():
    frequency[word] = frequency.get(word, 0) + 1

top_5 = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)[:5]

print("\nTop 5 Most Common Words:")

for word, count in top_5:
    print(f"{word}: {count}")
    
    



