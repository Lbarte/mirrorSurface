# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:38:43 2017

@author: Foxart
"""

class PointList:
    

    def __init__(self):
        self.pointXList = []
        self.pointYList = []

    def getPointX(self, pointXIndex):
        return self.pointXList[pointXIndex]

    def getPointY(self, pointYIndex):
        return self.pointYList[pointYIndex]

    def addPoint(self, pointX, pointY):
        self.pointXList.append(pointX)
        self.pointYList.append(pointY)
        
    def changePoint(self, pointIndex, newPointX, newPointY):
        self.pointXList[pointIndex] = newPointX
        self.pointYList[pointIndex] = newPointY
        
    def getLen(self):
        return len(self.pointXList)
        
    def getListX(self):
        return self.pointXList
        
    def getListY(self):
        return self.pointYList
        
    def setList(self, listX, listY):
        self.pointXList = []
        self.pointXList = listX
        self.pointYList = []
        self.pointYList = listY
        
    def setLightCoef(self, lightCoef):
        self.lightCoef = lightCoef
        
    def getLightCoef(self):
        return self.lightCoef