# -*- coding: utf-8 -*-
#popa

import math
from MirrorDecision import *


failedBool = False 

def testFail(whoFail, actualOutput, expectedOutput):
    print(whoFail + 'failed')
    print('Actual output:' + actualOutput)
    print('Expected output:' + expectedOutput)
  
def changeTest():
    mirror = MirrorDecision(0, 0, 0, 0)
    result = mirror.changeStepValueBool(0, 2, 1)
    if result == False:
        failedBool = True
        testFail('MirrorDecision.changeStepValueBool', result, True)
    result = mirror.changeStepValueBool(1, 1, 1)
    if result == False:
        failedBool = True
        testFail('MirrorDecision.changeStepValueBool', result, True)
    result = mirror.changeStepValueBool(2, 1, 1)
    if result == True:
        failedBool = True
        testFail('MirrorDecision.changeStepValueBool', result, False)
        
    
        
def failedCheck():
    if failedBool:
        print ('Unit-tests failed')
    else:
        print('Unit-tests success')

changeTest()
failedCheck()