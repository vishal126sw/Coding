#https://www.hackerrank.com/contests/smart-interviews/challenges/si-enclosing-substring/submissions/code/1334345395
def valid(cB,cA):
    for i in range(26):
        if(cA[i]<cB[i]):
            return False
    return True
 
 
tc = int(input())    
for iii in range(tc):
    b,a=[i for i in input().split()]
    m,n=len(b),len(a)
    countB = [0 for i in range(26)]    
    for i in b:
        countB[ord(i)-97] += 1
    min_ans,cur_ans = n+1,n+1
    for i in range(n):
        for j in range(i+1,n+1):
            countA=[0 for i in range(26)]
            temp = a[i:j]
            print(a[i:j])
            for ii in temp:
                countA[ord(ii)-97] += 1
            if(valid(countB,countA)):
                cur_ans = len(temp)
                if(cur_ans<min_ans):
                    min_ans = cur_ans
    print(min_ans) if min_ans != n+1 else print(-1)

            