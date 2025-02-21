import os
def view():
  if os.path.exists("data.txt"):
    f=open("data.txt",'r')
    print(f.read())
    f.close()
  else:
    print("data doesn't exists in file")
def add():
  f=open("data.txt",'a')
  s=input("enter the student name:")
  f.write(s+'\n')
  f.close()
  print(" Name is added successfully...")
def remove():
  f=open("data.txt",'r+')
  s=input("Enter name which u want delete:")
  l=f.readlines()
  f.close()
  os.remove("data.txt")
  if s+'\n' in l:
    l.remove(s+'\n')
    print("sucessful deleted ......")#y=''.join(l) #after remove  for loop
    f=open("data.txt",'w')
    for i in l:
      f.write(i)
  else:
    print("name doesn't exist")
  
  f.close()  
def search():
  f=open('data.txt','r')
  s=input("Enter name which u want find:")
  l=f.read()
 # l=f.readlines()
 # f.close()
  if s+'\n' in l:
    
    print("sucessful founded ......")
  else:
    print("name doesn't exist")
  f.close()
  '''for i in l:
    if s==i:
      f=0
      print("sucessful founded ......")
      break
    if s != i:
      f=1
  if f==1:
     print("not found.....")

'''

while True:
  print("_______________________________________________________________________________________________")
  print(" ***WELCOME TO STUDENT MANAGEMENT SYSTEM*** ")
  print("_______________________________________________________________________________________________")
  print(" 1. To View Student list")
  print(" 2. To add new list")
  print(" 3. To remove the data")
  print(" 4. To search data")
  print(" 5. Exit")

  n=int(input(" Please choose any one option:-"))
  if n==1:
    view()
  elif n==2:
    add()
  elif n==3:
    remove()
  elif n==4:
    search()
  elif n==5:
    exit()
  else:
    print("choices does not exist ")
  g=input("Do u want continue(Y/N)")
  if g=="Y"or g=='y':
    continue
  else:
    break
