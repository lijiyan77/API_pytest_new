# -*- coding: UTF-8 -*-
# @File  : test_0330.py
# author by : Li Jiyan
# date : 2020/3/30

# name=''
# while not name.strip():
#     name = input('Please enter your name: ')
# print('hello, %s' % name)

# numbers=[0,1,2,3,4,5,6,7,8,9]
# for number in range(0,10):
#     print(number)

# d={'x':1,'y':2,'z':3}
# for key,value in d.items():
#     print(key,"corresponds to",value)

# names=['anne','beth','george','damon']
# ages=[12,45,32,102]
# for i in range(len(names)):
#     print(names[i],'is',ages[i],'years old.')
# a=zip(names,ages)
# print(list(a))
# for name,age in list(zip(names,ages)):
#     print(name,'is',age,'years old.')


# from math import sqrt
# for n in range(99,0,-1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break


# word = 'dummy'
# while word:
#     word = input('please enter a word: ')
#     print('The word was ' + word)

# while True:
#     word = input('Please enter a word: ')
#     if not word:break
#     print("The word was " + word)

# from math import sqrt
# for n in range(99,81,-1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
# else:
#     print("Didn't find it")

# def hello(name):
#     return ('hello, '+name+'!')
#
# print(hello('jojo'))

# def fibs(num):
#     result = [0,1]
#     for i in range(num-2):
#         result.append(result[-2]+result[-1])
#     return result
#
# print(fibs(10))

# def print_params_3(**params):
#     print(params)
#
# print_params_3(x=1,y=2,z=3)

# def print_params_4(x,y,z=3,*pospar,**keypar):
#     print(x,y,z)
#     print(pospar)
#     print(keypar)
#
# print_params_4(1,2,3,5,6,7,foo=1,bar=2)

def store(data,*full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:names.insert(1,'')
        labels = 'first','middle','last'
        for label,name in list(zip(labels,names)):
            pass