# Python program to print all the numbers 
# divisible by 3 and 5 for a given number 

# Result function with N 
def result(N): 
	 
	for num in range(N): 
		 
			if num % 3 == 0 and num % 5 == 0: 
				print(str(num) + " ", end = "") 
				
			else: 
				pass

 
if __name__ == "__main__": 
	
 
	N = int(input('enter ending number:')) 
	result(N) 