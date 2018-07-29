def printTour(arr):
     
    n = len(arr)
   
    start = 0
    end = 1
     
    curr_petrol = arr[start].petrol - arr[start].distance 
    while(end != start or curr_petrol < 0 ):
    while(curr_petrol < 0 and start != end):
             
             tarting petrol pump. Change start
            curr_petrol -= arr[start].petrol - arr[start].distance
            start = (start +1)%n
             
            
            if start == 0:
                return -1
 
     
        curr_petrol += arr[end].petrol - arr[end].distance 
         
        end = (end +1) % n
 
    return start 