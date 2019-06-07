#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:27:41 2019

@author: bridgetboakye
"""

class Descriptive_Calc:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.total = sum(data)
        
def find_range(numbers):
    return max(numbers) - min(numbers)

NUMS = [1,4,5]
find_range(NUMS)