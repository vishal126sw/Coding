#https://www.hackerrank.com/contests/smart-interviews/challenges/si-triple-trouble
# replace #print with print
def checkbit(num,pos):
    return (num>>pos)%2==1

for iii in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    #print(l)
    ans=0
    for i in range(32):
        #print("FOR BIT : ",i)
        set= 0
        for j in l:
            if(checkbit(j,i)):
                set += 1
            #print(j,"is ",checkbit(j,i),"at",i,"th position")
        #does it contribute
        #print("set : ",set)
        if( (set%3)==1 ):
            #print("set is contributing")
            ans += (1<<i)
        #print()
    print(ans)