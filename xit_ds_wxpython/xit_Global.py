'''
        编写人：王晓峰
        编写时间：2020年1月15日
        类：xit_G
        功能：全局类，用来保存全局变量和静态文本。
        说明：部分静态对象也保存在xit_Global_XXXX中。
    
'''
import wx
from sympy import Rational

class G_fontcolour():
    def __init__(self):
        self._firstfont=wx.Font(wx.FontInfo(20).FaceName("新宋体"))
        self._firstcolour=wx.BLACK
        self._prefont=wx.Font(wx.FontInfo(20).FaceName("新宋体"))
        self._precolour=wx.BLACK
        self._middlefont=wx.Font(wx.FontInfo(20).FaceName("新宋体"))
        self._middlecolour=wx.BLACK
        self._postfont=wx.Font(wx.FontInfo(20).FaceName("新宋体"))
        self._postcolour=wx.BLACK
        self._gridfont=wx.Font(wx.FontInfo(20).FaceName("新宋体"))
        self._gridcolour=wx.BLACK
        self._treefont=wx.Font(wx.FontInfo(10).FaceName("新宋体"))
        self._treecolour=wx.BLACK
        self._downfont=wx.Font(wx.FontInfo(10).FaceName("新宋体"))
        self._downcolour=wx.BLACK

class xit_G():
    
    #左侧树控件用的文本，每个list元素是一个三元组，(A,B,C)。A代表树结点的名称，B代表A的父亲，C代表要显示在屏幕上的该结点的内容
    #说明：这里是树控件的内部结点，叶结点保存在xit_Global_topic中
    @classmethod
    def getTreeList(self):
        _treelist=[
                    ("DET","root","行列式"),                ("MAT","root","矩阵性质"),           ("FUN","root","线性方程组"),     ("VEC","root","向量性质"), ("ENG","root","特征值特征向量等"),
            ("DET_JC","DET","教材（课本）"), ("DET_LX","DET","配套练习册2019年8月版"), ("DET_TJ","DET","线性代数同济第六版"),
              ("DET_JC_LT","DET_JC","例题"),            ("DET_JC_XT","DET_JC","习题"),         ("DET_TJ_LT","DET_TJ","例题"), ("DET_TJ_XT","DET_TJ","习题"),
            ("MAT_JC","MAT","教材（课本）"), ("MAT_LX","MAT","配套练习册2019年8月版"), ("MAT_TJ","MAT","线性代数同济第六版"),
              ("MAT_JC_LT","MAT_JC","例题"),            ("MAT_JC_XT","MAT_JC","习题"),         ("MAT_TJ_LT","MAT_TJ","例题"), ("MAT_TJ_XT","MAT_TJ","习题"),
            ("FUN_JC","FUN","教材（课本）"), ("FUN_LX","FUN","配套练习册2019年8月版"), ("FUN_TJ","FUN","线性代数同济第六版"),
              ("FUN_JC_LT","FUN_JC","例题"),            ("FUN_JC_XT","FUN_JC","习题"),         ("FUN_TJ_LT","FUN_TJ","例题"), ("FUN_TJ_XT","FUN_TJ","习题"),
            ("VEC_JC","VEC","教材（课本）"), ("VEC_LX","VEC","配套练习册2019年8月版"), ("VEC_TJ","VEC","线性代数同济第六版"),
              ("VEC_JC_LT","VEC_JC","例题"),            ("VEC_JC_XT","VEC_JC","习题"),         ("VEC_TJ_LT","VEC_TJ","例题"), ("VEC_TJ_XT","VEC_TJ","习题"),
            ("ENG_JC","ENG","教材（课本）"), ("ENG_LX","ENG","配套练习册2019年8月版"), ("ENG_TJ","ENG","线性代数同济第六版"),
              ("ENG_JC_LT","ENG_JC","例题"),            ("ENG_JC_XT","ENG_JC","习题"),         ("ENG_TJ_LT","ENG_TJ","例题"), ("ENG_TJ_XT","ENG_TJ","习题"),
            ("MYTREE","root","我的自创矩阵")
            ]
        return _treelist
    @property
    def G_fontandcolour(self):#存储全局的字体和颜色
        pass
    @property
    def G_mycentertextnotebook(self):#中心区显示各个矩阵的notebook,将其保存为全局属性，便于其它者调用
        pass

    @property
    def G_myOP(self):#这是目前唯一的一个全局变量，保存变量为xit_Global_gird_op类型，在多个类中被调用和赋值，里面主要包含有MatrixUnit和Grid的相关内容
        pass

    @classmethod
    def getInvNumber(self,argList):#获得逆序数的函数
        ans = 0
        for i in range(len(argList)):
            for j in range(i):
                if j > i:
                    ans += 1
        return ans
       
    @classmethod
    def Command_Do(self,unit,commandname,args):#被用来连接控件和MatrixUnit中的计算方法，这里拼接了字符串，只要是矩阵操作（例如求行列式的值、求秩等）界面在使用
        if args=="":
            commandstr="unit.execommand('"+commandname+"')"
        else:
            commandstr="unit.execommand('"+commandname+"',"+args+")"
        
        re=eval(commandstr)
        return re    
    
