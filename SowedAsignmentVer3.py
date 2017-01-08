#Import Counter from Collections Module and Enter a new SMS string
from collections import Counter
#Enter the  2 SMS and Add them together to make one string
sms1 = input ("Enter the First SMS")
sms2 = input ("Please Enter another SMS")
sms= sms1+sms2
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
