# class TestClass:
#     x = 0
#
#     def __init__(self):
#         self.y = 0
#
#
# a = TestClass()
# b = TestClass()
#
# z = 0
#
# print(a.x, a.y, b.x, b.y)
#
# TestClass.x += 1
# a.y = 7
#
# print(a.x, a.y, b.x, b.y)
#
# a.x = 3
#
# TestClass.x = 2
#
# print(a.x, a.y, b.x, b.y)
#
# del(a.x)
#
# print(a.x)


# def f():
#     print(a)
#
# a = 3
# f()


# class TestClass:
#     x = []
#
#     def __init__(self):
#         self.y = 0
#
#
# a = TestClass()
# b = TestClass()
#
# z = 0
#
# print(a.x, a.y, b.x, b.y)
#
# a.x.append(1)
# a.y = 7
#
# print(a.x, a.y, b.x, b.y)
#
# a.x = a.x + [3]
#
# b.x.append(2)
#
# print(a.x, a.y, b.x, b.y)
#
# del(a.x)
#
# print(a.x)

# class TestClass:
#     cnt = 0
#
#     def __init__(self):
#         TestClass.cnt += 1
#
#     def __del__(self):
#         TestClass.cnt -= 1
#
#
# a = TestClass()
# print(a.cnt)
# b = TestClass()
# print(a.cnt)
# # del(b)
# b = TestClass()
# print(a.cnt)


class Node:
    def __init__(self, value, next=None):
        self.v = value
        self.n = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def append(self, value):
        self._len += 1
        if self._head is None:
            self._head = Node(value)
            self._tail = self._head
            return
        self._tail.n = Node(value)
        self._tail = self._tail.n

    def __getitem__(self, item):
        if item >= self._len:
            raise IndexError
        cur = self._head
        for i in range(item):
            cur = cur.n
        return cur.v

    def __len__(self):
        return self._len

    def __str__(self):
        res = []
        cur = self._head
        for i in range(len(self)):
            res.append(cur.v)
            cur = cur.n
        return str(res)


# A = LinkedList()
# for i in range(10):
#     A.append(i ** 2)
# print(A)
# print(A[3])
# # A[2] = 7
# print(len(A))
#
# for element in A:
#     print(element)


# A = [2, 8, 9, -4]
# it = iter(A)
# print(type(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
#
# def my_for(A):
#     it = iter(A)
#     try:
#         while True:
#             print(next(it))
#     except StopIteration:
#         return
#
# my_for(A)

# while True:
#     try:
#         x = int(input())
#         print(6 / x)
#     except ArithmeticError:
#         print("type non-zero value")
#     except ValueError:
#         print("type correct value")
#     else:
#         break
#     finally:
#         print("try was here")

# with open("class_data.txt", mode="r") as f:
#     f.readline()
#     for line in f:
#         print(line.strip())
#
# with open("class_data.txt", mode="a") as f:
#     f.write("abcd\n")


import pickle
x = {2: "abc", 7: "bf"}
with open("data.bin", mode="wb") as f:
    pickle.dump(x, f)




