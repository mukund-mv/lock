def computeHCF(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1 = int(input("enter your first number to find H.C.F:"))
num2 = int(input("enter your second number to find H.C.F:"))


print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))

def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter first number to find L.C.M: "))
num2 = int(input("Enter second number to find L.C.M: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))