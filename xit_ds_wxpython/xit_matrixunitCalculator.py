'''
    编写人：王晓峰
    编写时间：2020年1月19日
    功能：矩阵计算器
'''
from xit_matrixunit import xitMatrix
from xit_matrixunit import xitMatrixUnit
from sympy import Rational
def Int_to_ASCII(i): #将整数转成字符 0转A  1转B  2转C
    return chr(ord("A")+i)

def ASCII_to_Int(c):
    return ord(c)-ord("A")

class xitCalculator(xitMatrixUnit):
    def getFromxitMatrixUnit(myMatrixUnit):
        re=xitCalculator(myMatrixUnit._mat,myMatrixUnit.ID,myMatrixUnit.matType,myMatrixUnit.Command,myMatrixUnit.Chapter,myMatrixUnit.Riddle,myMatrixUnit.cur,myMatrixUnit.matList)
        return re
    def __init__(self,_mat=None,ID=None,matType=None,Command=None,Chapter=None,Riddle=None,cur=None,matList=None):
        super(xitCalculator,self).__init__(_mat,ID,matType,Command,Chapter,Riddle,cur,matList)
        self._calculateStr=""
        
    def get_N_attr(self):
        n=len(self)
        for i in range(n):
            tmpstr="self._"+str(i)+"_"
            exec(tmpstr+"=self["+str(i)+"]")
    def getAZattr(self):
        n=len(self)
        if n>15:n=15 #仅转换15个：ABCDE FGHIJ KLMNO
        for i in range(n):
            tmpstr="self."+Int_to_ASCII(i)
            exec(tmpstr+"=self["+str(i)+"]")
            print(tmpstr+"=self["+str(i)+"]")
    def Calculate(self,src):
        self.get_N_attr()
        self.getAZattr()
        n=len(self)
        if n>15:n=15
        newsrc=src
        for i in range(n):
            newsrc=newsrc.replace(Int_to_ASCII(i),"self."+Int_to_ASCII(i))
            print("after:",src,newsrc)
        
        re=eval(newsrc)
        return re
def test():
    var=xitCalculator(_mat="ABC",ID="T040403",matType="VEC_LX",Command="vec",Chapter="4.1",Riddle="第15页第3题，线性组合等价",matList=[xitMatrix([[0,1,2],[1,1,3],[1,0,-2]]),xitMatrix([[-1,1,3],[0,2,2],[1,1,-1]])])
    
    print(dir(var))
    
    print(var.Calculate("Rational(1/2)*A - A.inv()"))
if __name__ == '__main__':
   test()
