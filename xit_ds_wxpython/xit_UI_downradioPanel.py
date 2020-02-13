import wx
import wx.grid
from xit_matrixunit import *
from xit_Global import *
from xit_Global_radio import *
from xit_Global_radio_2 import *
from xit_Global_myop import *
from xit_matrixunitCalculator import xitCalculator
from xit_matrixunitCalculator import Int_to_ASCII


       
class MyButton(wx.Button):
    inputTextCtrl=None #静态变量，那个文本输入框
    resultTextCtrl=None#静态变量，提示和结果
    input_Show_Str=""  #静态变量，显示的文本
    def __init__(self,parent,label="",size=(80,40),pre="",post="",bz=""):
        wx.Panel.__init__(self,parent,label=label,size=size)
        self._label = label
        self._pre=pre
        self._post=post
        self._bz=bz
        self.SetMinSize(size)
        self.Bind(wx.EVT_BUTTON,self.OnButton)
        self.Bind(wx.EVT_ENTER_WINDOW,self.OnEnterWindow)
        self.Bind(wx.EVT_LEAVE_WINDOW,self.OnLeaveWindow)
    def OnEnterWindow(self,evt):
        self.Tip()
    def OnLeaveWindow(self,evt):
        MyButton.resultTextCtrl.SetValue("提示与结果显示")
    def OnButton(self,evt):
        tmp=MyButton.inputTextCtrl.GetValue()
        if self._bz=="All":
            tmp += self._pre+self._label+self._post
            MyButton.inputTextCtrl.SetValue(tmp)
        elif self._bz=="NoLabel":
            tmp += self._pre+self._post
            MyButton.inputTextCtrl.SetValue(tmp)
    def Tip(self):
        tmpstr=""
        if self._label=="det":
            tmpstr='''                  函数操作键:det(sympy库函数)
含义：行列式求值
功能：计算当前行列式（矩阵）的值
要求：矩阵的行、列必须相等
输入参数：无
输出：一个数字
其它参考：inv
举例：A.det()
(A+B).inv().det()
        '''
            
        elif self._label=="inv":
            tmpstr='''                  函数操作键:inv(sympy库函数)
含义：矩阵（方阵）求逆
功能：计算并显示当前矩阵的逆矩阵
要求：1.矩阵的行、列必须相等
      2.矩阵必须存在逆矩阵（行列式值不为0）
输出：矩阵
其它参考：det
举例：A.inv()
(A+B).inv().det()
            '''
  
        elif self._label=="rank":
            tmpstr='''                  函数操作键:rank(sympy库函数)
含义：矩阵求秩、把矩阵看做列向量组，就是列向量求秩
功能：计算当前矩阵的秩
输出：一个数字
其它参考：
举例：A.rank()
(A+B).rank()
A.row_join(B).rank()
            '''
        elif self._label=="adjugate":
            tmpstr='''                  函数操作键:adjugate(sympy库函数)
含义：求矩阵（方阵）的伴随矩阵
功能：计算并显示当前矩阵的伴随矩阵
要求：矩阵的行、列必须相等
输出：矩阵
其它参考：inv
举例：A.adjugate()
(A+B).adjugate()
            '''
        MyButton.resultTextCtrl.SetValue(tmpstr)
            
        
#-----xit_MyMatrixCalculatePanel-----下部下部操作选项卡中的第四个选项卡面板，矩阵计算器---------------
class xit_MyMatrixCalculatePanel(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, -1,style=wx.HSCROLL|wx.VSCROLL)
        self.SetScrollbars(1,1,300,200)
        self._inputTextCtrl=wx.TextCtrl(self,-1,'',size=(1400,-1))
        self._inputTextCtrl.SetFont(wx.Font(wx.FontInfo(20).FaceName("新宋体")))
        self._resultTextCtrl=wx.TextCtrl(self,-1,'提示与结果显示',style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY,size=(550,200))
        self._buttonList=[]
        for i in range(10):
            self._buttonList.append(MyButton(parent=self,label=str(i),size=(40,40),pre="",post="",bz="All"))
        for i in range(15):
            self._buttonList.append(MyButton(parent=self,label=Int_to_ASCII(i),size=(40,40),pre="",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="+",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label="-",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label="*",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label="/",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label=".",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label="(",bz="All"))
        self._buttonList.append(MyButton(parent=self,label=")",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="←",pre="",post="",bz="backspace"))
        self._buttonList.append(MyButton(parent=self,label="[",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label="]",size=(40,40),bz="All"))
        self._buttonList.append(MyButton(parent=self,label="T",pre=".",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="det",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="inv",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="rank",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="adjugate",pre=".",post="(method='berkowitz')",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="rref",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="pretty",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="Rational",pre="",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="factor",pre="",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="solve",pre="",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="linsolve",pre="",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="hstack",pre="",post="",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="extract",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="reshape",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="row",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="row_del",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="row_insert",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="row_join",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="row_swap",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="row_op",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="col",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="col_del",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="col_insert",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="col_join",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="col_swap",pre=".",post="()",bz="All"))
        self._buttonList.append(MyButton(parent=self,label="col_op",pre=".",post="()",bz="All"))

        MyButton.inputTextCtrl=self._inputTextCtrl
        MyButton.resultTextCtrl=self._resultTextCtrl

        #self._buttonList     0123456789  10--24    25  26  27  28  29  30  31  32   33   34   35  
        #                     0123456789   A--O     +   -   *   /   .   (   )   ←   [    ]    T      

        #self._buttonList     36     37         38     39         40     41       42        43        44     45         46        47       48          
        #                     det    inv        rank   adjugate   rref   pretty   Rational  factor    solve  linsolve   hstack    extract  reshape

        #self._buttonList     49     50         51            52         53        54             
        #                     row    row_del    row_insert    row_join   row_swap  row_op    

        #self._buttonList     55     56         57            58         59        60             
        #                     col    col_del    col_insert    col_join   col_swap  col_op    

                     




        sizer = wx.BoxSizer(wx.HORIZONTAL)#水平方向分割按钮
        _box=wx.StaticBox(self,-1,"数字键")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[1],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[2],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[3],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[4],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[5],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[6],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[7],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[8],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[9],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[0],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[29],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[25],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)

        _box=wx.StaticBox(self,-1,"矩阵序列键")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[10],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[11],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[12],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[13],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[14],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[32],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[15],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[16],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[17],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[18],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[19],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[30],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[20],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[21],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[22],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[23],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[24],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[31],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[26],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[27],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[28],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[33],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[34],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[35],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)

        _box=wx.StaticBox(self,-1,"函数操作键")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[36],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[40],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[44],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[48],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[52],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[56],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[60],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[37],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[41],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[45],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[49],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[53],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[57],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[38],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[42],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[46],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[50],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[54],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[58],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._buttonList[39],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[43],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[47],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[51],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[55],0,wx.EXPAND,2)
        _inputsizer.Add(self._buttonList[59],0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        
        #_box=wx.StaticBox(self,-1,"提示&结果")
        #_sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        
        #_sizer_ver.Add(self._resultTextCtrl,0,wx.ALL,2)
        sizer.Add(self._resultTextCtrl, 0, wx.ALL, 5)
        #最后的确认按钮
        _sizermain=wx.BoxSizer(wx.VERTICAL)
        _sizermain.Add(sizer,0,wx.ALL,2)
       
        _inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        _inputsizer.Add(self._inputTextCtrl,0,wx.EXPAND,2)

        _commitBtn=wx.Button(self,-1,"=")
        self.Bind(wx.EVT_BUTTON,self.OnButton,_commitBtn)
        _commitBtn.SetDefault()
        _inputsizer.Add(_commitBtn,0,wx.EXPAND,2)
        _sizermain.Add(_inputsizer,0,wx.ALL,2)
        
        self.SetSizer(_sizermain)
        
       
        
    def OnButton(self, event):
           
        myCal=xitCalculator.getFromxitMatrixUnit(xit_G.G_myOP._myMatrixUnit)
        re=myCal.Calculate(self._inputTextCtrl.GetValue())
        self._resultTextCtrl.SetValue(str(re))
        if isinstance(re,xitMatrix):
            re.presrc=self._inputTextCtrl.GetValue()
            xit_G.G_myOP._notebook.AddPageFromMatrix(re)
            xit_G.G_myOP._myMatrixUnit.matList.append(re)
            xit_G.G_myOP._myMatrixUnit.cur=len(xit_G.G_myOP._myMatrixUnit)-1
            xit_G.G_myOP._grid.setGrid(xit_G.G_myOP._myMatrixUnit.cur,xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur])
        elif isinstance(re,xitMatrixUnit):
            xit_G.G_myOP.setFromxitMatrixUnit(re,re.cur)
        else:#其它情况假设是字符串，虽然也有可能是turple
            if type(xit_G.G_myOP._myMatrixUnit.cur)==type(0):#当前是矩阵页
                xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur].postsrc=self._inputTextCtrl.GetValue()+"="+"\n"+str(re)
            else:
                xit_G.G_myOP._myMatrixUnit._mat=self._inputTextCtrl.GetValue()+"="+"\n"+str(re)
                xit_G.G_myOP._myMatrixUnit.cur="ZERO"
                
        
        

#-----xit_MyMatrixPanel-----下部操作选项卡中的第三个选项卡（暂时废弃！！）面板，用来对矩阵进行增删改，生成新的矩阵-----------------------------------------------------------------------------------------        
class xit_MyMatrixPanel(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, -1,style=wx.HSCROLL|wx.VSCROLL)
        self.SetScrollbars(1,1,300,200)
        sizer = wx.BoxSizer(wx.HORIZONTAL)#水平方向分割按钮,第一大块是矩阵增删
        self._radioList=xitRadioSRC().getCreateMatrixRadioList(self,sizer=sizer)
        #最后的确认按钮
        _sizermain=wx.BoxSizer(wx.VERTICAL)
        _sizermain.Add(sizer,0,wx.ALL,2)
        _commitBtn=wx.Button(self,-1,"确认")
        self.Bind(wx.EVT_BUTTON,self.OnRadio,_commitBtn)
        _commitBtn.SetDefault()
        _inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(_commitBtn,0,wx.EXPAND,2)
        _sizermain.Add(_inputsizer,0,wx.ALL,2)
        
        self.SetSizer(_sizermain)
        
       
        
    def OnRadio(self, event):
           
        for i in range(len(self._radioList)):
            if self._radioList[i]._radio.GetValue():
                xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur]=xit_G.Command_Do(xit_G.G_myOP._grid,self._radioList[i]._commandname,self._radioList[i].getargs())
        
        xit_G.G_myOP._notebook.setSelectionPageFromMatrix(xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur])
        xit_G.G_myOP._grid.setGrid(xit_G.G_myOP._myMatrixUnit.cur,xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur])
        

#-----xit_MyChoisePanel------下部选项卡中的第一个选项面板，用来对矩阵进行运算，求行列式的值，矩阵求逆等----------------------------------------------------------------------------------------
class xit_MyChoisePanel(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, -1,style=wx.HSCROLL|wx.VSCROLL)
        self.SetScrollbars(1,1,300,200)
        sizer = wx.BoxSizer(wx.HORIZONTAL)#水平方向分割按钮，一共5个大块，（最终的sizer不是这个）
       
        #调用xit_Global_radio中的方法进行单选钮的初始化
        self._radioList=xitRadioSRC().getRadioList(self,sizer=sizer)
        
        
        #最后的确认按钮
        _sizermain=wx.BoxSizer(wx.VERTICAL)
        _sizermain.Add(sizer,0,wx.ALL,2)
        _commitBtn=wx.Button(self,-1,"确认")
        self.Bind(wx.EVT_BUTTON,self.OnRadio,_commitBtn)
        _commitBtn.SetDefault()
        _inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(_commitBtn,0,wx.EXPAND,2)
        _sizermain.Add(_inputsizer,0,wx.ALL,2)
        
        self.SetSizer(_sizermain)
       
    
    
    def OnClick(self,event):
        pass
    def OnRadio(self, event):
        for i in range(len(self._radioList)):
            if self._radioList[i]._radio.GetValue():
                xit_G.G_myOP._myMatrixUnit=xit_G.Command_Do(xit_G.G_myOP._myMatrixUnit,self._radioList[i]._commandname,self._radioList[i].getargs())
            
        xit_G.G_myOP.setFromxitMatrixUnit(xit_G.G_myOP._myMatrixUnit,xit_G.G_myOP._myMatrixUnit.cur)
        
#-----xit_MyUnitPanel------下部选项卡中的第二个选项面板，用来对矩阵列表进行增删改---------------------------------------------------------------------------------------
class xit_MyUnitPanel(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent, -1,style=wx.HSCROLL|wx.VSCROLL)
        self.SetScrollbars(1,1,300,200)
        sizer = wx.BoxSizer(wx.HORIZONTAL)#水平方向分割按钮，一共5个大块，（最终的sizer不是这个）
       
        #调用xit_Global_radio中的方法进行单选钮的初始化
        self._radioList1=xitRadio2SRC().getCreateMatrixUnitRadioList(self,sizer=sizer)
        self._radioList2=xitRadio2SRC().getCreateMatrixRadioList(self,sizer=sizer)
        #2020年1月31日. 增加一个块，用来处理我的矩阵树
        _box=wx.StaticBox(self,-1,"控制我的矩阵树")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
       
        
        _addBtn=wx.Button(self,-1,"添加到我的自创矩阵（树）")
        self.Bind(wx.EVT_BUTTON,self.OnAddBtn,_addBtn)
        _delBtn=wx.Button(self,-1,"删除当前自创矩阵（树）")
        self.Bind(wx.EVT_BUTTON,self.OnDelBtn,_delBtn)
        self._matrixname=wx.TextCtrl(self,-1,'MatrixName',size=(400,-1))

        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(wx.StaticText(self,-1,'矩阵页名称:',style=wx.ALIGN_LEFT),0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.EXPAND,2)
        
        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(self._matrixname,0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.EXPAND,2)

        _inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(_addBtn,0,wx.EXPAND,2)
        _inputsizer.Add(_delBtn,0,wx.EXPAND,2)
        _sizer_ver.Add(_inputsizer,0,wx.ALL,2)

            
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        #最后的确认按钮
        _sizermain=wx.BoxSizer(wx.VERTICAL)
        _sizermain.Add(sizer,0,wx.ALL,2)
        _commitBtn=wx.Button(self,-1,"确认")
        self.Bind(wx.EVT_BUTTON,self.OnRadio,_commitBtn)
        _commitBtn.SetDefault()
        
        _inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        _inputsizer.Add(_commitBtn,0,wx.EXPAND,2)
        _sizermain.Add(_inputsizer,0,wx.ALL,2)
        
        self.SetSizer(_sizermain)
       
    def OnAddBtn(self,event):
        tmp=xit_G.G_myOP._tree.AppendItem(xit_G.G_myOP._treedict["MYTREE"],str(self._matrixname.GetValue()),1,data="")
        _unit= xit_G.G_myOP._myMatrixUnit.copy()
        _unit._mat=str(xit_G.G_myOP._notebook._pageList[0].GetValue())
        xit_G.G_myOP._tree.SetItemData(tmp,_unit)
    def OnDelBtn(self,event):
        treeid=xit_G.G_myOP._tree.GetSelection()
        _parent=xit_G.G_myOP._tree.GetItemParent(treeid)
        
        if xit_G.G_myOP._tree.GetItemText(_parent)=="我的自创矩阵":
            xit_G.G_myOP._tree.Delete(treeid)
        
    def OnClick(self,event):
        pass
    def OnRadio(self, event):
        for i in range(len(self._radioList1)):
            if self._radioList1[i]._radio.GetValue():
                xit_G.G_myOP._myMatrixUnit=xit_G.Command_Do(xit_G.G_myOP,self._radioList1[i]._commandname,self._radioList1[i].getargs())
                xit_G.G_myOP.setFromxitMatrixUnit(xit_G.G_myOP._myMatrixUnit,xit_G.G_myOP._myMatrixUnit.cur)
                return
        for i in range(len(self._radioList2)):
            if self._radioList2[i]._radio.GetValue():
                xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur]=xit_G.Command_Do(xit_G.G_myOP._grid,self._radioList2[i]._commandname,self._radioList2[i].getargs())
                xit_G.G_myOP._notebook.setSelectionPageFromMatrix(xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur])
                xit_G.G_myOP._grid.setGrid(xit_G.G_myOP._myMatrixUnit.cur,xit_G.G_myOP._myMatrixUnit[xit_G.G_myOP._myMatrixUnit.cur])
                return
       
        
        

#-----xit_MyNotebookPanel------下部的NoteBook，仅包含两个静态的选择面板----------------------------------------------------------------------------------------        
class xit_MyNotebookPanel(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, -1, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             # | wx.NB_MULTILINE
                             )
        win1 = xit_MyChoisePanel(self)
        win2 = xit_MyUnitPanel(self)
        #win3 = xit_MyMatrixPanel(self)
        win4 = xit_MyMatrixCalculatePanel(self)
        self.AddPage(win1, "单选面板")
        self.AddPage(win2, "自创矩阵页")
        #self.AddPage(win3, "当前矩阵选项钮")
        self.AddPage(win4, "矩阵计算器")
        
