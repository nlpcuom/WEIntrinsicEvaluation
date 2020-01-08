from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

import codecs

# First Step. You need to remove special characters and garbage characters from the corpus.
# Used a Sinhala tokenizer available in https://github.com/ysenarath/sinling with several modifications. See in singling folder

if __name__ == '__main__':
    f = codecs.open("D:/NLP/Corpus/wikipedia.si_filtered", encoding='utf-8', errors='ignore') # open source file
    f_w = codecs.open("wikipedia.si_filtered_tokenized.txt", 'w', 'utf-8')  # write to this file after processing

    tokenizer = SinhalaTweetTokenizer()
    docs = []
    i = 0
    for line in f:
        docs.append(line)

    for doc in docs:
        for sent in tokenizer.split_sentences(doc):
            tokens = tokenizer.tokenize(sent)
            line = " ".join(tokens)
            line = line + "\n"
            f_w.write(line)

f.close()
f_w.close()