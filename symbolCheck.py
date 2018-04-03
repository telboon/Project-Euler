def SimpleSymbols(ytr): 

  magic=ytr
  
  if (ord(magic[len(magic)-1]) in range(97,123)) or (ord(magic[len(magic)-1]) in range(65,91)):
    return "false"
  
  for i in range(0,len(magic)):
    if(ord(magic[i]) in range(97,123)) or (ord(magic[i]) in range(65,91)):
      if i==0:
        return str(i)+"false"
      if ((magic[i-1])!='+') or ((magic[i+1])!='+'):
        return "false"
  
  return "true"
# keep this function call here  
# to see how to enter arguments in Python scroll down
print(SimpleSymbols(raw_input()))


