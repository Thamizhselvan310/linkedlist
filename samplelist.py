def delete(val):
  n.remove(val)
  print(n)
def insert(pos,val):
  n.insert(pos-1,val)
  print(n)
def search(val):
  if(val in n):
    print("index of search element...",n.index(val))
  else:
    print("Element not found in list")
def update(a,b):
  c=n.index(a)
  n[c]=b
  print(n)

n=list(map(int,input().split()))
print("1.insertion")
print("2.delete")
print("3.search")
print("4.update")
print("5.exit")
choice=int(input("enter the choice"))
if(choice!=5):
  if(choice==1):
    ins=int(input("enter the element..."))
    p=int(input("enter the position you want insert..."))
    insert(p,ins)
  elif(choice==2):
    dele=int(input("enter the delete element..."))
    delete(dele)
  elif(choice==3):
    ser=int(input("enter the search element..."))
    search(ser)
  elif(choice==4):
    oldval=int(input("enter the element you want update...."))
    val=int(input("enter the updated element..."))
    update(oldval,val)
