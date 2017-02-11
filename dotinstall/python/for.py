# coding: UTF-8

sum=0
for i in [1, 3, 5, 7, 11]:
  sum += i
else:
  print sum

for i in range(10):
  if i == 3:
#    continue
    break
  print i
else:
  print "end"

a={"tama":200, "ike":300, "yama":400}

for k, v in a.iteritems():
  print "key: %s value: %d" % (k, v)

for k in a.iterkeys():
  print k

for v in a.itervalues():
  print v
