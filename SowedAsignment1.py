from collections import Counter
sms = input ("Please Enter an SMS")
word = sms.split()
print (word)
wordCount = Counter(word)
print (wordCount)
