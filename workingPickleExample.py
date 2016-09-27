import pickle, os

'''
Things stuff in this file does:
    - get past data from a list
    - update probabilities of the questions being asked
    - devise a way for the probability the question is asked to be changed based on some not yet known criteria

pickles/loads data, more importantly, it works
'''
twoList = [[1, 2, 3, 4], [5, 34, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
filename = "dataset3.pickle"

def getZeList(filename):
    if os.path.isfile(filename):
        fileObj = open(filename, 'rb')
        r = pickle.load(fileObj)
        fileObj.close()
        return r
    else:
        return []


theList = getZeList(filename)
theList.append([90,91,92,47])
fileObj = open(filename, 'wb')
pickle.dump(theList, fileObj)
fileObj.close()


import random
l = [('a', 1), ('b', 5), ('c', 5)]

def randitem(l):
    # Make the probabilities add up to 1, preserving ratios
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

# test
'''
res = {'a': 0, 'b': 0, 'c': 0}
for i in range(10000):
    #in the end how we'll pick questions to present to the Student
    res[randitem(l)] += 1
# the evidence that this method works
print('a: %s (%s%%)' % (res['a'], res['a'] / 100))
print('b: %s (%s%%)' % (res['b'], res['b'] / 100))
print('c: %s (%s%%)' % (res['c'], res['c'] / 100))
'''
if __name__ == '__main__':
    anotherFileObject = open(filename, 'rb')

    newPara = []
    for i in pickle.load(anotherFileObject):
        newPara.append( (i[0],i[-1]) )
    print(newPara)


