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
}


class Question:
    def __init__(self, questionNumber, question, answer, weightForQuestionSelector):
        self.number = questionNumber
        self.question = question
        self.answer = answer
        self.weightForQuestionSelector = weightForQuestionSelector


def makeItList(dictionary):
    h = []
    questionNumber = 1
    weightForQuestionSelector = 1
    for i in dictionary.keys():
        h.append(Question(questionNumber, i, dictionary[i], weightForQuestionSelector))
        questionNumber += 1
    return h

'''
for i in makeItList(fauxQA):
    print(i.question)
'''

''' because self testing the fauxQA was taking too damn long
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
'''

'''
iterate through Questions
difference between straight dictionary and these things
'''
def doQuiz( questionSection ):
    '''
    this is the main controller so to speak,
    :param questionSection: Question objects for the Student's question
    :return: dataset with questions from user taking the quiz
    '''
    #mode = mode.lower()
    numQuestions = len(questionSection)
    right =0.0
    datatable = []
    #print( "You are in " + mode + " mode.\nIf you put something other than train or test you ran the function wrong.")
    #print("However, test will test, and train or any other crap you inputted will train")
    for que in questionSection:
        userAnswer = ""
        questionNumber = 1

        #while not QuestionAnswered:
        before = time.time()
        print("Prompt, " + que.question)
        userAnswer = input("Yo Answer: ")

        after = time.time()
        answerTime = after - before
        userAnswer,correctAnswer = userAnswer.lower(), que.answer.lower()
        hamDist = hammingDistance(userAnswer, correctAnswer )

        #answerSimilarity = wordNetSimilarityTest(userAnswer, correctAnswer)
        # higher score based on how close the sentence is to the correct answer
        answerSimilarity = getSentenceSimilarity(userAnswer, correctAnswer)
        closeEnoughForGovernmentWork = False
        '''
        if q_ad[question] in lemmalist(userAnswer):
            closeEnoughForGovernmentWork = True
        '''
        if answerSimilarity > .80:
            closeEnoughForGovernmentWork = True

        if userAnswer == correctAnswer: right += 1.0
        elif answerSimilarity > .9: right += 1.0

        datatable.append( [que.number, answerTime,answerSimilarity, hamDist, closeEnoughForGovernmentWork, time.time() ] )
        #print( datatable )
        '''
        since we put que.number appending on the list we just need some matching thing then a sort at the end before we pickle it
        '''
    #train or test modes

    score = (right/numQuestions)
    print("Your score is: %s" % score,end="")
    if score < 40:
        print("; You're a fucking idiot")
    return datatable

def putInQuizResultsInFile( datatable ):
    '''
    This function sucks balls.

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
    if os.path.isfile('UserQuizHist.db'):
        return False

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



def getZeList(filename):
    if os.path.isfile(filename):
        fileObj = open(filename, 'rb')
        r = pickle.load(fileObj)
        fileObj.close()
        return r
    else:
        return []

if __name__ == '__main__':
    '''
    #Test indicators
    wordNetSimilarityTest(userAnswer, correctAnswer ):
    hammingDistance( userAnswer, correctAnswer  )
    lemmalist("brain")
    '''

    dt = doQuiz( makeItList(fauxQA) )
    filename = "dataset.pickle"
    theList = getZeList(filename)
    theList.append( dt)
    fileObj = open(filename, 'wb')
    pickle.dump(theList, fileObj)
    fileObj.close()
    #print(theList)