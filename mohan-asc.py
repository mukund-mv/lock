def decending(descinput): 
  # List for descending
  decendinglist=[]
  # Make a indefinite Loop unitill descinput is empty
  while len(descinput) != 0:
    #loop to find the highest number in the descinput list and write to decendinglist and remove the highest number from descinput list 
    highestnumber=0
    for i in descinput:
      if int(i) > int(highestnumber):
        highestnumber=i
    decendinglist.append(highestnumber)
    descinput.remove(highestnumber)
  return decendinglist

def asscending(ascinput): 
  asscendinglist=[]
  while len(ascinput) != 0:
    lowestnumber=0
    for i in ascinput:
      if lowestnumber == 0 or int(i) < int(lowestnumber):
        lowestnumber=i
    asscendinglist.append(lowestnumber)
    ascinput.remove(lowestnumber)
  return asscendinglist

#Declaring all my variables
mynumbers=[]
ascnumbers=[]
fnnumbers=[]
descinput=[]
#loop to get the inputs and store in mynumbers list
while True:
  test=input("Enter the Number, If you are done enter done: ")
  if test == "done":
      break
  mynumbers.append(test)
#copying mynumber list to ascinput and descinput
ascinput=mynumbers.copy()
descinput=mynumbers.copy()
#Call Descending Order Function and Print it
print("Descending Order:",decending(descinput))
#Call Asscending Order Function and Print it
print("Asscending Order:",asscending(ascinput))
