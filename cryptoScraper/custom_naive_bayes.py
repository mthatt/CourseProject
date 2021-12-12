
import numpy as np
import math
from tqdm import tqdm
from collections import Counter
import reader

def naiveBayes(train_set, train_labels, dev_set, laplace=1.0, pos_prior=0.5,silently=False):
    stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    posDict = {
    }
    negDict = {
    }
    allWords = []
    posWords = []
    negWords = []
    encoder = preprocessing.LabelEncoder()

    #Build a list of allwords and append them to respective sets
    for i in range(len(train_set)):
        #print("SET:", train_set[i])
        #print("LABELS:", train_labels[i], "\n")
        for j in range(len(train_set[i])):
            train_set[i][j] = train_set[i][j].lower()
            if train_set[i][j] not in stopWords:
                if train_labels[i] == 1:
                    posWords.append(train_set[i][j])
                elif train_labels[i] == 0:
                    negWords.append(train_set[i][j])

    #Build dictionaries for positive and negative words and their frequencies WITHIN their class
    count = 0
    for i in posWords:
        count += 1
    for i in negWords:
        count += 1
    counter = 0

    laPlace = .8

    #set all counts to 0
    for i in posWords:
        posDict[i] = 0
    for i in posWords:
        posDict[i] = posDict[i] + 1
    logPosDict = {
    }
    counter = 0
    for i in posWords:
        logPosDict[i] = np.log(float(posDict[i] + laPlace) / (float(len(posWords)) + (laPlace * (float(len(posDict) + 1)))))
        if counter <= 30:
            counter += 1
            print(i, posDict[i], logPosDict[i])

    for i in negWords:
        negDict[i] = 0
    for i in negWords:
        negDict[i] = negDict[i] + 1
    logNegDict = {
    }
    for i in negWords:
        logNegDict[i] = math.log(float(negDict[i] + laPlace) / (float(len(negWords)) + (laPlace * (float(len(negDict) + 1)))))

    unknownPos = math.log(laPlace / (float(len(posWords)) + (laPlace * (float(len(posDict) + 1)))))
    unknownNeg = math.log(laPlace / (float(len(negWords)) + (laPlace * (float(len(negDict) + 1)))))
    devLabels = []
    for i in range(len(dev_set)):
        devPosSum = 0
        devNegSum = 0
        for j in range(len(dev_set[i])):
            dev_set[i][j] = dev_set[i][j].lower()
            if dev_set[i][j] not in stopWords:
                devPosSum += logPosDict.get(dev_set[i][j], unknownPos)
                devNegSum += logNegDict.get(dev_set[i][j], unknownNeg)
        pcla = math.log(pos_prior) + devPosSum
        pclb = math.log(1 - pos_prior) + devNegSum
        if pcla > pclb:
            devLabels.append(1)
        else:
            devLabels.append(0)

        #math.log(float(posWords.count(i)) / float(len(posWords)))

    #Create the summation for all
    posProbsSum = 0


    return devLabels

