import nltk, re 
from nltk.corpus import stopwords 

def extractWord(line): 
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)

    return tokens  

def classify(tokens): 
    descriptions = [] 
    names = []
    for t in tokens: 
        if t.startswith('('): 
            description = t.strip()
            descriptions.append(t)
        else: 
            name = t 
            names.append(t)
    return (names, descriptions)


if __name__ == "main": 
    with open("output.txt", "r") as file: 
         file_read = [line.strip() for line in file if line.strip()] 

    for line in file_read[0:5]:
        classify(extractWord(line))    