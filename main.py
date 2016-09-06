'''
Studyer

By: Lucas Hagel
Started 8/29/16

ideas on what to do next:
POS tag the sentence and see if any of answer's noun is in lemmalist
PEG 100 list implement an all numerical metrics flashcard learning
session by session pickling remembering, cpickle for speed
feed it a notes file then it gives learning, diaplaying pictues on django site,
unit tests for every function, code coverage
learn Django and put an SSH to Alderon login
find a thesaurus for hints, like dict = {word : [synonyms] }
learning mode and test mode and an easy switch between them


Since I'm in school, this is an app to help me study "more effectively"
which is another way of saying "less"

Since this project is for a good time with a focus on good, the documentation
has an air of irony or a lack of seriousness, etc.

For now this is a non working app with set of working code parts
to be combined once I learn how to use Django,
I may decide not to use it.

Features To Do:
[all of them]

TESTING
extensive - unit test modules

UI
this will be on a Django driven webpage

QUESTION ANSWER HEURISTICS

Want the neural network to see the size of the vector and construct itself accordingly,
maybe do a binary search style parameter finding..

we're going to learn to predict the answers based on as many tests as we can think of
these test results will go to a neural network then presumably...
it'll feel pretty accurate to me the user

QUIZ
getting close enough to the right answer function
put question answer time in performance,
when the user doesn't get a close answer, have a hint

    ideas for criteria for answer being right:
        -quantify by weighing the criteria: sync with
                one's confidence of mastery of material

a mode where it gives you more than 1 try, "learning mode"
and a test mode for pressure's sake

f it  -A A

REMEMBERING YOUR PAST
take tab spaces words from a txt file and make flashcards

Memory 100 peg list helper, make it make crazy associations based on nouns not being on top 10000 english used
but also being syntactically close to current noun and the one associated with the number

ambiguity is an issue though
'''

questionAnswerDict = {"route flapping": "neighbors to switch to new routes and advertise them to their neighbor",
                      "BGP Wedgie": "ability of Charlie to force a BGP session reset can allow the configuration" + \
                                    " of Alice or Bob to transition into a stable but undesired forwarding state"}

# a first step to question answering logic
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

'''
here is a test question and answer simple, word association to make
fake data to test quiz answering subsystems

we only used 1 word things because word similarity function blows up
'''
fauxQA = {
    "MAC check": "Integrity",
    "Authentication assumes: ": "shared",
    'Authentication': "right",
    "privacy": "insecure",
    "integrity": "content",
    "cryptanalysis": "weaknesses",
    "confidentiality": "intended",
    "how secure is a crypto": "effort",
    #"breaking encryption: ": "ciphertext-only known-plaintext chosen-plaintext",
    "Why DH instead of all RSA": "forward",
    "Why is mono-alphabet security bad: ": "characteristics",
    "change 1 bit in DES encrypt": "half",
    "weakness in ECB: ": "pattern",
    "IV should known by: ": "both"
}


def doQuiz(q_ad):
    '''
    this is the main controller so to speak,
    and no logic,
    madness before method

    :param q_ad:
    :return: None
    '''

    datatable = []
    for question in q_ad.keys():

        correctAnswer = q_ad[question]
        userAnswer = ""
        #QuestionAnswered = False
        questionNumber = 1

        #while not QuestionAnswered:
        before = time.time()
        print("Prompt, " + question)
        userAnswer = input("A: ")

        # call a answer verify function implementing criteria here

        after = time.time()
        timeToAnswerQuestion = after - before
        hamDist = hammingDistance(userAnswer, correctAnswer )
        answerSimilarity = wordNetSimilarityTest(userAnswer, correctAnswer)

        closeEnoughForGovernmentWork = False

        if q_ad[question] in lemmalist(userAnswer):
            closeEnoughForGovernmentWork = True

        datatable.append( [timeToAnswerQuestion, hamDist, answerSimilarity, closeEnoughForGovernmentWork] )
    return datatable

def putInQuizResultsInFile( datatable ):
    '''

    :param datatable: these are user generated quiz results to be put in  a
     file to use later (serializing may be better
    :return: not sure
    '''

    with open("dataPoints.txt", 'w') as ofo:
        for dataPoint in datatable:
            for thing in dataPoint:
                ofo.write(str(thing) + '\t')
            ofo.write('\n')


if __name__ == '__main__':
    '''
    #Test indicators
    wordNetSimilarityTest(userAnswer, correctAnswer ):
    hammingDistance( userAnswer, correctAnswer  )
    lemmalist("brain")
    '''
    putInQuizResultsInFile( doQuiz(fauxQA) )
