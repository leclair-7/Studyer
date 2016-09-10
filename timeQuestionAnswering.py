
import time
# qaBank = [("red","rose"),("blue","bird"),("Kimberly","sublime"),("work","deep")]
qaBank = {"red": "rose", "blue": "bird", "Kimberly": "sublime", "work": "deep"}


def askAndTime(dictQA):
    '''
    in initial quiz to get timing information for another task

    :param dictQA:
    :return:
    '''
    listTimes = []
    que = ""
    ans = ""
    for q in dictQA.keys():
        tBegin = time.time()
        while ans == "":
            # print( )
            ans = input("[+] Relate: " + q + " ")
        # "[+] Relate: " + q + " ",end=''ans.strip()
        ans = ""

        tEnd = time.time()
        listTimes.append((q, tEnd - tBegin))
    return listTimes


if __name__ == '__main__':
    print(askAndTime(qaBank))