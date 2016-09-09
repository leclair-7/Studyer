import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
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

def getNounsAndVerbs(text):
    answer = nltk.word_tokenize(text)
    noun_list = []
    verb_list = []

    for i in nltk.pos_tag(answer):
        # print(i)
        if i[1] in ['NN', 'NNP', 'NNPS', 'NNS']:
            noun_list.append(i[0])
        elif i[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            verb_list.append(i[0])
    return noun_list, verb_list

def aSentenceMatchIdea(userAnswer, solution):
    # nouns and verbs from user, check if against
    # a first step for a sentence matcher heuristic
    # because language is complex
    n, v = getNounsAndVerbs(userAnswer)
    soln_nSyns, soln_vSyns = getNounsAndVerbs(solution)

    wordnet_lemmatizer = WordNetLemmatizer()
    soln_nSyns = [wordnet_lemmatizer.lemmatize(j) for j in soln_nSyns]
    soln_vSyns = [wordnet_lemmatizer.lemmatize(k) for k in soln_vSyns]
    n = [wordnet_lemmatizer.lemmatize(i) for i in n]
    v = [wordnet_lemmatizer.lemmatize(i) for i in v]

    noun_close = 0
    verb_close = 0
    for i in n:
        if i in soln_nSyns:
            noun_close += 1
    for i in v:
        if i in soln_vSyns:
            verb_close += 1

    endNoun = 1.0 * noun_close / (1.0 * len(n)) if len(n) > 0 else 0
    endVerb = 1.0 * verb_close / (1.0 * len(v)) if len(v) > 0 else 0

    return [endNoun, endVerb]

if __name__ == '__main__':
    print(aSentenceMatchIdea("stones and rocks", "rocks men at the grill"))
