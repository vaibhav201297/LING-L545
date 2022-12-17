from nltk.tokenize import sent_tokenize
import nltk.data
import sys
text= sys.stdin.read()

#
# Get the sentences using NLTK
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentences= sent_detector.tokenize(text.strip())
print(sentences)
print(len(sentences))
# Print each sentence in List



