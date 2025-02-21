class A():
    def __init__(self):
        self.name=''
        self.a=0
        self.ad=''
        self.check='00/00/00'
        self.checko='00/00/00'
        self.room=100
        self.t=0
        self.r=0
        self.g=0
        self.c=0
        
    def data(self):
        self.name=input('Enter your name:')
        self.ad=input('Enter your address:')
        self.check=input('Enter your check in date:')
        self.checko=input('Enter your check out date:')
        while True:
            self.room=self.room+1
            break
        print('Your Room no. is',self.room)
        
    def rr(self):
        print('follwing rooms are avaliable ')
        print("1. type A--->rs 6000 per day/-\n2. type B--->rs 5000 per day/-\n3. type C--->rs 4000 per day/-\n4. type D--->rs 3000 per day/-")
        ch=int(input("Enter ur choices:"))
        if ch==1:
            self.a=6000
        elif ch==2:
            self.a=5000
        elif ch==3:
            self.a=4000
        elif ch==4:
            self.a=3000
        else:
            print("u cann't select any option")
        n=int(input("How many days(24hr) want to stay here:"))
        self.a=n*self.a
        print("your Room rent is ",self.a)
    def rb(self):
        print('*******Restaurant Menu**********')
        print("1.Water--->rs 20/-\n2.tea--->rs10/-\n3.Breakfast combo--->rs 90/-\n4.lunch--->rs 110/-\n5.dinner--->rs 150/-\n6.Exit")
        while True:
            ch=int(input("Enter ur choices:"))
            if ch==6:
                break
            n=int(input("Enter the quantity:"))
            if ch==1:
                self.r=self.r+20*n
                
            elif ch==2:
                self.r=self.r+10*n
            elif ch==3:
                self.r=self.r+90*n
            elif ch==4:
                self.r=self.r+110*n
            
            elif ch==5:
                self.r=self.r+150*n
            
            
                
            else:
                print("u cann't select any option")
            
            
        print("Total food cost is ",self.r)
    def lb(self):
        print('*******Laundry Menu**********')
        print("1.Shorts--->rs 2/-\n2.trousers--->rs4/-\n3.Shirt--->rs5/-\n4.Jeans--->rs6/-\n5.Girlsuit--->rs 8/-\n6.Exit")
        while True:
            ch=int(input("Enter ur choices:"))
            if ch==6:
                break
            n=int(input("Enter the quantity:"))
            if ch==1:
                self.c=self.c+2*n
                
            elif ch==2:
                self.c=self.c+4*n
            elif ch==3:
                self.c=self.c+5*n
            elif ch==4:
                self.c=self.c+6*n
            
            elif ch==5:
                self.c=self.c+8*n
            
            
                
            else:
                print("u cann't select any option")
            
            
        print("Total Laundary bill =Rs",self.c)
    def gb(self):
        print('*******Game Menu**********')
        print("1.Table Tennis--->rs 60/-\n2.Bowling--->rs80/-\n3.Snooker--->rs 70/-\n4.video game--->rs 90/-\n5.Pool--->rs 50/-\n6.Exit")
        while True:
            ch=int(input("Enter ur choices:"))
            if ch==6:
                break
            n=int(input("no. of hours:"))
            if ch==1:
                self.g=self.g+60*n
                
            elif ch==2:
                self.g=self.g+80*n
            elif ch==3:
                self.g=self.g+70*n
            elif ch==4:
                self.g=self.g+90*n
            
            elif ch==5:
                self.g=self.g+50*n
            
                           
            else:
                print("u cann't select any option")
            
            
        print("Total Game bill is ",self.g)
    

    def total(self):
        print('Customer details:')
        print('Customer name:',self.name)
        print('Customer address:',self.ad)
        print('check in date:',self.check)
        print('check out date:',self.checko)
        print('Room no.:',self.room)
        print("your Room rent is ",self.a)
        print("your Food bill is ",self.r)
        print("your Laudary bill is ",self.c)
        print("your Game bill is ",self.g)
        self.t=self.r+self.a+self.g+self.c
        print("your Total bill is ",self.t)
        print("Additional Service Charges is ",1800)
        print("Your grand total bill is :",1800+self.t)









class main():
    a=A()
    print("****************Welcome To DavidSoni Pink Hotel*************")
    while(True):
        
        print("_"*60)
        print("1.Enter customer data")
        print("2.calculate Room Rent")
        print("3.Calculate Restaurant Bill")
        print("4.Calculate Laundry Bill")
        print("5.Calculate Game Bill")
        print("6.Show Total Cost")
        print("7.Exit")
        print("-"*60)
        c=int(input("Enter your choice:"))
        if c==1:
            a.data()
        elif c==2:
            a.rr()
        elif c==3:
            a.rb()
        elif c==4:
            a.lb()
        elif c==5:
            a.gb()
        elif c==6:
            a.total()
        elif c==7:
            exit()
        else:
            print("option doesn't exists")
        g=input("Do u want continue(Y/N)")
        if g=="Y"or g=='y':
            
            continue
        else:
            break
