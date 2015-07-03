'''
author : joe Huang R03922133@ntu.edu.tw
'''

from collections import Counter
from _ast import Num

myfile = open("input.txt", "r")
output = open("output.txt","w")
    
data = myfile.read()

def neednewline(i,count):
    
    while data[i] != ' ' :
        i += 1
        count += 1 
        if data[i] == ',' :
            break
        
    if count >= 60 :
        return True 
    else : 
        return False 

def countword(input_string):
    num = 0
    words = input_string.split()
    for index in range(len(words)): 
        num += 1
    return num 

count = 1 
UorL = 0  # 0: lower  1: upper
wordcount = 0
charcount = 1
need = 0

new_string = ''

#new_string = data[:index]+'\n' +data[index:]


for index in range(len(data)) :
        
    if data[index] == ' ' or data[index] == '.' or data[index] ==',' :
            
        if (index+1) != len(data) and neednewline(index+1, count+1) == True : 
            need = 1
        
        elif (index+1) == len(data) :     
            charcount += 1 
            break 
                
    if index ==0 :
        new_string += data[index].upper()
        charcount += 1
        count += 1
        continue 
    
    elif data[index] == '.' :    
        new_string += data[index] + " "
        need = 1
        UorL = 1
        charcount += 1     
        count += 1
        
    elif data[index] == ',' : 
        if data[index+1]==' ':
            new_string += data[index] 
            charcount += 1            
            count += 1
            
        elif data[index-1].isdigit() and data[index+1].isdigit() :
            new_string += data[index]
            charcount += 1
            count += 1
                   
        else : 
            new_string += data[index] + " "
            low = 1
            charcount += 2
            count += 1
            
    else :
        if UorL == 1 :
            new_string += data[index].upper()
            UorL = 0
            charcount += 1
            count += 1
              
        elif UorL == 0 :
            new_string += data[index].lower() 
            low = 0
            charcount += 1
            count += 1
                
    if need == 1 :
        new_string += "\n" 
        need = 0
        count = 1
        

wordcount = countword(new_string)

new_string += "\n"
new_string += "Total count : %d words, %d characters" %(wordcount , charcount)
         
output.close()

print new_string

output = open("output.txt","w")
output.write("%s" %new_string)


