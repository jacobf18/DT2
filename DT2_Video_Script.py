#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random

itemsIn = [
    'Forceps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps',
    'Clamps'
]

itemsRed = [
    'Scalpel Blade',
    'Scalpel Blade',
    'Scalpel Blade',
    'Scalpel Blade'
]

itemsOut = []

def moveItem(fromList, toList, fromName, placement, index):
    outputStr = ''
    if(placement == 'outside'):
        outputStr += 'Take a ' + fromList[index] + ' from the ' + fromName + ' out of the field.'
    else:
        outputStr += 'Put a ' + fromList[index] + ' into the ' + placement + ' from the ' + fromName + '.'
    toList.append(fromList[index])
    fromList.remove(fromList[index])
    return (outputStr + '\n')

def outputInstructions(taskCount):
    takeStr = 'Take out a '
    putStr = 'Put in a '
    outStr = ''
    fromLocal = ''
    toLocal = ''
    
    for i in range(taskCount):
        randNum = random.randint(0,100)
        # First we need to check if what we are about to move is a sharp
        mergedList = itemsIn + itemsRed + itemsOut
        index = random.randint(0, len(mergedList)-1)
        
        # If the selected object is a sharp, then can be moved between all locations.
        if(mergedList[index] == 'Scalpel Blade' or mergedList[index] == 'Needle'):
            # Now, the object can be moved anywhere.
            n = random.randint(0,1)
            if(index >= len(itemsIn) + len(itemsRed)):
                index -= len(itemsIn) + len(itemsRed)
                fromLocal = 'outside'
                if(n == 0):
                    toLocal = 'table'
                else:
                    toLocal = 'redbox'
            elif(index >= len(itemsIn)):
                index -= len(itemsIn)
                fromLocal = 'redbox'
                if(n == 0):
                    toLocal = 'table'
                else:
                    toLocal = 'outside'
            else:
                fromLocal = 'table'
                if(n == 0):
                    toLocal = 'outside'
                else:
                    toLocal = 'redbox'
            if(fromLocal == 'outside' and toLocal == 'table'):
                outStr += moveItem(itemsOut, itemsIn, fromLocal, toLocal, index)
            elif(fromLocal == 'outside' and toLocal == 'redbox'):
                outStr += moveItem(itemsOut, itemsRed, fromLocal, toLocal, index)
            elif(fromLocal == 'table' and toLocal == 'outside'):
                outStr += moveItem(itemsIn, itemsOut, fromLocal , toLocal, index)
            elif(fromLocal == 'table' and toLocal == 'redbox'):
                outStr += moveItem(itemsIn, itemsRed, fromLocal, toLocal, index)
            elif(fromLocal == 'redbox' and toLocal == 'outside'):
                outStr += moveItem(itemsRed, itemsOut, fromLocal, toLocal, index)
            elif(fromLocal == 'redbox' and toLocal == 'table'):
                outStr += moveItem(itemsRed, itemsIn, fromLocal, toLocal, index)
        # Not a sharp
        else:
            # The object can only be moved between outside and the table
            if(index >= (len(itemsIn) + len(itemsRed))):
                index -= len(itemsIn) + len(itemsRed)
                fromLocal = 'outside'
                toLocal = 'table'
            elif(index >= len(itemsIn)):
                index -= len(itemsIn)
                fromLocal = 'table'
                toLocal = 'outside'
            else:
                fromLocal = 'table'
                toLocal = 'outside'
            if(fromLocal == 'outside'):
                outStr += moveItem(itemsOut, itemsIn, 'outside', 'table', index)
            else:
                outStr += moveItem(itemsIn, itemsOut, 'table', 'outside', index)
    return (outStr)

print('How many instructions?')
x = input()
print(outputInstructions(int(x)))
