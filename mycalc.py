import re
getnumber=input("Enter the Calculation")
r1=re.findall(r"\d+",getnumber)
r2=re.findall(r'\W',getnumber)
r2count=len(r2)
i=0
result=0
while i<=r2count:
    if i == 0:
      result=result + int(r1[i])
    else:
        if r2[i-1] == '*':
            result=result * int(r1[i])
        if r2[i-1] == '+':
            result=result + int(r1[i])
        if r2[i-1] == '-':
            result=result - int(r1[i])
        if r2[i-1] == '/':
            result=result / int(r1[i])
    i=i+1
print(result)
