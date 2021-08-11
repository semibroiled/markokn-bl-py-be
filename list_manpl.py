#-----Generate list of numbers
import random 
numlst =[]
while len(numlst)<20:
    numlst.append(random.randint(-100,100))
print(numlst)
#Print all positive numbers and max number from those in lst
posnumlst=[]
for i, number in enumerate(numlst):
    if number>0:  
         posnumlst += [number]
           
print(posnumlst)
print(max(numlst))
   
#I want to incorporate a while loop  and make it all run under
#one code loop unit instead of separating script 