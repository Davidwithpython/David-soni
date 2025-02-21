l=["David",'loue','khushboo','Riya']
def view():
  print("student list is")
  for i in l:
    print(i)
def add():
  s=input("enter the student name:")
  l.append(s)
  print(" Name is added successfully...")
def remove():
  s=input("Enter name which u want delete:")
  if s in l:
    l.remove(s)
    print("sucessful deleted ......")
  else:
    print("name doesn't exist")
'''  for i in l:
    if s==i:
      l.remove(s)
      f=0
      print("sucessful deleted ......")
      break
    if s != i:
      f=1

  if f==1:
    print("name doesn't exist")


'''
def search():
  s=input("Enter name which u want find:")
  if s in l:
    print("sucessful founded ......")
  else:
    print("name doesn't exist")

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
    print("choices does not existence ")
  g=input("Do u want continue(Y/N)")
  if g=="Y"or g=='y':
    continue
  else:
    break
