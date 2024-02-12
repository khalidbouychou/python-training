


numbers = [0,1,2,3]
numbers = range(0,3)

for num in numbers:
    print("send -->",num)

for num in range(1,5):
    if num == 3:
        break
    print("send -->",num)

for num in range(1,5):
    if num == 3:
        continue
    print("send -->",num)
else:
    print ("else done")
#nested loops
    
for i in range(0,3):
    for j in range(0,3):
        print(f"|{i},{j}|")

#while loop
i = 0
while  i < 10:
    print (f"[{i}]salam")
    i += 1

print("-"*50) 
#list 
    
numbers = [10,-1,2,-3,55,-9]

negnum = []
posnum = []

for num in numbers:
    if num >= 0:
        posnum.append(num)
    else:
        negnum.append(num)

print(posnum)
print(negnum)

print("-"*50)

negnum = [num for num in numbers if num < 0]
posnum = [num for num in numbers if num >= 0]

print(posnum)
print(negnum)
