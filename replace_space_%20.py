def replace_space(s):
  l = list()
  for x in s:
    if x == " ":
      l.append("%20")
    else:
      l.append(x)
  return(''.join(l))

p = replace_space("nikita tank")
print(p)