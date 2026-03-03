def AverageStringLength(list):
    totalLength=0
    for i in range(len(list)):
        totalLength+=len(list[i])
    return(totalLength/len(list))

test=["hello","day"]
print(AverageStringLength(test))
