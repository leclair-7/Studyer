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
    "submittal":"another person given decision",
    "ball-in-court":"who has decision",

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

''' because self testing the fauxQA was taking too damn long
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
    numQuestions = len(questionSection)
    right =0.0
    datatable = []

    for que in questionSection:
        userAnswer = ""
        questionNumber = 1

        #while not QuestionAnswered:
        before = time.time()
        print("Prompt, " + que.question)
        userAnswer = input("Yo Answer: ")

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
        trainMode = False
        if trainMode and answerSimilarity < .8:
            while answerSimilarity < .8:
                '''
                make the user answer until he/she knows it.
                for example, B A, is a fan of mastery learning
                '''
                print("Prompt, " + que.question)
                userAnswer = input("Yo Answer: ")
                answerSimilarity = getSentenceSimilarity(userAnswer, correctAnswer)

        if userAnswer == correctAnswer:
            right += 1.0
            continue
        elif answerSimilarity > .9: right += 1.0
        after = time.time()
        answerTime = after - before
        finishingDateTime = datetime.datetime.now()
        incrementNumberOfTimesAnsweredThisQuestion = 1
        datatable.append([que.number, answerTime, answerSimilarity, hamDist, closeEnoughForGovernmentWork,
                           round(time.time(), 2), finishingDateTime, incrementNumberOfTimesAnsweredThisQuestion])

        '''
        since we put que.number appending on the list we just need some matching thing then a sort at the end before we pickle it
        '''
    #train or test modes

    score = (right/numQuestions)
    print("Your score is: %s" % score,end="")
    if score < .40:
        print("; You're a fucking idiot")
    else:
        print()
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


def getZeList(filename):
    if os.path.isfile(filename):
        fileObj = open(filename, 'rb')
        r = pickle.load(fileObj)
        fileObj.close()
        return r
    else:
        return []


def randitem(l):
    # Make the probabilities add up to 1, preserving ratios
    '''
    l = [('a', 1), ('b', 5), ('c', 5)]
    :param l: a list of tuples
    :return: the output is a random selection based on the number associated ith each number
    higher with respect to the rest of the numbers means it's more likely to get picked
    '''
    s = sum([b for (a, b) in l])
    l2 = []
    for (a, b) in l:
        l2.append((a, b / s))
    r = random.random()
    for (a, b) in l2:
        if r < b:
            return a
        else:
            r -= b


if __name__ == '__main__':
    '''
    #Test indicators
    wordNetSimilarityTest(userAnswer, correctAnswer ):
    hammingDistance( userAnswer, correctAnswer  )
    lemmalist("brain")
    '''

    dt = doQuiz( makeItList(fauxQA) )
    filename = "dataset5.pickle"
    theList = getZeList(filename)
    theList.append( dt )
    fileObj = open(filename, 'wb')
    pickle.dump(theList, fileObj)
    fileObj.close()
    #print(theList)
    newPara = []

    anotherFileObject = open(filename, 'rb')
    for i in pickle.load(anotherFileObject):
        for j in i:
            newPara.append((j[0], j[-1]))

    h = sorted(newPara, key=lambda tup: tup[0])
    #print(sorted_by_second)
    #a probability table on which question for the quiz function to base its likelihood of asking a question on
    t = [0] * h[-1][0]
    for i in h:
        t[i[0] - 1] += 1

    newLista = [0] * len(t)
    for i in range(len(t)):
        newLista[i] = (i + 1, t[i])
    print(newLista)