def highest_value(nums: list(int))->int:
  """The function takes a list of number as input 
    and computes the highest value among the list of numbers 
    Args: nums type:List
    returns: Integer which is the highest value in the list"""
  ans=0
  for i in nums:
    if i>ans:
      ans=i
  return ans

def count_occurrences(items: list,target: int )->int:
    """This functions takes a list of number as input along with that a target element
    if that element is not present in the list then it returns None which indicates the number not presented in the given list.
    if the target is found in the list then it counts the number of occurrences of the target.
    Args: items type:List, target type:Integer
    returns: An integer number which is the count of occurrences of the target in the list"""

    if target not in items:
      return None
    count=0
    for i in items:
      if i==target:
        count+=1
    return count

def filter_by_valid(d:dict,minimum:int)->dict:
  """ This function takes a dictionary as a input along with that a minimum which is used to find the dictionary items which are grater than that minimum value 
  Args: d type:Dictionary, minimum type:Integer
    returns: A dictionary which contains the items which are greater than the minimum value"""
  new_d={}
  for k,v in d.items():
    if v>minimum:
      new_d[k]=v
  return new_d

print(highest_value([10,90,100,120]))
print(count_occurrences([10,20,10,20,50,10],10))
d={"lakshman":10,"gowtham":20,"shyam":30}
print(filter_by_valid(d,12))



class Student:
  def __init__(self,name: str,grade: list):
    self.name=name
    self.grade=grade
  def compute_average(self,grades: list(int))->float:
    if len(grades)==0:
      return 0
    average=(sum(grades)/(len(grades)*100))*100
    return average

lakshman=Student("Lakshman",[90,80,90])
res=(lakshman.compute_average(lakshman.grade))
gowtham=Student("Gowtham",[80,90,60])
res2=(gowtham.compute_average(gowtham.grade))
print(round(res,2))
print(round(res2,2))

def score():
    scores=[]
    try:
        with open("scores.txt",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                try:
                    name,score=line.split(",")
                    scores.append(int(score))
                except ValueError:
                    print("Skipped line:",line)
    except FileNotFoundError:
        print("File not found")
    if scores:
        print("Average_score:",sum(scores)/len(scores))

score()
                             