from textblob import TextBlob
x = input("Enter in English")
y = TextBlob(x)
trans = y.translate(from_lang="en", to = "gu")
print(trans)
