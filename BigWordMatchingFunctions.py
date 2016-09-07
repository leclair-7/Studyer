import nltk
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

def getNounsAndVerbs(answer):
    text = nltk.word_tokenize(answer)
    noun_list = []
    verb_list = []
    for i in nltk.pos_tag(answer):
        # print(i)
        if i[1] in ['NN', 'NNP', 'NNPS', 'NNS']:
            noun_list.append(i[0])
        elif i[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            verb_list.append(i[0])
    return (noun_list, verb_list)

def aSentenceMatchIdea(userAnswer, solution):
    n,v = getNounsAndVerbs(userAnswer)
    nSyns = [lemmalist(i) for i in n]
    vSyns = [lemmalist(i) for i in v]

    numNoun = len(n)
    numVerb = len(v)


    n_Syn,v_Syn= getNounsAndVerbs(solution)
    soln_nSyns = [lemmalist(i) for i in n_Syn]
    soln_vSyns = [lemmalist(i) for i in v_Syn]

    noun_close = 0
    verb_close = 0

    for i in n:
        if i in soln_nSyns:
            noun_close += 1
    for i in v:
        if i in soln_vSyns:
            verb_close += 1



if __name__ == '__main__':
    pass
