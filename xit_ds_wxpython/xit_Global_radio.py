'''
        编写人：王晓峰
        编写时间：2010年1月25日
        类：xit_Control_radio、xitRadioSRC
        功能：生成矩阵操作面板的各个单选按钮，并使单选按钮与matrixUnit操作相联系
'''
import wx

#-----xit_Control_radio----------------------------------------------------------------------------------------------

class xit_Control_radio():
    def __init__ (self,parent,name,style,sizer,arglist,commandname,commandparalist):
        self._radio=None
        self._arglist=[]
        self._inputsizer=wx.BoxSizer(wx.HORIZONTAL)
        self._name=name
        self._commandname=commandname
        self._commandparalist=commandparalist
        if style==None:
            self._radio=wx.RadioButton(parent,-1,name)
        else:
            self._radio=wx.RadioButton(parent,-1,name,style=wx.RB_GROUP)
        self._inputsizer.Add(self._radio,0,wx.ALIGN_RIGHT,2)
        for obj in arglist:
            objControl=eval(obj)
            self._arglist.append(objControl)
            self._inputsizer.Add(objControl,0,wx.EXPAND,2)
        
        parent.Bind(wx.EVT_RADIOBUTTON, parent.OnRadio, self._radio)
        sizer.Add(self._inputsizer,0,wx.ALL,2)
    def getargs(self):
        CommandStr=""
        count=0
        for (x,y) in self._commandparalist:
            if count==0:
                pass
            else:
                CommandStr +=","
            if x=="Str":
                CommandStr += y
            elif x=="NoRational":
                CommandStr +=  str(self._arglist[int(str(y))].GetValue())#修改时间：20200128，原因：也不是所有情况都要转换成Rational,例如拉普拉斯变换，需要输入列表参数
            else:
                CommandStr +=  "Rational('"+str(self._arglist[int(str(y))].GetValue())+"')"#修改时间：20200117，原因：如果不转换成Rational,像1/7这种循环小数在计算中会取近似值，可用“同一数字”单选钮测试
            count=count+1
            
        return CommandStr

#-----xitRadioSRC------------------------------------------------------------------------------------------------------    
class xitRadioSRC():

    @classmethod
    def getRadioList(self,parent,sizer):#这个sizer是水平的，有5大块那种
        self._radioList=[]

        #行列式选项钮
        _box=wx.StaticBox(parent,-1,"行列式")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求序列逆序数",
                                        style=wx.RB_GROUP,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="DET_InvNumber",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求值（按定义）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="DET_STEP_DEF",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求值（按某行余子式）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="DET_STEP_COFACT",
                                        commandparalist=[("Posation",0)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求值（按行列式性质）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="DET_SETP_ROWOP",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        
        
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求某行、某列元素的代数余子式",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="DET_COFACT",
                                        commandparalist=[("Posation",0),("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="验证拉普拉斯定理（行列式的任意阶展开）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.TextCtrl(parent,-1,'',size=(100,-1))"],
                                        commandname="DET_LAPLACE",
                                        commandparalist=[("NoRational",0)])#20200128拉普拉斯定理的参数不要转换成Ratioanl
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="参数方程、行列式带参数（值为零）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="DET_PARAM",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="克莱姆法则解线性方程组",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="FUN_CLARM_SOLVE",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        for i in range(1):
            _sizer_ver.Add(0,18,0,wx.ALL,2)#占位符，宽度为0，高度为18，高度18是测试的结果，与单选钮高度几乎一致
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        #初等变换选项钮
        _box=wx.StaticBox(parent,-1,"操作")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
       
        _sizer_ver.Add(wx.StaticText(parent,-1,"初等行变换    ",style=wx.ALIGN_LEFT),0,wx.ALL,2)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="互换两行          ",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'r',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'←→r',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="MAT_OP",
                                        commandparalist=[("Str","'row_swap'"),("Posation",1),("Posation",3),("Str","0")])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="i行乘以k           ",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'r',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'   ×   ',style=wx.ALIGN_LEFT)",
                                                 "wx.TextCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="MAT_OP",
                                        commandparalist=[("Str","'row_op1'"),("Posation",1),("Str","0"),("Posation",3)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="i行累加j行乘以k",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'r',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'   +   ',style=wx.ALIGN_LEFT)",
                                                 "wx.TextCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'  ×r',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="MAT_OP",
                                        commandparalist=[("Str","'row_op2'"),("Posation",1),("Posation",5),("Posation",3)])
        self._radioList.append(_radioControl)
        _sizer_ver.Add(wx.StaticLine(parent,-1,size=(400,-1),style=wx.LI_HORIZONTAL),0,wx.ALL,2)
        _sizer_ver.Add(wx.StaticText(parent,-1,"初等列变换    ",style=wx.ALIGN_LEFT),0,wx.ALL,2)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="互换两列          ",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'c',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'←→c',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="MAT_OP",
                                        commandparalist=[("Str","'col_swap'"),("Posation",1),("Posation",3),("Str","0")])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="i列乘以k           ",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'c',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'   ×   ',style=wx.ALIGN_LEFT)",
                                                 "wx.TextCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="MAT_OP",
                                        commandparalist=[("Str","'col_op1'"),("Posation",1),("Str","0"),("Posation",3)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="i列累加j列乘以k",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'c',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'   +   ',style=wx.ALIGN_LEFT)",
                                                 "wx.TextCtrl(parent,-1,'',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'  ×c',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'',size=(50,-1))"],
                                        commandname="MAT_OP",
                                        commandparalist=[("Str","'col_op2'"),("Posation",1),("Posation",5),("Posation",3)])
        self._radioList.append(_radioControl)
        #_sizer_ver.Add(wx.StaticLine(parent,-1,size=(400,-1),style=wx.LI_HORIZONTAL),0,wx.ALL,2)

        
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        #下面开始处理第3个块： 线性方程组
        _box=wx.StaticBox(parent,-1,"线性方程(组)与向量表示")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="系数矩阵求齐次线性方程组",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="MAT_FUNSOLVE_LINEAR",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="增广矩阵求非齐次线性方程组",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="MAT_FUNSOLVE_NONLINEAR",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="矩阵方程AX=B",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="MAT_FUNSOLVE_AXB",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求向量组的极大无关组，并把其它向量用无关组线性表示",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="VEC_LINEAR",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="两个向量组的互相线性表示",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="VEC_TWO_LINEAR",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="两个向量组是否相等（秩）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="VEC_EQ",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        for i in range(3):
            _sizer_ver.Add(0,18,0,wx.ALL,2)#占位符，宽度为0，高度为18，高度18是测试的结果，与单选钮高度几乎一致
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        #下面开始处理第4个块： 矩阵性质
        _box=wx.StaticBox(parent,-1,"矩阵、特征值、合同等")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="最简行阶梯矩阵（初等行变换）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="MAT_STEP_RREF",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        
        _radioControl=xit_Control_radio(parent=parent,
                                        name="(A,E)求逆（初等行变换）",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="MAT_STEP_DEV_ROWOP",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="向量组的施密特正交化",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="VEC_SHWI",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求矩阵的特征值与特征向量",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="ENG_VECVALUE",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="矩阵特征值特征向量的求解步骤",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="ENG_STEP_VECVALUE",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求P矩阵，将矩阵相似于对角阵",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="ENG_P_DIAG",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        for i in range(3):
            _sizer_ver.Add(0,18,0,wx.ALL,2)#占位符，宽度为0，高度为18，高度18是测试的结果，与单选钮高度几乎一致
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        #下面开始处理第4个块： 向量与特征值等
        _box=wx.StaticBox(parent,-1,"向量与特征值等")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        
        
        
        _radioControl=xit_Control_radio(parent=parent,
                                        name="求P矩阵，将矩阵合同于对角阵",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="ENG_P_HETONG",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        for i in range(2):
            _sizer_ver.Add(0,18,0,wx.ALL,2)#占位符，宽度为0，高度为18，高度18是测试的结果，与单选钮高度几乎一致
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        return self._radioList
