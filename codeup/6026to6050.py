#2022.03.29
#codeup 파이썬 기초 100제


#6026
a=float(input())
b=float(input())

print(a+b)

#6027
num=int(input())
print("%x"%num);

#6028
num=int(input())
print("%X"%num);

#6029
num=int(input(),16)
print("%o"%num)

#6030 
n=ord(input()) ##입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
print(n)

#6031
n=int(input())
print(chr(n)) #n에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 


#6032
num=int(input())
print(-num)

#6033
str =ord(input())
print(chr(str+1))

#6034
a,b= input().split()
print(int(a)-int(b))

#6035
a,b=input().split()
print(float(a)*float(b))

#6036
w,n=input().split()
for i in range(int(n)):
    print(w,end='')

#6037
n=int(input())
w=input()
for i in range(n):
    print(w,end='')

#6038
a,b=input().split()
print(int(a)**int(b))

#6039
f1,f2 = input().split()
print(float(f1)**float(f2))

#6040
a,b = input().split()
print(int(a)//int(b)) #몫

#6041 
a,b=input().split()
print(int(a)%int(b))

#6042 
a=float(input())
print(format(a,".2f"))

#6043 
f1,f2 = map(float,input().split()) 
res = f1/f2
print("%0.3f"%res)


#6044
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%0.2f"%(float(a)/float(b)))

#6045
a,b,c=input().split()
sum= int(a)+int(b)+int(c)
avg = float(int(a)+int(b)+int(c))/3
print(sum,"%.2f"%avg)

#6046
n=int(input())
print(n<<1) #2배

#6047
a,b=map(int,input().split())
print(a<<b)

#6048
a,b=map(int,input().split())
print(a<b)

#6049
a,b=map(int,input().split())
print(a==b)

#6050 
a,b=map(int,input().split())
print(a<=b)
