'''
        编写人：王晓峰
        编写时间：2010年1月26日
        类：xit_MyMatrixTable、xit_MyGrid_OP
        功能：1.生成全局MatrixUnit和Grid，其中有针对Grid的操作
'''
import wx
import wx.grid
import random
from sympy import *
from xit_matrixunit import *
from xit_Global import xit_G

#-----xit_MyMatrixTable----------------------------------------------------------------------------------------------
'''
    类：xit_MyMatrixTable
    功能：生成grid需要的table,供grid存储数据使用，其中数据主要由初始化时的myMatrix提供
    说明：初始化时必须提供myMatrix
'''
class xit_MyMatrixTable(wx.grid.PyGridTableBase):
    def __init__(self,myMatrix):
        wx.grid.GridTableBase.__init__(self)
        self.data=myMatrix
    def GetNumberRows(self):
        return self.data.rows
    def GetNumberCols(self):
        return self.data.cols
    def IsEmptyCell(self,row,col):
        return str(self.data[row,col])==""
    def GetValue(self,row,col):
        value=self.data[row,col]
        if value is not None:
            return value
        else:
            return ""
    def SetValue(self,row,col,value):
        self.data[row,col]=value
    def GetColLabelValue(self,col):#列标签
        return "第"+str(col)+"列"
    def GetRowLabelValue(self,row):#行标签
        return "第"+str(row)+"行"

#-----xit_MyGrid_OP------------------------------------------------------------------------------------------------------
'''
    类：xit_MyGrid
    功能：1.主要保存myMatrixUnit和Grid，在各个类之间传递信息；2.含有较多的Grid类别操作，对网格进行的增删改方法在这里定义
    初始化各参数说明：
        1.parent:一般parent参数应该保存最外层的窗体（是否是Grid的父亲目前不是很重要），在某些情况下，可能需要对窗体进行刷新
        2.myMatrixUnit:在整个系统中，凡是myMatrixUnit被更改掉，需要及时通知到该类，但建议用方法setxitGrid通知
        3.grid:当前用来操作的grid
        4.cur:myMatrixUnit中的cur，这里单列出来是表示如果不一致，可在这里修改，即这里的cur是更新后的cur
'''
class xit_MyGrid(wx.grid.Grid):
    def __init__(self,parent,myMatrix=xitMatrix(3,3,[0,0,0,0,0,0,0,0,0])):
        wx.grid.Grid.__init__(self,parent,id=-1,style=wx.HSCROLL|wx.VSCROLL)
        self._myMatrix=myMatrix
        self._table=xit_MyMatrixTable(myMatrix)
        self.SetTable(self._table,True)
        
        self.SetDefaultCellFont(wx.Font(wx.FontInfo(20).FaceName("新宋体")))
        self.setSmartSize()
        self.SetDefaultColSize(50,resizeExistingCols=False)
        self.SetDefaultRowSize(50,resizeExistingRows=False)
        self.AutoSize()
        parent.Bind(wx.grid.EVT_GRID_CELL_CHANGED,self.ContentChange,self)
    def ContentChange(self,evt):
        print(pretty(self._table.data))
        xit_G.G_myOP.updateMatrix(self._table.data)
    def execommand(self,command,*args):
        re= getattr(self, command)(*args)
        return re

    #setSmartSize用来在更改了grid之后，重新计算grid的大小，通常在setxitGrid方法中被调用
    def setSmartSize(self):
        self.AutoSize()
        rowsN=self.GetNumberRows()
        rowsMax=self.GetRowSize(0)
        for i in range(1,rowsN):
            rowSize=self.GetRowSize(i)
            if rowsMax<rowSize:
                rowsMax=rowSize
        colsN=self.GetNumberCols()
        colsMax=self.GetColSize(0)
        for i in range(1,colsN):
            colSize=self.GetColSize(i)
            if colsMax<colSize:
                colsMax=colSize
        self.SetDefaultColSize(colsMax,resizeExistingCols=True)
        self.SetDefaultRowSize(rowsMax,resizeExistingRows=True)

    def setGrid(self,cur=0,myMatrix=None):#这个方法是外界经常调用的方法，用来根据参数myMatrix设置新的grid，同时保存新的myMatrixUnit
        self.ClearGrid()
        self._myMatrix=myMatrix
        self._table=xit_MyMatrixTable(myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.Fit()
  

    def initZero(self,row,col):
        self._myMatrix=xitMatrix(row,col,zeros(row,col))
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.FitInside()
        return self._myMatrix
    def reShape(self,row,col):
        M=self._myMatrix
        self._myMatrix=M.reshape(row,col)
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        return self._myMatrix
    def addRow(self,row,element="0"):
        M=self._myMatrix
        self._myMatrix=xitMatrix(M.row_insert(row,zeros(1,M.cols)))
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.Fit()
        return self._myMatrix
    def addCol(self,col,element="0"):
        M=self._myMatrix
        self._myMatrix=xitMatrix(M.col_insert(col,zeros(M.rows,1)))
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.Fit()
        return self._myMatrix
    def delRow(self,row):
        M=self._myMatrix
        M.row_del(row)
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.Fit()
        return self._myMatrix
    def delCol(self,col):
        M=self._myMatrix
        M.col_del(col)
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.Fit()
        return self._myMatrix
    def updateOnes(self,elem):
        M=self._myMatrix
        self._myMatrix=xitMatrix(Rational(str(elem))*ones(M.rows,M.cols))
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.FitInside()
        return self._myMatrix
    def updateRandom(self,minv,maxv):
        tmpList=[]
        M=self._myMatrix
        for i in range(M.rows):
            for j in range(M.cols):
                tmpList.append(random.randint(minv,maxv))
                
        self._myMatrix=xitMatrix(M.rows,M.cols,tmpList)
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.FitInside()
        return self._myMatrix
    def updataRange(self,start,step):
        tmpList=[]
        M=self._myMatrix
        count=Rational(start)
        for i in range(M.rows):
            for j in range(M.cols):
                tmpList.append(count)
                count +=Rational(step)
        self._myMatrix=xitMatrix(M.rows,M.cols,tmpList)
        self._table=xit_MyMatrixTable(self._myMatrix)
        self.SetTable(self._table,True)
        self.setSmartSize()
        self.ForceRefresh()
        self.FitInside()
        return self._myMatrix
