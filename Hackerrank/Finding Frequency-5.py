def mergesort(l,lo,hi):
    if(lo == hi):
        return 
    mid=(lo+hi)//2
    mergesort(l,lo,mid)
    mergesort(l,mid+1,hi)
    merge(l,lo,hi)

def merge(l,lo,hi):
    mid=(lo+hi)//2
    i=lo
    j=mid+1
    temp=[0 for i in range(hi-lo+1)]
    k=0
    while(i<=mid and j<=hi):
        if(l[i]<=l[j]):
            temp[k] =l[i]
            k += 1
            i += 1
        else:
            temp[k] =l[j]
            k += 1
            j += 1
    while(i<=mid):
        temp[k]=l[i]
        k += 1
        i += 1
    while(j<=hi):
        temp[k]=l[j]
        k += 1
        j += 1
    for i in range(0,hi-lo+1,1):
        l[lo+i] = temp[i]

def binary_search(l , n , key):
    lo = 0
    hi = n-1
    while(lo <= hi):
        mid = (lo + hi)//2
        if(l[mid] == key):
            return mid
        elif(l[mid] < key):
            l  = mid + 1
        elif(l[mid] > key):
            hi = mid - 1
    return -1

n = int(input())
l=[int(i) for i in input().split()]
mergesort(l,0,n-1)
#elements r sorted now
total_queries = int(input())
compress , frequency = [] , []

i,j = 0,0
count=0
while(True):
    if(l[i]==l[j]):
        if(l[i] not in compress):
            compress.append(l[i])
            #print(l[i],' appended ')
        count += 1   
        #print('count : ' , count )               
        j += 1
    else:
        frequency.append(count)
        #print('count appended')
        count=0
        #print('count back to 0')
        i=j

    # break statemment
    if(j>(n-1) ):
        frequency.append(count) 
        # why?-> the last elements is getting counted, but is not appending
        # so we added this to appned the count of last element
        break
#print(compress)
#print(frequency)

i=len(compress)
for count in range(total_queries):
    j = int(input())
    l  = binary_search( compress, i ,j )
    if(l == -1):
        print(0)
    else:
        print(frequency[l])