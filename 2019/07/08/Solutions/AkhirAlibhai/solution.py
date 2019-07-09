def rotate_array(array, k):
    k = k % len(array)
    return(array[len(array)-k:len(array)] + array[0:len(array)-k])