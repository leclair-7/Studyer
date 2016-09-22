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

}

''' because self testing the fauxQA was taking too damn long

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
'''


def doQuiz(q_ad, mode):
    '''
    this is the main controller so to speak,
    :param q_ad:
    :param numDictSample: number from dictionary want to sample
    :param mode: "train" or "test"
    :return: None
    '''
    mode = mode.lower()
    numQuestions = len(q_ad)
    right =0.0
    datatable = []
    print( "You are in " + mode + " mode.\nIf you put something other than train or test you ran the function wrong.")
    print("However, test will test, and train or any other crap you inputted will train")
    for question in q_ad.keys():

        correctAnswer = q_ad[question]
        userAnswer = ""
        questionNumber = 1

        #while not QuestionAnswered:
        before = time.time()
        print("Prompt, " + question)
        userAnswer = input("A: ")
        userAnswer,correctAnswer = userAnswer.lower(), correctAnswer.lower()
        #print("Your answer: ", userAnswer)
        # call a answer verify function implementing criteria here
        if userAnswer == correctAnswer: right += 1.0
        after = time.time()
        timeToAnswerQuestion = after - before
        hamDist = hammingDistance(userAnswer, correctAnswer )

        #answerSimilarity = wordNetSimilarityTest(userAnswer, correctAnswer)
        answerSimilarity = getSentenceSimilarity(userAnswer, correctAnswer)

        '''
        what is that var below for???
        '''
        closeEnoughForGovernmentWork = False

        if q_ad[question] in lemmalist(userAnswer):
            closeEnoughForGovernmentWork = True

        datatable.append( [timeToAnswerQuestion, hamDist, answerSimilarity, closeEnoughForGovernmentWork] )
    #train or test modes
    if mode != "test":
        return datatable[:-1]
    print("Your score is: %s" % (right/numQuestions))
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

def putQuizResultsInDbForUser(datatable):
    import sqlite3
    conn = sqlite3.connect('UserQuizHist.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE UserHistory
                 (timeToAnsQuestion REAL, HammDist REAL, SentenceSimilarity REAL, CloseEnough INTEGER)''')

    for i in datatable:
        if i[3] == True:
            c.execute("INSERT INTO UserHistory VALUES ( "+str(i[0]) + " ," +
                                                       str(i[1]) + " , " + str( i[2]) +
                                                        ", " + '1' + ')' )
        else:
            c.execute("INSERT INTO UserHistory VALUES ( " + str(i[0]) + " ," +
                      str(i[1]) + " , " + str(i[2]) +
                      ", " + '0' + ')')

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


if __name__ == '__main__':
    '''
    #Test indicators
    wordNetSimilarityTest(userAnswer, correctAnswer ):
    hammingDistance( userAnswer, correctAnswer  )
    lemmalist("brain")
    '''

    dt = doQuiz(fauxQA, "test")[:-1]
    putInQuizResultsInFile( dt )
    #gets an exception from nan
    #putQuizResultsInDbForUser( dt )