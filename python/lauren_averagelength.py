words = ["hello", "hi", "bye", "goodbye", "hola"]
sum = 0
avg = 0
for word in words:
    sum += len(word)
avg = sum / len(words)
print(avg)