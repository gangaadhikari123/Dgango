

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


def myFunction():
  return True

print(myFunction())



x = 200
print(isinstance(x,int))# to check the data type of x



numbers = [1,2,3,4,5]
count = len(numbers)
if count > 3:
  print(f"List has {count} elements")
  
  if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

    x=5 
    print(1 < x < 10)
    print(1 < x and x < 10)
    
