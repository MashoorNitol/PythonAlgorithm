# Validating sequence : Two approaches with same Time and Space Complexity [O(n) / O(1)]
# Using while loop
def isValidSubSquence(array,subsequence):
  arrID = 0
  seqID = 0
  while arrID < len(array) and seqID < len(subsequence):
		if array[arrID] == subsequence[seqID]:
			seqID +=1
		arrID +=1
	return seqID == len(subsequence)

# Using for loop
def isValidSubSquence(array,subsequence):
  seqID = 0
  for i in range(len(array)):
		if seqID == len(subsequence):
			break
		if array[i] == subsequence[seqID]:
			seqID +=1
	return seqID == len(subsequence)
		
    
