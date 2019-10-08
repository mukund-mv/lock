start =input('enter starting number to find prime number:') 
end = input('enter ending number to find prime number:') 
  
for val in range(int(start),int(end)+ 1):   
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

    




