n=int(input("enter vale of n : "))
n1 ,n2= 0,1
sum=0
for i in range(0,n):
    print(sum,end=" ")
    n1=n2
    n2=sum
    sum=n1+n2
      
