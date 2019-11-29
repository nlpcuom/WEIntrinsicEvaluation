import os

import gensim.models.fasttext as fasttext

import numpy as np


model = fasttext.FastText.load("trained_fasttext_100/fasttext_100.w2v")
print(np.copy(model.wv['වැනි']))


