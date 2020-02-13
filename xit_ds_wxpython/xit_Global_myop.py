'''
        编写人：王晓峰
        编写时间：2020年1月16日
        类：xit_MyMatrixTable、xit_MyGrid_OP
        功能：1.生成全局MatrixUnit和Grid，其中有针对Grid的操作
'''
import wx
import wx.grid
from sympy import *
from xit_matrixunit import *
from xit_Global import *
from xit_main import xit_MyCenterTextNotebook

#-----xit_MyGrid_OP------------------------------------------------------------------------------------------------------
'''
    
'''
class xit_MyOP():
    def __init__(self,myMatrixUnit=xitMatrixUnit(matList=[xitMatrix(3,3,[0,0,0,0,0,0,0,0,0])]),\
                 myCenterTextNotebook=None,cur=0,grid=None,tree=None,treedict=None,menudict=None,\
                 mainwindow=None):
        self._myMatrixUnit=myMatrixUnit
        self._myMatrixUnit.cur=cur
        self._notebook=myCenterTextNotebook
        self._grid=grid
        self._tree=tree
        self._treedict=treedict
        self._menudict=menudict
        self._mainwindow=mainwindow
       
        
    def execommand(self,command,*args):
        re= getattr(self, command)(*args)
        return re
    
    def setFromxitMatrixUnit(self,xitMatrixUnit,cur=0):
        self._myMatrixUnit=xitMatrixUnit
        self._myMatrixUnit.cur=cur
        if cur!="ZERO":
            self._grid.setGrid(cur,xitMatrixUnit[cur])
        self._notebook.setALLPagesFromMatrixUnit(xitMatrixUnit)

    def setUnitAndGridFromCUR(self,cur="ZERO"):
        self._myMatrixUnit.cur=cur
        if cur!="ZERO":
            self._grid.setGrid(cur,self._myMatrixUnit[cur])
    def initMatrixUnit(self,row,col):
        self.setFromxitMatrixUnit(xitMatrixUnit=xitMatrixUnit(matList=[xitMatrix(zeros(row,col))]),cur=0)
        return self._myMatrixUnit
    def initFirstMatrix(self):
        self._myMatrixUnit._mat=self._myMatrixUnit.ShowMatrixUnitAll()
        self._myMatrixUnit.cur="ZERO"
        
        return self._myMatrixUnit
    def insertMatrix(self,pos):
        cur=pos
        n=len(self._myMatrixUnit)
        if cur<0 or cur>n:return self._myMatrixUnit
        M=xitMatrix(3,3,[0,0,0,0,0,0,0,0,0])
        self._myMatrixUnit.matList.insert(cur,M)
        self.setFromxitMatrixUnit(self._myMatrixUnit,cur)
        return self._myMatrixUnit
    def deleteMatrix(self):
        cur=self._myMatrixUnit.cur
        n=len(self._myMatrixUnit)
        if cur=="ZERO":
            del self._myMatrixUnit[0]
        elif cur<0 or cur>=n-1:
            return self._myMatrixUnit
        else:
            del self._myMatrixUnit[cur+1]
        self.setFromxitMatrixUnit(self._myMatrixUnit,cur)
        return self._myMatrixUnit
    def updateMatrix(self,myMatrix):
        cur=self._myMatrixUnit.cur
        self._myMatrixUnit[cur]=myMatrix
        self._notebook.setSelectionPageFromMatrix(self._myMatrixUnit[cur])
        return self._myMatrixUnit

