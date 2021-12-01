def lcm_list(l):
    lcm = 1
    for i in l:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def gcd(x, y):
   while(y):
       x, y = y, x % y 
   return x

for i in range(int(input())):
    n = int(input())
    changer = [0]+ [int(i) for i in input().split()]
    visited = []
    non_visited = [int(i+1) for i in range(n)]
    cur=[0]*(n+1)
    ans=[]
    while(len(non_visited)>0):
        pos_1 = non_visited[0]
        print("For pos",pos_1,":")
        cur[pos_1]=1
        val = pos_1
        steps =  0
        while(True):
            cur[val]=0
            val = changer[val]
            cur[val] = 1
            steps += 1
            visited.append(val)
            non_visited.remove(val)
            print(cur)
            if(cur[pos_1]==1):
                ans.append(steps)
                cur[pos_1]=0
                break
        print(visited)
        print(non_visited)
    print(ans)
    print(lcm_list(ans))


