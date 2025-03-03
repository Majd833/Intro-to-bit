num1=10
num2=5
num3=12
num4=16
num5=(num1&num2)|num3^num4
count=0
while (num5):
    num5>>1
    count+=1
if count!= 3:
    print("True")
print("count=",count)
print("num5=",num5)
