'''
Studyer

By: Lucas Hagel
Started 8/29/16

Since I'm in school, this is an app to help me study more effectively
which is another word for less

For now this is a non working app with set of working code parts to be combined once I learn how to use Django, I may decide not to use it.


Features To Do:
[all of them]

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
import hammmingDistance
import timeQuestionAnswering

def wordNetSimilarityTest():
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
    print("Elapsed time: " + "%.02f" % (time.time() - now ) )

#################################################################


def lemmalist(str):
    syn_set = []
    for synset in wn.synsets(str):
        for item in synset.lemma_names():
            syn_set.append(item)
    return syn_set

curr = time.time()
print( lemmalist("brain") )
print("Yeah it took " + "%.02f" % (time.time() - curr) + " seconds.")


'''
It is good practice to use the with keyword when dealing with file objects. This has the advantage that the file is
properly closed after its suite finishes, even if an exception is raised on the way. It is also much shorter than
writing equivalent try-finally blocks

Idea: to somehow take memory of last session's progress and use that logic to choose questions for this one
'''

#with open('workfile', 'r') as f:
#    for line in f:


def doQuiz(questionAnswerDict):
    '''
    this is the main controller so to speak, although right now it's a motley of things
    and no logic,
    madness before method

    :param questionAnswerDict:
    :return: None
    '''
    for question in questionAnswerDict.keys():
        '''
        this block does 1 question
        '''
        apprenticeIn = ""
        QuestionAnswered = False
        questionNumber = 1

        #print("pre Answer now: " + "%.02f" % now)
        while not QuestionAnswered:
            now = time.time()
            print("Prompt: " + question)
            apprenticeIn = input("A: ")

            # call a answer verify function implementing criteria here
            if apprenticeIn == questionAnswerDict[question]:
                print("Right " + "%.02f" % now)

            aSecondTime = time.time()
            print("It toook " + "%.02f" % (aSecondTime-now) + " to enter the answer")



if __name__=='__main__':
    wordNetSimilarityTest()
