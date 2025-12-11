for number in range (3):
    print("Attempt", number + 1, (number+1 ) * ".")

for num in range (1,4):
    print("Attempt",num ,num * ".")
    if num == 3:
        print("Success")


        # break statement 
        sucess = False
        for num in range (3):
            if sucess:
                print("Successfull")
                break 
            else: 
                print("attemped")


                #outer loop and inner looop

#  nestes l[p

                for x in range (5):
#                     for y in range(3):
                        print (f"({x}, {y})")


#iterable loops

for x in "Pythion ":
    print(x)

    #in is used as iterable


#whike looop
num = 20
while num >0:
    print(num)
    num //= 2


   

command = ""
while command!= "quit":
        command = input(">")
        print("ECHO", command)


count = 0
for num in range(1,10):
                if num % 2 == 0:
                        print(num)
                        count +=1
                        print(num)
print("Total even numbers:", count)
                        
