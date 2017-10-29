import subprocess
import os

totalLineCharCount = 40

def getWordList(fortune):
    wordlist = fortune.split(" ")
    return wordlist

def getStartLine():
    return '    | '

def lineCharCount(mystring):
    x = 0
    for i in mystring:
        x = x + 1
    return x

def getLineRemainder(wordLineCount):
    remainingChars = totalLineCharCount - wordLineCount
    x = 0
    theRemainder = ""
    while x < remainingChars -1:
        theRemainder = theRemainder + " "
        x = x + 1
    theRemainder = theRemainder + "|"
    return theRemainder
    
def fetchFortune():
    command = ['fortune']
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    text = p.stdout.read()
    retcode = p.wait()
    return text

def printTopBottom():
    print(
        '    ___________________________________'
        )

def removeEtc(word):
    newword = word.replace('\n','')
    newword = newword.replace('\r','')
    newword = newword.replace('\t',' ')
    newword = newword.strip()
    newword = newword.strip(os.linesep)
    return newword.strip('\n\r')

def printPumpkin():
    command = ['cat', 'pumpkinasc.txt']
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    text = p.stdout.read()
    retcode = p.wait()
    print(text)

def mainLoop():
    printTopBottom()
    myfortune = fetchFortune()
    myWordList = getWordList(myfortune)
    tempLine = ""
    lenWordList = len(myWordList)
    wordCount = 0
    for word in myWordList:
        wordCount = wordCount + 1
        revisedWord = removeEtc(word)
        if lineCharCount(getStartLine() + tempLine + " " + revisedWord) < totalLineCharCount - 2:
            tempLine = tempLine + " " + revisedWord
        else:
            print(getStartLine() + tempLine + getLineRemainder(lineCharCount(getStartLine() + tempLine)))
            tempLine = ""
            tempLine = revisedWord
        if wordCount == lenWordList:
            print(getStartLine() + tempLine + getLineRemainder(lineCharCount(getStartLine() + tempLine)))
        
        
    printTopBottom()
    printPumpkin()
    print("Happy Halloween!!!!")

mainLoop()

