
final={}

l=[ 'Name','Address','Phone no.','Govt Id','Account Type','Amount']
def new():
    k=[]
    a=input('enter the account no.:')
    for i in l:
        j=input('Enter %s :'%i)
        k.append(j)
    
    final[a]=dict(zip(l,k))
    #k=[]
    print('Account Created')
    print(final)
def exist():
    print("1.Check Balance\n2.Withdraw\n3.Deposit")
    n=int(input("Enter the choice:"))
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
    


while True:
    print("_______________________________________________________________________________________________")
    print(" \t \t \t Bank MANAGEMENT SYSTEM*** ")
    print("_______________________________________________________________________________________________")
    print(" 1. New Customer")
    print(" 2. Existing Customer")
    print(" 3. Exit")

    n=int(input(" Please choose any one option:-"))
    if n==1:
        new()

    elif n==2:
        a=input("enter the account number: ")
        if a in final:
            print("record is found")  
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
