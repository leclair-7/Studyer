import pickle

twoList = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
filename = "dataset.pickle"
fileObj = open(filename, 'wb')
pickle.dump(twoList, fileObj)
fileObj.close()
anotherFileObject = open("dataset.pickle", 'rb')
r = pickle.load(anotherFileObject)

print(r)
