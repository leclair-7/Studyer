from nltk.corpus import wordnet as wn
import time
from hammmingDistance import *
import timeQuestionAnswering

def wordNetSimilarityTest(userAnswer, correctAnswer):
    assert userAnswer != "", "empty user answer"
    assert correctAnswer != "", "Empty right answer, which is ironic"

    s1 = wn.synsets(userAnswer)
    s2 = wn.synsets(correctAnswer)
    ss1 = s1[0]
    ss2 = s2[0]

    if ss1.path_similarity(ss2) == None: return 0

    return ss1.path_similarity(ss2)

#################################################################

def lemmalist(str):
    syn_set = []
    for synset in wn.synsets(str):
        for item in synset.lemma_names():
            syn_set.append(item)
    return syn_set

#################################################################

