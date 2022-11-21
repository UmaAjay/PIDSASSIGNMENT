#6.5.2
# UMA AJAY KUMAR REDDY P S   19ETCS002134

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([5,6,7,8,9,10,11,12])

print ("the array after removing duplicate elements",np.delete(x, 4))

print("the index of duplicate element is",[key for key,val in enumerate(x) if val in set(y)])
z = np.array([1,2,3,4,5,19,10,11,24])
answer_range = np.where(np.logical_and(y>=5, y<=11))
print ("the elements until range are",answer_range)
z = np.array([2,2,3,3,6,7,7,8,8,91,91])
p=np.unique(z)
print("the duplicate elements are",p)
print("sliced elements",z[1:3])