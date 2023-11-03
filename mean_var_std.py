import numpy as np
import pprint as pp
def calculate(lst):
    print('Enter nine numbers')
    arr = np.array(lst)
    arr3 = np.reshape(arr, (3,3))
    data = {
        'Mean':[(np.mean(arr3,axis=0)),(np.mean(arr3,axis=1)),(np.mean(arr3))],
        'Variance' : [(np.var(arr3,axis=0)),(np.var(arr3,axis=1)),(np.var(arr3))],
        'standard deviation' : [(np.std(arr3,axis=0)),(np.std(arr3,axis=1)),(np.std(arr3))],
        'min' : [(np.min(arr3,axis=0)),(np.min(arr3,axis=1)),(np.min(arr3))],
        'max' : [(np.max(arr3,axis=0)),(np.max(arr3,axis=1)),(np.max(arr3))],
        'sum' : [(np.sum(arr3,axis=0)),(np.sum(arr3,axis=1)),(np.sum(arr3))]
        }
    pp.pprint(data) 

if __name__ == "__main__"  :
    lst1=[]
    for i in range(0,9):
        inp = (int(input('enter number in list')))
        lst1.append(inp)
    calculate(lst1)