First we preprocess Common Crawl Dataset to remove numbers, short sentences and special characters. This repo also includes code to remove stop words.

Then we train three types of word embedding models;
  1) Word2Vec
  2) Glove
  3) FastText
  
Preprocessed Data can be found via https://drive.google.com/drive/folders/1lb4-eAr1rpFFGg_rk_djPCCVYiOpY6Hi?usp=sharing

Trained Models (300 dimensions) can be found via https://drive.google.com/drive/folders/1VD8J-zYix3mD31jbIBhqK2fke-VFLD5P?usp=sharing

Also, this repo contains source code and datasets to two types of intrinsic evalaution;
  1) Analogy Evaluation
  2) Relatedness Evaluation
  
You can follow the steps below to do the evaluation.

Preprocessing Steps

* Run tokenizer.py. Put source file consists of Sinhala Corpus as input. Output will be a file consists of sentences in each line.

* Process the output file of the first step using remove_numeric_lines.py, remove_short_sentenes.py. If you want to train embedding models without stop words, use remove_stop_words.py to remove them from the corpus. It will remove predefined stop words included in “stop words.txt” file. You can add, remove or modify those stop words if you want.

Training Steps

* Train word2vec using wor2vec_train.py (Change ‘sg’ hyperparameter to select between CBOW and Skipgram)
* Train fasttext using fasttext_train.py
* Train glove using glove_train.py

Intrinsic Evaluation

* For word2vec and fasttext models, use analogy_evaluation_word2vec_fasttext.py for analogy evaluation.
* For glove models, use analogy_evaluation_glove.py for analogy evaluation.
* For relatedness evaluation, use relatedness_measure_fasttext.py, relatedness_measure_glove.py and relatedness_meausre_word2vec.py

Extrinsic Evaluation

* Sentiment Analysis for Sinhala can be conducted as desicribed in https://github.com/theisuru/sentiment-tagger

* POS tagging can be performed based on https://github.com/wantinghuang/tensorflow-lstmcrf-postagger. This repo contains preprocessed POS tag data set which was used for POS tagging evaluation task.



