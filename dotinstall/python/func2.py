# coding: UTF-8

def double(x):
  return x*x

print map(double, [1,2,5])
print map(lambda x:x*x, [1,2,5])
