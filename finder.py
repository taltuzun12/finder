# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:34:04 2022

@author: Gökhan Tüzün
"""
import pandas as pd
import numpy as np
import warnings


warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

data=pd.read_csv('data.csv')

frame=pd.DataFrame(data)
frame=frame.fillna(0)

class finder(object):


    
    array_new=[]
    null= 0
    
    
    def __init__(self, enter, y, z):

        
        
        for x in frame.loc[:, y]:
            if x == enter:
                self.null += 1
                
                self.array_new.append(frame.loc[self.null-1 , z])
       
                
        
            else:
                self.null += 1
            
                
            
    def show(self):
        print(self.array_new)
        
        
        
        
hey=finder("x",'This solution is a Prototype', "id")
hey.show()
        
        
        
        
        





