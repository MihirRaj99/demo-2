'''
Created on 19-May-2022

@author: Asus
'''
class employee:
    def __init__(self,name,salary,age):
        self.name = name
        self.age = age
        self.salary = salary
    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.salary)
ob = employee('mihir',10000,22)
ob.show_details()
#demo code
