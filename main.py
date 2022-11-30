# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp): 
    array=arr
    if (len(array)):
        half=len(array)//2
        left=array[:half]
        right=array[half:]
        merge_sort(left,cmp)
        merge_sort(right,cmp)
        i=j=k=0
        while (i<len(left) and j<len(right)):
            if (cmp(left[i],right[j])<0):
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        while (i<len(left)):
            array[k]=left[i]
            i+=1
            k+=1
        while (j<len(right)):
            array[k]=right[j]
            j+=1
            k+=1
    return array 
    pass

# must be in-place sort
def quick_sort(arr,cmp):
    pass
