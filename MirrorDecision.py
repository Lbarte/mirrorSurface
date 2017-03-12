# -*- coding: utf-8 -*-

import math
from PointList import *

class MirrorDecision:
    
    DETALISATION = 1
    
    def __init__(self, mirrorLength, pipeNumber, pipeDiameter, pipeLayer):
        self.mirrorExtremePointList = PointList()
        self.extremeDepthFunctionList = []
        self.mirrorSpacePointList = PointList()
        self.downsideCheck = 0  
        self.rayBeginPointList = PointList()
        self.rayEndPointList = PointList()
        self.mirrorSpacePointData = PointList()
        self.sumLightCoefList = [] 
        self.pipeRadius = 0
        self.pipePointList = PointList()
        self.zeroPointList = PointList()
        self.mirrorLength = mirrorLength
        self.pipeNumber = pipeNumber
        self.pipeDiameter = pipeDiameter
        self.pipeLayer = pipeLayer
        self.angleBefore = 20
        self.angleAfter = 160
        self.parabolaSpaceTiltAngle = 0
        self.directrixBeginPoint = PointList()
        self.directrixEndPoint = PointList()
        self.focusPoint = PointList()
        self.directrixPerpendicularFunctionList = []
        self.parabolaTiltAngle = 0
        self.zeroPointDirectrixLength = 0
        self.focusPointDirectrixLength = 0
    
    def pipePositionInSpace(self, zeroPointList):
        #return pipeRadius, pipePointList
        self.zeroPointList = zeroPointList
        pipeLine = (self.pipeLayer + self.pipeDiameter)*(self.pipeNumber-1) + self.pipeDiameter
        self.pipeRadius = self.pipeDiameter/2
        for numberIndex in range (self.pipeNumber):
            xpi = self.zeroPointList.getPointX(0) - (pipeLine/2) + self.pipeRadius + (self.pipeDiameter + self.pipeLayer)*(numberIndex)
            ypi = self.zeroPointList.getPointY(0)
            self.pipePointList.addPoint(xpi, ypi)

    def searchBestCoef(self):
        while(self.parabolaPositionInSpace()):
            self.parabolaMirrorForming()
            self.usefulReflectiveSpace()
            self.saveData()
            
    def changeStepValueBool(self, begin, stop, adds):
        #True if there is no ability to continue
        if (begin < stop):
            if (begin+adds > stop):
                return True
            if (begin+adds == stop):
                return False
        elif (begin > stop):
            if (begin-adds < stop):
                return True
            if (begin-adds == stop):
                return False
        else:
            #begin==stop
            return True
            
    def parabolaPositionInSpace(self):
        continueBool = True
        tiltAngleContinueBool = self.changeStepValueBool(self.parabolaTiltAngle, maxParabolaTiltAngle, parabolaTiltAngleAdds)
        if tiltAngleContinueBool:
            self.parabolaTiltAngle += parabolaTiltAngleAdds
        toDirectrixContinueBool = self.changeStepValueBool(self.zeroPointDirectrixLength, maxZeroPointDirectrixLength, zeroPointDirectrixAdds)
        if toDirectrixContinueBool:
            self.zeroPointDirectrixLength += zeroPointDirectrixAdds
        toFocusContinueBool = self.changeStepValueBool(self.focusPointDirectrixLength, maxFocusPointDirectrixLength, focusPointDirectrixAdds)
        if toFocusContinueBool:
            self.focusPointDirectrixLength += focusPointDirectrixAdds
        if (tiltAngleContinueBool & toDirectrixContinueBool & toFocusContinueBool):
            continueBool = False
        return continueBool
        
    def getFirstIfParamIsBigger(self, first, twice, param1, param2):
        if param1 > param2:
            return first
        elif param1 < param2:
            return twice
            
    def getPointForQuadraticEquation(self, x, angle, anotherPoint):
        return Point(x0, math.tan(angle)*(x0-anotherPoint.getPointX(0)) + anotherPoint.getPointY(0))
        
    def getPointFromAnother(self, distance, angle, anotherPoint):
        D = 4*math.pow(anotherPoint.getPointX(0)*(1 + math.pow(math.tan(), 2)), 2) - 4*(math.pow(math.tan(), 2)+1)*(anotherPoint.getPointX(0)*(1 + math.pow(math.tan(), 2))-(distance*distance))
        x01 = (anotherPoint.getPointX(0)*(1 + math.pow(math.tan(), 2)) + math.pow(D, 1/2))/2*(math.pow(math.tan(), 2)+1)
        x02 = (anotherPoint.getPointX(0)*(1 + math.pow(math.tan(), 2)) - math.pow(D, 1/2))/2*(math.pow(math.tan(), 2)+1)
        if x01<x02:
            x0 = getFirstIfParamIsBigger(x01, x02, angle, 0)
            return getPointForQuadraticEquation(x0, angle, anotherPoint)
        elif x01>x02:
            x0 = getFirstIfParamIsBigger(x02, x01, angle, 0)
            return getPointForQuadraticEquation(x0, angle, anotherPoint)
        else:
            return getPointForQuadraticEquation(x01, angle, anotherPoint)
            
    def whereIsPointForLine(self, point, lineAngle, linePoint):
        yLine = math.tan(lineAngle)*(point.getPointX(0) - linePoint.getPointX(0)) + linePoint.getPointY(0)
        if yLine < point.getPointY(0):
            return -1
        elif yLine > point.getPointY(0):
            return 1
        else:
            return 0
            
    def checkLimits(self, point):
        if point.getPointY(0) > self.zeroPointList.getPointY(0):
            return False
        cond1 = (point.getPointX(0) < self.zeroPointList.getPointY(0)-(self.mirrorLength/2))
        cond2 = (point.getPointX(0) > self.zeroPointList.getPointY(0)+(self.mirrorLength/2))
        if cond1 | cond2:
            return False
        if whereIsPointForLine(point, self.parabolaTiltAngle, self.directrixPoint) < 0:
            return False
        return True
            
    def parabolaMirrorForming(self):
        
        
    def directrixBeginEndPointCalculation(self):
        self.directrixBeginPoint.addPoint(self.zeroPointList.getPointX(0), self.zeroPointList.getPointY(0)-self.pipeRadius)
        self.directrixEndPoint.addPoint(self.zeroPointList.getPointX(0), self.zeroPointList.getPointY(0)+self.mirrorLength)
            
    def beginEndPointsCalculation(self):
        #return mirrorExtremePointList
        self.mirrorExtremePointList.addPoint(self.zeroPointList.getPointX(0) - (self.mirrorLength/2), self.zeroPointList.getPointY(0))
        self.mirrorExtremePointList.addPoint(self.zeroPointList.getPointX(0) + (self.mirrorLength/2), self.zeroPointList.getPointY(0))


    def depthCalculation(self):
        #return extremeDepthFunctionList
        leftFuncAngle = -70
        rightFuncAngle = 70
        maxDepth = self.mirrorLength
        self.extremeDepthFunctionList.append(math.tan(leftFuncAngle)) #k0
        self.extremeDepthFunctionList.append(self.mirrorExtremePointList.getPointX(0)) #x0
        self.extremeDepthFunctionList.append(self.mirrorExtremePointList.getPointY(0)) #y0
        self.extremeDepthFunctionList.append(math.tan(rightFuncAngle)) #k1
        self.extremeDepthFunctionList.append(self.mirrorExtremePointList.getPointX(1)) #x1
        self.extremeDepthFunctionList.append(self.mirrorExtremePointList.getPointY(1)) #y1
        crossingX = (self.mirrorExtremePointList.getPointY(1) - self.mirrorExtremePointList.getPointY(0) + (self.mirrorExtremePointList.getPointX(0) * math.tan(rightFuncAngle)) - (self.mirrorExtremePointList.getPointX(1) * math.tan(leftFuncAngle))) / (math.tan(rightFuncAngle) - math.tan(leftFuncAngle))
        crossingY = (math.tan(rightFuncAngle) * (crossingX - self.mirrorExtremePointList.getPointX(0))) + self.mirrorExtremePointList.getPointY(0)
        if(abs(crossingY - self.mirrorExtremePointList.getPointY(0)) <= maxDepth):
            self.extremeDepthFunctionList.append(crossingX) #xh0
            self.extremeDepthFunctionList.append(crossingY) #yh0
            self.extremeDepthFunctionList.append(crossingX) #xh1
            self.extremeDepthFunctionList.append(crossingY) #yh1
        else:
            self.extremeDepthFunctionList.append(self.extremeDepthFunctionList[1] - (maxDepth/self.extremeDepthFunctionList[0]))
            self.extremeDepthFunctionList.append(self.mirrorExtremePointList.getPointY(0) - maxDepth)
            self.extremeDepthFunctionList.append(self.extremeDepthFunctionList[4] - (maxDepth/self.extremeDepthFunctionList[3]))
            self.extremeDepthFunctionList.append(self.mirrorExtremePointList.getPointY(0) - maxDepth)

    def parabolaMirrorForming(self, directrix, focus):
        mirrorSpaceGenerator = self.mirrorFormingGenerator(self.zeroPointList.getPointX(0)-(self.mirrorLength/2), self.zeroPointList.getPointX(0)+(self.mirrorLength/2))
        #TODO
        #need there parabola tilt angle to build parabolaPoint
        for mirrorPoint in mirrorSpaceGenerator:
            parabolaPoint = Point()
            parabolaPoint.addPoint()
            if (self.parabolaPointSetInPossibleSpace(parabolaPoint)):
                self.mirrorSpacePointList.addPoint(parabolaPoint)
            
    def mirrorFormingGenerator(self, start, end):
        # return mirror forming generator
        if((start-end) >= 100):
            step = 1/self.DETALISATION
        else:
            step = (end - start)/(100*self.DETALISATION)
        current = start
        #print('start', start, 'stop', (end - step), 'step', step)
        while current < (end - step):
            current += step
            yield current
            
    def addMirrorSpacePoint(self, spacePointX, spacePointY):
        self.mirrorSpacePointList.addPoint(spacePointX+self.zeroPointList.getPointX(0), spacePointY+self.zeroPointList.getPointY(0))
            
    def mirrorSpaceFormation(self):
        #return mirrorSpacePointList
        self.mirrorSpacePointList.addPoint(self.mirrorExtremePointList.getPointX(0), self.mirrorExtremePointList.getPointY(0))
        mirrorSpaceGenerator = self.mirrorFormingGenerator(self.mirrorExtremePointList.getPointX(0), self.mirrorExtremePointList.getPointX(1))
        for pointX in mirrorSpaceGenerator:
            self.mirrorSpacePointList.addPoint(pointX, self.mirrorExtremePointList.getPointY(1))
        self.mirrorSpacePointList.addPoint(self.mirrorExtremePointList.getPointX(1), self.mirrorExtremePointList.getPointY(1))
        #print('mirrorSpacePointList len', self.mirrorSpacePointList.getLen())

    
    def searchBestMirrorSpace(self):
        #return lightCoefSum, mirrorSpacePointList
        while (self.downsideCheck < self.mirrorSpacePointList.getLen()):
            self.rayProjection()
            lightCoefSum = self.usefulReflectiveSpace()
            self.saveData(lightCoefSum)
            self.wallowMirrorSpace()
        
    def rayProjection(self):
        #return rayBeginPointList, rayEndPointList
        for mirrorPointIndex in range (self.mirrorSpacePointList.getLen()):
            for angle in range (self.angleBefore, self.angleAfter):
                self.rayEndPointList.addPoint(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex))
                if(angle < 90):
                    self.rayBeginPointList.addPoint(self.rayEndPointList.getPointX(mirrorPointIndex) - self.pipeRadius*math.cos(angle), self.rayEndPointList.getPointY(mirrorPointIndex) - self.pipeRadius*math.sin(angle))
                elif angle == 90:
                    self.rayBeginPointList.addPoint(self.rayEndPointList.getPointX(mirrorPointIndex), self.rayEndPointList.getPointY(mirrorPointIndex) - self.pipeRadius*math.sin(angle))
                else:
                    self.rayBeginPointList.addPoint(self.rayEndPointList.getPointX(mirrorPointIndex) + self.pipeRadius*math.cos(angle), self.rayEndPointList.getPointY(mirrorPointIndex) - self.pipeRadius*math.sin(angle))

    def isSmaller(self, number1, number2):
        #return True or False
        if(number1>number2):
            return False
        else:
            return True
        
    def checkCloser(self, x, y, x1, y1, x2, y2):
        #return True or False
        'if (x1,y1) closer to (x,y) than (x2,y2): return True; else: False'
        if(((x-x1)**2 + (y-y1)**2)**(1/2) < ((x-x2)**2 + (y-y2)**2)**(1/2)):
            return True
        else:
            return False

    def getCrossPoint(self, x1, y1, x2, y2, R):
        #return crossPoint for point and circle as if there was line for point and circle center
        result = PointList()
        if(self.getDistance(x1, y1, x2, y2) == R):
            #print('distance = R')
            result.addPoint(x1, y1)
            result.setLightCoef(True)
            return result
        elif (self.getDistance(x1, y1, x2, y2) == 0):
            #print('distance = 0')
            result.setLightCoef(False)
            return result
        elif((x1-x2)**2==(y1-y2)**2):
            #print('Point 1, Point 2 vector have any axis angle 45')
            if ((x1<x2)&(y1<y2))|((x2<x1)&(y2<y1)):
                if (self.getDistance(x1, y1, x2, y2) > R):
                    if(x1 < x2):
                        result.addPoint(x2 - (R/(2**(1/2))), y2 - (R/(2**(1/2))))
                        result.setLightCoef(True)
                        return result
                    elif(x1 > x2):
                        result.addPoint(x2 + (R/(2**(1/2))), y2 + (R/(2**(1/2))))
                        result.setLightCoef(True)
                        return result
                else:
                    result.setLightCoef(False)
                    return result
            elif ((x1<x2)&(y1>y2))|((x2<x1)&(y2>y1)):
                if (self.getDistance(x1, y1, x2, y2) > R):
                    if (x1 > x2):
                        result.addPoint(x2 + (R/(2**(1/2))), y2 - (R/(2**(1/2))))
                        result.setLightCoef(True)
                        return result
                    elif (x2 > x1):
                        result.addPoint(x2 - (R/(2**(1/2))), y2 + (R/(2**(1/2))))
                        result.setLightCoef(True)
                        return result
                else:
                    result.setLightCoef(False)
                    return result
        elif ((x1 != x2) & (y1 != y2))&(self.getDistance(x1, y1, x2, y2)>R):
            #print('quadratic equation')
            #D = ((1/((x2-x1)**2))-2*x2)**2 - 4*(1+(((y2-y1)**2)/((x2-x1)**2)))*((x2**2)*((((y2-y1)**2)/((x2-x1)**2))+1)-R)
            resultYList = []
            D = 4*((y2)**2)*((y1-y2)**2-(x1-x2)**2)**2-4*((x1-x2)**2+(y1-y2)**2)*(((x1-x2)**2*((y1-y2)**2-y1)**2)+(y2**2-R**2)*(y1-y2)**2)
            resultYList.append(((-1)*(y2*((y1-y2)**2-(x1-x2)**2))+D**(1/2))/(2*((x1-x2)**2-(y1-y2)**2)))
            #resultXList.append((((-1)*((1/((x2-x1)**2))-2*x2))+D)/(2*(1+((y2-y1)**2/(x2-x1)**2))))
            resultYList.append(((-1)*(y2*((y1-y2)**2-(x1-x2)**2))-D**(1/2))/(2*((x1-x2)**2-(y1-y2)**2)))
            resultY = 0
            #print ('ResultYList', resultYList[0].real, resultYList[1].real)
            if self.isSmaller((resultYList[0].real - y1), (resultYList[1].real - y1)):
                resultY = resultYList[0].real
            else:
                resultY = resultYList[1].real
            resultX = (((x1-x2)*(resultY-y1))/(y1-y2)) + x1
            result.addPoint(resultX, resultY)
            result.setLightCoef(True)
            return result
        elif (abs(y2-y1)>=R) & (x1==x2):
            #print('x1=x2 and vector distance more than R')
            resultY = y2 - R
            resultX = x1
            result.addPoint(resultX, resultY)
            result.setLightCoef(True)
            return result
        elif (abs(x2-x1)>=R) & (y1==y2): 
            #(y1 == y2):
            #print('y1=y2 and vector distance more than R')
            resultX = x2-R
            resultY = y1
            result.addPoint(resultX, resultY)
            result.setLightCoef(True)
            return result
        else:
            result.setLightCoef(False)
            return result

    def checkContact(self, mirrorX, mirrorY, originalPipeIndex):
        #return True or False
        #print ('pipepointList len', self.pipePointList.getLen())
        originalCrossPointList = self.getCrossPoint(mirrorX, mirrorY, self.pipePointList.getPointX(originalPipeIndex), self.pipePointList.getPointY(originalPipeIndex), self.pipeRadius)
        for pipeIndex in range (self.pipePointList.getLen()):
            if(pipeIndex == originalPipeIndex):
                break
            if (originalCrossPointList.getLightCoef()):
                if(self.checkCloser(mirrorX, mirrorY, originalCrossPointList.getPointX(0), originalCrossPointList.getPointY(0), self.pipePointList.getPointX(pipeIndex), self.pipePointList.getPointY(pipeIndex))):
                    return False
        return True

    def getDistance(self, x1, y1, x2, y2):
        # return distance between two points
        result = ((x1-x2)**2+(y1-y2)**2)**(1/2)
        #print ('Coordinates', x1, y1, x2, y2)
        #print ('Distance', result)
        
        return result
       
    def getSum(self, angleList):
        # return sum of angle differences in angleList
        sum = 0
        for angleIndex in range (angleList.getLen()):
            sum += abs(angleList.getPointY(angleIndex) - angleList.getPointX(angleIndex))
        return sum
        
    def takeNeighbourPoints(self, x1, y1, x2, y2):
        neighbourPointList = PointList()
        if (((y1==y2)&(x1==x2))|(x1==x2)):
            neighbourPointList.addPoint(x1, y1+1)
            neighbourPointList.addPoint(x1, y1-1)
            return neighbourPointList
        if y1==y2:
            neighbourPointList.addPoint(x1+1, y1)
            neighbourPointList.addPoint(x1-1, y1)
            return neighbourPointList
        k = math.tan(math.atan((y1-y2)/(x1-x2))-90)
        yn = (-1)*k+y1
        xn = ((yn-y1)/k) + x1
        neighbourPointList.addPoint(xn, yn)
        yn = k+y1
        xn = ((yn-y1)/k) + x1
        neighbourPointList.addPoint(xn, yn)
        return neighbourPointList
        
    def usefulReflectiveSpace(self):
        # return lightCoefSum
        lightCoefSum = []
        for mirrorPointIndex in range (self.mirrorSpacePointList.getLen()):
            lightCoefSum.append(0)
            neighbourPointList = []
            
            mirrorTiltAngleList = []
            for pipePointIndex in range(self.pipePointList.getLen()):
                #need some pipePoints
                neighbourPointList.append(self.takeNeighbourPoints(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), self.pipePointList.getPointX(pipePointIndex), self.pipePointList.getPointX(pipePointIndex)))
                if (neighbourPointList[pipePointIndex].getPointX(0) - self.mirrorSpacePointList.getPointX(mirrorPointIndex)) > 0:
                    mirrorTiltAngleList.append(math.atan(self.getDistance(neighbourPointList[pipePointIndex].getPointX(0), self.mirrorSpacePointList.getPointY(mirrorPointIndex), neighbourPointList[pipePointIndex].getPointX(0), neighbourPointList[pipePointIndex].getPointY(0))/(neighbourPointList[pipePointIndex].getPointX(0) - self.mirrorSpacePointList.getPointX(mirrorPointIndex))))
                elif (neighbourPointList[pipePointIndex].getPointX(0) - self.mirrorSpacePointList.getPointX(mirrorPointIndex)) == 0:
                    mirrorTiltAngleList.append(90)
                else:
                    mirrorTiltAngleList.append(math.atan(self.getDistance(neighbourPointList[pipePointIndex].getPointX(1), self.mirrorSpacePointList.getPointY(mirrorPointIndex), neighbourPointList[pipePointIndex].getPointX(1), neighbourPointList[pipePointIndex].getPointX(1))/(neighbourPointList[pipePointIndex].getPointX(1) - self.mirrorSpacePointList.getPointX(mirrorPointIndex))))
            tiltAngleList = []
            halfOfContactAngleList = []
            for pipeIndex in range (self.pipePointList.getLen()):
                if(self.checkContact(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), pipeIndex)):
                    closerNeighbourList = PointList()
                    if self.checkCloser(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), neighbourPointList[pipeIndex].getPointX(0), neighbourPointList[pipeIndex].getPointY(0), neighbourPointList[pipeIndex].getPointX(1), neighbourPointList[pipeIndex].getPointY(1)):
                        closerNeighbourList.addPoint(neighbourPointList[pipeIndex].getPointX(0), neighbourPointList[pipeIndex].getPointY(0))
                    else:
                        closerNeighbourList.addPoint(neighbourPointList[pipeIndex].getPointX(1), neighbourPointList[pipeIndex].getPointY(1))
                    mirrorPointAndProectedPipePointDistance = ((self.pipePointList.getPointX(pipeIndex)-self.mirrorSpacePointList.getPointX(mirrorPointIndex))**2+(self.pipePointList.getPointY(pipeIndex)-self.mirrorSpacePointList.getPointY(mirrorPointIndex))**2-(((self.pipePointList.getPointX(pipeIndex) - self.mirrorSpacePointList.getPointX(mirrorPointIndex))**2*closerNeighbourList.getPointX(0)**2+(self.pipePointList.getPointY(pipeIndex) - self.mirrorSpacePointList.getPointY(mirrorPointIndex))**2*closerNeighbourList.getPointY(0)**2)/(closerNeighbourList.getPointX(0)**2+closerNeighbourList.getPointY(0)**2)))**(1/2)
                    #print ('Distance 1 = ', mirrorPointAndProectedPipePointDistance)
                    #print ('Distance 2 = ', self.getDistance(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), self.pipePointList.getPointX(pipeIndex), self.pipePointList.getPointY(pipeIndex)))
                    #print ('Sin tilt angle', mirrorPointAndProectedPipePointDistance/self.getDistance(mirrorSpacePointList.getPointX(mirrorPointIndex), mirrorSpacePointList.getPointY(mirrorPointIndex), pipePointList.getPointX(pipeIndex), pipePointList.getPointY(pipeIndex)))
                    if (self.getDistance(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), self.pipePointList.getPointX(pipeIndex), self.pipePointList.getPointY(pipeIndex)) != 0):
                        tiltAngleList.append(math.degrees(math.asin((mirrorPointAndProectedPipePointDistance/self.getDistance(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), self.pipePointList.getPointX(pipeIndex), self.pipePointList.getPointY(pipeIndex))).real)))
                        halfOfContactAngleList.append(math.degrees(math.atan(self.pipeRadius/self.getDistance(self.mirrorSpacePointList.getPointX(mirrorPointIndex), self.mirrorSpacePointList.getPointY(mirrorPointIndex), self.pipePointList.getPointX(pipeIndex), self.pipePointList.getPointY(pipeIndex)))))
                        #print ('TiltAngleList', tiltAngleList, 'mirrorIndex', mirrorPointIndex)
                        #print ('halfOfContactAngleList', halfOfContactAngleList)
            for angle in range (self.angleBefore, self.angleAfter+1):
                for tiltAngleIndex in range (len(tiltAngleList)):
                    if angle > mirrorTiltAngleList[tiltAngleIndex]:
                        reflectedAngle = 0
                    if angle == mirrorTiltAngleList[tiltAngleIndex] + 90:
                        reflectedAngle = mirrorTiltAngleList[tiltAngleIndex] + 90
                    else:
                        reflectedAngle = 180 + mirrorTiltAngleList[tiltAngleIndex] - angle
                    if (reflectedAngle >= tiltAngleList[tiltAngleIndex] - halfOfContactAngleList[tiltAngleIndex]) & (reflectedAngle <= tiltAngleList[tiltAngleIndex] + halfOfContactAngleList[tiltAngleIndex]):
                        lightCoefSum[mirrorPointIndex] += 1
                        #print ('true light coef')
        return lightCoefSum
    
    def saveData(self, lightCoefSum):
        # return mirrorSpacePointData, sumLightCoefList
        self.mirrorSpacePointData.addPoint(self.mirrorSpacePointList.getListX(), self.mirrorSpacePointList.getListY())
        self.sumLightCoefList.append(lightCoefSum)
        
    def wallowMirrorSpace(self):
        # return downsideCheck and mirrorSpacePointList
        descentY = 0
        if(self.mirrorLength >= 100):
            descentY = 1
        else:
            descentY = self.mirrorLength/100
        self.downsideCheck = 0
        for spaceIndex in range (self.mirrorSpacePointList.getLen()):
            if(self.mirrorSpacePointList.getPointX(spaceIndex) <= self.extremeDepthFunctionList[6]):
                if(self.mirrorSpacePointList.getPointY(spaceIndex) == (self.extremeDepthFunctionList[0]*(self.mirrorSpacePointList.getPointX(spaceIndex)-self.extremeDepthFunctionList[1])+self.extremeDepthFunctionList[2])) | (descentY > abs((self.extremeDepthFunctionList[0]*(self.mirrorSpacePointList.getPointX(spaceIndex)-self.extremeDepthFunctionList[1])+self.extremeDepthFunctionList[2])-self.mirrorSpacePointList.getPointY(spaceIndex))):
                    self.downsideCheck += 1
                else:
                    self.mirrorSpacePointList.changePoint(spaceIndex, self.mirrorSpacePointList.getPointX(spaceIndex), self.mirrorSpacePointList.getPointY(spaceIndex) - descentY)
            elif (self.mirrorSpacePointList.getPointX(spaceIndex) >= self.extremeDepthFunctionList[8]):
                if(self.mirrorSpacePointList.getPointY(spaceIndex) == (self.extremeDepthFunctionList[3]*(self.mirrorSpacePointList.getPointX(spaceIndex)-self.extremeDepthFunctionList[4])+self.extremeDepthFunctionList[5])) | (descentY > abs((self.extremeDepthFunctionList[3]*(self.mirrorSpacePointList.getPointX(spaceIndex)-self.extremeDepthFunctionList[4])+self.extremeDepthFunctionList[5])-self.mirrorSpacePointList.getPointY(spaceIndex))):
                    self.downsideCheck += 1
                else:
                    self.mirrorSpacePointList.changePoint(spaceIndex, self.mirrorSpacePointList.getPointX(spaceIndex), self.mirrorSpacePointList.getPointY(spaceIndex) - descentY)
            elif (self.mirrorSpacePointList.getPointX(spaceIndex) < self.extremeDepthFunctionList[8]) & (self.mirrorSpacePointList.getPointX(spaceIndex)>self.extremeDepthFunctionList[6]):
                if(abs(self.extremeDepthFunctionList[7]-self.mirrorSpacePointList.getPointY(spaceIndex)) == descentY) | (descentY > abs(self.extremeDepthFunctionList[7]-self.mirrorSpacePointList.getPointY(spaceIndex))):
                    self.downsideCheck += 1
                else:
                    self.mirrorSpacePointList.changePoint(spaceIndex, self.mirrorSpacePointList.getPointX(spaceIndex), self.mirrorSpacePointList.getPointY(spaceIndex) - descentY)

        
    def bestDecisionSearch(self):
        # return mirrorSpacePointList
        mirrorBestSpacePoint = PointList()
        for mirrorPointIndex in range (self.mirrorSpacePointList.getLen()):
            maxLightCoefIndex = -1
            mirrorLightCoef = []
            for lightIndex in range (len(self.sumLightCoefList)):
                mirrorLightCoef.append(self.sumLightCoefList[lightIndex][mirrorPointIndex])
            maxLightCoefIndex = mirrorLightCoef.index(max(mirrorLightCoef))#self.sumLightCoefList.index(max(self.sumLightCoefList))
            listX = self.mirrorSpacePointData.getPointX(maxLightCoefIndex)
            listY = self.mirrorSpacePointData.getPointY(maxLightCoefIndex)
            mirrorBestSpacePoint.addPoint(listX[mirrorPointIndex], listY[mirrorPointIndex])
        self.mirrorSpacePointList = mirrorBestSpacePoint
        
    def printMirrorSpacePointData(self):
        for mirrorSpPD in range(self.mirrorSpacePointData.getLen()):
            print('Mirror space point data lists')
            print(self.mirrorSpacePointData.getListX(), self.mirrorSpacePointData.getListY())
            print('Light coef sum list')
            print(self.sumLightCoefList)
        