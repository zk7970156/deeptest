# -*- coding:utf-8 -*-

__author__ = "菜鸟中年人"

class Cacl:
    #初始化
    def __init__(self,a,b):
        self.a = a
        self.b = b
    #重置数值
    def __set__(self,a,b):
        self.a = a
        self.b = b
    #加法
    def add(self):
        return self.a + self.b
    #减法
    def sub(self):
        return self.a - self.b
    #乘法
    def mul(self):
        return self.a * self.b
    #除法
    def div(self):
        if b != 0:
            #3代表保留小数点后三位
            return round(self.a / self.b,3)
        else:
           print ("Dividend can not be 0!")
def test_sum(cacl):
    sum = cacl.add()
    print(sum)
def test_sub(cacl):
    sub = cacl.sub()
    print(sub)
def test_mul(cacl):
    mul = cacl.mul()
    print(mul)
def test_div(cacl):
    div = cacl.div()
    print(div)
if __name__ =="__main__":
    #while循环
    var = 1
    while var == 1:
     #判断a和b的类型进行异常处理
        try:
            a = float(input("Please enter a:"))
            b = float(input("Please enter b:"))
            select = input("Please select(+,-,*,/):")
            cacl = Cacl(a,b)
            #判断运算符号！
            if select == "+":
                test_sum(cacl)
            elif select == "-":
                test_sub(cacl)
            elif select == "*":
                test_mul(cacl)
            elif select =="/":
                test_div(cacl)
            else:
                print("Please select the correct operation symbol")
                break
        except :
            print("The type a is wrong!")
