print("half pyramig pattern of numbers: ")
n=int(input("enter the number of rows: "))
num=1
for i in range(n):
    for j in range(1,i+1):
       print(num, end=" ")
       num=num+1
    print()