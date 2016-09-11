'''
Studyer

By: Lucas Hagel
Started 8/29/16

here is a test question and answer simple, word association to make
fake data to test quiz answering subsystems

we only used 1 word answers/"values" because word similarity function blows up
'''

from config import *

fauxQA = {
    "MAC check": "Integrity",
    "Authentication assumes: ": "shared",
    'Authentication': "right",
    "privacy": "insecure",
    "integrity": "content",
    "cryptanalysis": "weaknesses in crypto protocol",
    "confidentiality": "intended",
    "how secure is a crypto": "effort",
    #"breaking encryption: ": "ciphertext-only known-plaintext chosen-plaintext",
    "Why DH instead of all RSA": "forward",
    "Why is mono-alphabet security bad: ": "characteristics",
    "change 1 bit in DES encrypt": "half",
    "weakness in ECB: ": "pattern",
    "IV should known by: ": "both"
}


def doQuiz(q_ad, mode):
    '''
    this is the main controller so to speak,
    :param q_ad:
    :param numDictSample: number from dictionary want to sample
    :param mode: "train" or "test"
    :return: None
    '''

    numQuestions = len(q_ad)
    right =0.0
    datatable = []
    print( "You are in " + mode + " mode.\nIf it's not train or test you ran the function wrong.")
    for question in q_ad.keys():

        correctAnswer = q_ad[question]
        userAnswer = ""
        questionNumber = 1

        #while not QuestionAnswered:
        before = time.time()
        print("Prompt, " + question)
        userAnswer = input("A: ")
        print("Your answer: ", userAnswer)
        # call a answer verify function implementing criteria here
        if userAnswer == correctAnswer: right += 1.0
        after = time.time()
        timeToAnswerQuestion = after - before
        hamDist = hammingDistance(userAnswer, correctAnswer )
        answerSimilarity = wordNetSimilarityTest(userAnswer, correctAnswer)

        '''
        what is that var below for???
        '''
        closeEnoughForGovernmentWork = False

        if q_ad[question] in lemmalist(userAnswer):
            closeEnoughForGovernmentWork = True

        datatable.append( [timeToAnswerQuestion, hamDist, answerSimilarity, closeEnoughForGovernmentWork] )
    #train or test modes
    if mode == "train":
        return datatable[:-1]
    print("test mode, your score is: %s" % (right/numQuestions))
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
    putInQuizResultsInFile( doQuiz(fauxQA)[:-1] )
