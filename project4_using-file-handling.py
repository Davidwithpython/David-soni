import pickle
import os
final={}
print("_______________________________________________________________________________________________")
print(" \t \t \t Bank MANAGEMENT SYSTEM*** ")
print("_______________________________________________________________________________________________")
l=[ 'Name','Address','Phone no.','Govt Id','Account Type','Amount']
def new():
    k=[]
    o=open('database.txt','ab')
    a=input('enter the account no.:')
    for i in l:
        j=input('Enter %s :'%i)
        k.append(j)
    
    final[a]=dict(zip(l,k))
    pickle.dump(final,o)
    #k=[]
    print('Account Created')
    o.close()
def exist():
    
    r=open('database.txt','rb')
    print("1.Check Balance\n2.Withdraw\n3.Deposit")
    n=int(input("Enter the choice:"))
    final=pickle.load(r)
    r.close()
    os.remove('database.txt')
    
    r2=open('database.txt','wb')
    print(final)
    if n==1:
        print("Balance is ",final[a]['Amount'])
      
    if n==2:
        
        p=int(input("Enter the amount to withdraw:"))
        print("----------------------------------------------------------------------------\nwithdraw successful ")
        u=int(final[a]['Amount'])
        print("Available Balance :",u-p)
        final[a]['Amount']=str(u-p)
        
        
        
        print("--------------------------------------------------------------------------")
      
    if n==3:
        p=int(input("Enter the amount to deposit:"))
        print("----------------------------------------------------------------------------\ndeposit successful ")
        u=int(final[a]['Amount'])
        print("Available Balance :",u+p)
        final[a]['Amount']=str(u+p)
        print("--------------------------------------------------------------------------")
    pickle.dump(final,r2)
   # r2=open('database.txt','rb')
   # final=pickle.load(r2)
    #print(final)
    r2.close()


while True:
    print("_______________________________________________________________________________________________")
    print(" 1. New Customer")
    print(" 2. Existing Customer")
    print(" 3. Exit")

    n=int(input(" Please choose any one option:-"))
    if n==1:
        new()

    elif n==2:
        r=open('database.txt','rb')
        a=input("enter the account number: ")
        
        
        if a in pickle.load(r):
            
            print("record is found")
            r.close()
            exist()
        else:
            print('record is not found')
    
    elif n==3:
        exit()
    else:
        print("choices does not exist ")
    g=input("Do u want continue(Y/N)")
    if g=="Y"or g=='y':
        continue
    else:
        break
