# Time O (n^2) | Space O (1)
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
          secondNum = array[j]
          if firstNum + secondNum == targetSum:
              return [firstNum, secondNum]
    return []
  
# Time O (n) | Space O (n)
def twoNumberSum(array,targetSum):
    hashTable = {}
    for x in array:
        y = targetSum - x
        if y in hashTable:
            return [x,y]
        else:
            hashTable[x] = True
    return []
  
# Time O(n log(n)) | Space O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    leftNum = 0
    rightNum = len(array) -1
    while leftNum < rightNum:
        currentSum =  array[leftNum] + array[rightNum]
        if currentSum == targetSum:
            return [array[leftNum],array[rightNum]]
        elif currentSum < targetSum:
            leftNum  += 1
        elif currentSum > targetSum:
            rightNum -= 1
    return[]
