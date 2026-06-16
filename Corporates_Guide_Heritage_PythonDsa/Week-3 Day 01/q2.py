text = "python is easy and python is powerful"

words = text.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Expected Output
print(word_freq)