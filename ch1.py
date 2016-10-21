Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> X= range(100)
>>> X
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> Y=[value **2 for value in X]
>>> Y
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
>>> plt.plot(X,Y)
[<matplotlib.lines.Line2D object at 0x7efe393e4990>]
>>> plt.show()
>>> sum(X)
4950
>>> import math
>>> T=range(100)
>>> X=[(2*math.pi*T)]

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    X=[(2*math.pi*T)]
TypeError: can't multiply sequence by non-int of type 'float'
>>> X=[(2*math.pi*t) / len(T) for t in T]
>>> Y=[math.sin(value) for value in X]
>>> plt.plot(X,Y)
[<matplotlib.lines.Line2D object at 0x7efe39ab2a50>]
>>> plt.show()
>>> import numpy as np
>>> X= np.linspace(0, 2*np.pi, 100)
>>> Y= np.sin(X)
>>> plt.plot(X,Y)
[<matplotlib.lines.Line2D object at 0x7efe39a62c90>]
>>> plt.show()
>>> 
>>> X=np.linspace(-3,2,200)
>>> Y=X**2-2*X+1
>>> plt.plot(X,Y)
[<matplotlib.lines.Line2D object at 0x7efe38b83890>]
>>> plt.show()
>>> 
>>> X= np.linspace(0,2*np.pi, 100)
>>> Ya= np.sin(X)
>>> Yb=np.cos(X)
>>> plt.plot(X, Ya)
[<matplotlib.lines.Line2D object at 0x7efe38ab5910>]
>>> plt.plot(X,Yb)
[<matplotlib.lines.Line2D object at 0x7efe39ac1510>]
>>> plt.show()
>>> 
