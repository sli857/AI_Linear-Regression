# Name: David Li
# Email: sli857@wisc.edu
# NetID: sli857
# CS Login: sli857

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import math

NUM_OF_ENTRIES = 0


def cleanCSV(filename):
    out = open("hw5.csv", "w")
    out.write("year,days\n")
    with open(filename, "r") as csvfile:
        input = csv.reader(csvfile, delimiter=',')
        next(input)
        for line in input:
            out.write("{0},{1}\n".format(line[0].split("-")[0], line[1]))
    csvfile.close()
    out.close()


def readCSV(filename):
    with open(filename, "r") as csvfile:
        input = csv.reader(csvfile, delimiter=",")
        next(input)
        years = np.empty((NUM_OF_ENTRIES, 2), dtype="int64")
        durations = np.empty(NUM_OF_ENTRIES, dtype="int64")
        currIndex = 0
        for line in input:
            if (line[0] in years):
                print(1)
            years[currIndex] = np.array([1, line[0]])
            durations[currIndex] = np.array(line[1])
            currIndex += 1
    return years, durations


def calcMLE(X, Y):
    dotProd = np.dot(np.transpose(X), X)
    print("Q3c:")
    print(dotProd)

    inverse = np.linalg.inv(dotProd)
    print("Q3d:")
    print(inverse)

    PI = np.dot(inverse, np.transpose(X))
    print("Q3e:")
    print(PI)

    MLE = np.dot(PI, Y)
    print("Q3f:")
    print(MLE)

    return MLE


def prediction(MLE, x):
    pred = MLE[0] + MLE[1] * x
    print("Q4: " + str(pred))


def getNumOfLines(filename):
    rowCount = 0
    for row in open(filename):
        if (row == "year,days\n"):
            continue
        rowCount += 1
    return rowCount


def plotData(x, y):
    fig = plt.figure()
    plt.plot(x, y, label='Data')
    plt.xlabel('Year')
    plt.ylabel('Number of Frozen Days')
    plt.show()
    fig.savefig("plot.jpg")


def main():
    global NUM_OF_ENTRIES
    # dirtySource = "./chart.csv"
    # cleanCSV(dirtySource)
    targetSource = sys.argv[1]
    NUM_OF_ENTRIES = getNumOfLines(targetSource)
    X, Y = readCSV(targetSource)
    plotData([x[1] for x in X], Y)

    print("Q3a:")
    print(X)
    print("Q3b:")
    print(Y)
    MLE = calcMLE(X, Y)
    prediction(MLE, 2022)

    print("Q5a:", end=" ")
    if (MLE[1] > 0):
        print(">")
        print("Q5b: A positive slope of the regression line indicates that Lake Mandota will have longer frozen period year by year.")
        estimation = (-MLE[0]) / MLE[1]
        endYear = math.floor(estimation)
        print("Q6a: " + str(estimation))
        print("Q6b: Based on prediction, before year {0} (inclusive), Lake Mandota have had 0 day of ice cover".format(
            endYear))
    elif (MLE[1] < 0):
        print("<")
        print("Q5b: A negative slope of the regression line indicates that Lake Mandota will have shorter frozen period year by year.")
        estimation = (-MLE[0]) / MLE[1]
        endYear = math.ceil(estimation)
        print("Q6a: " + str(estimation))
        print(
            "Q6b: Base on prediction, after year {0} (inclusive), Lake Mandota will have 0 day of ice cover".format(endYear))

    elif (MLE[1] == 0):
        print("=")
        print("Q5b: The slope of the regression line being 0 indicates that Lake Mandota will keep the same frozen period year by year.")
        print("Q6a: N/A")
        print("Q6b: The frozen period of Lake Mandota is constant, that means there will not be or was no such a year that Lake Mandota has 0 day of ice cover, unless Lake Mandota is always not covered by ice which has been contradicted by the non-zero data.")


if __name__ == "__main__":
    main()
