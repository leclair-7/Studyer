from config import *

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

def makeHint(text):
    '''
    :param text: the inputted answer to the question
    :return: string: a sentence with nouns and verbs replaced by synonyms if available
    '''
    answer = nltk.word_tokenize(text)
    tags = nltk.pos_tag(answer)

    for i in range(len(tags)):
        if tags[i][1] in ['NN', 'NNP', 'NNPS', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            synonyms = lemmalist(tags[i][0])
            for maybeDiff in synonyms:

                if maybeDiff != tags[i][0]:
                    tags[i] = (maybeDiff, tags[i][1])
                    break
    h = []
    for i in tags:
        h.append(i[0])
    return " ".join(h)

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

def makeSentenceHint(phrase):
    '''
    a function to output a sentence with some synonyms replacing the prompt
    for quiz hints
    '''
    if phrase.split() <= 1:
        return phrase

    synonyms =""
    for i in nltk.pos_tag(phrase):
        if i[1] in ['NN', 'NNP', 'NNPS', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            synonyms = wn.synsets(i[0])


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

    # random phrase with proper nouns and honest prose
    print(makeHint("Lucas said Kimberly is sublime"))
