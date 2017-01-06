#Import Counter from Collections Module and Enter a new SMS string
from collections import Counter
sms = input ("Please Enter an SMS")
#Split the string into individual words and store them in a list
word = sms.split()
print("")
print("The individual words in the SMS are the following:")
print("---------------------------------------------")
print (word)
#Count the Individual words and list down each occurence.
wordCount = Counter(word)
print("")
print("Number of occurences of each word in the SMS")
print("---------------------------------------------")
print (wordCount)
