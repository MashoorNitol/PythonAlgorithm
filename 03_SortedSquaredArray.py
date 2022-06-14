import math
# Brute-force method O(n log n) time | O(n) Space complexity
def SortedSquaredArray(array):
  initialOutput = []
  for i in range(len(array)):
    initialOutput.append(math.pow(array[i],2))
  initialOutput.sort()
  return initialOutput

# Optimal Solution O(n) time | O(n) Space complexity
def SortedSquaredArray(array):
  initialOutput = [0 for _ in range(len(array))]
  smallValueID = 0
  largeValueID = len(array) - 1
  for i in reversed(range(len(array))):
    smallValue = array[smallValueID]
    largeValue = array[largeValueID]
    if abs(smallValue) < abs(largeValue):
      initialOutput[i] = math.pow(largeValue,2)
      largeValueID -=1
    else:
      initialOutput[i] = math.pow(smallValue,2)
      smallValueID -=1
   return initialOutput
