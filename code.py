import threading
import time
d={}
def validate(key):
    if((key in d) and (time.time()<=(d[key][1]))):
        return 1
    else:
        return 0
    
def create(key,value,timeout=0):
    if(key in d):
        print("---------------------------error : key already present-------------------")
    else:
        
        if(key.isalpha() and len(d)<(1024*1024*1024) and len(bin(int(value))[2:])<=(16*1024*1024)):
            d[key]=[value,time.time()+timeout]
            print(d)
            print("_____________________________________________created "+ key +" successfully")


def read(key):
    if(validate(key)):
        print("_____________________________________"+key,d[key][0])
    else:
        print("----------time's up----------------------")

def update(key,value):
    if(validate(key)):
        d[key][0]=value
        print("___________________________________________updated successfully")
        print(key,d[key][0])
    else:
        del d[key]
        print("-------------------------time's up-----------------------------")

def delete(key):
    if(validate(key)):
        del d[key]
        print("___________________________________________________deleted successfully")
        print(".")
    # elif((key in d) and (time.time()>(d[key][1]))):
    #     del d[key]
    #     print("----------------------time is up this key is  going to be deleted-----------------------")
    else:
        del d[key]
        print("----------------------time's up-----------------------")

   
def run():
    print("choose opertion to be performed \n1.create,\n2.read,\n3.update,\n4.delete,\n5.exit,\n6.view")
    option=input()
    if(option=="1"):
        print("please enter key, value, timeout in seconds")
        key=input()
        value=input()
        timeout=int(input())
        t1 = threading.Thread(target=create, args=(key,value,timeout))
        t1.start()
        run()
    elif(option=="2"):
        print("please enter key")
        key=input()
        t2 = threading.Thread(target=read, args=(key, )) 
        t2.start()
        run()
    elif(option=="3"):
        print("please enter key, value")
        key=input()
        value=input()
        t3 = threading.Thread(target=update, args=(key,value)) 
        t3.start()
        run()
    elif(option=="4"):
        print("please enter key")
        key=input()
        t4 = threading.Thread(target=delete, args=(key)) 
        t4.start()
        run()
    elif(option=="5"):
        print("Good Bye")
        print(d)
    elif(option=="6"):
        print(d)
        run()
    else:
        print("please enter valid option")
        run()

run()

