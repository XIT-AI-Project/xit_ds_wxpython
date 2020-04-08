

import pickle
import wx
import wx.grid
import wx.html
import wx.aui as aui
from wx.py.shell import Shell
from xit_matrixunit import *
from xit_Global import *
from xit_Global_myop import *

from xit_UI_tripleTextPanel import xit_MyTripleElementScrolledWindow
from xit_UI_mygrid import *
from xit_UI_downradioPanel import *
from xit_UI_menu import MyMenuControl
from six import BytesIO

  
#----------------------------------------------------------------------
def GetMondrianData():
    return \
b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00qID\
ATX\x85\xed\xd6;\n\x800\x10E\xd1{\xc5\x8d\xb9r\x97\x16\x0b\xad$\x8a\x82:\x16\
o\xda\x84pB2\x1f\x81Fa\x8c\x9c\x08\x04Z{\xcf\xa72\xbcv\xfa\xc5\x08 \x80r\x80\
\xfc\xa2\x0e\x1c\xe4\xba\xfaX\x1d\xd0\xde]S\x07\x02\xd8>\xe1wa-`\x9fQ\xe9\
\x86\x01\x04\x10\x00\\(Dk\x1b-\x04\xdc\x1d\x07\x14\x98;\x0bS\x7f\x7f\xf9\x13\
\x04\x10@\xf9X\xbe\x00\xc9 \x14K\xc1<={\x00\x00\x00\x00IEND\xaeB`\x82'


def GetMondrianBitmap():
    return wx.Bitmap(GetMondrianImage())


def GetMondrianImage():
    stream = BytesIO(GetMondrianData())
    return wx.Image(stream)


def GetMondrianIcon():
    icon = wx.Icon()
    icon.CopyFromBitmap(GetMondrianBitmap())
    return icon




#-----xit_MyCenterTextNotebook---------中心部分的NoteBook,包含有矩阵前页，矩阵第一页、第二页等------------------------------------------------------------------------------------- 
class xit_MyCenterTextNotebook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, -1, style=wx.BK_DEFAULT )
        self._pageList=[]
        textctrlPage=wx.TextCtrl(self,-1,style=wx.TE_MULTILINE|wx.HSCROLL)
        textctrlPage.SetFont(xit_G.G_fontandcolour._firstfont)
        textctrlPage.SetForegroundColour(xit_G.G_fontandcolour._firstcolour)
        self._pageList.append(textctrlPage)
        self.AddPage(textctrlPage, "矩阵前页")
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    

    #用崭新的myMatrixUnit替换所有页面，这适用于矩阵页的完全更换
    def setALLPagesFromMatrixUnit(self,myMatrixUnit):
        cur=myMatrixUnit.cur
        #除首页外，其它页全部删除
        n=self.GetPageCount()
        for i in range(1,n):
            j=n-i
            self.DeletePage(j)
        self._pageList=[self._pageList[0]]

        self._pageList[0].SetValue(str(myMatrixUnit._mat))#首页赋值

        n=len(myMatrixUnit.matList)
               
        for i in range(n):
               
                myTextPage=xit_MyTripleElementScrolledWindow(self,myMatrixUnit[i])
                self._pageList.append(myTextPage)
                name=("第%d个矩阵" %(i+1))
                self.AddPage(myTextPage, name)
        
        if cur=="ZERO":
            self.SetSelection(0)
        else:
            self.SetSelection(cur+1)    
    
    def setSelectionPageFromMatrixUnit(self,myMatrixUnit):
        new=self.GetSelection()
        if new==0:
            self._pageList[0].SetValue(str(myMatrixUnit._mat))
        else:
            self._pageList[new].setMyText(myMatrixUnit[new-1])
    def setSelectionPageFromMatrix(self,myMatrix):
        new=self.GetSelection()
        if new==0:
            self._pageList[0].SetValue(str(myMatrix))
        else:
            self._pageList[new].setMyText(myMatrix)

    def AddPageFromMatrix(self,myMatrix):#增加时间：2020年1月20日，增加一个页面，避免刷屏
        n=self.GetPageCount()
        myTextPage=xit_MyTripleElementScrolledWindow(self,myMatrix)
        myTextPage.setMyText(myMatrix)
        self._pageList.append(myTextPage)
        name=("第%d个矩阵" %(n))
        self.AddPage(myTextPage, name)
        self.SetSelection(n)
            
    def OnPageChanged(self, event):
        if self:
            old = event.GetOldSelection()
            new = event.GetSelection()
            sel = self.GetSelection()
            if new==0:
                xit_G.G_myOP.setUnitAndGridFromCUR("ZERO")
            else:
                xit_G.G_myOP.setUnitAndGridFromCUR(new-1)
        event.Skip()
    def OnPageChanging(self, event):
        if self:
            old = event.GetOldSelection()
            new = event.GetSelection()
            sel = self.GetSelection()
        
        event.Skip()
#  
#-----xit_AUIFrame----------------主面板-------------------------------------------------------        
class xit_AUIFrame(wx.Frame):

    def __init__(self, parent, id=-1, title="线性代数小专家",style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |wx.MAXIMIZE|
                                            wx.CLIP_CHILDREN):

        wx.Frame.__init__(self,parent,id=id,title=title,pos=wx.DefaultPosition,
                 size=wx.Size(900,650),style=style)

        # tell FrameManager to manage this frame
        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self._perspectives = []
        self.n = 0
        self.x = 0
        self._matTree=[]
        self.font = wx.Font(wx.FontInfo(10).FaceName("新宋体"))
        xit_G.G_fontandcolour=G_fontcolour()

        #生成菜单
        self._menudict={}
        mb = wx.MenuBar()
        menuctrl=MyMenuControl(self,"mainframe")
        #文件菜单       
        file_menu = wx.Menu()
        tmp=file_menu.Append(wx.ID_ANY,"新建(&N)")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, menuctrl.Control, id=tmp.GetId())
        tmp=file_menu.Append(wx.ID_ANY,"打开...")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, menuctrl.Control, id=tmp.GetId())
        tmp=file_menu.Append(wx.ID_ANY,"合并打开...")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, menuctrl.Control, id=tmp.GetId())
        tmp=file_menu.Append(wx.ID_ANY,"保存")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, menuctrl.Control, id=tmp.GetId())
        tmp=file_menu.Append(wx.ID_ANY,"另存为...")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, menuctrl.Control, id=tmp.GetId())
        tmp=file_menu.Append(wx.ID_ANY,"退出")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, menuctrl.Control, id=tmp.GetId())
        #视图菜单--视图菜单的方法在这里更方便
        view_menu = wx.Menu()
        tmp=view_menu.Append(wx.ID_ANY,"显示左侧矩阵树")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, self.ViewControl, id=tmp.GetId())
        tmp=view_menu.Append(wx.ID_ANY,"显示矩阵网格")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, self.ViewControl, id=tmp.GetId())
        tmp=view_menu.Append(wx.ID_ANY,"显示下侧面板")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, self.ViewControl, id=tmp.GetId())
        tmp=view_menu.Append(wx.ID_ANY,"显示控制台")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, self.ViewControl, id=tmp.GetId())
        tmp=view_menu.Append(wx.ID_ANY,"恢复默认设置")
        self._menudict[tmp.GetId()]=tmp
        self.Bind(wx.EVT_MENU, self.ViewControl, id=tmp.GetId())

        #self.Bind(wx.EVT_CONTEXT_MENU, MyMenuControl(self).OnContextMenu)

        mb.Append(file_menu, "文件(&F)")
        mb.Append(view_menu, "视图(&V)")
       
        self.SetMenuBar(mb)
        #生成子面板
       
        self._mymattree=self.CreateTreeCtrl()
        self._mygrid=xit_MyGrid(self)
        self._mycentertextnotebook=xit_MyCenterTextNotebook(self)
        self._myshell=self.CreateShell()
        self._mynotebook=xit_MyNotebookPanel(self)

        
        xit_G.G_myOP=xit_MyOP(myCenterTextNotebook=self._mycentertextnotebook,cur="ZERO",grid=self._mygrid,tree=self._mymattree,treedict=self.treedict,menudict=self._menudict,mainwindow=self)
        
       
        self.SetIcon(GetMondrianIcon())
        self.SetMinSize(wx.Size(800, 600))

        self._mymattree.SetFont(self.font)
        self._myshell.SetFont(self.font)
        self._mynotebook.SetFont(self.font)
        # add a bunch of panes
        self._mgr.AddPane(self._mymattree, aui.AuiPaneInfo().Name("练习题集合").Caption("练习题集合").BestSize(wx.Size(250,600)).Left())
        self._mgr.AddPane(self._myshell, aui.AuiPaneInfo().Name("控制台").Caption("控制台").BestSize(wx.Size(600,800)).Right())
        self._mgr.AddPane(self._mynotebook, aui.AuiPaneInfo().Name("选项卡").Caption("选项卡").BestSize(wx.Size(650,350)).Bottom())
        self._mgr.AddPane(self._mygrid, aui.AuiPaneInfo().Name("矩阵网格").Caption("矩阵网格").BestSize(wx.Size(250,200)).Left().Position(1))
        # create some center panes
        
        self._mgr.AddPane(self._mycentertextnotebook, aui.AuiPaneInfo().Name("结果").CenterPane())

        # make some default perspectives

        self._mgr.GetPane("练习题集合").Show()
        self._mgr.GetPane("选项卡").Show()
        self._mgr.GetPane("控制台").Show()
        self._mgr.GetPane("结果").Show()
        self._mgr.GetPane("矩阵网格").Show()
        #self._mgr.GetPane("测试框").Hide()
        self.perspective_default = self._mgr.SavePerspective()

        # "commit" all changes made to FrameManager
        self._mgr.Update()

      

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Show How To Use The Closing Panes Event
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
       
    
    def ViewControl(self,event):
        menuname=self._menudict[event.GetId()].GetName()
        if menuname=="显示左侧矩阵树":
            '''self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Caption("Tree Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).CloseButton(True).MaximizeButton(True))
            ''' 
            self._mgr.GetPane("练习题集合").Float().FloatingSize(wx.Size(250,500)).CloseButton(True).MaximizeButton(True).Show()
            self._mgr.Update()
        elif menuname=="显示矩阵网格":
            self._mgr.GetPane("矩阵网格").Float().FloatingSize(wx.Size(400,300)).CloseButton(True).MaximizeButton(True).Show()
            self._mgr.Update()
        elif menuname=="显示下侧面板":
            self._mgr.GetPane("选项卡").Float().FloatingSize(wx.Size(1000,300)).CloseButton(True).MaximizeButton(True).Show()
            self._mgr.Update()
        elif menuname=="显示控制台":
            self._mgr.GetPane("控制台").Float().FloatingSize(wx.Size(400,1000)).CloseButton(True).MaximizeButton(True).Show()
            self._mgr.Update()
        elif menuname=="恢复默认设置":
            self._mgr.LoadPerspective(self.perspective_default)
    def DoUpdate(self):

        self._mgr.Update()


    def OnEraseBackground(self, event):

        event.Skip()


    def OnSize(self, event):

        event.Skip()


    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(250, 100),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER|wx.TR_HIDE_ROOT)

        root = tree.AddRoot("线性代数习题集")
        items = []
        self.treedict={}

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16,16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        tree.AssignImageList(imglist)
        for (_id,_father,_label) in xit_G.getTreeList():
            if _father=="root":
                self.treedict[_id]=tree.AppendItem(root,_label, 0)
            else:
                self.treedict[_id]=tree.AppendItem(self.treedict[_father], _label,0)
                
              
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded_Tree,tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED,self.OnItemCollapsed_Tree,tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,   self.OnSelChanged_Tree,tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,self.OnActivated_Tree,tree)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDING,self.OnItemExpanding_Tree,tree)
        init_printing(use_unicode=True)
        Lst=FileHelper.getUnitListFromSRC()

        for _matUnit in Lst:
            
            self.treedict[_matUnit.ID]=tree.AppendItem(self.treedict[_matUnit.matType], _matUnit.Riddle,1,data="")
            tree.SetItemData(self.treedict[_matUnit.ID],_matUnit)
        
        #添加时间：2020年2月1日，初始化我的矩阵
        try:
            f=open("mytreedefault.dat","rb")
            while True:
                _unit=pickle.load(f)
                if _unit==None:
                    break
                tmp=tree.AppendItem(self.treedict["MYTREE"], _unit.Riddle,1,data="")
                tree.SetItemData(tmp,_unit)
        except:
            pass
        finally:
            pass
            

        return tree

    def OnItemExpanded_Tree(self,evt):
        pass
    def OnItemCollapsed_Tree(self,evt):
        pass
    def OnSelChanged_Tree(self,evt):
        
        item=evt.GetItem()
        
        xit_G.G_myOP._myMatrixUnit=self._mymattree.GetItemData(item)
        if xit_G.G_myOP._myMatrixUnit!=None:
            xit_G.G_myOP._myMatrixUnit.cur=0
            xit_G.G_myOP.setFromxitMatrixUnit(xit_G.G_myOP._myMatrixUnit,0)
        self._mgr.Update()    
       
        self._myshell.prompt()
        
        
       
        #self._mgr.Update()
     
    def OnActivated_Tree(self,evt):
        pass
    def OnItemExpanding_Tree(self,evt):
        pass

    def CreateShell(self):
        ctrl=Shell(parent=self)
        ctrl.redirectStdout(redirect=True)
        ctrl.redirectStdin(redirect=True)
        ctrl.redirectStderr(redirect=True)
        init_printing(use_unicode=False)
             
        return ctrl

    
        

    def OnPaneClose(self, event):

        caption = event.GetPane().caption

        if caption in ["Tree Pane", "Dock Manager Settings", "Fixed Pane"]:
            msg = "Are You Sure You Want To Close This Pane?"
            dlg = wx.MessageDialog(self, msg, "AUI Question",
                                   wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

            if dlg.ShowModal() in [wx.ID_NO, wx.ID_CANCEL]:
                event.Veto()
            dlg.Destroy()


    def OnClose(self, event):
        self._mgr.UnInit()
        del self._mgr
        self.Destroy()


    def OnExit(self, event):
        self.Close()

    def OnAbout(self, event):

        msg = "wx.aui Demo\n" + \
              "An advanced window management library for wxWidgets\n" + \
              "(c) Copyright 2005-2006, Kirix Corporation"
        dlg = wx.MessageDialog(self, msg, "About wx.aui Demo",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


#------------------------------------------------------------------------------------------------  
OP=None
U=None
M=None
def Update():
    print("你牛！你操作吧！！\n")
    print("A--当前运行的矩阵（中心页面没有定位矩阵则为None）")
    global OP,U,M
    OP=xit_G.G_myOP
    U=xit_G.G_myOP._myMatrixUnit
    if xit_G.G_myOP._myMatrixUnit!=None and type(xit_G.G_myOP._myMatrixUnit.cur)==type(0):
        M=xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur]
if __name__ == '__main__':
    app=wx.App()
    frame = xit_AUIFrame(parent=None)

    frame.Show()
    app.MainLoop()
