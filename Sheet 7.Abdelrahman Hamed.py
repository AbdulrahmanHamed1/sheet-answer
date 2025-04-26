#1)
 #Q1)
import numpy as np  
 #Q2)
arr1 = np.array([1, 2, 3])  
print(arr1,"\n")
 #Q3)
arr2 = np.array(list(range(1, 101)))  
print(arr2,"\n")
 #Q4)
arr3 = np.arange(1, 101)  
print(arr3,"\n")
 #Q5)
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(arr4)


#2)
import numpy as np
 #Q6)
arr_2D = np.arange(1, 10).reshape(3, 3)  
print(arr_2D)
 #Q7)
arr_1D = arr_2D.flatten()  
print(arr_1D)
 #Q8)
arr2 = np.arange(100)  
arr3 = arr2.reshape(4, -1)  
print(arr3)
print(arr3.shape)




#3)

import numpy as np
 #Q9)
a = np.arange(100).reshape(-1, 10)  
b = a[9][2]
print(b)
 #Q10)
third_row= a[2,:]  
print(third_row)
 #Q11
fourth_clmn = a[:,3]  
print(fourth_clmn)


#4)
import numpy as np
 #Q12)
arr = np.arange(0, 1.1, 0.1) 
print(arr)
 #Q13)
a = np.arange(100).reshape(-1, 10)  
double_a = a.astype('float64')  
print(double_a)


#5)
import numpy as np

a = np.arange(100).reshape(-1, 10)  
 #Q14)
print("\n a + 1: \n", a+1)  
print("\n a - 1: \n", a-1)
print("\n a * 2: \n", a*2)
print("\n a / 2: \n", a/2)
print("\n a ** 2: \n", a**2)
 #Q15)
print("\n a > 50: \n", a>50)  
print("\n a < 50: \n", a<50)
print("\n a >= 50: \n", a>=50)
 #Q16)
a = np.array([1, 2, 3])  
b = np.array([4, 5, 6])
print("\n a + b: \n", a+b)
print("\n a - b: \n", a-b)
print("\n a * b: \n", a*b)
print("\n a / b: \n", a/b)
 #Q17)
print("\n a > b: \n", a>b)  
print("\n a < b: \n", a<b)
print("\n a >= b: \n", a>=b)


#6)
Output=[[5 6 7]
        [6 7 8]
        [7 8 9]]
