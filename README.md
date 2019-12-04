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
  
Sentiment Analysis for Sinhala can be conducted as desicribed in https://github.com/theisuru/sentiment-tagger

POS tagging can be performed based on https://github.com/wantinghuang/tensorflow-lstmcrf-postagger. This repo contains preprocessed POS tag data set which was used for POS tagging evaluation task.

