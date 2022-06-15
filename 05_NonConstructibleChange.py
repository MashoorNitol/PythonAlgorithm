def nonConstructibleChange(coins):
  coins.sort()
  change = 0
  for value in coins:
    if value > change+1:
      return change+1
    
    change += value
      
  return change+1
    
    
