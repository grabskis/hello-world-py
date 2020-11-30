  
def multiply(a, b):
  i = 0  
  
  for x in range(a):
    i += b

  print(i)

def modulus(a, b):
  while not a >= b:
    a = a - b
    print(a)
  
  print(a)



multiply(6000, 90)
modulus(6, 15)


