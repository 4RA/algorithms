n=int(input())
count = 0
flag =0
first = n


while(flag==0):
    new = n//10 + n%10
    p=str(n%10)+str(new%10)
    n=int(p)
    if(first == n):
        flag=1
    count+=1    
        

print(count)

