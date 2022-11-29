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
    pass

# must be in-place sort
def quick_sort(arr,cmp):
    leng=len(arr)
    high=[]
    low=[]
    equal=[]

    if(leng>1):
        piv=arr[0]
        for i in arr:
            if ( cmp(i,piv)<0):
                low.appned (i)
            elif (cmp(i,piv) ==0):
                equal.append(i)
            elif (cmp(i,piv)>0):
                high.append (i)
        return quick_sort(low)+equal+quick_sort(high)
    else:
        return arr

    pass



def cmp(a,b):
    if (a<b):
        return -1
    if (a>b):
        return 1
    if (a==b):
        return 0
