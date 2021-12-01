def BS_right(l,n,key):
    low = 0 
    high = n-1
    ans = -1
    no_of_loops = 0 
    while(low <= high):
        no_of_loops += 1
        mid = (low + high)//2
        if(l[mid] == key):
            ans = mid
            low = mid + 1
        elif(l[mid] < key):
            low = mid + 1
        else:
            high = mid - 1
        if(no_of_loops > 20):
            break
    return ans

def BS_left(l,n,key):
    low = 0 
    high = n-1
    ans = -1
    while(low <= high):
        mid = (low + high)//2
        if(l[mid] == key):
            ans = mid
            high = mid -1
        elif(l[mid] < key):
            low = mid + 1
        else:
            high = mid - 1
    return ans


n = int(input())
l=[int(i) for i in input().split()]
l.sort()
total_queries = int(input())

for iii in range(total_queries):
    search = int(input())
    p1 = BS_right(l,n,search)
    p2 = BS_left(l,n,search)
    if(p1==-1):
        print(0)
        continue
    print(p1-p2+1)
    

