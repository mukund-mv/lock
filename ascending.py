 
def sortedSentence(Sentence): 

	words = Sentence.split(" ") 
	
	words.sort() 
	
 
	newSentence = " ".join(words) 
	

	return newSentence 



Sentence = ""

print(sortedSentence(Sentence)) 

Sentence = "3
 2 1"
 
print(sortedSentence(Sentence)) 
 

