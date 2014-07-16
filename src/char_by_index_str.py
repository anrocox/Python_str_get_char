#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

How to get the character that is in an index of the string in python?

Como obtener el caracter que se encuentra en un indice del string en python?
'''

#create a str
s = 'fresh fried fish'
print(s)

#is similar to the handling of lists, the index is defined in brackets
c = s[3]
print(c)

#return the character in the index 6
c = s[6]
print(c)

#can also use negative indices to get a character from string
c = s[-3]
print(c)
