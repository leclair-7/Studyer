'''
An implementation of hamming distance,
Auxiliary function makes the word lengths equal
'''

import unittest

def lengthNormalizer(s1, s2):
    '''
    this function feeds the hamming distance function
    it makes strings equal length
    '''
    if len(s1) is len(s2):
        return s1, s2
    else:
        didswap = False
        while len(s1) != len(s2):
            # print(s1,s2)
            if len(s1) > len(s2):
                toExtend = len(s1) - len(s2)
                for i in range(toExtend):
                    # because who the hell
                    # answers a quiz with _?
                    s2 = s2 + "_"
                return s1, s2
            else:
                didswap = True
                t = s2
                s2 = s1
                s1 = t

        if didswap:
            t = s2
            s2 = s1
            s1 = t
    return s1, s2


def hammingDistance(s1, s2):
    '''
    number of letters that have to be changed
    to make 1 word the other

    string :param s1:
    string :param s2: 
    float :return: Hamming Distance
    '''

    s1, s2 = s1.lower(), s2.lower()
    baseNum = max(len(s1), len(s2))
    right, wrong = 0, 0

    if len(s1) != len(s2):
        s1, s2 = lengthNormalizer(s1, s2)
    assert len(s1) is len(s2), "word lengths don't match, dumbass"
    #this one gets in production which is effin annoying
    #print(s1, s2)

    if len(s1) == len(s2) and len(s1) > 0:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                wrong += 1
            else:
                right += 1
    if baseNum < .00001:
        baseNum = 1
        return 0
    return (right * 1.0) / baseNum


class TestHammingDistance(unittest.TestCase):
    def setUp(self):
        pass

    def testEmptyInputs(self):
        self.assertAlmostEqual( hammingDistance("", ""), 0)

    def testSameWords(self):
        self.assertAlmostEqual( hammingDistance("blue, bird", "blue, bird"), 1.0)

    def testFirstFuncCallHigherScore(self):
        self.assertGreater( hammingDistance("platypus", "platypuz"), hammingDistance("brick", "steve"))

    def testFirstBlank(self):
        self.assertIsNotNone( hammingDistance("","amadour"))

    def testSecondBlank(self):
        self.assertIsNotNone( hammingDistance("giacomo", ""))

    def testFirstShorter(self):
        self.assertIsNotNone(hammingDistance("Pardonnez-vous", "oiseau") )

    def testSecondShorter(self):
        self.assertIsNotNone( hammingDistance("oiseau", "Pardonnez-vous") )

if __name__ == '__main__':
    unittest.main()
