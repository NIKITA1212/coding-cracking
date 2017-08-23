def uniquechar(s):
  f =1
  for x in s:
    if s.count(x) >1 :
      f=0
      break

  if f is 0:
    return("String has not unique character")
  else:
    return("string has unique character")
  
  
p = uniquechar("nikta")
print(p)