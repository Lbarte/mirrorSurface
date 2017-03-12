# -*- coding: utf-8 -*-

from main import *
import math

def tests():
    pointListTest()
    #mirrorDecisionTest()
    neighbourPointTest()
    
def pointListTest():
    print('Test pointList')
    pointListObj = PointList()
    pointListObj.addPoint(1, 2)
    print ('Point: ', pointListObj.getPointX(0), pointListObj.getPointY(0))
    pointListObj.addPoint(5, 6)
    pointListObj.changePoint(0, 3, 4)
    print ('Len: ', pointListObj.getLen())
    print ('Lists: ', pointListObj.getListX(), pointListObj.getListY())
    pointListObj.setList([0, 1], [2, 3])
    print ('Lists: ', pointListObj.getListX(), pointListObj.getListY())
    
def mirrorDecisionTest():
    testMirrorLength = 20
    pipeNumber = 2
    pipeDiameter = 5
    pipeLayer = 5
    decision = MirrorDecision(testMirrorLength, pipeNumber, pipeDiameter, pipeLayer)
    testPipePositionInSpaceMethod(decision)
    testBeginEndPointsCalculation(decision)
    testDepthCalculation(decision)
    testMirrorSpaceFormation(decision)
    #testGenerator(decision)
    testSearchBestMirrorSpace(decision)
    #testRayProjection(decision, decision.mirrorSpacePointList)
    #testIsSmaller(decision)
    #testCheckCloser(decision)
    #testGetCrossPoint(decision)
    #testD()
    #testCheckContact(decision)
    #testGetDistance(decision)
    #testGetSum(decision)
    #testPrepareCos(decision)
    #testUsefulReflectiveSpace(decision)
    #testSaveData(decision)
    #testWallowMirrorSpace(decision)
    testBestDecisionSearch(decision)
    print ('Pow test')
    print ('1**2', 1**2, '2**2', 2**2, '4**(1/2)', 4**(1/2))
   
    
def testPipePositionInSpaceMethod(decision):
    #pipePositionInSpace(self, zeroPointList):
    #return pipeRadius, pipePointList
    print('Test pipePositionInSpace')
    zeroPosition = PointList()
    zeroPosition.addPoint(400, 300)
    decision.pipePositionInSpace(zeroPosition)
    print (decision.pipeRadius, decision.pipePointList.getListX(), decision.pipePointList.getListY())

def testBeginEndPointsCalculation(decision):
    #beginEndPointsCalculation(self):
    #return mirrorExtremePointList
    print('Test beginEndPointsCalculation')
    decision.beginEndPointsCalculation()
    print ('ExtremePointList', decision.mirrorExtremePointList.getListX(), decision.mirrorExtremePointList.getListY())
    
def testDepthCalculation(decision):
    #depthCalculation(self):
    #return extremeDepthFunctionList
    print('Test depthCalculation')
    decision.depthCalculation()
    print ('ExtremeDepthFunctionList', decision.extremeDepthFunctionList)
    
def testMirrorSpaceFormation(decision):
    # mirrorSpaceFormation(self):
    # return mirrorSpacePointList
    print('Test mirrorSpaceFormation')
    decision.mirrorSpaceFormation()
    print ('MirrorSpacePointList', decision.mirrorSpacePointList.getListX(), decision.mirrorSpacePointList.getListY())
    
def testGenerator(decision):
    # mirrorSpaceFormingGenerator(self, start, end):
    # return mirror forming generator
    print('Test mirrorSpaceFormingGenerator')
    start = 0
    end = 10
    testGenerator = decision.mirrorSpaceFormingGenerator(start, end)
    last = 0
    for index in testGenerator:
        last = index
    print('last', last)
    
def testSearchBestMirrorSpace(decision):
    # searchBestMirrorSpace(self):
    # return sumLightCoef/lightCoefSum, mirrorSpacePointList
    print('Test searchBestMirrorSpace')
    decision.searchBestMirrorSpace()
    print ('LightCoefSum', decision.sumLightCoefList) #, 'MirrorSpacePointList', 'XPoints', decision.mirrorSpacePointList.getListX(), 'YPoints', decision.mirrorSpacePointList.getListY())
    
def testRayProjection(decision):
    # rayProjection(self):
    # return rayBeginPointList, rayEndPointList
    print('Test rayProjection')
    decision.rayProjection()
    print ('RayBeginPointList', 'pointsX', decision.rayBeginPointList.getLen())
    print ('RayEndPointList', 'pointsX', decision.rayEndPointList.getLen())
    
def testIsSmaller(decision):
    #isSmaller(self, number1, number2):
    #return True or False
    print ('Test getSmaller')
    number1 = True
    number2 = False
    print('Smaller value', decision.isSmaller(number1, number2))
    
def testCheckCloser(decision):
    #checkCloser(self, x, y, x1, y1, x2, y2):
    #return True or False
    print('Test checkCloser')
    print('First one closer?', decision.checkCloser(1, 0, 2, 0, 2, 0))
    
def testGetCrossPoint(decision):
    #getCrossPoint(self, x1, y1, x2, y2, R):
    #return crossPoint for point and circle as if there was line for point and circle center
    print('Test getCrossPoint')
    pointList = decision.getCrossPoint(3, 0, 0, 4, 5)
    print('Cross point', pointList.getListX(), pointList.getListY())
    
def testD():
    print ('Test D')
    print('D =', (0)**(1/2))
    
def testCheckContact(decision):
    #checkContact(self, mirrorX, mirrorY, originalPipeIndex, pipePointList, pipeRadius):
    #return True or False
    print('Test checkContact')
    print('Is contact?', decision.checkContact(decision.mirrorSpacePointList.getPointX(0), decision.mirrorSpacePointList.getPointY(0), 0, decision.pipePointList, decision.pipeRadius))
    
def testGetDistance(decision):
    #getDistance(self, x1, y1, x2, y2):
    # return distance between two points
    print('Test getDistance')
    print('Distance', decision.getDistance(20,-7,-5,1))
    
def testGetSum(decision):
    #getSum(angleList):
    # return sum of angle differences in angleList
    print('Test getSum')
    angleList = PointList()
    angleList.addPoint(-25, 2.45)
    print('Sum', decision.getSum(angleList))
    
def testPrepareCos(decision):
    #prepareCos(self, result):
    #return prepared cos
    print ('Test prepareCos')
    cos = -1.45
    print('Prepared cos', decision.prepareCos(cos).getPointX(0), decision.prepareCos(cos).getPointY(0))
    
def testUsefulReflectiveSpace(decision):
    # usefulReflectiveSpace(self):
    # return lightCoefSum
    print('Test usefulReflectiveSpace')
    print ('LightCoef', decision.usefulReflectiveSpace(decision.mirrorSpacePointList, decision.pipePointList, decision.pipeRadius))
    
def testSaveData(decision):
    # saveData(self, lightCoefSum):
    # return mirrorSpacePointData, sumLightCoefList
    print('Test saveData')
    decision.saveData(decision.usefulReflectiveSpace())
    print('Saved data. Mirror space points', decision.mirrorSpacePointData.getListX(), decision.mirrorSpacePointData.getListY())
    print('Coefficients sum', decision.sumLightCoefList)
    
def testWallowMirrorSpace(decision):
    #wallowMirrorSpace(self):
    # return downsideCheck and mirrorSpacePointList
    print('Test wallowMirrorSpace')
    decision.wallowMirrorSpace()
    print('Mirror space points', decision.mirrorSpacePointList.getListX(), decision.mirrorSpacePointList.getListY(), 'Downside check', decision.downsideCheck)
    
def testBestDecisionSearch(decision):
    #bestDecisionSearch(self):
    # return mirrorSpacePointList
    print('Test bestDecission')
    decision.bestDecisionSearch()
    print('Best decision mirror', decision.mirrorSpacePointList.getListX(), decision.mirrorSpacePointList.getListY())
    print ('Max light coef', max(decision.sumLightCoefList))
    print ('Light coef list len', len(decision.sumLightCoefList))
    print ('Max light coef, again', decision.sumLightCoefList.index(max(decision.sumLightCoefList)))
    #print ('X points best space', decision.mirrorSpacePointData.getPointX(decision.sumLightCoefList.index(max(decision.sumLightCoefList))))
    #print ('Y points best space', decision.mirrorSpacePointData.getPointY(decision.sumLightCoefList.index(max(decision.sumLightCoefList))))
    #print ('Space data', decision.mirrorSpacePointData.getListX(), decision.mirrorSpacePointData.getListY())
    
    
def testForList():
    print ('Test for with list')
    l = []
    l.append('1 num')
    l.append('2 num')
    for index in range (len(l)):
        print(l[index], index)
        
def neighbourPointTest():
    xm = 0
    ym = 0
    xp = 1
    yp = 1
    angle = 90
    distRmP = getDistance(xm, ym, xp, yp)
    angle0 = 45
    x1 = ((-1)*(2*yp*math.tan(angle) - 2*xm - 2*xp*math.tan(angle) - 2*ym*math.tan(angle)) + ((2*yp*math.tan(angle) - 2*xm - 2*xp*math.tan(angle) - 2*ym*math.tan(angle))**2 - 4*(1+math.tan(angle)**2)*(xm**2+xp**2-2*xp*yp*math.tan(angle) + yp**2+ym**2-(distRmP*math.tan(angle0))**2+2*xp*ym*math.tan(angle)-2*yp*ym))**(1/2))/(2*(1+math.tan(angle)**2))
    x1 = x1.real
    x2 = ((-1)*(2*yp*math.tan(angle) - 2*xm - 2*xp*math.tan(angle) - 2*ym*math.tan(angle)) - ((2*yp*math.tan(angle) - 2*xm - 2*xp*math.tan(angle) - 2*ym*math.tan(angle))**2 - 4*(1+math.tan(angle)**2)*(xm**2+xp**2-2*xp*yp*math.tan(angle) + yp**2+ym**2-(distRmP*math.tan(angle0))**2+2*xp*ym*math.tan(angle)-2*yp*ym))**(1/2))/(2*(1+math.tan(angle)**2))
    x2 = x2.real
    y1 = (x1-xp)*math.tan(angle)+yp
    y2 = (x2-xp)*math.tan(angle)+yp
    print ('x1', x1, 'x2', x2, 'y1', y1, 'y2', y2)
    
def getDistance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
    
tests()