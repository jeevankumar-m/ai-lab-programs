import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "Natural Language Processing is a branch of Artificial Intelligence."
text = text.lower()

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words
                  if word.isalpha() and word not in stop_words]

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("Original Text:", text)
print("Tokens:", words)
print("After Stop Word Removal:", filtered_words)
print("After Stemming:", stemmed_words)