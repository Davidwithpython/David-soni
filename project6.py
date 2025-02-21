import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='contact')
cur=conn.cursor()
print('='*80)
print("\t\t\t\t Contact Book Project")
print('='*80)


def Add():
    print("\n Add New Contact")
    n=input(" Enter Name :")
    a=input("Enter Address:")
    m=int(input("Enter Mobile no."))
    e=input("Enter E-mail id :")
    s=str("insert into book(Name,Address,Mobile,email) values('%s','%s',%d,'%s')"%(n,a,m,e))
    cur.execute(s)
    conn.commit()
    print('successfully added')
    

def search():
    print("\n Search Record By Name")
    n=input("Enter the name which u want search :")
    
    cur.execute("select * from book")
    s=cur.fetchall()
    for i in s:
        if n==i[0]:
            
            print("Name :",i[0])
            print("Address :",i[1])
            print("Mobile no. :",i[2])
            print("E-mail id:",i[3])
            flag=0
            break
        else :
            flag=1
    if flag==1:
        print("record not exists")
    



def dis():
    print("\n Display All Records")
    cur.execute("select * from book")
    s=cur.fetchall()
    print(" Name \t\t  \t  Address \t \t \t   Mobile no. \t \t \t   E-mail id \n")
    for i in s:
        print(i[0],"\t \t \t" ,i[1],'\t \t \t',i[2],"\t \t \t",i[3]  )
    

def delete():
    print("\nDelete Record")
    n=input("Enter the name which u want to delete :")
    cur.execute("select * from book")
    s=cur.fetchall()
    for i in s:
        if n==i[0]:            
            t=str("delete from book where Name='%s'"%n)
            cur.execute(t)
            conn.commit()
            flag=0
            print("Record  deleted successfully")
            break
        else :
            flag=1
    if flag==1:
        print("record not exists")
    
def mod():
    print("\n Modify  Record")
    n=input("Enter the name which record u want to update:")
    cur.execute("select * from book")
    s=cur.fetchall()
    for i in s:
        if n==i[0]:
            cho(n)
            flag=0
            break
        else :
            flag=1
    if flag==1:
        print("record not exist")
def cho(n):
    while True:
        print("\n\nPress the Option you want to edit:")
        print("1.modify the name  \n 2.modify the Address \n 3.modify the mobile no. \n 4. modify the email id \n 5.Back\n")
        c = int(input("Select  Your  Option (1-5) : "))
        if c==1:            
            na=input("Enter New Name:")
            w=str("update book set Name ='%s' where Name='%s'"%(na,n))
        
        elif c==2:
            na=input("Enter  New Address:")
            w=str("update book set Address ='%s' where Name='%s'"%(na,n))
        
        elif c==3:
            na=int(input("Enter New Mobile no.:"))
            w=str("update book set Mobile ='%d' where Name='%s'"%(na,n))
        
        elif c==4:
            na=input("Enter New E-mail id:")
            w=str("update book set email='%s' where Name='%s'"%(na,n))
        elif c==5:            
            break
        else:
            print(" Select only suitable option")
        print("Record is successfully updated")

        cur.execute(w)
        conn.commit()


    
while (True):
    print("\n\nMAIN MENU")
    print(" 1. ADD    NEW    RECORD\n 2. SEARCH   RECORD \n",end=' ')
    print("3. DISPLAY  ALL   RECORDS  \n 4. DELETE   RECORDS \n 5. MODIFY   RECORD \n 6. EXIT \n \n")
    n = int(input("Select  Your  Option (1-6) : "))
    if n==1:
        Add()
        
    elif n==2:
        search()
        
    elif n==3:
        dis()
        
    elif n==4:
        delete()
        
    elif n==5:
        mod()
        
    elif n==6:
        conn.close()
        print("\nThanks for using Contact Book")
        exit()
    else:
        print(" Select only suitable option")
           
                   

