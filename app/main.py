#!/usr/bin/env python

# w,b,g,r
# (b + g) hour, (g + r)*5 min
# 1,1,2,3,5


import sys
argv = sys.argv
argc = len(argv)

#error

if argc != 3:
  print "rrrrr"
  sys.exit()
  
try:
  hour = int(argv[1])
  min = int(argv[2])

  if ((hour > 11) or (hour < 0)):
    print "rrrrr"
    sys.exit()

  if (min % 5 != 0) or ((min > 55) or (min < 0)):
    print "rrrrr"
    sys.exit()

  
except ValueError:
  print "rrrrr"
  sys.exit()


#calc
  
list = [5,3,2,1,1]
dict = {5:'w',3:'w',2:'w',1:'w',1:'w'}

w = 0
b = 0
g = 0
r = 0

b = {0:list[0]}
g = {1:list[1]}


#多分elseじゃダメ elifで今度はhourを超過したらの処理が必要

for i in range(len(list)):
  for j in range(len(list)-2):
    if (sum(b.values()) + sum(g.values())) == hour:
      print b
      print g
      break
    else:
      g.update({j+2:list[j+2]})


#for k,v in sorted(dict.items(), reverse=True):
  #print k, v
