# -*- coding: utf-8 -*-
"""DAWP_EX_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YkjHISRwBzAxqUvWWfNGT53DQVgsaU5S

**AIM:Create a Ipython notebook to work with numpy module**
.(a)creating 1D And 2D arrays
.(b)Arithetic operations on arrays
.(c)Basic indexing,Slicing And Boolean Indexing
.(d)Transposing Arrays and Swapping axes
"""

import numpy as np

"""**(a) Creating 1D and 2D Arrays**"""

#Creating 1D Array from the list
arr1d=np.array([10,20,30,40,50])#it take argument as any iterable object
print(arr1d)#the main diff b/w array & list is list seperate by ',' but array doesn't seperate by ','

numbers=[10,20,30,40,50,60]
arr1d=np.array(numbers)

type(arr1d)#nd means number of dimensions

#Creating 2D Array from the list
arr2d=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr2d)

#properties of 1D array
arr1d.size#it returns no.of elements in array

arr1d.ndim#ndim is no.of dimensions of given array

arr1d.shape#it returns the onlysize because it has only one row

arr2d.size#it returns total number of elements

arr2d.ndim#it return the no.of dimensions

arr2d.shape#it returns the no.of rows and no.of columns

#creating 1D array from numpy arrange()
ar1d=np.arange(10,16)#arange(start,stop,stepsize)
print(ar1d)

#creating 1d array with all zeros
zero1d=np.zeros(5)#by default the all zeros array is in float
print(zero1d)
zero1d1=np.zeros(5,dtype=int)
print(zero1d1)

#creating 2D array with all zeros
zero2d=np.zeros(())
zero2d=np.zeros((3,3))
print(zero2d)

#creating 1D array with all ones
one1d=np.ones(5)#by default the all zeros array is in float
print(one1d)
one1d1=np.ones(5,dtype=int)
print(one1d1)

#creating 2d array with all ones
one12d=np.ones((3,3))
print(one12d)

#creating Identity matrix
id_matrix=np.eye(3)
print(id_matrix)#here all diagonals are 1

#creating arrays using numpy random module
from numpy import random

#creating 1-D & 2-D arrays using randint()
rint1d = random.randint(10,size=5)#here 10 is also inclusive
print(rint1d)
rint2d=random.randint(2,35,size=(3,3))
print(rint2d)

#creating 1-D ANd 2-D arrays using randn()-normal distribution
rn1d=random.randn(5)#1-D array
rn2d=random.randn(3,3)
print(rn1d)
print(rn1d.round(2))
print(rn2d)
print(rn2d.round(2))

#creating 1-D & 2-D arrays using rand()-uniform Distribution
rnd1d=random.rand(4)
print(rnd1d)
rnd2d=random.rand(3,3)
print(rnd2d)

##creating 1-D & 2-D arrays using random()-values wil be Half interval b/w [0.0,1.0) "[ is inclusive ,) is exclusive"
rndm1d=random.random(4)
print(rndm1d)
rndm2d=random.random((2,2))
print(rndm2d)

#Create 1-D array with equal distance b/w elements - linspace()
lns1d=np.linspace(10,20,5)
print(lns1d)

"""**(B)Arithemetic operations on arrays**"""

import numpy as np

a1=np.array([2,4,3,1])
a2=np.arange(5,9)
n=5
m=2

a1+n

print(a2-3)

a1/m

print(a1)
print(m)
print(a1/m)#floating point divison

print(a1)
print(m)
print(a1//m)#integer divison

print(a2)
print(a2**2)

"""**arithematic operation between arrays**"""

print("a1=",a1)
  print("a2=",a2)

a1+a2

a3=[4,5,6,7,8,9,10]

a1+a3#to perform addition b/w two two arrays there should be equal size of both arrays

a1/a2

a1//a2

a1/np.zeros(4)#here we will not get runtime error we will get only runtime warning

from numpy import random

#2-D arrays
b1=random.randint(5,20,size=(3,3))
b2=random.randint(1,10,size=(3,3))
b3=np.eye(3)

print(b1)
print(b2)
print(b3)

b1+b3

b1/b3

b1//b3

print(5//2)#here int/int only returns the int as result in integer divison
print(5//2.0)
print(5.0//2.0)

"""**Boolean indexing**"""

import numpy as np

arr1d=np.random.randint(-10,10,size=8)
print(arr1d)

bool_1d=arr1d>=0
print(bool_1d)
print(arr1d[bool_1d])

arr2d=np.arange(5,21).reshape(4,4)
print(arr2d)

bool_2d=arr2d < 13
print(bool_2d)

print(arr2d[bool_2d])

"""**Fancy Indexing**"""

ar2d=np.arange(10,26).reshape(4,4)

ar2d

ar2d[2,3]

ar2d[[2,3]]

ar2d[[3,1]]

ar2d[[3,3]][:,[2,0]]#combination of slicing and fancy indexing

ar2d[[3,1],[2,3]]

"""**Transpose**"""

ar2d.T

ar2d.transpose()

