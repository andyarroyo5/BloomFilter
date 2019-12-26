# -*- coding: utf-8 -*-
"""
@author: soarroyo
"""

import math
import random

from bloomfilter import BloomFilter


def probability_falsePositives (k, n, m):
    probability_of_success = math.e**(
        (-k * float(n)) / m)
    return (1.0 - probability_of_success)**k

def calculateN(self, k, m):       
        n= k /math.log(2)*m  
        return int(n)   
    
def calculateM( n, p):
    m=-(n * math.log(p))/(math.log(2)**2) 
    return m

def calculateK( m, n):       
    k = (m/n) * math.log(2) 
    return int(k)  

#trycatch when bf is not defined
def look(bf):
    keepLooking=True
    print("######## Looking ##########")

    while(keepLooking):
        res=input("Write a word to lookUp or exit\n")
        if(res=="exit"):
            keepLooking=False
        else:
            if(bf.lookup(res)):
                print("Probably")
                if(res not in itemsAdded):
                    false_positives.append(res)
                    print("False Postive")
            else:
                print("Definetely not")
                if(res not in itemsAdded):
                    print("Correct")     

if __name__ == '__main__':
       
    print("######## Read WordList File ##########")  
    #338882 - number of words
    lines = open("./wordlist.txt").read().splitlines()     
    items=[]
    itemsAdded=[]
    false_positives=[]
    preset_config=True
    
    
    res=int(input("Fast Config 1-yes 2-no?\n"))
    if(res!=1):
        preset_config=False 
    
    # All items but without user option, configuration set
    #Todo: memory storage
   
    if(preset_config):
        items=lines[1000:7000]
        itemsNotInSet=2500
        AddItems=round(len(items)-itemsNotInSet)
        prob=0.4
        
        bf = BloomFilter(AddItems, prob)
        
        itemsAdded=items[:-int(itemsNotInSet)]   
        for i in range(AddItems):
            print("adding word: ",i,"out of ",AddItems)
            bf.add(items[i])
            
            
        notInSet=items[2501:]      
        
        for i in range(itemsNotInSet):  
            if(i%2==0):
                word=items[i]
            else:
               word=notInSet[i]
                          
            if(bf.lookup(word)):
                print("Probably")
                if(word in notInSet):
                    false_positives.append(word)
                    print("False Postive")
            else:
                print("Definetely not")
                if(word in notInSet):
                    print("Correct")
                    
        print("False positives:", len(set(false_positives)))    
        print("{0:.0%}".format(len(set(false_positives))/len(items)))                   
        print("TotalItems",len(items))
        print("Items Added",AddItems)
        print("Not Added Items",len(notInSet))
        bf.printResults()            
            
                
    else:  
        try:
            totalItems=int(input("Enter number of items or default\n"))
            for i in range(totalItems):
                items.append(random.choice(lines))
        except ValueError:
            items=lines
       
       
        try:
            percent=float(input("Set percentage % of items not in the list (ex: 10,25,50) or enter for default\n"))
            #print(percent/100)       
            percent=round(percent*len(items)/ 100, 2)
        except ValueError:
            percent=0.1      
        
        itemsNotInSet=int(percent)
        if(itemsNotInSet<1):
            itemsNotInSet=math.ceil(itemsNotInSet)
        AddItems=round(len(items)-itemsNotInSet)
        
        print("Items not in the set",itemsNotInSet)
        print("Items to add",AddItems)
       
           
        try:
            prob=float(input("Set percentage of Probability of false positives (ex: 10,25,50)\n"))
            prob=round(prob/100, 2)    
        except ValueError:
            prob=0.3       
        print("Probability",prob)
        
        
        print("######## Bloom Filter ##########")  
                
        bf = BloomFilter(AddItems, prob)
        bf.printResults()
    
    
        for i in range(AddItems):
                while True:
                    r=random.choice(items)
                    if(r  not in itemsAdded):
                        itemsAdded.append(r)
                        bf.add(r)
                        break
           
        notInSet= [x for x in items if x not in itemsAdded]          
                   
        for i in range(len(notInSet)):  
            if(i%2==0):
                word=random.choice(itemsAdded)
            else:
               word=random.choice(notInSet)
                          
            if(bf.lookup(word)):
                print("Probably")
                if(word in notInSet):
                    false_positives.append(word)
                    print("False Postive")
            else:
                print("Definetely not")
                if(word in notInSet):
                    print("Correct")
                    
       #input loook
        look(bf)                
                    
        print("False positives:", len(set(false_positives)))    
        print("{0:.0%}".format(len(set(false_positives))/len(items)))                   
        print("TotalItems",len(items))
        print("Items Added",AddItems)
        print("Not Added Items",len(notInSet))
        bf.printResults()   
 



    
    

