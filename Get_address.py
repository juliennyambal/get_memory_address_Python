#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 22:05:57 2017

@author: julien
"""

#from https://stackoverflow.com/questions/16408472/print-memory-address-of-python-variable

#Get memory address

import matplotlib.pyplot as plt


img = plt.imread('/home/julien/Pictures/000456.jpg')
print hex(id(img))

#in this case, clone1, links to the same address as img: clone --> img --> actual image
#if we modify clone1, we will also modify the content of img, since img point to the 
#same address as clone1
clone1 = img
print hex(id(clone1))

#In this case, clone2, is the copy of img but in a different memory address.
#it implies that the changes on img do not affect clone2
#which is: img --> actual image and clone2 --> actual image, but the point to 
#different memory addresses
clone2 = img.copy()
print hex(id(clone2))