
import random
import datetime
import time

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def resetFiles(inFileName, outFileName):
    response = "wait"
    inFile = open(inFileName, 'w')
    inFile.writelines(str(response)+"\n")
    inFile.close()

    outFile = open(outFileName, 'w')
    outFile.writelines(str(response)+"\n")
    outFile.close()


if __name__ == '__main__':
    status = "wait"
    inFileName = "isLeapYearInput.txt"
    outFileName = "isLeapYearOutput.txt"

    while status == "wait":
        time.sleep(7)
        inFile = open(inFileName, 'r')
        text = inFile.readline()
        inFile.close()
        text = text.rstrip()

        if text == "stop":
            exit(0)
        if text == "wait":
            continue

        try:
            print(text)
            text = int(text)
            response = isLeapYear(text)

        except:
            response = "Error: Not an integer"
            outFile = open(outFileName, 'w')
            outFile.writelines(str(response)+"\n")
            outFile.close()
            print("Sleeping for 30 on bad input")
            time.sleep(30)
            response = "wait"
            outFile = open(outFileName, 'w')
            outFile.writelines(str(response)+"\n")
            outFile.close()
            resetFiles(inFileName, outFileName)
            continue

        outFile = open(outFileName, 'w')
        outFile.writelines(str(response)+"\n")
        outFile.close()
        print("Results are Ready!")

        time.sleep(30)
        resetFiles(inFileName, outFileName)







