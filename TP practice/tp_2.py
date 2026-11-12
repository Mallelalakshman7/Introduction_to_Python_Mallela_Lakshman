class shop:
  items=[]
  def __init__(self,menu):
    self.menu=menu
    self.display(menu)
  def display(self,menu):
    while True:
      for i,option in enumerate(menu,start=1):
        print(f"{i}.{option}",end=" ")
      choice=input("\n Enter your choice: ")
      if choice=='1':
        self.add()
      elif choice=='2':
        self.remov()
      elif choice=='3':
        self.show()
      elif choice=='4':
        self.empty()
      elif choice=='5':
        return 
      else:
        print("Enter the valid option")

  def add(self):
    take=input("Item:").lower().split()
    self.items.extend(take)
    return
  def remov(self):
    take=input("Item:")
    if take not in self.items:
      print("There is no such items to remove")
      return 
    self.items.remove(take)
    return 
  def show(self):
    if len(self.items)<=0:
      print("There are no Items")
      return 
    for i,item in enumerate(self.items,start=1):
      print(f"{i}.{item}")
    return 
  def empty(self):
    self.items.clear()
    return 

menu=['Add','Remove','Show','Clear','Exit']
lakshman=shop(menu)
    
        
        
    