def printer(l):
    for i in l:
        print(i)

for iii in range(int(input())):
    print("Case #"+str(iii+1)+":")
    n = int(input())
    l=[]
    for i in range(n):
        l.append([0]*(n+n))
    s = 10
    e = 10*((n*n)+n)
    total = s+e
    for i in range(n):      
        for j in range(n+n):
            if(j<2*i):
                l[i][j]="*"
            elif(j<2*i+(n-i)):
                l[i][j] = s
                s += 10
            else:
                l[i][j] = total - l[i][(n+n-1)+(i*2) - j]
            if(j==(n+n-1)):
                l[i][j] = l[i][j]//10
    for i in l:
        print(*i,sep="")
    print()


