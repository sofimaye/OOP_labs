"""модифікувати лабораторну роботу 3"""

class Text: #масив речень
    def __init__(self, sentences): #sentences is a list of Sentence
        self.sentences = sentences



class Sentence: #масив слів і розділових знаків
    def __init__(self, word_and_punc): #words_and_punc is a list of Word or Punctuation
        self.word_and_punc = word_and_punc

    def __repr__(self):
        return str(self.word_and_punc)


class Word: #масив літер
    def __init__(self, word): #word is a string
        self.word = word

    def __repr__(self):
        return str(self.word)

    def __eq__(self, other):
        return self.word == other

class Punctuation: #список розділових знаків
    def __init__(self, punctuation):  #punctuation is a string
        self.punctuation = punctuation

    def __repr__(self):
        return str(self.punctuation)

    def __eq__(self, other):
        return self.punctuation == other

# S = "Etymologically, the word science is derived from the Latin word scientia meaning knowledge." \
#     "science refers to a systematic and organized body of knowledge"\
#     " in any area of inquiry that is acquired using 'the scientific method'."
#
# C = ['word', 'refers', 'systematic', 'organized']

text = Text(
    [
        Sentence(
            [
                Word('Etymologically'),
                Punctuation(','),
                Word('the'),
                Word('science'),
                Word('is'),
                Word('derived'),
                Word('from'),
                Word('the'),
                Word('Latin'),
                Word('word'),
                Word('scientia'),
                Word('meaning'),
                Word('knowledge'),
                Punctuation('.')
            ]
        ),
        Sentence(
            [
                Word('science'),
                Word('refers'),
                Word('to'),
                Word('a'),
                Word('systematic'),
                Word('and'),
                Word('organized'),
                Word('body'),
                Word('of'),
                Word('knowledge'),
                Punctuation('.')
            ]
        )
    ]
)  # Text
words = [Word('word'), Word('refers'), Word('systematic'), Word('organized')] # list of Word


def sentences_count(text, word): #text is a Text #word is a Word
    sent_count = 0
    for sentence in text.sentences:
        if word in sentence.word_and_punc:
            sent_count = sent_count + 1
    return sent_count


for word in words:
    print(word, sentences_count(text, word))


