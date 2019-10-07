 
def sortedSentence(Sentence): 

	words = Sentence.split(" ") 
	
	words.sort() 
	
 
	newSentence = " ".join(words) 
	

	return newSentence 



Sentence = ""

print(sortedSentence(Sentence)) 

Sentence = "" 
print(sortedSentence(Sentence)) 
 

