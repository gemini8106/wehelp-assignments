1.
def caculate(min,max):
  n=min
  sum=0
  while n<=max:
    sum+=n
    n+=1
  print(sum)
caculate(1,3)
caculate(4,8)




2.
def avg(data):
  i=0
  sum = 0
  while i < data["count"]:
    sum = sum + data["employees"][i]["salary"]
    i+=1
  x = sum/data["count"]
  print(x)
avg({
  "count":3,
  "employees":[ 
    {
      "name":"John",
      "salary":30000 
    },
    {
      "name":"Bob",
      "salary":60000 },
    {
      "name":"Jenny",
      "salary":50000 
    }
  ]
}); 




3.
def maxProduct(nums):
  final = []
  length = len(nums)
  for i in range(0,length-1):
    for j in range(i+1,length):
      final.append(nums[i]*nums[j])
  print(max(final))

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2]) 
maxProduct([-1, -2, 0])




4.
def twoSome(nums, target):
  length = len(nums)
  for i in range(0,length-1):
    for j in range(i+1,length):
      if (nums[i]+nums[j]) == target:
        return([i,j])
result= twoSome([2, 11, 7, 15],9)
print(result)




5.
def maxZeros(nums):
  con=0
  final = []
  length = len(nums)
  for i in range(length):
    if nums[i] == 0:
      con+=1
    elif nums[i] == 1:
      con=0
    final.append(con)
  print(max(final))
maxZeros([0, 1, 0, 0]) 
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) 
maxZeros([1, 1, 1, 1, 1]) 
maxZeros([0, 0, 0, 1, 1]) 


  















