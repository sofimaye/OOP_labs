"""String builder"""



S = "Etymologically, the word science is derived from the Latin word scientia meaning knowledge." \
    "science refers to a systematic and organized body of knowledge"\
    "in any area of inquiry that is acquired using 'the scientific method'."


C = ['word', 'refers', 'systematic', 'organized']



def find_sentences(text): #text is a string; #returns list of strings
    return text.split(".")

print(find_sentences(S))

def sentence_count(sentences, word): #sentences is a list of strings #word is a string  #returns integer
    s = 0
    for sentence in sentences:
        if word in sentence:
            s = s + 1
    return s

def count_word(text, words):  #text is a string #words is a list of strings #returns list
    separate_sentences = find_sentences(text)
    for word in words:
        print(sentence_count(separate_sentences, word), word)

print(count_word(S,C))






