from sympy import *
import traceback
import sys
import itertools
import copy
from xit_Global_topic import xitTopicSRC
from xit_matrixunit_AlgorithmExplanation import xit_MatrixUnitExplain
'''
       sympy之xitMatrix

xitMatrix继承自Matrix,所以下面的方法与Sympy的介绍类似
xitMatrix的家族关系：

MatrixShaping（矩阵的形状运算：比如行、列的删除；矩阵的合并等方法都在这里定义，试一下改动）
MatrixSpecial（一些特殊矩阵的形成方法在这里定义，例如单位阵，one阵等）
MatrixProperties（矩阵的属性在这里定义，例如是否是单位阵，能够改变数值等）
MatrixOperations(矩阵的一元基本运算，例如求矩阵的迹等)
MatrixArithmetic(矩阵的二元运算，例如矩阵的加减乘等)

                                      MatrixRequired(矩阵必备)
                                                |
   -------------------------------------------------------------------------------------
  |                     |                 |                        |                   |
MatrixShaping         MatrixSpecial     MatrixProperties     MatrixOperations    MatrixArithmetic
  |                     |                 |                        |                   |
  --------------------------------------------------------------------------------------
                                          |
                                     MatrixCommon


一、 xitMatrix的初始化：

>>> M=xitMatrix([[1,0,0],[0,0,0]])
>>> M
⎡1  0  0⎤
⎢       ⎥
⎣0  0  0⎦
>>> xitMatrix([M,(0,0,-1)])
⎡1  0  0 ⎤
⎢        ⎥
⎢0  0  0 ⎥
⎢        ⎥
⎣0  0  -1⎦
>>> xitMatrix([1,2,3])
⎡1⎤
⎢ ⎥
⎢2⎥
⎢ ⎥
⎣3⎦
>>> xitMatrix([[1,2,3]])
[1  2  3]
>>> xitMatrix(2,3,[1,2,3,4,5,6])
⎡1  2  3⎤
⎢       ⎥
⎣4  5  6⎦
>>> xitMatrix([eye(3),zeros(3),ones(3),diag(1, Matrix([[1, 2], [3, 4]]))])
⎡1  0  0⎤
⎢       ⎥
⎢0  1  0⎥
⎢       ⎥
⎢0  0  1⎥
⎢       ⎥
⎢0  0  0⎥
⎢       ⎥
⎢0  0  0⎥
⎢       ⎥
⎢0  0  0⎥
⎢       ⎥
⎢1  1  1⎥
⎢       ⎥
⎢1  1  1⎥
⎢       ⎥
⎢1  1  1⎥
⎢       ⎥
⎢1  0  0⎥
⎢       ⎥
⎢0  1  2⎥
⎢       ⎥
⎣0  3  4⎦
>>> xitMatrix([[eye(3),zeros(3),ones(3),diag(1, Matrix([[1, 2], [3, 4]]))]])
⎡⎡1  0  0⎤  ⎡0  0  0⎤  ⎡1  1  1⎤  ⎡1  0  0⎤⎤
⎢⎢       ⎥  ⎢       ⎥  ⎢       ⎥  ⎢       ⎥⎥
⎢⎢0  1  0⎥  ⎢0  0  0⎥  ⎢1  1  1⎥  ⎢0  1  2⎥⎥
⎢⎢       ⎥  ⎢       ⎥  ⎢       ⎥  ⎢       ⎥⎥
⎣⎣0  0  1⎦  ⎣0  0  0⎦  ⎣1  1  1⎦  ⎣0  3  4⎦⎦
>>> xitMatrix.hstack(eye(3),zeros(3),ones(3),diag(1, xitMatrix([[1, 2], [3, 4]])))
⎡1  0  0  0  0  0  1  1  1  1  0  0⎤
⎢                                  ⎥
⎢0  1  0  0  0  0  1  1  1  0  1  2⎥
⎢                                  ⎥
⎣0  0  1  0  0  0  1  1  1  0  3  4⎦
>>> 
>>> xitMatrix(3, 4, lambda i,j: 1 - (i+j) % 2)
⎡1  0  1  0⎤
⎢          ⎥
⎢0  1  0  1⎥
⎢          ⎥
⎣1  0  1  0⎦
>>> def f(i,j):
	if i==j:
	    return 1
	else:
	    return 0

	
>>> xitMatrix(2,4,f)
⎡1  0  0  0⎤
⎢          ⎥
⎣0  1  0  0⎦

二、xitMatrix的取元素操作和切片操作


xitMatrix的线性代数基本操作

M.col_del(0) #删除指定的行
M.col_insert(1, V) #在指定的位置插入一列或者多列
M.col_join(V) #两个矩阵按照列合并在一起
M.col(0) #返回指定列

>>> M=xitMatrix(4,3,range(12))
>>> M
⎡0  1   2 ⎤
⎢         ⎥
⎢3  4   5 ⎥
⎢         ⎥
⎢6  7   8 ⎥
⎢         ⎥
⎣9  10  11⎦
>>> M.extract([0,1,3],[0,1])
⎡0  1 ⎤
⎢     ⎥
⎢3  4 ⎥
⎢     ⎥
⎣9  10⎦
M.get_diag_blocks（） #获得对角阵的对角子阵列表
M.reshape(self, rows, cols)  #将矩阵的行列值重新定义

三、线性代数基本操作

>>> M=eye(3)
>>> M.col_op(1,lambda v,i:v+2*M[i,0]);M
⎡1  2  0⎤
⎢       ⎥
⎢0  1  0⎥
⎢       ⎥
⎣0  0  1⎦
# col_op(i,lambda v,row:v+k*M[row,j]) 可以将第j列乘以k加到第i列
>>> def f(i,j,k):
	M.col_op(i,lambda v,row:v+k*M[row,j])

	
>>> f(2,1,4);
>>> M
⎡1  2  8⎤
⎢       ⎥
⎢0  1  4⎥
⎢       ⎥
⎣0  0  1⎦

# col_swap(self, i, j): i,j两列值原地交换
# copyin_list(self, key, value): 这个复制操作可以直接用切片赋值操作
>>> I = eye(3)
>>> I[:2, 0] = [1, 2] # col
>>> I
Matrix([
 [1, 0, 0],
 [2, 1, 0],
 [0, 0, 1]])
>>> I[1, :2] = [[3, 4]]
>>> I
Matrix([
 [1, 0, 0],
 [3, 4, 0],
 [0, 0, 1]])

>>> M = eye(3)
>>> M.row_op(1, lambda v, j: v + 2*M[0, j]); M
Matrix([
 [1, 0, 0],
 [2, 1, 0],
 [0, 0, 1]])
'''
def getInvNumber(argList):
    ans = 0
    for i in range(len(argList)):
        for j in range(i):
            if argList[j] > argList[i]:
                ans += 1
    return ans
class xitMatrix(Matrix):
    def __init__(self,*args,**kargs):
        self.desc="" #desc是矩阵用来进行描述的字符串
        self.argsList=[] #argsList是一个参数列表，不同的command可能argslist不同
        self.presrc=""
        self.postsrc=""

    def execommand(self,command,*args):
        re= getattr(self, command)(*args)
        return re

    #得到某个矩阵row,col处的余子式，结果返回一个新的Unit，其第一个矩阵是原有矩阵，其第二个矩阵是余子式矩阵，参数列表中是[-1系数,代数余子式的值]
    def xitcofactor(self,row,col):
        copy=self[:,:]#得到备份，而不是直接操作
        copy.presrc="原始矩阵A[" +str(row)+","+str(col)+ "]="+str(copy[row,col])+",它的余子式\n\n"
        copy.row_del(row)
        copy.col_del(col)
        args=1
        newUnit=xitMatrixUnit(ID="",matType="",Command="某行某列的余子式",Chapter="",Riddle="余子式")
        _mat=self[:,:]
        newUnit.matList=[_mat,copy]
        _mat.presrc=copy.presrc+pretty(copy)
        _mat.postsrc="它的代数余子式要乘以-1的"+str(row+col)+"次方,"
        if (row+col)%2==0:
            _mat.postsrc +="即乘以1\n"
        else:
            args=-1
            _mat.postsrc +="即乘以-1\n"
        _mat.postsrc +="其余子式的值是："+str(copy.det())+"\n\n"
        if (row+col)%2==0:
            _mat.postsrc +="其代数余子式的值是："+str(copy.det())+"\n\n"
        else:
            _mat.postsrc +="其代数余子式的值是："+str(-copy.det())+"\n\n"
        newUnit._mat=_mat
        newUnit[1].argsList=[args,args*copy.det()]
        return newUnit


    def xitdet_definition(self):
        n=self.rows
        sumresult=0
        sumstr="行列式的值=\n"
        count=0
        for i in itertools.permutations(range(n),n):
            count=count+1
            colList=list(i)
            mul_p=1
            str_p=""
            for x in range(len(colList)):
                y=colList[x]
                mul_p *=self[x,y]
                if x==0:
                    str_p += ("%-3d" %(self[x,y]))
                else:
                    str_p += ("*%-3d" %(self[x,y]))
            m_p=getInvNumber(colList)
            mul_p = ((-1)**m_p)*mul_p
            str_p = " (-1)**"+str(m_p)+"  *"+str_p+" "
            if sumstr=="行列式的值  =\n" :
                sumstr += "   "+str_p+"(NO"+str(count)+":["+str(colList)+"])\n"
            else:
                sumstr += " + "+str_p +"(NO"+str(count)+":["+str(colList)+"])\n"
            sumresult +=mul_p
            print("mul_p=",str(mul_p),"sum=",str(sumresult))
            
        sumstr += " = "+str(sumresult)    
        self.presrc="按定义求解行列式"
        self.postsrc=sumstr
        return self
            
    #不再保存其它矩阵，因为比较乱
    def xitcofactor_laplace(self,rowList=[]): #用拉普拉斯定理来找所有的余子式
        n=self.rows
        rowsL=len(rowList)
        
        #建一个新的Unit，原有的矩阵页不再存在！
        newUnit=xitMatrixUnit(ID="",matType="",Command="余子式计算行列式",Chapter="",Riddle="余子式",cur=0)
        newUnit.cur=0
        newUnit.matList=[]
        _firstmatList=[]
        if rowsL>0:
            m=n-rowsL
            count=0
            for i in itertools.combinations(range(n),rowsL):
                count += 1
                colList=list(i)
                rowList.sort()
                copycol=self[:,:]
                _matrixList=[]
                sum_xishu=0
                for x in rowList:
                    for y in colList:
                        _matrixList.append(copycol[x,y])

                
                copyrow=xitMatrix(rowsL,rowsL,_matrixList) #得到余子式
                colList.reverse()
                for y in colList:
                    copycol.col_del(y)
                    sum_xishu += y
                rowList.reverse()
                for x in rowList:
                    copycol.row_del(x)
                    sum_xishu += x
                copyrow.argsList=[(-1)**sum_xishu]

                copyrow.presrc="No"+str(2*count-1)+":按照"+str(rowList)+"行展开的第"+str(count)+"个拉普拉斯子式\n"
                copyrow.postsrc="拉普拉斯子式是计算行列式过程中的被乘数\n"
                
                
                copycol.presrc="No"+str(2*count)+":按照"+str(rowList)+"行展开的第"+str(count)+"个余子式\n"
                copycol.postsrc="余子式是计算行列式过程中的乘数\n"
                
                
                newUnit.matList.append(copyrow)
                newUnit.matList.append(copycol)
                _firstmatList.append(copyrow)
                _firstmatList.append(copycol)
            copy=self[:,:]
            copy.presrc=""
            cofsum=0
            for x in range(count):
                if newUnit.matList[2*x].argsList[0]==1:
                    cofsum += newUnit.matList[2*x].det() * newUnit.matList[2*x+1].det()
                    copy.presrc += str(newUnit.matList[2*x].det())+"*"+str(newUnit.matList[2*x+1].det())+"  "
                else:
                    cofsum -= newUnit.matList[2*x].det() * newUnit.matList[2*x+1].det()
                    copy.presrc += "(-1)*"+str(newUnit.matList[2*x].det())+"*"+str(newUnit.matList[2*x+1].det())+"  "
                if x!=count-1:
                    copy.presrc += "  +  "
            copy.presrc += "  =  "+str(cofsum)
            n=len(_firstmatList)
            _firstMatrix=xitMatrix(n//2,2,_firstmatList)
            copy.postsrc=pretty(_firstMatrix)
            copy.postsrc=copy.presrc+"\n\n"+copy.postsrc
            copy.presrc=""
            newUnit.matList.insert(0,copy)
            newUnit._mat=newUnit.ShowMatrixUnitAll()
        else:
            pass
        return newUnit
    def xit_GramSchmidt(self,orthonormal=False): #施密特正交化
        newUnit=xitMatrixUnit(ID="",matType="",Command="xit_GramSchmidt",Chapter="",Riddle="施密特正交化")
        newUnit.matList=[]
        _unitmat=self[:,:]
        _unitmat.presrc="GramSchmidt"
        vlist=[]
        for x in range(self.cols):
            vlist.append(self[:,x:x+1])
        re=GramSchmidt(vlist,orthonormal)
        _mat=xitMatrix(1,len(re),re)
        _unitmat.postsrc=pretty(_mat)
        newUnit.matList.append(_unitmat)
        return newUnit
    def xit_linsolve(self,other=[]):#解线性方程组，目前没研究明白，不知道L:FiniteSet怎么能够遍历
        _mat=self[:,:]
        n=_mat.cols #未知数的个数
        _mat,turple=_mat.rref()
        SbList=symarray('x',n-1)
        print(SbList[1])
        L=linsolve(self,SbList.tolist())
        m=L.subs([(SbList[1],1)])
        print(m)
        print(L)
        

    def xit_rref(self,other=[]):#解齐次线性方程组20200128
        _mat=self[:,:]
        n=_mat.cols #未知数的个数
        _mat,turple=_mat.rref()
        turple=list(turple)

        symbol_1=Symbol("最简行阶梯 : \n")
        symbol_2=Symbol(pretty(_mat))
        symbol_3=Symbol("线性无关的向量组下标为: "+str(turple))
        tmpmat=xitMatrix(3,1,[symbol_1,symbol_2,symbol_3]) 
        self.postsrc=str(tmpmat)+"\n\n"
        self.postsrc +="下面求基础解系：\n"
        _matrank=len(turple)
        count=0
        vectorlist=[]
        for x in range(n):
            if x not in turple: #这第x个列表是可以被线性表示的
                count=count+1
                copy=_mat[:,x]
                tmpvector=[]
                for i in range(n): #i代表列，遍历每一列
                    if i not in turple and i!=x:#这一列不是关键列，那就应该添加0
                        tmpvector.append(0)
                    elif i==x:
                        tmpvector.append(1)
                    else: #i是关键列，那要看对应x的哪一行
                        for j in range(_mat.rows):
                            if _mat[j,i]==1:#行号找到了，是j
                                tmpvector.append(-1*_mat[j,x])
                                break
                self.postsrc +="\nNo"+str(count)+":"+str(tmpvector)
                vectorlist.append(tmpvector)
        if vectorlist==[]:
            self.postsrc +="\n\n所以该齐次线性方程组仅有零解\n"
            return [self,xitMatrix([])]
        else:
            self.postsrc +="\n\n所以该齐次线性方程组的通解为:\n"
        count=0
        malist=[]
        returnmat=xitMatrix([])
        for tvec in vectorlist:
            count=count+1
            returnmat=returnmat.row_join(xitMatrix(tvec))
            if count==1:#第一个
                malist.append(Symbol("c"+str(count)+"*"))
                malist.append(xitMatrix(tvec))
                
            else:
                 malist.append(Symbol("   + c"+str(count)+"*"))
                 malist.append(xitMatrix(tvec))
                 
        tmpxitMatrix=xitMatrix(1,len(malist),malist)
        self.postsrc +=pretty(tmpxitMatrix)
        return [self,returnmat]
    def xit_rref_nonliear(self):#解非齐次线性方程组self是增广矩阵

        #首先，显示行阶梯阵
        _mat,turple=self.rref()
        symbol_1=Symbol("增广矩阵的最简行阶梯阵 : \n")
        symbol_2=Symbol(pretty(_mat))
        tmpmat=xitMatrix(2,1,[symbol_1,symbol_2]) 
        self.postsrc=str(tmpmat)+"\n\n"
        #接下来，判断是否有解
        vec_special=self[:,0:-1].xit_vec_linear(self[:,-1])
        if vec_special==[]:
             self.postsrc +="由最简阵易看出，该方程组无解\n\n"
             return [self,xitMatrix([]),xitMatrix([])]
        else:
            #接下来去求齐次方程的通解
            [_Amat,vec_usually]=self[:,0:-1].xit_rref()
            self.postsrc +="由最简阵易看出，该方程组有解，下面先求齐次方程的通解:\n"
            malist=[]
            returnmat=xitMatrix([])
            for x in range(vec_usually.cols):
                if x==0:#第一个
                    malist.append(Symbol("c"+str(x+1)+"*"))
                else:
                    malist.append(Symbol("   + c"+str(x+1)+"*"))
                malist.append(vec_usually[:,x])
            tmpxitMatrix=xitMatrix(1,len(malist),malist)
            self.postsrc +=pretty(tmpxitMatrix)
            #再然后列出非齐次方程的特解
            self.postsrc +="\n\n接下来，根据最简行阶梯阵，求出非齐次方程的一个特解:"
            self.postsrc +=str(vec_special)
            self.postsrc +="\n\n所以，非齐次线性方程的通解为:\n"
            malist.insert(0,xitMatrix(vec_special))
            if len(malist)>1:
                malist.insert(1,Symbol(" + "))
            tmpxitMatrix=xitMatrix(1,len(malist),malist)
            self.postsrc +=pretty(tmpxitMatrix)
        return [self,vec_usually,xitMatrix(vec_special)]
    def xit_eigenvals(self):#求矩阵的特征值和特征向量

        newUnit=xitMatrixUnit(ID="",matType="",Command="xit_eigenvals",Chapter="",Riddle="特征值和特征向量")
        newUnit.matList=[]
        eigendic=self.eigenvals() #特征值和特征向量的字典
        for val in eigendic: #val是特征值
            _xitmatList=[Symbol("lambda=%d" %(val))]
            copy=self-val*eye(self.rows)
            copyUnit=copy.xit_reff()
            for n in range(3,len(copyUnit.matList)):
                _xitmatList.append(copyUnit[n])
            _matShow=xitMatrix(1,len(_xitmatList),_xitmatList)
            newUnit.matList.append(_matShow)
        return newUnit
    def xit_diagonalize(self):#对角化矩阵
        P,D=self.diagonalize()
        newUnit=xitMatrixUnit(ID="",matType="矩阵对角化",Command="xit_diagonalize",Chapter="Chapter",Riddle="矩阵对角化")
        newUnit.matList=[P,D,P**-1]
        _matShow=xitMatrix(1,3,[P,D,P**-1])
        newUnit.matList.insert(0,_matShow)
        return newUnit
    def xit_eq_two_vectors(self,other,method="rank"):  #做出两个向量组是否等价的判断
        _matA=self[:,:]
        _matB=other[:,:]
        _matAB=_matA.row_join(_matB)
        newUnit=xitMatrixUnit(ID="",matType="向量组等价",Command="xit_eq_two_vectors",Chapter="Chapter",Riddle="向量组等价")
        newUnit.matList=[]
        rank_A=_matA.rank()
        newUnit.matList.append(_matA)
   
        rank_B=_matB.rank()
        newUnit.matList.append(_matB)

        rank_AB=_matAB.rank()
        newUnit.matList.append(_matAB)
       
        _matShow00=Symbol("%-2s" %"A")
        _matShow01=_matA
        _matShow02=Symbol("Rank:%-2s" %str(rank_A))
        _matShow10=Symbol("%-2s" %"B")
        _matShow11=_matB
        _matShow12=Symbol("Rank:%-2s" %str(rank_B))
        _matShow20=Symbol("%-2s" %"AB")
        _matShow21=_matAB
        _matShow22=Symbol("Rank:%-2s" %str(rank_AB))
        _matShow=xitMatrix(3,4,[_matShow00,_matShow01,_matShow01.rref()[0],_matShow02,_matShow10,_matShow11,_matShow11.rref()[0],_matShow12,_matShow20,_matShow21,_matShow21.rref()[0],_matShow22])
        newUnit.matList.insert(0,self[:,:])
        newUnit[0].presrc="两个向量组是否等价"
        newUnit[0].postsrc=pretty(_matShow)
        #newUnit.matList.insert(0,_matShow)
        return newUnit
    def xit_max_linear_independent(self): #把矩阵作为列向量组，得到极大无关组，并把其他向量用无关组表示
        _matAB=self[:,:]
        rows=_matAB.rows
        #首先，显示行阶梯阵
        _mat,turple=self.rref()
        symbol_1=Symbol("矩阵的最简行阶梯阵 : \n")
        symbol_2=Symbol(pretty(_mat))
        tmpmat=xitMatrix(2,1,[symbol_1,symbol_2]) 
        self.postsrc=str(tmpmat)+"\n\n"
        #下面确定无关组
        turple=list(turple)
        _maxMatrix=_matAB.extract(list(range(_matAB.rows)),turple)#得到极大无关组矩阵
        _maxShowMatrix=xitMatrix([])
        for x in range(_maxMatrix.cols):
            symbol_1=Symbol("V"+str(turple[x]))
            symbol_2=Symbol(pretty(_maxMatrix[:,x]))
            tmpmat=xitMatrix(1,2,[symbol_1,symbol_2])
            _maxShowMatrix=_maxShowMatrix.row_join(tmpmat)
        self.postsrc += "极大无关组向量组:\n"
        self.postsrc +=pretty(_maxShowMatrix)
        #接下来表示
        self.postsrc += "\n其它向量用无关组线性表示:\n"
        for x in range(_matAB.cols):
            if x not in turple: #这是需要表示的向量
                count=0
                relist=[]
                tmpvec=_maxMatrix.xit_vec_linear(_matAB[:,x])
                #relist.append(Symbol(pretty(_matAB[:,x])))
                relist.append(_matAB[:,x])
                relist.append(Symbol("= "))
                for i in tmpvec:
                    if count!=0:
                        symbol_1=Symbol("+")
                    else:
                        symbol_1=Symbol(" ")
                    
                    if i==0:
                        count = count + 1
                        continue
                    else:
                        count = count + 1
                        symbol_2=Symbol(str(i)+"*")
                        relist.append(symbol_1)
                        relist.append(symbol_2)
                        #relist.append(Symbol(pretty(_maxMatrix[:,count-1])))
                        relist.append(_maxMatrix[:,count-1])
                tmpMatrix=xitMatrix(1,len(relist),relist)
                self.postsrc += pretty(tmpMatrix)+"\n\n"        
        
        return self
    '''
    方法名：xit_vec_linear
    编写人：王晓峰
    编写时间：2020年1月28日
    功能：将vec用self中的向量线性表示
    说明：判断一个向量组能否被另一个向量组表示时，可调用此函数，求线性方程组的特解时，也可以调用此函数，此函数可得到其中的一组解，不能得到全部的解
    参数：self:列向量组 other:列向量，other向量被self向量组线性表示
    返回：List,如果能够表示，返回表示的系数，不能表示，返回[]
    
    '''
    def xit_vec_linear(self,other):
        _matA=self[:,:]
        A_cols=_matA.cols
        _matB=other[:,:]
        _matAB=_matA.row_join(_matB)
        rows=_matAB.rows
        _mat,turple=_matAB.rref()#得到的_mat是最简行阶梯阵，turple是自由向量
        if A_cols in turple:#turple中包含other这个列向量（因为下标从0开始，所以A_cols表达的向量已经不在A中了）
            return []
        tmpvector=[]
        for x in range(A_cols):
            if x in turple:
                for i in range(rows):
                    if _mat[i,x]==1:
                        tmpvector.append(_mat[i,A_cols])
            else:
                tmpvector.append(0)
                
        return tmpvector
    def xit_AXB(self,other):#解方程AX=B
        _matA=self[:,:]
        A_cols=_matA.cols
        _matB=other[:,:]
        B_cols=_matB.cols
        _matAB=_matA.row_join(_matB)
        rows=_matAB.rows
        _mat,turple=_matAB.rref()
        #首先，显示行阶梯阵
        symbol_1=Symbol("联合矩阵的最简行阶梯阵 : \n")
        symbol_2=Symbol(pretty(_mat))
        tmpmat=xitMatrix(2,1,[symbol_1,symbol_2]) 
        self.postsrc=str(tmpmat)+"\n\nX=:\n"
        _mat=xitMatrix([])
        for x in range(B_cols):
            tmpvec=self[:,:].xit_vec_linear(other[:,x])
            if tmpvec==[]:
                return xitMatrix([])
            else:
                _mat=_mat.row_join(xitMatrix(tmpvec))
        self.postsrc +=pretty(_mat,wrap_line=False)
        return _mat
    def xit_rep_linear(self,other):
        _matA=self[:,:]
        A_cols=_matA.cols
        _matB=other[:,:]
        B_cols=_matB.cols
        _matAB=_matA.row_join(_matB)
        rows=_matAB.rows
        _mat,turple=_matAB.rref()
        #首先，显示行阶梯阵
        symbol_1=Symbol("联合矩阵的最简行阶梯阵 : \n")
        symbol_2=Symbol(pretty(_mat,wrap_line=False))
        tmpmat=xitMatrix(2,1,[symbol_1,symbol_2]) 
        self.postsrc=str(tmpmat)+"\n\n向量的线性表示:\n"



        for x in range(B_cols):
            tmpvec=self[:,:].xit_vec_linear(other[:,x])
            count=0
            relist=[]
            relist.append(other[:,x])
            relist.append(Symbol("= "))
            if tmpvec==[]:
                relist.append(Symbol("[]"))
                tmpMatrix=xitMatrix(1,len(relist),relist)
                self.postsrc += pretty(tmpMatrix,wrap_line=False)+"\n\n"
                continue
            else:
                for i in tmpvec:
                    if count!=0:
                        symbol_1=Symbol("+")
                    else:
                        symbol_1=Symbol(" ")
                    
                    if i==0:
                        count = count + 1
                        continue
                    else:
                        count = count + 1
                        symbol_2=Symbol(str(i)+"*")
                        relist.append(symbol_1)
                        relist.append(symbol_2)
                        #relist.append(Symbol(pretty(_maxMatrix[:,count-1])))
                        relist.append(self[:,count-1])
                tmpMatrix=xitMatrix(1,len(relist),relist)
                self.postsrc += pretty(tmpMatrix,wrap_line=False)+"\n\n"       
        
        return self

    def xit_DetValue_Elimination(self):
        self.outer_count=1
        def FindNoZeroElement(other,row,col): #从当前位置(row,col)开始，找到非零元与其交换
            if row<0 or row>=other.rows or col<0 or col>=other.cols:
                return False
            for i in range(row,other.rows):
                if other[i,col]!=0 and i==row: #一开始就不等于0，直接成功
                    return True
                elif other[i,col]!=0: #找到非零元，但不在第row行，和第row行交换
                    copy=other[:,:]
                    if hasattr(other,"argsList") and len(other.argsList)>0:
                        if hasattr(copy,"argsList"):
                            copy.argsList.append(other.argsList[0])
                        else:
                            copy.argsList=[other.argsList[0]]

                    copy.presrc="第"+str(self.outer_count)+"步:  "+("r%-1d <-> r%-1d" %(row,i))+"\n"
                    copy.postsrc="第"+str(self.outer_count-1)+"步"+":\n"+str(copy)+"\n第"+str(self.outer_count)+"步:  "+("r%-1d <-> r%-1d" %(row,i))+"\n"
                    self.outer_count=self.outer_count+1
                    if hasattr(copy,"argsList")==False:
                        copy.argsList=[-1]
                    elif len(copy.argsList)==0:
                        copy.argsList.append(-1)
                    else:
                        copy.argsList[0] *=-1
                    copy.row_swap(row,i)
                    copy.postsrc +=str(copy)
                    newUnit.matList.append(copy)
                    other[:,:]=copy[:,:]
                    if hasattr(copy,"argsList"):
                        if len(copy.argsList)>0:
                            if hasattr(other,"argsList"):
                                if len(other.argsList)==0:
                                    other.argsList.append(copy.argsList[0])
                                else:
                                    other.argsList[0]=copy.argsList[0]
                            else:
                                other.argsList=[copy.argsList[0]]
                            
                    return True
            return False
        def IamOnly(other,row,col): #当前元素将其它同列元素全变成零
            for i in range(other.rows):
                if i>row and other[i,col]!=0 :
                    k=-1*Rational(other[i,col])/Rational(other[row,col])
                    copy=other[:,:]

                    copy.presrc="第"+str(self.outer_count)+"步:  "+("r%-1d + %1s * r%-1d" %(i,str(k),row))+"\n"
                    copy.postsrc="第"+str(self.outer_count-1)+"步"+":\n"+str(copy)+"\n第"+str(self.outer_count)+"步:  "+("r%-1d + %1s * r%-1d" %(i,str(k),row))+"\n"
                    self.outer_count=self.outer_count+1
                    
                    copy.row_op(i,lambda v, y: v + k*other[row,y])
                    copy.postsrc +=str(copy)
                    newUnit.matList.append(copy)
                    other[:,:]=copy[:,:]
        newUnit=xitMatrixUnit(ID="",matType="",Command="行列式性质求行列式的值",Chapter="Chapter",Riddle="行列式性质求行列式的值")
        newUnit.matList=[]
        other=self[:,:]
        row=0
        col=0
        while row<other.rows and col<other.cols:
            if not FindNoZeroElement(other,row,col):
                col=col+1
            else:
                IamOnly(other,row,col)
                row=row+1
                col=col+1
        if len(newUnit.matList)>=1:
            _tmpmat=newUnit.matList[len(newUnit.matList)-1]
        else:
            _tmpmat=self[:,:]
        _p=1
        _rd="行列式的值="
        for i in range(_tmpmat.rows):
           _p *= _tmpmat[i,i]
           if i==0:
               _rd += "   "+str(_tmpmat[i,i])
           else:
               _rd += " * "+str(_tmpmat[i,i])
        _rd +="  =  "+str(_p)
           
        _mat=self[:,:]
        _mat.presrc="原始行列式:\n"
        _mat.postsrc=_rd
        newUnit.matList.insert(0,_mat)
        _tmpmatstr=""
        for _mat in newUnit.matList:
            _tmpmatstr += _mat.presrc+pretty(_mat)+"\n\n"
        _tmpmatstr +=newUnit[0].postsrc    
        newUnit._mat=_tmpmatstr
        newUnit.cur=0
        return newUnit
    def xit_GaussElimination(self):
        self.count=0
        def FindNoZeroElement(other,row,col): #从当前位置(row,col)开始，找到非零元与其交换
            if row<0 or row>=other.rows or col<0 or col>=other.cols:
                return False
            for i in range(row,other.rows):
                if other[i,col]!=0 and i==row: #一开始就不等于0，直接成功
                    return True
                elif other[i,col]!=0: #找到非零元，但不在第row行，和第row行交换
                    copy=other[:,:]
                    self.count=self.count+1
                    copy.presrc="STEP"+str(self.count)+":\n" 
                    copy.presrc +="r%-1d <-> r%-1d" %(row,i)
                    copy.row_swap(row,i)
                    newUnit.matList.append(copy)
                    other[:,:]=copy[:,:]
                    return True
            return False
        def ElementTo1(other,row,col): #当前位置的元素变成1
            assert other[row,col]!=0
            if other[row,col]==1:
                return True
            else:
                k=1/Rational(other[row,col])
                copy=other[:,:]
                self.count=self.count+1
                copy.presrc="STEP"+str(self.count)+":\n" 
                copy.presrc +="r%-1d * %s" %(row,str(k))
                copy.row_op(row,lambda v,y: k*v)
                newUnit.matList.append(copy)
                other[:,:]=copy[:,:]
                return True
        def IamOnly(other,row,col): #当前元素将其它同列元素全变成零
            for i in range(other.rows):
                if i!=row and other[i,col]!=0:
                    k=-1*Rational(other[i,col])
                    copy=other[:,:]
                    self.count=self.count+1
                    copy.presrc="STEP"+str(self.count)+":\n"
                    copy.presrc +="r%-1d + %1s * r%-1d" %(i,str(k),row)
                    copy.row_op(i,lambda v, y: v + k*other[row,y])
                    newUnit.matList.append(copy)
                    other[:,:]=copy[:,:]
                    
        newUnit=xitMatrixUnit(ID="",matType="",Command="xit_GaussElimination",Chapter="Chapter",Riddle="高斯消元法解决初等行变换")
        newUnit.matList=[]
        other=self[:,:]
        row=0
        col=0
        while row<other.rows and col<other.cols:
            if not FindNoZeroElement(other,row,col):
                col=col+1
            else:
                ElementTo1(other,row,col)
                IamOnly(other,row,col)
                row=row+1
                col=col+1
        
        _firstList=[]
        for _mat in newUnit.matList:
            _mats=Symbol(_mat.presrc)
            _firstList.append(_mats)
            _firstList.append(_mat)
        n=len(_firstList)
        while n%2!=0:
            _firstList.append(Symbol(" "))
            n=n+1
        n=len(_firstList)
        _matShow=xitMatrix(n//2,2,_firstList)
        _matShow.argsList=_firstList
        _matShow.presrc=""
        _matShow.postsrc=""
        _mat=self[:,:]
        _mat.presrc="高斯消元法进行初等行变换的过程"
        _mat.postsrc=pretty(_matShow)
        newUnit.matList.insert(0,_mat)
        return newUnit
    def xit_partition(self,rowList=[],colList=[],spec=""):
        if spec=="avg":
            return self.xit_partition(rowList=[self.rows//2],colList=[self.cols//2],spec="")
        elif spec=="col":
            return self.xit_partition(rowList=[],colList=list(range(1,self.cols)),spec="")
        elif spec=="row":
            return self.xit_partition(rowList=list(range(1,self.rows)),colList=[],spec="")
        newUnit_return=xitMatrixUnit(ID="",matType="",Command="xit_partition",Chapter="Chapter",Riddle="Riddle",matList=[])
        newUnitList=newUnit_return.matList
        copy=self[:,:]#得到备份，而不是直接操作
        copy.presrc="矩阵分块"
        rowList.sort()
        colList.sort()
        rowList.reverse()
        colList.reverse()
        x=self.rows
        y=self.cols
        for x in rowList:
            copyDown=copy[x:copy.rows,:]
            for y in colList:
                copyRight=copyDown[:,y:copyDown.cols]
                #newUnit=xitMatrix(1,1,[copyRight])
                #newUnitList.insert(0,newUnit)
                newUnitList.insert(0,copyRight)
                copyDown=copyDown[:,0:y]
            #newUnit=xitMatrix(1,1,[copyDown])
            #newUnitList.insert(0,newUnit)
            newUnitList.insert(0,copyDown)
            copy=copy[0:x,:]
        copyDown=copy[0:x,:]
        for y in colList:
            copyRight=copyDown[:,y:copyDown.cols]
            #newUnit=xitMatrix(1,1,[copyRight])
            #newUnitList.insert(0,newUnit)
            newUnitList.insert(0,copyRight)
            copyDown=copyDown[:,0:y]
        #newUnit=xitMatrix(1,1,[copyDown])
        #newUnitList.insert(0,newUnit)
        newUnitList.insert(0,copyDown)
        _matShow=xitMatrix(len(rowList)+1,len(colList)+1,newUnitList)
        newUnitList.insert(0,_matShow)
        return newUnit_return

    '''
        编写人：王晓峰
        编写时间：2020年1月21日
        修改时间：2020年1月30日 修改：不再用矩阵形式，直接显示字符串（避免居中显示）
        功能：显示包括前置字符串、矩阵、后置字符串的所有相关内容，用来代替__str__
              __str__和__repr__只用来显示矩阵的内容
    '''
    def ShowMatrixAll(self):
        resultstr=""
        if hasattr(self,"presrc")==False:
            resultstr +="\n"
        elif self.presrc.strip()=="":
            resultstr +="\n"
        else:
            resultstr +="\n"+self.presrc

        resultstr +="\n"+pretty(self,wrap_line=False)

        if hasattr(self,"postsrc")==False:
            resultstr +="\n"
        elif self.postsrc.strip()=="":
            resultstr +="\n"
        else:
            resultstr +="\n"+self.postsrc

       
        return resultstr
    def __str__(self):
        return str(pretty(self,wrap_line=False))
    def __repr__(self):
        return str(pretty(self,wrap_line=False))
    
class FileHelper():
    @classmethod
    def getUnitListFromFile(self,filename):
        unitList=[]
        f=open(filename,mode='r',encoding="utf-8-sig")
        lst = f.readlines()
        for line in lst:
            _unitTmp=eval(line.strip())
            unitList.append(_unitTmp)
        return unitList
    @classmethod
    def getUnitListFromSRC(self):
        unitList=[]
        lst = xitTopicSRC.getSRC().split()
        for line in lst:
            _unitTmp=eval(line.strip())
            unitList.append(_unitTmp)
        return unitList
'''

    编写人：王晓峰
    修改时间：2020年1月18日
    修改内容：将Unit中的cur增加一个值ZERO，来代表矩阵首页；改变矩阵首页就是矩阵第一页的状态；矩阵第一页的cur=0......矩阵第k页的cur=k-1
    
'''
class xitMatrixUnit():
    def __init__(self,_mat=None,ID=None,matType=None,Command=None,Chapter=None,Riddle=None,cur=None,matList=None): #Riddle是关于题目的描述性解释
        self._mat=_mat
        self.ID=ID
        self.matType=matType
        self.Command=Command
        self.Chapter=Chapter
        self.Riddle=Riddle
        self.cur=cur
        if self.cur==None:
            self.cur="ZERO"
        else:
            self.cur=cur
        self.matList=matList
        if self._mat==None:
            self._mat ="矩阵首页：可以介绍矩阵后面页的整体情况\n"
            self._mat +="也可以介绍课本于此相对应的相关知识点\n"
    
    def execommand(self,command,*args):
        re= getattr(self, command)(*args)
        #添加时间：2020年1月30日，单选按钮执行结束后，改变首页内容，并定位至首页
        if type(self)==type(re):
            re._mat=re.ShowMatrixUnitAll()
            if type(re.cur)==type(0):
                re[re.cur].presrc=str(xit_MatrixUnitExplain(command))
            re.cur="ZERO"
        return re    
    def DET_InvNumber(self,*args):#逆序数
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_InvNumber"))
        self[self.cur].postsrc="序列:"+str(list(self[self.cur].row(0)))+"的逆序数是:"+str(getInvNumber(self[self.cur].row(0)))
        return self
    def DET_VALUE(self,*args):#行列式求值
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_VALUE"))
        self[self.cur].postsrc="行列式:\n"+str(self[self.cur])+"\n值:"+str(self[self.cur].det())
        return self

    def DET_COFACT(self,row=0,col=0,*args):#某行某列的余子式
        copy=self[self.cur][:,:]#得到备份，而不是直接操作
        copy.presrc="原始矩阵A[" +str(row)+","+str(col)+ "]="+str(copy[row,col])+",它的余子式\n\n"
        copy.postsrc=""
        copy.row_del(row)
        copy.col_del(col)
        args=1
        _mat=self[self.cur][:,:]
        self.matList.append(copy)
        _mat.presrc=copy.presrc+pretty(copy)
        _mat.postsrc=_mat.presrc+"\n它的代数余子式要乘以-1的"+str(row+col)+"次方,"
        if (row+col)%2==0:
            _mat.postsrc +="即乘以1\n\n"
        else:
            args=-1
            _mat.postsrc +="即乘以-1\n\n"
        _mat.postsrc +="其余子式的值是："+str(copy.det())+"\n\n"
        if (row+col)%2==0:
            _mat.postsrc +="其代数余子式的值是："+str(copy.det())+"\n\n"
        else:
            _mat.postsrc +="其代数余子式的值是："+str(-copy.det())+"\n\n"
        self._mat=_mat
        self[self.cur]=_mat
        self[len(self.matList)-1].argsList=[args,args*copy.det()]#以前写得这句话应该被修改了
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_COFACT"))
        return self
    
    def DET_STEP_COFACT(self,row=0,*args):#按余子式求行列式的值
        self=self[self.cur].xitcofactor_laplace([row])
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_STEP_COFACT"))
        return self

    def DET_STEP_DEF(self,*args):#按定义求行列式的值
        self[self.cur]=self[self.cur].xitdet_definition()
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_STEP_DEF"))
        return self
    def DET_SETP_ROWOP(self,*args):#按性质求行列式的值
        self=self[self.cur].xit_DetValue_Elimination()
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_SETP_ROWOP"))
        return self
    def DET_LAPLACE(self,*args):
        return self[self.cur].xitcofactor_laplace(args[0])
    def DET_PARAM(self,*args):#行列式参数方程求解
        strdet=str(self[self.cur].det())
        strfactor=str(factor(strdet))
        strsolve=str(solve(strfactor))
        self[self.cur].postsrc = "行列式方程:"+strdet+"\n"
        self[self.cur].postsrc += "因式分解:"+strfactor+"\n"
        self[self.cur].postsrc += "解:"+strsolve+"\n"
        self[self.cur].presrc=str(xit_MatrixUnitExplain("DET_PARAM"))
        return self
    def FUN_CLARM_SOLVE(self,*args):#克莱姆法则求线性方程组的解，当前矩阵是增广矩阵
        A_b=self[self.cur][:,:]
        A=A_b[:,0:-1]
        b=A_b[:,-1]
        A_cols=A.cols
        
        tmpList=[]
        D=A.det()
        symbol_1=Symbol("D = ")
       
        symbol_2=Symbol(" = "+str(D))
        tmpmat=xitMatrix(1,3,[symbol_1,A,symbol_2]) 
        self[self.cur].postsrc=str(tmpmat)+"\n\n"

        if A.det()==0:
            self[self.cur].postsrc +="系数行列式为0，无法用克莱姆法则求解\n"
        else:
            for x in range(A_cols):
                _mat=A[:,:]
                _mat.col_op(x,lambda v,row:b[row])
                symbol_1=Symbol("D"+str(x)+" = ")
                symbol_2=Symbol(" = "+str(_mat.det()))
                tmpmat=xitMatrix(1,3,[symbol_1,_mat,symbol_2]) 
                self[self.cur].postsrc +=pretty(tmpmat)+"\n\n"
                tmpList.append(_mat.det()/D)
            self[self.cur].postsrc +="\n方程组的解:"+str(tmpList)+"\n"
        self[self.cur].presrc=str(xit_MatrixUnitExplain("FUN_CLARM_SOLVE"))
        return self
        
    def MAT_RANK(self,*args):#矩阵求秩
        self[self.cur].postsrc="矩阵秩:"+str(self[self.cur].rank())
        return self
    def MAT_ADJ(self,*args):#矩阵求伴随阵
        self[self.cur].postsrc="伴随阵:\n"+pretty(self[self.cur].adjugate(method='berkowitz'))+"\n"
        self.matList.insert(self.cur+1,xitMatrix(self[self.cur].adjugate(method='berkowitz')))
        return self
    def MAT_INV(self,*args):#矩阵求逆
        if self[self.cur].det()!=0:
            self[self.cur].postsrc="逆矩阵:\n"+str(pretty(self[self.cur].inv()))
            self.matList.insert(self.cur+1,xitMatrix(self[self.cur].inv()))
        else:
            self[self.cur].postsrc="\n该矩阵行列式值为零，没有逆矩阵\n"
        return self
    def MAT_STEP_RREF(self,*args):#最简行阶梯

        return self[self.cur].xit_GaussElimination()
    def MAT_STEP_DEV_ROWOP(self,*args):#（A,E）求逆
        rowN=self[self.cur].rows
        copy=xitMatrix(self[self.cur].row_join(eye(rowN)))
        newUnit=copy.xit_GaussElimination()
        newUnit.matList.insert(0,self[self.cur])
        return newUnit
    def MAT_FUNSOLVE_LINEAR(self,*args):#齐次线性方程组
        alist=self[self.cur].xit_rref()
        self.matList.append(alist[1])
        self._mat=self.ShowMatrixUnitAll()
        return self
    def MAT_FUNSOLVE_NONLINEAR(self,*args):#非齐次线性方程组
        alist=self[self.cur].xit_rref_nonliear()
        self.matList.append(alist[1])
        self.matList.append(alist[2])
        self._mat=self.ShowMatrixUnitAll()
        return self
    def MAT_FUNSOLVE_AXB(self,*args):#方程AX=B
        X=self[self.cur].xit_AXB(self[self.cur+1])
        self.matList.append(X)
        return self
        
    def resetFirstShow(self):#重新定义首页的_mat
        A=xitMatrix([])
        prestrA=Symbol(" ")
        poststrA=Symbol(" ")
        for i in range(len(self.matList)):
            if hasattr(self.matList[i],"presrc"):
                prestrA=Symbol(self.matList[i].presrc)
            if hasattr(self.matList[i],"postsrc"):
                poststrA=Symbol(self.matList[i].postsrc)
            B=xitMatrix(1,3,[prestrA,self.matList[i],poststrA])
            A=A.col_join(B)
            prestrA=Symbol(" ")
            poststrA=Symbol(" ")
        self._mat=A
    #初等变换的操作，*args的顺序：op="row_swap row_op1 row_op2,col_swap,col_op1,col_op2,start,pre",i,j,k
    def MAT_OP(self,op="start",i=0,j=0,k="0",*args):
        #首先删除当前cur之后的其它矩阵
        n=len(self)
        cur=self.cur
        for x in range(n-cur-1):
            self.matList.pop()
       
        
        if op=="start":#重新开始
            if len(self.matList)>1:
                self[0]=self[1][:,:]
            else:
                self.matList.append(self[0][:,:])
            self[0].presrc=""
            self[0].postsrc=""
            self.Command=1
            return self
        elif op=="pre":
            if self.Command>1:
                self.Command=self.Command-1
                self[0]=self[self.Command][:,:]
                self[0].presrc=""
                self[0].postsrc=""
            else:
                self.Command=1
                self[0]=self[self.Command][:,:]
                self[0].presrc=""
                self[0].postsrc=""
            return self
        elif op=="row_swap":
            self.matList.append(self[self.cur][:,:])
            self.cur=self.cur+1
            self[self.cur].row_swap(i,j)
            self[self.cur].postsrc=("r%-1d <-> r%-1d" %(i,j))
            self[self.cur].presrc=("第%d次：交换两行操作" %(cur+1))
            self.resetFirstShow()
            return self
        elif op=="col_swap":
            self.matList.append(self[self.cur][:,:])
            self.cur=self.cur+1
            self[self.cur].col_swap(i,j)
            self[self.cur].postsrc=("c%-1d <-> c%-1d" %(i,j))
            self[self.cur].presrc=("第%d次：交换两列操作" %(cur+1))
            self.resetFirstShow()
            return self
        elif op=="row_op1":#行自乘
            self.matList.append(self[self.cur][:,:])
            self.cur=self.cur+1
            self[self.cur].row_op(i,lambda v,col:Rational(k)*v) 
            self[self.cur].postsrc=("r%-1d * %s" %(i,str(k)))
            self[self.cur].presrc=("第%d次：行自乘" %(cur+1))
            self.resetFirstShow()
            return self
        elif op=="col_op1":#列自乘
            self.matList.append(self[self.cur][:,:])
            self.cur=self.cur+1
            self[self.cur].col_op(i,lambda v,row:Rational(k)*v) 
            self[self.cur].postsrc=("c%-1d * %s" %(i,str(k)))
            self[self.cur].presrc=("第%d次：列自乘" %(cur+1))
            self.resetFirstShow()
            return self
        elif op=="row_op2":#行累加
            self.matList.append(self[self.cur][:,:])
            self.cur=self.cur+1
            self[self.cur].row_op(i,lambda v,col:v+Rational(k)*self[self.cur][j,col]) 
            self[self.cur].postsrc=("r%-1d + %1s * r%-1d" %(i,str(k),j))
            self[self.cur].presrc=("第%d次：行累加" %(cur+1))
            self.resetFirstShow()
            return self
        elif op=="col_op2":#列累加
            self.matList.append(self[self.cur][:,:])
            self.cur=self.cur+1
            self[self.cur].col_op(i,lambda v,row:v+Rational(k)*self[self.cur][row,j]) 
            self[self.cur].postsrc=("c%-1d + %1s * c%-1d" %(i,str(k),j))
            self[self.cur].presrc=("第%d次：列累加" %(cur+1))
            self.resetFirstShow()
            return self
        return self
        
    def VEC_TWO_LINEAR(self,*args):#B向量组被A向量组线性表示
        self[self.cur].xit_rep_linear(self[self.cur+1])
        self[self.cur+1].xit_rep_linear(self[self.cur])
        return self

    def VEC_RANK(self,*args):#向量组的秩
        newUnit=self.copy()
        newUnit[0].presrc="向量组的秩"
        newUnit[0].postsrc="秩:"+str(newUnit[0].rank())
        return newUnit
    def VEC_EQ(self,*args):#两个向量组是否等价
        return self[0].xit_eq_two_vectors(self[1])


    def VEC_LINEAR(self,*args):#求向量组的极大无关组，并把其他的用无关组线性表示
        self[self.cur].xit_max_linear_independent()
        
        return self
    def VEC_SHWI(self,*args):
        self[self.cur].xit_GramSchmidt()
        return self
    
        
   
    
    def apart(self,cur=0):
        newUnitList=[]
        n=len(self.matList)
        if cur>=0 and cur<n:
            newUnit=xitMatrixUnit(ID=self.ID,matType=self.matType,Command=self.Command,Chapter=self.Chapter,Riddle=self.Riddle,matList=[self.matList[cur][:,:]])
            newUnitList.append(newUnit)
        for i in range(n):
            if i!=cur:
                newUnit=xitMatrixUnit(ID=self.ID,matType=self.matType,Command=self.Command,Chapter=self.Chapter,Riddle=self.Riddle,matList=[self.matList[i][:,:]])
                newUnitList.append(newUnit)
        return newUnitList  
        
                
    def copy(self):
        newUnit=xitMatrixUnit(ID=self.ID,matType=self.matType,Command=self.Command,Chapter=self.Chapter,Riddle=self.Riddle,matList=copy.deepcopy(self.matList))
        return newUnit
    def __len__(self):
        return len(self.matList)
    def __getitem__(self,key):
        return self.matList[key]
    def __setitem__(self,key,value):
        self.matList[key]=value
    def __add__(self,other):#重载加法运算，所谓的加法运算，就是把矩阵列表进行合并，合并到第一个列表
        self.matList.extend(other.matList)
        return self
    def __delitem__(self,key):
        del self.matList[key]
        return
    def __str__(self):
        return str(pretty(self._mat,wrap_line=False))
    def __repr__(self):
        return str(pretty(self._mat,wrap_line=False)) 

    '''
        编写人：王晓峰
        编写时间：2020年1月21日
        修改时间：2020年1月30日 修改：不再用矩阵形式，直接显示字符串（避免居中显示）
        功能：显示矩阵单元的所有矩阵的所有内容包括前置字符串、矩阵、后置字符串的所有(但不包括_mat)
    '''
    def ShowMatrixUnitAll(self):
        resultstr=""
        if self==None:return "[None]"
        n=len(self)
        if n==0:return "矩阵数量：0"
        resultstr +="\n矩阵,共:"+str(n)+"个\n"
        for i in range(n):
            resultstr +="\n-----------------第"+str(i+1)+"个矩阵:-----------------------\n" 
            resultstr +=self[i].ShowMatrixAll()+"\n"
            
        return resultstr
    

def test_xitcofactor_laplace():
    A=xitMatrix([[1,-1,4],[2,3,-1],[-1,1,0]])
    C=xitMatrix(4,4,range(16))
    B=C.xitcofactor_laplace([0,2,3])
    print(B)
def test_xit_GramSchmidt():
    A=xitMatrix([[1,-1,4],[2,3,-1],[-1,1,0]])
    B=A.xit_GaussElimination()
    print(B)

def test_xit_diagonalize():
    A=xitMatrix([[-2,1,1],[0,2,0],[-4,1,3]])
    B=A.xit_diagonalize()
    A=xitMatrix([[0,-1,1],[-1,0,1],[1,1,0]])
    B=A.xit_diagonalize()
    print(pretty(B[0]))
def test_xit_eigenvals():
    A=xitMatrix([[-1,1,0],[-4,3,0],[1,0,2]])
    B=A.xit_eigenvals()
    for x in range(len(B.matList)):
        print(pretty(B[x]))
    A=xitMatrix([[3,-1],[-1,3]])
    B=A.xit_eigenvals()
    for x in range(len(B.matList)):
        print(pretty(B[x]))
    A=xitMatrix([[0,-1,1],[-1,0,1],[1,1,0]])
    B=A.xit_eigenvals()
    for x in range(len(B.matList)):
        print(pretty(B[x]))
def test_xit_max_linear_independent():
    A=xitMatrix([[1,3],[-1,1],[1,1],[-1,3]])
    N1=A.xit_max_linear_independent()
    print(pretty(N1[0]))
    print(pretty(N1[1]))
    B=xitMatrix([[2,1,3],[0,1,-1],[1,0,2],[1,2,0]])
    N1=B.xit_max_linear_independent()
    print(pretty(N1[0]))
    print(pretty(N1[1]))
    C=xitMatrix([[25,31,17,43],[75,94,53,132],[75,94,54,134],[25,32,20,48]])
    N1=C.xit_max_linear_independent()
    print(pretty(N1[0]))
    print(pretty(N1[1]))
def test_xit_reff():
    A=xitMatrix([[1,3,0],[-1,1,0],[1,1,0],[-1,3,0]])
    N1=A.xit_reff()
    print(pretty(N1[0]))
    B=xitMatrix([[2,1,3,0],[0,1,-1,0],[1,0,2,0],[1,2,0,0]])
    N1=B.xit_reff()
    print(pretty(N1[0]))
    C=xitMatrix([[25,31,17,43,0]])
    N1=C.xit_reff()
    print(pretty(N1[0]))

def test_xit_rep_linear():
    A=xitMatrix([[1,3],[-1,1],[1,1],[-1,3]])
    B=xitMatrix([[2,1,3],[0,1,-1],[1,0,2],[1,2,0]])
    N1=A.xit_rep_linear(B)
    print(pretty(N1[0]))
    N1=B.xit_rep_linear(A)
    print(pretty(N1[0]))
def test_xit_vec_linear():
    B=xitMatrix([[0,3,2],[1,0,3],[2,1,0],[3,2,1]])
    A=xitMatrix([[2,0,4],[1,-2,4],[1,1,1],[2,1,3]])
    A.col_swap(0,1)
    for x in range(B.cols):
        list_result=A.xit_vec_linear(B[:,x])
        print(pretty(A))
        print()
        print(pretty(B[:,x]))
        print()
        print(list_result)
def test_xit_rep_linear2():
    A=xitMatrix([[0,3,2],[1,0,3],[2,1,0],[3,2,1]])
    B=xitMatrix([[2,0,4],[1,-2,4],[1,1,1],[2,1,3]])
    N1=A.xit_rep_linear(B)
    print(pretty(N1[0]))
    N1=B.xit_rep_linear(A)
    print(pretty(N1[0]))
def test_xit_partition():
    A=xitMatrix([[0,3,2],[1,0,3],[2,1,0],[3,2,1]])
    B=xitMatrix([[2,0,4],[1,-2,4],[1,1,1],[2,1,3]])
    N1=A.xit_partition(spec="col")
    print(pretty(N1[0]))
    N1=B.xit_partition(spec="row")
    print(pretty(N1[0]))
    C=xitMatrix(8,8,range(64))
    N1=C.xit_partition([1,3,4],[2,5,6,7])
    print(pretty(N1[0]))
def test_main():
    Lst=FileHelper.getUnitListFromFile("_mat.data")
    init_printing(use_unicode=True)
    #print(Lst[8].matList[0].det())
    #X=Lst[8].xitcofactor_laplace(0,[1])
    #X.Show()
    M=xitMatrixUnit(ID="",matType="",Command="Command",Chapter="Chapter",Riddle="Riddle",matList=[xitMatrix(8,8,range(64))])
    M=xitMatrixUnit(matList=[xitMatrix([[2,-1,-1,1],[1,1,-2,1],[4,-6,2,-2],[3,6,-9,7]])])
    M=xitMatrixUnit(matList=[xitMatrix([[0,1],[1,1],[1,0]]),xitMatrix([[-1,1,3],[0,2,2],[1,1,-1]])])
    A=xitMatrix([[0,1],[1,1],[1,0]])
    B=xitMatrix([[-1,1,3],[0,2,2],[1,1,-1]])
    M=xitMatrix([[2,-1,-1,1],[1,1,-2,1],[4,-6,2,-2]])
    N=A.xit_eq_two_vectors(M)
    #N.SShow()
    #print(pretty(N[0]))
    #N=M.xit_GaussElimination()
    #N.SShow()



    N1=A.xit_rep_linear(B)
    print(pretty(N1[0]))
    #N1.Show()
    #N2=M.xit_rep_linear(1,0)
    #N2.Show()
if __name__ == '__main__':
   init_printing(use_unicode=True)
   test_xit_vec_linear()
   
'''
if __name__ == '__main__':
    Lst=FileHelper.getUnitListFromFile("_mat.data")
    i=0
    init_printing(use_unicode=True)
    for xmat in Lst:
        i=i+1
        xmat.Show(str(i))
    X=Lst[7].xitcofactor(cur="all",row="row",col="col")
    X.Show()
    for i in range(2):
        X=X.xitcofactor(cur="all",row="row",col="col")
        X.Show()
if __name__ == '__main__':
    try:
        init_printing(use_unicode=True)
        myMat=xitMatrix([[1,2,3,5],[5,6,7,8],[3,4,5,6],[5,7,8,9]])
        pprint(myMat,use_unicode=True)
        myMat.col_ex(1,2)
        pprint(myMat,use_unicode=True)
        myMat.col_mul(3,3)
        pprint(myMat,use_unicode=True)
        myMat.col_add(3,0,1)
        pprint(myMat,use_unicode=True)
        pprint(myMat.acofactor(0,1),use_unicode=True)
    except xitOutOfBoundsException as ex:
        print(ex.show())
        #print(sys._getframe().f_lineno, 'str(e):\t\t', str(ex))
        #print(sys._getframe().f_lineno, 'repr(e):\t', repr(ex))
       
        print(sys._getframe().f_lineno, 'traceback.format_exc():\n%s' % traceback.format_exc())



xitMatrixPlatform

编号：

矩阵列表：

状态：实时、按运算映射

运算映射（det,[0,1,2]）,(jfc,[4,5,7])
结果列表：(结果描述，矩阵列表)



import time

def deco(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        execution_time_ = (end_time - start_time)*1000
        print("time is %d ms" %execution_time)
    return wrapper


@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def f2(a,b,c):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f2(3,4,5)
    f(3,4)

 import sys
 sys.path.append("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\proj\\线性代数")
 from xitMatrix import *




'''
