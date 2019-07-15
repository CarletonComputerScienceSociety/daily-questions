def pushZeroes(arr):
    return [i for i in arr if i != 0] + [i for i in arr if i == 0]
    
print(pushZeroes([0,1,0,3,12]))