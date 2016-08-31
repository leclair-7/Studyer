
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
            if len(s1) > len(s2):
                toExtend = len(s1) - len(s2)
                for i in range(toExtend):
                    # because who the hell
                    # answers a quiz with _?
                    s2 = s2 + "_"
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

    baseNum = max(len(s1), len(s2))
    right, wrong = 0, 0

    if len(s1) != len(s2):
        s1,s2 = lengthNormalizer(s1, s2)

    if len(s1) == len(s2) and len(s1) > 0:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                wrong += 1
            else:
                right += 1
    return (right * 1.0) / baseNum


if __name__ == '__main__':
    print(hammingDistance("rucas hasdfdsfel", "rucas hagel"))

