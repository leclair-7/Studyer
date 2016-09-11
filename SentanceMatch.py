
'''
Sentence Matcher function



'''
import gensim
from gensim import corpora
import os
from nltk.corpus import brown
import numpy as np
from scipy import spatial
from nltk.corpus import stopwords
'''
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
'''
def avg_feature_vector(words, model, num_features, index2word_set):
    # function to average all words vectors in  the sentence
    featureVec = np.zeros((num_features,), dtype="float32")
    nwords = 0

    # list containing names of words in the vocabulary
    for word in words:
        if word in index2word_set:
            nwords = nwords + 1
            featureVec = np.add(featureVec, model[word])

    if nwords > 0:
        featureVec = np.divide(featureVec, nwords)

    # print(featureVec[:10], featureVec.shape, np.zeros( (numpy), dtype="float32").shape)
    return featureVec

def getSentenceSimilarity(sentence_1, sentence_2):
    sentence_1 = " ".join([word for word in sentence_1.lower().split() if word not in stopwords.words('english')])
    sentence_2 = " ".join([word for word in sentence_2.lower().split() if word not in stopwords.words('english')])

    if os.path.exists("The_Brown_Model_For_Studyer"):
        #dictionary = corpora.Dictionary.load('deerwester.dict')
        model_w2v = gensim.models.Word2Vec.load('The_Brown_Model_For_Studyer')
        print("Used previously calculated model!!")
    else:
        sentences = brown.sents()
        model_w2v = gensim.models.Word2Vec(sentences, min_count=1)
        model_w2v.save('The_Brown_Model_For_Studyer')
    PARAM_index2word = set(model_w2v.index2word)

    sentence_1_avg_vector = avg_feature_vector(sentence_1.split(), model=model_w2v, num_features=100,
                                               index2word_set=PARAM_index2word)
    sentence_2_avg_vector = avg_feature_vector(sentence_2.split(), model=model_w2v, num_features=100,
                                               index2word_set=PARAM_index2word)

    sen1_sen2_similarity = 1 - spatial.distance.cosine(sentence_1_avg_vector, sentence_2_avg_vector)
    return sen1_sen2_similarity


if __name__=='__main__':
    sentence_1 = "entropy of the code"
    sentence_2 = "scramble the bits"
    print( getSentenceSimilarity(sentence_1, sentence_2))