import numpy as np

python_list=[2,4,6,8,10]

numpy_list=np.array([1,3,5,7,9])

print(python_list)
print(numpy_list)

python_list=python_list + python_list

numpy_list=numpy_list + numpy_list

print("Python List:",python_list)
print("Numpy List",numpy_list)


#my personal practice
'''my personal observation: 
my_list=np.array([
    [],
    [],
])

it works as well as python normal list which can be:
"my_list=([
    [],
    [],
])" or
"my_list=[
    [],
    [],
]" without a bracket() but np.array with work withou a bracket it would raise an error, i have mastered all syntax

'''
old_list=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


new_list=[]
for values in old_list:
    new_list.append(values[1])

print("NEW LIST",new_list)
print(old_list[1])
