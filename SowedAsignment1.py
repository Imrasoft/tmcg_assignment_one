#Import the Counter Function from the Collections Module
from collections import Counter
#Ask the user to Enter an SMS
#The SMS is Entered as a string so that it can be split with the Split Function
sms = input ("Please Enter an SMS")
word = sms.split()
print (word)
wordCount = Counter(word)
print (wordCount)
