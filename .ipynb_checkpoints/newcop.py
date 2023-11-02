#prog to finmd the num is palin or not
num = int(input("Enter the number"))
temp = num
res = 0
while temp>0:
    rem = temp%10
    res = res*10+rem
    temp=temp//10

if res==num:
    print("Yes")

else:
    print("No")