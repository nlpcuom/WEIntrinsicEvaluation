from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

import codecs

if __name__ == '__main__':
    f = codecs.open("D:/NLP/Corpus/wikipedia.si_filtered", encoding='utf-8', errors='ignore')
    f_w = codecs.open("wikipedia.si_filtered_tokenized.txt", 'w', 'utf-8')

    tokenizer = SinhalaTweetTokenizer()
    docs = []
    i = 0
    for line in f:
        # i += 1
        # if(i<5000000):
        #     continue

        docs.append(line)
        # if(i>6000000):
        #     break

    for doc in docs:
        for sent in tokenizer.split_sentences(doc):
            tokens = tokenizer.tokenize(sent)
            line = " ".join(tokens)
            line = line + "\n"
            f_w.write(line)

f.close()
f_w.close()