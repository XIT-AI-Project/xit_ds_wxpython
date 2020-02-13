#!/usr/bin/env python

import wx
import wx.adv
from sympy import *
from xit_matrixunit import *
from xit_Global import *
from xit_UI_menu import MyMenuControl
#---------------------------------------------------------------------------

class xit_MyTripleElementScrolledWindow(wx.ScrolledWindow):

    def __init__(self, parent,myxitMatrix=xitMatrix(3,3,[0,0,0,0,0,0,0,0,0])):
        wx.ScrolledWindow.__init__(self, parent, id=-1,style=wx.HSCROLL|wx.VSCROLL|wx.DEFAULT_FRAME_STYLE)
        self.SetScrollbars(1,1,300,200)
        self._myxitMatrix=myxitMatrix
       
        winids = []
       

        # A window to the left of the client window
        leftwin1 =  wx.adv.SashLayoutWindow(
                self, -1, wx.DefaultPosition, (0, 30),
                wx.NO_BORDER|wx.adv.SW_3D
                )

        leftwin1.SetDefaultSize((620, 1000))
        leftwin1.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        leftwin1.SetAlignment(wx.adv.LAYOUT_LEFT)
        #leftwin1.SetBackgroundColour(wx.Colour(0, 255, 0))
        leftwin1.SetSashVisible(wx.adv.SASH_RIGHT, True)
        leftwin1.SetExtraBorderSize(5)
        self._preText = wx.TextCtrl(
                        leftwin1, -1, "", wx.DefaultPosition, wx.DefaultSize,
                        wx.TE_MULTILINE|wx.HSCROLL|wx.SUNKEN_BORDER
                        )
        self._preText.SetFont(xit_G.G_fontandcolour._prefont)
        self._preText.SetForegroundColour(xit_G.G_fontandcolour._precolour)
        self._preText.SetValue("前置字符串")
        if hasattr(myxitMatrix,"presrc"):
            self._preText.SetValue(myxitMatrix.presrc)

        
        leftwin1.Bind(wx.EVT_CONTEXT_MENU, MyMenuControl(self,"前置字符串").OnContextMenu)

        self.leftWindow1 = leftwin1
        winids.append(leftwin1.GetId())


        # Another window to the left of the client window
        leftwin2 = wx.adv.SashLayoutWindow(
                self, -1, wx.DefaultPosition, (0, 30),
                wx.NO_BORDER|wx.adv.SW_3D
                )

        leftwin2.SetDefaultSize((420, 1000))
        leftwin2.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        leftwin2.SetAlignment(wx.adv.LAYOUT_LEFT)
        #leftwin2.SetBackgroundColour(wx.Colour(0, 255, 255))
        leftwin2.SetSashVisible(wx.adv.SASH_RIGHT, True)
        leftwin2.SetExtraBorderSize(5)
        leftwin2.Bind(wx.EVT_CONTEXT_MENU, MyMenuControl(self,"矩阵").OnContextMenu)
        self._myxitmatrixText=wx.TextCtrl(leftwin2,-1,style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)

        self._myxitmatrixText.SetFont(xit_G.G_fontandcolour._middlefont)
        self._myxitmatrixText.SetForegroundColour(xit_G.G_fontandcolour._middlecolour)
     
        self._myxitmatrixText.SetValue("矩阵")
        if myxitMatrix!=None:
            self._myxitmatrixText.SetValue(str(myxitMatrix))
        self.leftWindow2 = leftwin2
        winids.append(leftwin2.GetId())

        # will occupy the space not used by the Layout Algorithm
        self.remainingSpace = wx.adv.SashLayoutWindow(
                self, -1, wx.DefaultPosition, (0, 30),
                wx.NO_BORDER|wx.adv.SW_3D
                )
        self._postText=wx.TextCtrl(self.remainingSpace,-1,style=wx.TE_MULTILINE|wx.HSCROLL)

        self._postText.SetFont(xit_G.G_fontandcolour._postfont)
        self._postText.SetForegroundColour(xit_G.G_fontandcolour._postcolour)
        
        self._postText.SetValue("后置字符串")
        if hasattr(myxitMatrix,"postsrc"):
            self._postText.SetValue(myxitMatrix.postsrc)

        self.remainingSpace.Bind(wx.EVT_CONTEXT_MENU, MyMenuControl(self,"后置字符串").OnContextMenu)

        self.Bind(
            wx.adv.EVT_SASH_DRAGGED_RANGE, self.OnSashDrag,
            id=min(winids), id2=max(winids)
            )

        self.Bind(wx.EVT_SIZE, self.OnSize)

    def setMyText(self,myxitMatrix=None):
        self._preText.SetValue("前置字符串")
        self._myxitmatrixText.SetValue("矩阵")
        self._postText.SetValue("后置字符串")
        if myxitMatrix==None:
            return
        if hasattr(myxitMatrix,"presrc"):
            self._preText.SetValue(myxitMatrix.presrc)
        self._myxitmatrixText.SetValue(str(myxitMatrix))
        if hasattr(myxitMatrix,"postsrc"):
            self._postText.SetValue(myxitMatrix.postsrc)
    def OnSashDrag(self, event):
        if event.GetDragStatus() == wx.adv.SASH_STATUS_OUT_OF_RANGE:
            
            return

        eobj = event.GetEventObject()

        if  eobj is self.leftWindow1:
            
            self.leftWindow1.SetDefaultSize((event.GetDragRect().width, 1000))


        elif eobj is self.leftWindow2:
            
            self.leftWindow2.SetDefaultSize((event.GetDragRect().width, 1000))

        

        wx.adv.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
        self.remainingSpace.Refresh()

    def OnSize(self, event):
        wx.adv.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
    
   

#---------------------------------------------------------------------------
class myFrame(wx.Frame):
    def __init__(self,parent,id=-1):
        wx.Frame.__init__(self,parent,id=id,size=wx.Size(900,600))
        o=xit_MyTripleElementScrolledWindow(self)
        #self.SetSizer(o.sizer_element)
        self.Update()

if __name__ == '__main__':
    app=wx.App()
    frame = myFrame(parent=None)
    frame.Show()
    app.MainLoop() 

#---------------------------------------------------------------------------





