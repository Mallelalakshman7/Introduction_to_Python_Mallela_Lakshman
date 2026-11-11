def convertor(con: str,temp: float)-> str:
  if con=="F":
    temp1=((temp*9)/5)+32
    print(f"{temp}C={temp1}{con}") 
  elif con=="C":
    temp1=(temp-32)*5/9
    print(f"{temp}F={temp1}{con}") 
  else:
    print("Invalid Direction")

con=input("Convert to (C/F):")
temp=float(input("Temperature:"))
convertor(con,temp)

def bmoi(height: float,weight: int)->str:
  res=weight/height**2
  if res<=18.5:
    print(f"BMI: {res:.1f} (Under weight)")
  elif res>18.5 and res<=25:
    print(f"BMI: {res:.1f} (Normal)")
  elif res>25 and res<=30:
    print(f"BMI: {res:.1f} (Over weight)")
  elif res>30:
    print(f"BMI: {res:.1f} (obese)")
  else:
    print("Enter the proper height and weight proportions")

height=float(input("Height (m):"))
weight=float(input("Weight (kg):"))
bmoi(height,weight)

def fiz(n:int)->str:
  if n==0:
    return 0
  for i in range(1,n+1):
    if i%3==0 and i%5==0:
      print("FizzBuzz",end=" ")
    elif i%3==0:
      print("fizz",end=" ")
    elif i%5==0:
      print("Buzz",end=" ")
    else:
      print(i,end=" ")

n=int(input("Enter a number:"))
fiz(n)

import math 
def prime(n:int)->str:
  if n<=1:
    print("Not a prime number")
    return
  if n==2 or n==3:
    print(f"{n} is a prime number")
    return
  for i in range(4,int(math.sqrt(n))):
    if(n%i==0):
      print(f"{n} is divisible by {i}")
      print(f"{n} is not a prime number")
      return
  print(f"{n} is a prime number")

n=int(input("Enter a number:"))
prime(n)

def table(n:int)->str:
  print(f"table of {n}")
  for i in range(1,11):
    print(f"{n} x {i} = {(n*i)}")

n=int(input("enter a number:"))
table(n)

def grade()->str:
  while True:
    n=float(input("Grade (0-20): "))
    if n>0 and n<=20:
      print(f"Grade saved:{n}")
      break
    else:
      print("Invalid try again")

grade()

def menu():
  balance=0
  while True:
    print("1) Deposit 2) Balance 3)Withdraw 0)Quit")
    choice=int(input("Choice: "))
    if choice==1:
      amount=float(input("Amount: "))
      balance+=amount
    elif choice==2:
      print(f"Balance: {balance:.2f}E")
    elif choice==3:
      out=float(input("Enter withdraw amount: "))
      if out>balance:
        print("Insufficient funds to withdraw")
      else:
        balance-=out
        print(f"Withdrawl success {out}")
        print(f"Remaining balance {balance}")
    elif choice==0:
      break
    else:
      print("Invalid choice")

menu()
      
def report():
  names=["Ana","Ben","Chloe","Dan"]
  grades=[14.5,8.0,17.0,11.5]
  sum=0
  for i,(name,grade) in enumerate(zip(names,grades),start=1):
    sum+=grade
    if grade>=10:
      print(f"{i}. {name}: {grade} PASS")
    else:
       print(f"{i}. {name}: {grade} FAIL")
  print(f"Average: {sum/len(names):.2f}")
      

report()

def quiz():
  question=["what is the sum of 97+12:","expand OOPS:","what is an instance of class:"]
  answer=["109","Object Oriented Programming","Object"]
  user_ans=[]
  while True:
    for i in question:
      print(i)
      ans=input("Enter your answer:")
      user_ans.append(ans)
    score=0
    for right,ans in zip(answer,user_ans):
      if right==ans:
        score+=1
    print(f"You got {score} out of {len(answer)}")
    choice=input("Play again?(Y/N):")
    if choice=="Y":
      continue
    if choice=='N':
      break
    

quiz()
    