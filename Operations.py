import threading
from threading import*
import time
import sys
#Dictionary to store the keys and values
dic={}
#File name where the text file is saved
filename=r'C:\Users\A YASVANTH SAI\Desktop\End Semester\test.txt'
#Creating a operation with timeout or without timeout
def create(key,value,timeout=0):
    sys.stdout=open(filename,'w')
    if key in dic:
        print('Similar key exists') #error message
        sys.stdout.close()
    else:
        if key.isalpha(): #If all char are from a-z
            if len(dic)<(1024*1024*1024) and value<=(16*1024*1024): #Checking space constraint
                if timeout==0:
                    lst=[value,timeout]
                else:
                    lst=[value,time.time()+timeout]
                if len(key)<=32: #if not exceeds 32
                    dic[key]=lst
            else:
                print('Your memory limit has exceeded') #error message
                sys.stdout.close()
        else:
            print('Error: Enter again') #error message
            sys.stdout.close()
#Read operation: key is sufficient
def read(key):
    sys.stdout=open(filename,'w')
    if key not in dic:
        print('Key not present in dictionary')#error message
        sys.stdout.close()
    else:
        a=dic[key]
        if a[1]!=0:
            if time.time()<a[1]: #Checking time to live condition
                print(str(key)+":"+str(a[0]))
                sys.stdout.close()
            else:
                print('Expired')
                sys.stdout.close()        
        else:
            print(str(key)+":"+str(a[0]))
            sys.stdout.close()
        
#Deleting a key if present
def delete(key):
    sys.stdout=open(filename,'w')
    if key not in dic:
        print('Key is not available to delete')#error message
        sys.stdout.close()
    else:
        a=dic[key]
        if a[1]!=0:
            if time.time()<a[1]:
                del dic[key]
                print('Key successfully deleted')
                sys.stdout.close()
            else:
                print('Time to live expired')
                sys.stdout.close()
        else:
            del dic[key]
            print('Key successfully deleted')
            sys.stdout.close()

#Modifying a value of a key if needed to be changed
def modify(key,value):
    sys.stdout=open(filename,'w')
    a=dic[key]
    if a[1]!=0:
        if time.time()<a[1]:
            if key not in dic:
                print('Key not available to modify')#error message
                sys.stdout.close()
            else:
                l=[]
                l.append(value)
                l.append(a[1])
                dic[key]=l
        else:
            print('Error')
            sys.stdout.close()
    else:
        if key not in dic:
            print('Key not available to modify')#error message
            sys.stdout.close()
        else:
            l=[]
            l.append(value)
            l.append(a[1])
            dic[key]=l
            
        








