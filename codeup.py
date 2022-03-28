#codeup 6001 to 6025
#date: 2022.03.28

#6001
print("Hello")

#6002
print("Hello World")

#6003
print("Hello")
print("World")

#6004
print(" \'Hello\' ")

#6005
print('\"Hello World\"')
#6006
print("\"!@#$%^&*()\'")

#6007
print('\"C:\Download\\\'hello\'.py\"')

#6008
print("print(\"Hello\\nWorld\")")

#6009
str = input()
print(str)

#6010
num = int(input())
print(num)

#6011
num = float(input())
print(num)

#6012 
a=int(input())
b=int(input())
print(a)
print(b)

#6013 
a=input()
b=input()
print(b)
print(a)

#6014
real_num = float(input())
for i in range(3):
    print(real_num)

#6015 
a,b = input().split()
print(a)
print(b)

#6016
a,b = input().split()
print(b+" "+a)

#6017 
s = input()
print(s,s,s)

#6018
a,b=input().split(":")
print(a,b,sep=":")

#6019 
year,mon,day=input().split(".")
print(day,mon,year,sep="-")

#6020 
front_num,back_num=input().split("-")
print(front_num,back_num,sep='')

#6021
s=input()
for i in range(5):
    print(s[i])

#6022
s=input()
print(s[0:2],s[2:4],s[4:6])


#6023
a,b,c=input().split(":")
print(b)

#6024
a,b=input().split()
print(a,b,sep=(""))

#6025 
a,b=input().split()
c=int(a)+int(b)
print(c)