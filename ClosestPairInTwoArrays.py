n1 = 4
n2 = 4
arr1 =[1,4,5,7]
arr2 =[10,20,30,40]
k = 32
diff = 9999999999
arr1.sort()
arr2.sort()
res_l=0
res_r =0
l = 0
r = n2-1
while l< n1 and r >=0:

    if abs(arr1[l] +arr2[r] - k) < diff:
        l=l
        res_r=r
        print ("res_l ", res_l , "res_r " ,res_r)
        print("before diff" , diff)
        diff = abs(arr1[l] + arr2[r] - k)
        print("after diff" , diff)
    if arr1[l] + arr2[r] > k:
        print( "arr1[l] ", arr1[l], "arr2[r] ",arr2[r])
        r=r-1
    else:

        l=l+1
        print(l)
print( arr1[res_l], arr2[res_r])