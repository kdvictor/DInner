# class Father():
#     def PrintFirstName(self):
#         print("Liu")
#
# class Child(Father):
#     def PrintLastName(self):
#         print("Huan")
#     def PrintFirstName(self):
#         print("liu")
#
# child = Child()
# child.PrintFirstName()
# child.PrintLastName()


# 多重继承
# class A():
#     def PrintA(self):
#         print("A")
#
# class B():
#     def PrintB(self):
#         print("B")
#
# class C(A, B):
#     def PrintC(self):
#         print("C")
#
# c = C()
# c.PrintA()
# c.PrintB()
# c.PrintC()

# struct
# from struct import *
# pack_data = pack('iif', 4,6,6.7)
# print(pack_data)
# print(calcsize('i'))
# print(calcsize('f'))
# print(calcsize('iif'))
# orgin_data = unpack('iif', pack_data)
# print(orgin_data)

# map函数，不会改变原有列表，会返回一个新的列表
def Double(number):
    return number*2
list_original = [23.4, 43, 56]
list_new = list(map(Double, list_original))

print(list_new)
