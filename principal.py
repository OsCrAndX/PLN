from nltk.tokenize import sent_tokenize, word_tokenize

example_string = "Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."

sentence_tokenize = sent_tokenize(example_string)

words_tokenize = word_tokenize(example_string)

print(words_tokenize)
print(f"The number of tokenized words are: {len(words_tokenize)}")
print(sentence_tokenize)
print(f"The number of sentences tokenized are: {len(sentence_tokenize)}")