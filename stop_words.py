from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

worf_quote = "Sir, I protest. I am not a merry man!"

word_in_quote = word_tokenize(worf_quote)
print(word_in_quote)

stop_words = set(stopwords.words("english"))

filtered_list = []

for word in word_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

print(filtered_list)