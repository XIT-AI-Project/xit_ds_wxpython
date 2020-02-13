import wx
from xit_Global_radio import xit_Control_radio
class xitRadio2SRC():
    @classmethod
    def getCreateMatrixRadioList(self,parent,sizer):#这个sizer是水平的，有5大块那种
        self._radioList=[]
        #下面开始处理第1个块：矩阵增删
        _box=wx.StaticBox(parent,-1,"当前矩阵的修改")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="更改为零矩阵",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'0',size=(50,-1))",
                                                 "wx.SpinCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="initZero",
                                        commandparalist=[("Posation",0),("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="改变矩阵形状",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'0',size=(50,-1))",
                                                 "wx.SpinCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="reShape",
                                        commandparalist=[("Posation",0),("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="添加一行",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="addRow",
                                        commandparalist=[("Posation",0)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="添加一列",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="addCol",
                                        commandparalist=[("Posation",0)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="删除一行",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="delRow",
                                        commandparalist=[("Posation",0)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="删除一列",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="delCol",
                                        commandparalist=[("Posation",0)])
        self._radioList.append(_radioControl)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        #下面开始处理第2个块：特殊矩阵
        _box=wx.StaticBox(parent,-1,"特殊矩阵的填充")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="单位矩阵",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="DET_SETP_ROWOP",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="同一数字",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.TextCtrl(parent,-1,'0',size=(50,-1))"],
                                        commandname="updateOnes",
                                        commandparalist=[("Posation",0)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="序列填充",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'初始值:',style=wx.ALIGN_LEFT)",
                                                 "wx.TextCtrl(parent,-1,'0',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'步长:',style=wx.ALIGN_LEFT)",
                                                 "wx.TextCtrl(parent,-1,'1',size=(50,-1))"],
                                        commandname="updataRange",
                                        commandparalist=[("Posation",1),("Posation",3)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="随机数填充",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'最小值:',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'0',size=(50,-1),min=-10000,max=10000)",
                                                 "wx.StaticText(parent,-1,'最大:',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'100',size=(50,-1),min=-10000,max=10000)"],
                                        commandname="updateRandom",
                                        commandparalist=[("Posation",1),("Posation",3)])
        self._radioList.append(_radioControl)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        return self._radioList
    @classmethod
    def getCreateMatrixUnitRadioList(self,parent,sizer):
        self._radioList=[]
        _box=wx.StaticBox(parent,-1,"矩阵页的增删改")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="初始化默认矩阵页",
                                        style=wx.RB_GROUP,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'3',size=(50,-1))",
                                                 "wx.SpinCtrl(parent,-1,'3',size=(50,-1))"],
                                        commandname="initMatrixUnit",
                                        commandparalist=[("Posation",0),("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="插入新的矩阵页",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'插入第:',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'0',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'个矩阵之后',style=wx.ALIGN_LEFT)"],
                                        commandname="insertMatrix",
                                        commandparalist=[("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="删除当前矩阵页的后继矩阵",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="deleteMatrix",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        
        _box=wx.StaticBox(parent,-1,"矩阵页的移动与复制")
        _sizer_ver=wx.StaticBoxSizer(_box,wx.VERTICAL)#垂直sizer，处理每一个模块
        _radioControl=xit_Control_radio(parent=parent,
                                        name="重新生成矩阵前页",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="initFirstMatrix",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="移动当前矩阵页",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.SpinCtrl(parent,-1,'3',size=(50,-1))",
                                                 "wx.SpinCtrl(parent,-1,'3',size=(50,-1))"],
                                        commandname="initMatrixUnit",
                                        commandparalist=[("Posation",0),("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="复制当前矩阵页",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=["wx.StaticText(parent,-1,'插入第:',style=wx.ALIGN_LEFT)",
                                                 "wx.SpinCtrl(parent,-1,'0',size=(50,-1))",
                                                 "wx.StaticText(parent,-1,'个矩阵之后',style=wx.ALIGN_LEFT)"],
                                        commandname="insertMatrix",
                                        commandparalist=[("Posation",1)])
        self._radioList.append(_radioControl)
        _radioControl=xit_Control_radio(parent=parent,
                                        name="删除当前矩阵页的后继矩阵",
                                        style=None,
                                        sizer=_sizer_ver,
                                        arglist=[],
                                        commandname="deleteMatrix",
                                        commandparalist=[])
        self._radioList.append(_radioControl)
        sizer.Add(_sizer_ver, 0, wx.ALL, 5)
        return self._radioList