import time
tiempo = time.time()
def counting_sort(array, maxval):
    """in-place counting sort"""
    m = maxval + 1
    count = [0] * m               
    for a in array:
        count[a] += 1             
    i = 0
    for a in range(m):           
        for c in range(count[a]): 
            array[i] = a
            i += 1
    return array
print counting_sort( [9, 8, 5, 6, 12, 13, 1, 4, 2, 3, 2, 1], 14 )
print time.time()-tiempo
