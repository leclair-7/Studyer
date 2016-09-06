'''
Studyer

By: Lucas Hagel
Started 8/29/16

Since I'm in school, this is an app to help me study "more effectively"
which is another way of saying "less"

Since this is for a good time with a focus on good, the documentation
has an air of irony or a lack of seriousness, etc.

For now this is a non working app with set of working code parts to be combined once I learn how to use Django,
I may decide not to use it.

Features To Do:
[all of them]

UI
this will be on a Django driven webpage

QUESTION ANSWER HEURISTICS

WAnt the neural network to see the size of the vector and construct itself accordingly,
maybe do a binary search style parameter finding..

we're going to learn to predict the answers based on as many tests as we can think of
these test results will go to a neural network then presumably...
it'll feel pretty accurate

QUIZ
getting close enough to the right answer function
put question answer time in erformance,
when the user doesn't get a close answer, have a hint

    ideas for criteria for answer being right:
        -syntactic distance, 3 words match, hamming distance,
        - then quantify by weighing the criteria, how to make it in sync with
                one's confidence with knowing the material? sense and sensibility

a mode where it gives you more than 1 try, "learning mode"
and a test mode for pressure's sake


REMEMBERING YOUR PAST
take tab spaces words from a txt file and make flashcards

input file:
    -take in either tab spaced
    - word then '-' then definition
    - word then paragraph

Memory 100 peg list helper, make it make crazy associations based on nouns not being on top 10000 english used
but also being syntactically close to current noun and the one associated with the number

ambiguity is an issue though

'''

'''
import time
from gensim.models import Word2Vec

model = Word2Vec.load()
model.similarity('apple', 'orange')
'''

modes = ["wordToDefinition", "definitionToWord", "createRelation"]
mode = "wordToDefinition"
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

    '''
    w1 = 'boat'
    w2 = 'frog'
    w3 = 'cat'
    w4 = 'boat'

    s1 = wn.synsets(w1)
    s2 = wn.synsets(w2)
    s3 = wn.synsets(w3)
    s4 = wn.synsets(w4)

    now = time.time()
    ss1 = s1[0]
    ss2 = s2[0]
    ss3 = s3[0]
    ss4 = s4[0]

    print( ss1.path_similarity(ss2) )
    print( ss1.path_similarity(ss4) )
    #time here in testing is more of a runtime bad news getter
    # i.e. it's damn slow for our purpose
    print("Elapsed time: " + "%.02f" % (time.time() - now ) )
    '''
    s1 = wn.synsets(userAnswer)
    s2 = wn.synsets(correctAnswer)
    ss1 = s1[0]
    ss2 = s2[0]
    return ss1.path_similarity(ss2)


#################################################################


def lemmalist(str):
    syn_set = []
    for synset in wn.synsets(str):
        for item in synset.lemma_names():
            syn_set.append(item)
    return syn_set


'''
curr = time.time()
print(lemmalist("brain"))
print("Yeah it took " + "%.02f" % (time.time() - curr) + " seconds.")
import sys
sys.exit()
print("mambo number 5")
'''

'''
It is good practice to use the with keyword when dealing with file objects. This has the advantage that the file is
properly closed after its suite finishes, even if an exception is raised on the way. It is also much shorter than
writing equivalent try-finally blocks

Idea: to somehow take memory of last session's progress and use that logic to choose questions for this one
'''

# with open('workfile', 'r') as f:
#    for line in f:

'''

here is a test question and answer simple, word association to make
fake data to test subsystems

but make real questions!!!
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
        '''
        this block does 1 question
        '''

        correctAnswer = q_ad[question]
        userAnswer = ""
        #QuestionAnswered = False
        questionNumber = 1

        #while not QuestionAnswered:
        before = time.time()
        print("Prompt: " + question)
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
    # under here is a list of functions for the test indicator
    '''
    def wordNetSimilarityTest(userAnswer, correctAnswer ):
    hammingDistance( userAnswer, correctAnswer  )
    lemmalist("brain")
    '''
    putInQuizResultsInFile(doQuiz(fauxQA) )
