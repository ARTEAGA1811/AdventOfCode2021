def myFunction():
    pass

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def testCode():
    testCases = [
    ]

    outputs = [

    ]

    for i in range(len(testCases)):
        solution = None
        try:
            solution = myFunction(testCases[i]) #parameters
            assert solution == outputs[i]
            print(
                bcolors.OK+"\nCORRECT ANSWER:"+bcolors.RESET+f"\ntest {testCases[i]}, result {solution}")
        except Exception as error:
            print(
                bcolors.FAIL+"\nERROR: "+bcolors.RESET+f"\ntest {testCases[i]}, "+bcolors.WARNING+"\nExpected "+bcolors.RESET+f"{outputs[i]}, "+bcolors.WARNING+"\nCalculated "+bcolors.RESET+f"{solution}", error)

testCode()

#this file is created for testing purposes
#David Arteaga