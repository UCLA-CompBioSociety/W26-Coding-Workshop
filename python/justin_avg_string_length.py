def avg(words):
    return sum([len(word) for word in words]) / len(words)

print(avg(["hello", "ethan", "justin"]))
