def binary_search(l , n , key):
    low = 0
    high = n-1
    while(low <= high):
        mid = (low + high)//2
        if(l[mid] == key):
            return mid
        elif(l[mid] < key):
            low  = mid + 1
        elif(l[mid] > key):
            high = mid - 1
    return -1

def traverse_left(l , index , n , key):
    c=0
    while(True):
        index -= 1
        if(l[index] == key):
            c += 1
        else:
            return c

def traverse_right(l , index , n , key):
    c=0
    while(True):
        index += 1
        if(l[index] == key):
            c += 1
        else:
            return c


n = int(input())
l = [int(i) for i in input().split()]
l.sort()
print("sorted list :",l)
total_queries = int(input())

for i in range(total_queries):
    key = int(input())
    count=0
    index = binary_search(l,n,key)

    if(index != -1):
        count = 1
        if(index == 0):
            count += traverse_right(l , index , n , key)
        elif(index ==n-1):
            count +=  traverse_left(l , index , n , key)
        else:
            count +=  traverse_left(l , index , n , key)
            count += traverse_right(l , index , n , key)
    print(count)




