# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from graphics import *
from MirrorDecision import *
from PointList import *

ZOOM = 5

WINDOWX = 1200
WINDOWY = 650

GRAPHMAXX = 800 #window width
GRAPHMAXY = 600 #window height

ZEROPOINTX = 400
ZEROPOINTY = 300

FRAMEWIDTH = 10

SIDEWINDOWWIDTH = WINDOWX - GRAPHMAXX - FRAMEWIDTH
SIDEWINDOWHEIGHT = WINDOWY - (FRAMEWIDTH*2)

SIDEWINDOWZEROX = GRAPHMAXX + FRAMEWIDTH
SIDEWINDOWZEROY = FRAMEWIDTH

SIDEWINDOWCENTERX = SIDEWINDOWZEROX + (SIDEWINDOWWIDTH/2)

ENTRYHEIGHT = 50

def getZeroPoint():
    return Point(ZEROPOINTX, ZEROPOINTY)
    
def getAxisX():
    return Line(Point(0+FRAMEWIDTH, ZEROPOINTY), 
                Point(GRAPHMAXX-FRAMEWIDTH, ZEROPOINTY))

def getAxisY():
    return Line(Point(ZEROPOINTX, 0+FRAMEWIDTH), 
                Point(ZEROPOINTX, GRAPHMAXY-FRAMEWIDTH))

def getAxisColor():
    return color_rgb(56, 172, 237)
    
def makeLabeledEntry(entryCenterPt, entryWidth, initialStr, labelText, win):
    '''Return an Entry object with specified center, width in characters, and
    initial string value.  Also create a static label over it with
    specified text.  Draw everything in the GraphWin win.
    '''
    entry = Entry(entryCenterPt, entryWidth)
    entry.setText(initialStr)
    entry.draw(win)
    labelCenter = entryCenterPt.clone()
    labelCenter.move(0, 30)
    Text(labelCenter,labelText).draw(win)
    return entry
    
def drawSheet(win):
    for sheetIndexX in range (ZEROPOINTX-(GRAPHMAXX-ZEROPOINTX), GRAPHMAXX, 10*ZOOM):
        sheetLineX = Line(Point(sheetIndexX, ZEROPOINTY-(GRAPHMAXY-ZEROPOINTY)), Point(sheetIndexX, GRAPHMAXY))
        sheetLineX.setFill('black')
        sheetLineX.draw(win)
    for sheetIndexY in range (ZEROPOINTY-(GRAPHMAXY-ZEROPOINTY), GRAPHMAXY, 10*ZOOM):
        sheetLineY = Line(Point(ZEROPOINTX-(GRAPHMAXX-ZEROPOINTX), sheetIndexY), Point(GRAPHMAXX, sheetIndexY))
        sheetLineY.setFill('black')
        sheetLineY.draw(win)
        
def getZeroPointList():
    zeroPointList = PointList()
    zeroPointList.addPoint(ZEROPOINTX, ZEROPOINTY)
    return zeroPointList
  
def outSet(win, mirrorSpacePointList, pipePointList, pipeRadius):
        # return drawn mirrorSpace and pipe/-s
        for mirrorSpaceIndex in range (mirrorSpacePointList.getLen()):
            mirrorPoint = Point((mirrorSpacePointList.getPointX(mirrorSpaceIndex)-ZEROPOINTX)*(-1)*ZOOM+ZEROPOINTX, (mirrorSpacePointList.getPointY(mirrorSpaceIndex)-ZEROPOINTY)*(-1)*ZOOM+ZEROPOINTY)
            mirrorPoint.draw(win)
        for pipeIndex in range (pipePointList.getLen()):
            pipePoint = Point((pipePointList.getPointX(pipeIndex)-ZEROPOINTX)*ZOOM+ZEROPOINTX, (pipePointList.getPointY(pipeIndex)-ZEROPOINTY)*ZOOM+ZEROPOINTY)
            pipeCircle = Circle(pipePoint, pipeRadius*ZOOM)
            pipeCircle.setFill('red')
            pipeCircle.draw(win)
        listX = mirrorSpacePointList.getListX()
        listY = mirrorSpacePointList.getListY()
        for index in range (len(listX)):
            listX[index] = listX[index] - ZEROPOINTX
            listY[index] = listY[index] - ZEROPOINTY
        resultFile = open("result.txt", "w")
        for index in range (len(listX)):
            resultFile.write('%.10f' % listX[index]);
            resultFile.write(" ");
            resultFile.write('%.10f' % listY[index]);
            resultFile.write("\n");
        resultFile.close()
        
def searchBestMirrorDecision(win, mirrorLength, pipeNumber, pipeDiameter, pipeLayer):
    mirrorDecision = MirrorDecision(mirrorLength, pipeNumber, pipeDiameter, pipeLayer)
    mirrorDecision.pipePositionInSpace(getZeroPointList())
    mirrorDecision.beginEndPointsCalculation()
    mirrorDecision.depthCalculation()
    mirrorDecision.mirrorSpaceFormation()
    mirrorDecision.searchBestMirrorSpace()
    mirrorDecision.bestDecisionSearch()
    mirrorDecision.printMirrorSpacePointData()
    outSet(win, mirrorDecision.mirrorSpacePointList, mirrorDecision.pipePointList, mirrorDecision.pipeRadius)
    
def getParabolaLightCoef(win, mirrorLength, pipeNumber, pipeDiameter, pipeLayer):
    mirror = MirrorDecision(mirrorLength, pipeNumber, pipeDiameter, pipeLayer)
    mirror.pipePositionInSpace(getZeroPointList())
    #mirror.beginEndPointsCalculation()
    #mirror.depthCalculation()
    #mirror.mirrorSpaceFormation()
    #mirror.searchBestMirrorSpace()
    #mirror.bestDecisionSearch()
    mirror.addMirrorSpacePoint(-50, 25-25)
    mirror.addMirrorSpacePoint(-43.75, 19.14-25)
    mirror.addMirrorSpacePoint(-37.50, 14.06-25)
    mirror.addMirrorSpacePoint(-31.25, 9.77-25)
    mirror.addMirrorSpacePoint(-25.0, 6.25-25)
    mirror.addMirrorSpacePoint(-18.75, 3.52-25)
    mirror.addMirrorSpacePoint(-12.5, 1.56-25)
    mirror.addMirrorSpacePoint(-6.25, 0.39-25)
    mirror.addMirrorSpacePoint(0.0, 0.0-25)
    mirror.addMirrorSpacePoint(6.25, 0.39-25)
    mirror.addMirrorSpacePoint(12.5, 1.56-25)
    mirror.addMirrorSpacePoint(18.75, 3.52-25)
    mirror.addMirrorSpacePoint(25.0, 6.25-25)
    mirror.addMirrorSpacePoint(31.25, 9.77-25)
    mirror.addMirrorSpacePoint(37.5, 14.06-25)
    mirror.addMirrorSpacePoint(43.75, 19.14-25)
    mirror.addMirrorSpacePoint(50.0, 25.0-25)
    lightCoef = mirror.usefulReflectiveSpace()
    print('Parabola light coef: ', lightCoef)
    lightCSum = 0
    for lightC in range (len(lightCoef)):
        lightCSum += lightC
    mirror.saveData(lightCSum)
    mirror.printMirrorSpacePointData()
    
    
    
        
def main():
    win = GraphWin('Right side up', WINDOWX, WINDOWY) # give title and dimensions
    
    zeroPoint = getZeroPoint()
    zeroPoint.draw(win)
    
    axisX = getAxisX()
    axisX.setFill(getAxisColor())
    axisX.setWidth(1)
    axisX.draw(win)
    
    axisY = getAxisY()
    axisY.setFill(getAxisColor())
    axisY.setWidth(1)
    axisY.draw(win)
    
    
    
    entry1 = makeLabeledEntry(Point(SIDEWINDOWCENTERX, SIDEWINDOWZEROY), 25,
                          '0', 'Mirror length:', win)
    entry2 = makeLabeledEntry(Point(SIDEWINDOWCENTERX, 
                                    SIDEWINDOWZEROY+ENTRYHEIGHT), 25, '0', 'Number of pipes:', win)
    entry3 = makeLabeledEntry(Point(SIDEWINDOWCENTERX, 
                                    SIDEWINDOWZEROY+(ENTRYHEIGHT*2)), 25,
                          '0', 'Pipe`s diameter', win)
    entry4 = makeLabeledEntry(Point(SIDEWINDOWCENTERX, 
                                    SIDEWINDOWZEROY+(ENTRYHEIGHT*3)), 25,
                          '0', 'Pipe`s air layer size', win)
    #entry5 = makeLabeledEntry(Point(SIDEWINDOWCENTERX, 
    #                                SIDEWINDOWZEROY+(ENTRYHEIGHT*4)), 25,
    #                      '1', 'Zoom', win)
    
    win.getMouse()
    
    #ZOOM = int(entry5.getText())
    
    drawSheet(win)
    
    mirrorLength = int(entry1.getText())
    pipeNumber = int(entry2.getText())
    pipeDiameter = int(entry3.getText())
    pipeLayer = int(entry4.getText())
    
    searchBestMirrorDecision(win, mirrorLength, pipeNumber, pipeDiameter, pipeLayer)
    
    getParabolaLightCoef(win, mirrorLength, pipeNumber, pipeDiameter, pipeLayer)
    
    Str = 'yummy'
    result1 = "Yeap, it is working".format(**locals())
    result2 = "and mirror length: {mirrorLength}".format(**locals())
    Text(Point(SIDEWINDOWZEROX + (SIDEWINDOWWIDTH/2), 
               SIDEWINDOWZEROY+(ENTRYHEIGHT)*4), result1).draw(win)
    Text(Point(SIDEWINDOWZEROX + (SIDEWINDOWWIDTH/2), 
               SIDEWINDOWZEROY+((ENTRYHEIGHT)*4)+25), result2).draw(win)
    win.getMouse()
    win.close()
    
main()