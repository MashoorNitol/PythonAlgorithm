def threeNumberSum(array, targetSum):
    array.sort()
    finalArray = []
    for i in range(len(array)-2):
        leftID0 = i
        leftID1 = i+1
        rightID = len(array) - 1
        while leftID1 < rightID:
            currentSum = array[leftID0] + array[leftID1] + array[rightID]
            if currentSum == targetSum:
                finalArray.append([array[leftID0],array[leftID1],array[rightID]])
                leftID1 +=1
                rightID -=1
            elif currentSum < targetSum:
                leftID1 +=1
            elif currentSum > targetSum:
                 rightID -=1
    return finalArray
