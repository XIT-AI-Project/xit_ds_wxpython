'''
    编写人：王晓峰
    开始时间：2010年1月21日
    功能：提供每个算法的描述，单列出来，便于其他人阅读
'''
class xit_MatrixUnitExplain():
    def __init__(self,name):
        self._name=""         #名称
        self._gbkname=""      #中文名称
        self._function=""     #功能描述
        self._args=""         #输入参数
        self._knowlege=""    #相应知识点
        self._program_pre=""  #前置条件
        self._program_post="" #后置条件
        if hasattr(self,name)==True:
            getattr(self,name)()
       
    def __str__(self):
        tmpstr ="算法名称:"+self._name+"\n"
        tmpstr +="算法中文描述:"+self._gbkname+"\n"
        tmpstr +="算法功能介绍：\n"
        tmpstr +=self._function 
            
        if self._args!=None and self._args.strip()!="":
            tmpstr +="\n输入参数:\n"
            tmpstr +=self._args
        else:
            tmpstr +="\n输入参数:[无]\n"
        if self._knowlege!=None and self._knowlege.strip()!="":
            tmpstr +="\n相应知识点：\n"
            tmpstr +="--------------------------------------------------------------\n"
            tmpstr +=self._knowlege
            tmpstr +="\n--------------------------------------------------------------\n"
        tmpstr +="                    运行条件\n"
        tmpstr +="算法运行的前置条件:\n"
        tmpstr +=self._program_pre
        tmpstr +="\n算法运行的后置条件:\n"
        tmpstr +=self._program_post
        return tmpstr
    def DET_InvNumber(self):
        self._name="DET_InvNumber"
        self._gbkname="求序列的逆序数"

        self._function='''
        算法DET_InvNumber可以求一个序列的逆序数
        算法源代码：
        def getInvNumber(argList):
            ans = 0
            for i in range(len(argList)):
                for j in range(i):
                    if argList[j] > argList[i]:
                        ans += 1
        return ans
        '''
        self._knowlege='''
        对于n个不同的元素，先规定各元素之间有一个标准次序，
        在这n个不同的元素的任一排列中，当某两个元素的先后次序与标准次序不同时，
        就说该排列有一个逆序，一个排列中所有逆序的总数叫做这个排列的逆序数.
        逆序数为奇数的排列叫奇排列，逆序数为偶数的排列叫偶排列.
        一个排列每经过一次对换都会改变排列的奇偶性.
        在全部的n阶排列中，奇排列和偶排列个数相等.
        '''
        self._program_pre='''
        1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)
        2. 矩阵只需要有一行，如果矩阵有多行，算法只对第一行进行逆序数的计算
        '''
        self._program_post ='''
        1.运行结束后，矩阵（行列式）的前置字符串会有说明文字
        2.后置字符串会显示逆序数的值
        3.算法对矩阵本身没有任何影响,对其它矩阵页也没有影响.(比如矩阵前页，不会同步更新)
        '''
        return self
    def DET_VALUE(self):
        self._name="DET_VALUE"
        self._gbkname="行列式直接求值"

        self._function="%+*s算法DET_VALUE可以求任意阶行列式的值\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*s算法DET_VALUE直接通过sympy模块的det函数求值，若想观察计算过程，请参阅：\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*sDET_STEP_DEF：按行列式定义求值\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*sDET_STEP_COFACT：行列式按某行代数余子式展开求值\n" %(len("算法功能介绍：\n")," ")

        self._knowlege="行列式值的定义:\n不同行、不同列的n个数的乘积，\n并冠以(-1)的t次方，\n其中t为这个排列的逆序数\n"
        self._program_pre="%+*s1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)\n" %(len("算法运行的前置条件:\n")," ")
        self._program_pre+="%+*s2. 矩阵的行数与列数必须相等\n" %(len("算法运行的前置条件:\n")," ")

        self._program_post ="%+*s1.运行结束后，矩阵（行列式）的前置字符串会进行本算法的说明\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s2.后置字符串会显示矩阵(行列式)本身及行列式的值\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s3.算法对矩阵本身没有任何影响,对其它矩阵页也没有影响.(比如矩阵前页，不会同步更新)\n" %(len("算法运行的后置条件:\n")," ")
        return self
    def DET_STEP_DEF(self):
        self._name="DET_STEP_DEF"
        self._gbkname="按行列式定义求值"

        self._function="%+*s算法DET_STEP_DEF可以按定义求任意阶行列式的值\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*s算法DET_STEP_DEF通过排列组合，将所有不同行不同列的元素相乘计算行列式\n" %(len("算法功能介绍：\n")," ")
        
        self._knowlege="行列式值的定义:\n不同行、不同列的n个数的乘积，\n并冠以(-1)的t次方，\n其中t为这个排列的逆序数\n"
        self._program_pre="%+*s1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)\n" %(len("算法运行的前置条件:\n")," ")
        self._program_pre+="%+*s2. 矩阵的行数与列数必须相等\n" %(len("算法运行的前置条件:\n")," ")

        self._program_post ="%+*s1.运行结束后，矩阵（行列式）的前置字符串会进行本算法的说明\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s2.后置字符串会显示矩阵(行列式)通过定义计算的公式及行列式的值\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s3.后置字符串每一行的后段，会显示No数字，之后是列的组合情况，行默认[0,1,...n-1],行列值都从0开始\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s4.算法对矩阵本身没有任何影响,对其它矩阵页也没有影响.(比如矩阵前页，不会同步更新)\n" %(len("算法运行的后置条件:\n")," ")
        return self
    def DET_COFACT(self):
        self._name="DET_COFACT"
        self._gbkname="求行列式某行某列的余子式"

        self._function='''
        算法DET_COFACT可以求一个行列式某行某列的余子式
        算法源代码：
        def getInvNumber(argList):
            ans = 0
            for i in range(len(argList)):
                for j in range(i):
                    if argList[j] > argList[i]:
                        ans += 1
        return ans
        '''
        self._knowlege='''
        对于n个不同的元素，先规定各元素之间有一个标准次序，
        在这n个不同的元素的任一排列中，当某两个元素的先后次序与标准次序不同时，
        就说该排列有一个逆序，一个排列中所有逆序的总数叫做这个排列的逆序数.
        逆序数为奇数的排列叫奇排列，逆序数为偶数的排列叫偶排列.
        一个排列每经过一次对换都会改变排列的奇偶性.
        在全部的n阶排列中，奇排列和偶排列个数相等.
        '''
        self._program_pre='''
        1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)
        2. 矩阵只需要有一行，如果矩阵有多行，算法只对第一行进行逆序数的计算
        '''
        self._program_post ='''
        1.运行结束后，矩阵（行列式）的前置字符串会有说明文字
        2.后置字符串会显示逆序数的值
        3.算法对矩阵本身没有任何影响,对其它矩阵页也没有影响.(比如矩阵前页，不会同步更新)
        '''
        return self
    def DET_PARAM(self):
        self._name="DET_PARAM"
        self._gbkname="求解参数方程，行列式值为0"

        self._function='''
        算法DET_COFACT可以求一个行列式某行某列的余子式
        算法源代码：
        def getInvNumber(argList):
            ans = 0
            for i in range(len(argList)):
                for j in range(i):
                    if argList[j] > argList[i]:
                        ans += 1
        return ans
        '''
        self._knowlege='''
        对于n个不同的元素，先规定各元素之间有一个标准次序，
        在这n个不同的元素的任一排列中，当某两个元素的先后次序与标准次序不同时，
        就说该排列有一个逆序，一个排列中所有逆序的总数叫做这个排列的逆序数.
        逆序数为奇数的排列叫奇排列，逆序数为偶数的排列叫偶排列.
        一个排列每经过一次对换都会改变排列的奇偶性.
        在全部的n阶排列中，奇排列和偶排列个数相等.
        '''
        self._program_pre='''
        1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)
        2. 矩阵只需要有一行，如果矩阵有多行，算法只对第一行进行逆序数的计算
        '''
        self._program_post ='''
        1.运行结束后，矩阵（行列式）的前置字符串会有说明文字
        2.后置字符串会显示逆序数的值
        3.算法对矩阵本身没有任何影响,对其它矩阵页也没有影响.(比如矩阵前页，不会同步更新)
        '''
        return self
    def FUN_CLARM_SOLVE(self):
        self._name="FUN_CLARM_SOLVE"
        self._gbkname="克莱姆法则求解线性方程组"

        self._function='''
        算法DET_COFACT可以求一个行列式某行某列的余子式
        算法源代码：
        def getInvNumber(argList):
            ans = 0
            for i in range(len(argList)):
                for j in range(i):
                    if argList[j] > argList[i]:
                        ans += 1
        return ans
        '''
        self._knowlege='''
        对于n个不同的元素，先规定各元素之间有一个标准次序，
        在这n个不同的元素的任一排列中，当某两个元素的先后次序与标准次序不同时，
        就说该排列有一个逆序，一个排列中所有逆序的总数叫做这个排列的逆序数.
        逆序数为奇数的排列叫奇排列，逆序数为偶数的排列叫偶排列.
        一个排列每经过一次对换都会改变排列的奇偶性.
        在全部的n阶排列中，奇排列和偶排列个数相等.
        '''
        self._program_pre='''
        1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)
        2. 矩阵只需要有一行，如果矩阵有多行，算法只对第一行进行逆序数的计算
        '''
        self._program_post ='''
        1.运行结束后，矩阵（行列式）的前置字符串会有说明文字
        2.后置字符串会显示逆序数的值
        3.算法对矩阵本身没有任何影响,对其它矩阵页也没有影响.(比如矩阵前页，不会同步更新)
        '''
        return self
    def DET_STEP_COFACT(self):
        self._name="DET_STEP_COFACT"
        self._gbkname="行列式的按行展开法则求值"

        self._function="%+*s算法DET_STEP_COFACT利用行列式的按行展开法则计算行列式的值\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*s算法根据输入参数确定要展开的行列式的行号，然后显示出每个余子式及最终行列式的值\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*sDET_STEP_COFACT是拉普拉斯定理的特殊情况，可参考验证拉普拉斯定理\n" %(len("算法功能介绍：\n")," ")

        self._args="row--整数，代表要展开行列式的行号.注意：从零开始，即第1行要输入0；第k行要输入(k-1)\n"
        self._knowlege="行列式按行展开法则：\nn阶行列式的值等于它的任意一行各元素与其代数余子式乘积之和\n"

        self._program_pre="%+*s1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)\n" %(len("算法运行的前置条件:\n")," ")
        self._program_pre+="%+*s2. 矩阵的行数与列数必须相等\n" %(len("算法运行的前置条件:\n")," ")
        self._program_pre+="%+*s3. 输入的参数必须是整数，必须大于等于0，小于行列式的行数\n" %(len("算法运行的前置条件:\n")," ")

        self._program_post ="%+*s1.运行结束后，会出现2n+1个矩阵，其中第1个是原矩阵\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post ="%+*s  其它2n个矩阵分别是展开的子式和余子式\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s2.行列式的算式及子式的整体介绍在第1个矩阵的后置字符串中\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s3.矩阵前页也包含了除知识要点外的所有的内容，知识要点在第1个矩阵的前置字符串中\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s4.算法产生全新的矩阵页，原有矩阵页中的所有矩阵不再出现在运算结果中\n" %(len("算法运行的后置条件:\n")," ")
        return self
    
    def DET_SETP_ROWOP(self):
        self._name="DET_SETP_ROWOP"
        self._gbkname="按行列式的性质求值"

        self._function="%+*s算法DET_SETP_ROWOP利用行列式的性质计算行列式的值\n" %(len("算法功能介绍：\n")," ")
        self._function+="%+*s算法根据行列式的性质（主要是下文说明的两个），显示行变换的每一步，最终显示行列式的值.\n" %(len("算法功能介绍：\n")," ")
        

        
        self._knowlege="行列式的性质：\n    互换行列式的两行，行列式变号\n"
        self._knowlege +="    用行列式的某行的元素乘以k加到其他行的对应元素上去，行列式的值不变\n"

        self._program_pre="%+*s1. 矩阵页面必须定位至矩阵页（不要定位到矩阵首页)\n" %(len("算法运行的前置条件:\n")," ")
        self._program_pre+="%+*s2. 矩阵的行数与列数必须相等\n" %(len("算法运行的前置条件:\n")," ")
        

        self._program_post ="%+*s1.运行结束后，会出现多个矩阵，最后一个一般是上三角阵\n" %(len("算法运行的后置条件:\n")," ")
        self._program_post +="%+*s5.算法产生全新的矩阵页，原有矩阵页中的所有矩阵不再出现在运算结果中\n" %(len("算法运行的后置条件:\n")," ")
        return self
