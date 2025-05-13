import numpy as np
import matplotlib.pyplot as plt
a=np.arange(25)
print(a)
print("\n")
print(a[::2])
print("\n")
print(a[1::2])
print("\n")
#print(a[::2,::2])#??
a_2d = a.reshape(5, 5) 
print(a_2d)
print("\n")
print(a_2d[::2, ::2])
print("\n")
print(a_2d[1::2, 1::2])