import wx
import os
import pickle
from xit_Global_myop import *
from xit_Global import *

class MyFileOP():
    def savedefault(self,filename="mytreedefault.dat"):
        f=open(filename,"wb")
        parent=xit_G.G_myOP._treedict["MYTREE"]
        item,cookie=xit_G.G_myOP._tree.GetFirstChild(parent)
        while item:
            _unit=xit_G.G_myOP._tree.GetItemData(item)
            _unit.Riddle=xit_G.G_myOP._tree.GetItemText(item)
            pickle.dump(_unit,f)
            item,cookie=xit_G.G_myOP._tree.GetNextChild(parent,cookie)
        f.close()
    def deletemytree(self):
        item=xit_G.G_myOP._treedict["MYTREE"]
        xit_G.G_myOP._tree.DeleteChildren(item)
    def union_onefile(self,filename):
        f=open(filename,"rb")
        while True:
            if f==None:
                break
            _unit=pickle.load(f)
            if _unit==None:
                break
            tmp=xit_G.G_myOP._tree.AppendItem(xit_G.G_myOP._treedict["MYTREE"], _unit.Riddle,1,data="")
            xit_G.G_myOP._tree.SetItemData(tmp,_unit)
        f.close()    
    def opendefault(self):
        dlg = wx.FileDialog(
            xit_G.G_myOP._tree, message="请选择您要加载的文件",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="树数据文件 (*.dat)|*.dat|"     \
                     "所有文件 (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW )
        if dlg.ShowModal() == wx.ID_OK:
           self.deletemytree()
           paths = dlg.GetPaths()
           for filename in paths:
               self.union_onefile(filename)     
        dlg.Destroy()
    def openunion(self):
        dlg = wx.FileDialog(
            xit_G.G_myOP._tree, message="请选择您要加载的文件",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="树数据文件 (*.dat)|*.dat|"     \
                     "所有文件 (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW )
        if dlg.ShowModal() == wx.ID_OK:
           paths = dlg.GetPaths()
           for filename in paths:
               self.union_onefile(filename)     
        dlg.Destroy()
    def saveas(self):
        dlg = wx.FileDialog(
            xit_G.G_myOP._tree, message="文件保存至 ...", defaultDir=os.getcwd(),
            defaultFile="", wildcard="树数据文件 (*.dat)|*.dat|"     \
                     "所有文件 (*.*)|*.*", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) 
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        dlg.Destroy()
        self.savedefault(path)
class MyMenuControl():
    def __init__(self,window=None,string=None):
        self._window=window
        self._string=string
    def execommand(self,command,*args):
        re= getattr(self, command)(*args)
        return re
    def Control(self,event):
        menuname=xit_G.G_myOP._menudict[event.GetId()].GetName()
        if menuname=="新建(N)":
            xit_G.G_myOP.initMatrixUnit(3,3)
        elif menuname=="打开...":
            MyFileOP().opendefault()
        elif menuname=="合并打开...":
            MyFileOP().openunion()
        elif menuname=="保存":
            MyFileOP().savedefault()
        elif menuname=="另存为...":
            MyFileOP().saveas()
        elif menuname==self._string+"字体设置...":
            data=wx.FontData()
            data.EnableEffects(True)
            win=None
            if self._string=="前置字符串":
                win=xit_G.G_myOP._notebook._pageList[1]._preText
                data.SetColour(xit_G.G_fontandcolour._precolour)
                data.SetInitialFont(xit_G.G_fontandcolour._prefont)
                dlg = wx.FontDialog(win, data)
                if dlg.ShowModal() == wx.ID_OK:
                    data = dlg.GetFontData()
                    font = data.GetChosenFont()
                    colour = data.GetColour()
                    win.SetFont(font)
                    win.SetForegroundColour(colour)
                    xit_G.G_fontandcolour._prefont=font
                    xit_G.G_fontandcolour._precolour=colour
            elif self._string=="后置字符串":
                win=xit_G.G_myOP._notebook._pageList[1]._postText
                data.SetColour(xit_G.G_fontandcolour._postcolour)
                data.SetInitialFont(xit_G.G_fontandcolour._postfont)
                dlg = wx.FontDialog(win, data)
                if dlg.ShowModal() == wx.ID_OK:
                    data = dlg.GetFontData()
                    font = data.GetChosenFont()
                    colour = data.GetColour()
                    win.SetFont(font)
                    win.SetForegroundColour(colour)
                    xit_G.G_fontandcolour._postfont=font
                    xit_G.G_fontandcolour._postcolour=colour
            elif self._string=="矩阵":
                win=xit_G.G_myOP._notebook._pageList[1]._myxitmatrixText
                data.SetColour(xit_G.G_fontandcolour._middlecolour)
                data.SetInitialFont(xit_G.G_fontandcolour._middlefont)
                dlg = wx.FontDialog(win, data)
                if dlg.ShowModal() == wx.ID_OK:
                    data = dlg.GetFontData()
                    font = data.GetChosenFont()
                    colour = data.GetColour()
                    win.SetFont(font)
                    win.SetForegroundColour(colour)
                    xit_G.G_fontandcolour._middlefont=font
                    xit_G.G_fontandcolour._middlecolour=colour
           
            print("ok!")

        
    
    def OnContextMenu(self,event):
        
        # make a menu
        context_menu = wx.Menu()
        tmp=context_menu.Append(wx.ID_ANY,self._string+"字体设置...")
        xit_G.G_myOP._menudict[tmp.GetId()]=tmp
        self._window.Bind(wx.EVT_MENU, self.Control, id=tmp.GetId())
        self._window.PopupMenu(context_menu)
        context_menu.Destroy()


    

        
