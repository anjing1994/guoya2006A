# a = 1,2,3,4,5
# print (a)
#
# a = 10
# b = 20
# print (a + b)
#
#
# a,b,c = [1,2,3]
#
# print(a)
#
# a = 10
# b = 20
# print (a * b)
#
#
# a = 123
# b = 456
#
# print(a + b)
# print(a)
# print(b)
#
# a = "12345678910"
# print(a[0])
# print(a[1:])
# print(a[:3])
# print(a[3:8])

#
# a,b,c,*z = (1,2,3,4,5,6,7,8,9)
# print(a)
# print(b)
# print(z)
#
#
# a =5
# b = 10
# print(a + b)
#
#
# print(a/b)
# print(a%b)
# print(a//b)
#
# z = 856230
# print(z % 10)
#
#
#
# b = 85665
# print(b % 1000)
#  #b = b // 10
# b //= 1000
# print(b)
#
# print(b % 10)
#
#
# #a_ = [30,50,80,75,65,90,73,46,88,23,100]
#
#
# #for a in a_:
#     if(a > 0 and a < 60 ):
#         print ("不及格")
#     elif(a>60 and a < 70 ):
#         print ("及格")
#     elif (a > 71 and a < 80):
#         print("良好")
#     elif (a > 81 and a < 100):
#         print("优秀")
#
#
# flag = True
# a = 55
#
# while flag:
#     b = int(input("请输入数字"))
#     if b > a :
#         print("大了")
#     elif (b < a) :
#         print("小了")
#     else:
#         print("恭喜你猜对了！")
#         flag = False




# flag = True
# a = 78
# while flag:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("猜大了")
#     elif b < a:
#         print("猜小了")
#     else:
#         print("猜对了")
#         flag = False
# s = 0
# for i in range(1,10):
#     s=s + i
# print(s)

# a_ = [30,20,66,76,44,80,79,80]
#
# for a in a_:
#     if (a>0 and a<60):
#         print("不及格")
#     if (a>=60and a<=70):
#         print("及格")
#     if (a>=71 and a<=80):
#         print("良好")
#     if (a>80 and a<100):
#         print("优秀")
#



#找出100以内可以被3整除的数字
# for i in range (1,100):
#     if (i % 3!=0):
#         continue
#     print(i)


# def shang_yu(a,b):
#     if(b == 0):
#         return None
#     else:
#         return  (a//b,a%b)
#

# uuu=shang_yu(10,20)
# uuu=shang_yu(b=20,a=10)
# if uuu is  None:
#     print("参数错误")
# else:
#     print("商为：",uuu[0],"余数为:",uuu[1])
#

#
# def sm(a,b=2):
#     return  a+b
#
# print(sm(2,3))


# def suml(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
#
# print(suml(1,2,3,4,5,6,7,8,9))



# #面向对象
# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c=calc()  #类的实例化 c对象
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()



#
# class calc():
#     res=None
#
#     def __init__(self,a,b):  #魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c= calc(100,50)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

#
# #九九乘法表
# for i in range (1,10):
#     for j in range(1,i+1):
#         print("aaaaa",end="\t")
#     print()
#
# for i in range (1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",j*i, end="\t")
#     print()


#
# l = [2,3,1,5,234,2,78,89,9,3,1,6,8,95,3,2,5,8,9]
#
# length = len(l)
# for i in range(length-1,0,-1):
#     for j in range(i):
#         if (l[j] > l[j+1] ):
#             l[j],l[j+1] = l[j+1],l[j]
#
# print(l)

# g = '我是全局变量' # 全局变量
#
# def var():
#     j = "我是局部变量" # def可以修改变量作用域
#     print(j)
#     print(g)
#
# var()
# print(g)
# print(j) # j是局部变量，代码块结束就被python解释器回收


# l = ["小明","小张"]
# l.append("小红")
# print(l)
#
#
# l = ["小明","小张"]
# t = ["小红","小李"]
# l.extend(t)
# print(l)
#
#
# l = ["小明","小张"]
# l.insert(1,"小红")
# print(l)



# class aaa():
#
#     pub_res = "公有变量"
#     __pri_res = "私有变量1"
#     _pri_res = "私有变量2"
#
#     def pub_function(self):
#         print("公有方法")
#     def _pri_function(self):
#         print("私有方法1")
#     def __pri_function(self):
#         print("私有方法2")
#
#
# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa().pub_function())
# print(aaa()._pri_function())


# class parent():
#
#     money = 888
#     house = 8
#     __yi_wu = "衬衫"
#
#     def shou_yi(self):
#         print("乾坤大罗移")
#
#
#
# class Child(parent):
#     ai_hao = '花钱'
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#     pass
#
#
# c = Child()
# print(c.ai_hao)
# print(c.money)
# print(c.house)
# c.shou_yi()




# 字符串转列表  列表 元组 集合
# t = (1,2,3,4)
# # l = [1,2,3,4,5,65,7]
# # s = {1,2,3,4,6,9,8}
# # print(list(t))
# # print(tuple(l))
# # print(set(l))
# # print(list(s))
# # print(set(t))


#  打开模式：r读取  w清空写入  a追加写入   b二进制模式

# f = open("nba.txt",'w')
# f.write("i love you")  #输出
# f.close()
# f = ()


# f = open("nba.txt",'r')
# #print(f.read()) #默认读取全部数据
# #print(f.read(4)) #读取指定大小的数据
# #print(f.readline()) #按行读取，读取一行
# #print(f.readlines()) #按行读取，读取所有行
# f.close()

a = "abcdefghijklmnopqrstuvwxyz"
# print(a[0])
# print(a[-1])
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[::1])
# print(a[2:])
# print(a[:-2])


##  .format
# for i in range (1,10):
#      for j in range(1,i+1):
#          print("{} X {} = {}".format(j,i,i*j), end="\t")
#      print()
## 通过占位符格式化
# for i in range (1,10):
#      for j in range(1,i+1):
#          print("%d X %d = %d"%(j,i,i*j), end="\t")
#      print()



# l = [1,2,3,4,5,6,7,8,9]
#
# # l[0] = 999
# # print(l)
# l[1:3] = [777,888]
# print(l)



# print("{:,}".format(100000000000))
# # #
# # # print("{:^10}".format(123))
# # #
# # # print("{:.2f}".format(2.3456789))


# l = [2,3,4,5]
# # l.insert(1,"大内密探008")
# # print(l)
#
# print(l.pop(1))
# print(l)


# l = [1,2,3,4,5,6,7,8,9]
# l.remove(9)
# print(l)


# l = [True,1,2,3,4,5,6] #true=1   false=0
# l.remove(1)
# print(l)
#
#
# l.clear()
# print(l)

# a = [2,8,1,9,7,3,6,5,0,4]
# a.sort(reverse=True)
# print(a)
#
# a = [2,8,1,9,7,3,6,5,0,4]
# a.sort()
# print(a)
#
#
# d = {"name":"小明","age":"18","sex":"男"}




# try:
#     f = open("nba.txt","r")   #异常
#     print(f.read())
#     f.close()
# except:
#     print("北京欢迎你")
#
# print("上海欢迎你")
#
#
# def div(a,b):
#     try:
#         return a / b
#     except:
#         return
#
# print(div(10,0))