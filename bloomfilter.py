# -*- coding: utf-8 -*-
"""
@author: soarroyo
"""

import math
import mmh3
from fnvhash import fnv1a_32
 
from bitarray import bitarray



class BloomFilter:
    
    #IDEA to save bit array for future uses
    #IDEA escalable bloom filter and other hashing options
    #TODO: better performance when adding large number of items

    def __init__(self, n,prob=0):               
        self.n=n
        self.addedWords=0            
        if(prob==0):
            self.prob=0.4  
        else:
            self.prob=prob
        self.m=math.ceil(self.calculateM(self.n,prob))        
        self.k=self.calculateK(self.m, self.n)            
        self.bit_array = bitarray(self.m)
        self.bit_array.setall(0)        
        
    
    def probability_falsePositives (self, k, n, m):
        probability_of_success = math.e**(
            (-k * float(n)) / m)
        return (1.0 - probability_of_success)**k

        
    def add(self,word):  
        print("Adding :",word, "to 1 in",self.k,"indexes")     
        if(self.addedWords<self.n):
            self.addedWords+= 1
            for h in range(self.k):
                murmur = mmh3.hash(word)          
                fnvhash= fnv1a_32(word.encode('utf8'))   
                hIndex=(murmur+ h*fnvhash) % self.m
                print("\tIn index:",hIndex)
                self.bit_array[hIndex] = 1 
        else:
            print("Cannot add anymore words")
        
    def calculateM(self, n, p):
        m=-(n * math.log(p))/(math.log(2)**2) 
        return m
    
    def calculateK(self, m, n):       
        k = (m/n) * math.log(2) 
        if(k<1):
            k=1
        return int(k)  
    
    def lookup(self, word):
        #print("Checking",self.k,"linear combinations of ",word)
        print("****Looking :",word)     
        found=True
        for h in range(self.k):
            murmur = mmh3.hash(word)          
            fnvhash= fnv1a_32(word.encode('utf8'))   
            hIndex=(murmur+ h*fnvhash) % self.m
            if self.bit_array[hIndex]==0:
                found=False
                                   
        return found
          
    
    def printResults(self):
        print("****Print Results***** :")
        print("bit array size(m) :",self.m)
        print("items entered (n):",self.n)
        print("Hash Functions(k):",self.k)
        #print("Bit array",self.bit_array)
        print("False positives Probability",self.prob)
        

