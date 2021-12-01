#https://www.hackerrank.com/contests/smart-interviews/challenges/si-enclosing-substring/submissions/code/1334345395
def valid(cB,cA):
    for i in range(26):
        if(cA[i]<cB[i]):
            return False
    return True
 
 
def checkAllValid(countB,countA,b,a,m,n,ln):
    """for a length , will return true if a valid substring is formed"""
    countA = [0 for i in range(26)]
    for i in range(0,ln):
        countA[ord(a[i])-97] += 1
    #print(countA)
    #print(countB)
    #check from 0 to ln
    if valid(countB,countA):
    	return True
    #check from ln to n
    for i in range(ln,n):
        #print("deleting: ",a[i-ln],"adding: ",a[i])
        countA[ord(a[i])-97] += 1
        countA[ord(a[i-ln])-97] -= 1
        if valid(countB,countA):
    	    return True
        #print(countA)
        #print(countB)
    return False
 
 
def BS(countB,countA,b,a,m,n):
    lo = m-1
    hi = n
    ans = -1
    while(lo<=hi):
        mid = (lo+hi)//2
        #print("checking length :" ,mid)
        if(checkAllValid(countB,countA,b,a,m,n,mid)):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans
 
tc = int(input())    
for iii in range(tc):
    b,a=[i for i in input().split()]
    m,n=len(b),len(a)
    countA = [0 for i in range(26)]
    countB = [0 for i in range(26)]    
    for i in b:
        countB[ord(i)-97] += 1
    #print("CountB : ", countB)
    ans = BS(countB,countA,b,a,m,n)
    #print("Case ",str(iii+1),": ")
    print(ans)