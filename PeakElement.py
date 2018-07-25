def funct(arr,low,high,n):
    mid = low+(high-low)//2
    
    if ((mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid])):
        return mid
    
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return funct(arr, low, (mid - 1), n)
    
    else:
        return funct(arr, (mid + 1), high, n)


def peakElement(arr, n):
    # Code here
    
    return funct(arr,0,n-1,n)
    
    
