# python library

# numpy-(array)it is used to work on large da ta set
# range is too large
# high order function
# array reshape
# create n dimension array 

# how to use numpy->goto terminal-> pip install numpy

import numpy as np


# create numpy array to store
# friends name, edit

myfriends=np.array(["ivan         ","anshu","wani","anjali"])

# print(myfriends)
# print(type(myfriends))
print(myfriends[1])

for f in myfriends:
  print(f)
myfriends[0]="ivan sharma"
print(myfriends)
print(myfriends[0])




# sorting function
myfriends.sort()
print(myfriends)

# reverse sort using flip
# rev = np.flip(myfriends)
# print(rev)

# reverse sort using slicing
# rev2 = myfriends[::-1]
# print(rev2)

# reverse using while loop
y=3
while y>=0:
  print(myfriends[y])
  y=y-1