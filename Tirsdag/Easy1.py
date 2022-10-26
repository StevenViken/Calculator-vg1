word1 = 2
word2 = 4
word3 = 6
word4 = -2
word5 = 10

while True:
    whileList = []
    whileList.append(word1)
    whileList.append(word2)
    whileList.append(word3)
    whileList.append(word4)
    whileList.append(word5)
    summere = 0
    for i in range(len(whileList)):
        summere = summere + whileList[i]
    print(summere)
    break