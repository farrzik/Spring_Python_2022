#!/usr/bin/env python
# coding: utf-8

# In[4]:


def twoSum_casual(self, nums, target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return i,j

def twoSum_b_search(self, numbers, target: int):
    i = 0
    j = len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            return i+1,j+1
        elif s > target:
            j -= 1
        else:
            i += 1

def twoSum_set(self, numbers, target: int):
    a = set(numbers)
    for i in range(len(numbers)):
        b = target - numbers[i]
        if b in a:
            if i == numbers.index(b):
                return i+1,numbers.index(b)+2
            else:
                return i+1,numbers.index(b)+1


# In[ ]:




