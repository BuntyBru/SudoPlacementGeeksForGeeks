#Your task is to complete this function
#Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
def bin_search(arr, left, high, key):
    #Code here
    high = len(arr)-1
    found = False
    while left <= high and not found:
        m = (high+left)//2
        if arr[m] == key:
            return arr.index(key)
        else:
            if key < arr[m]:
                high = m-1
            else:
                left = m+1
    if not found:
        return -1