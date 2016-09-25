import pickle, os

'''
Things stuff in this file does:
    - get past data from a list
    - update probabilities of the questions being asked
    - make the

try to load pickle
every time we run the proram the pickle thing loads the dataset
appends and repickles
'''
twoList = [[1, 2, 3, 4], [5, 34, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
filename = "dataset.pickle"


def getZeList(filename):
    if os.path.isfile(filename):
        fileObj = open(filename, 'rb')
        r = pickle.load(fileObj)
        fileObj.close()
        return r
    else:
        return []


theList = getZeList(filename)
theList.append(["damn thing appends haha"])

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
    res[randitem(l)] += 1
# the evidence
print('a: %s (%s%%)' % (res['a'], res['a'] / 100))
print('b: %s (%s%%)' % (res['b'], res['b'] / 100))
print('c: %s (%s%%)' % (res['c'], res['c'] / 100))
'''
if __name__ == '__main__':
    anotherFileObject = open(filename, 'rb')
    print(pickle.load(anotherFileObject))
