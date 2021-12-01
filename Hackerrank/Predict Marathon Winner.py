#https://www.hackerrank.com/contests/smart-interviews-codevita/challenges/si-predict-marathon-winner

for iii in range(int(input())):
    n,s=[int(i) for i in input().split()]
    l=[]
    for i in range(n):
        l.append([int(i) for i in input().split()])
    #changing array to show total steps taken at each time
    for i in range(n):
            ini =0
            steps = l[i][-1]
            for j in range(s):
                ini += l[i][j]*steps
                l[i][j] = ini
    #check who won for each round
    who_won = []
    for j in range(s):
        mx=0
        for i in range(n):
            if(l[i][j]>mx):
                mx = l[i][j]
        for i in range(n):
            if(l[i][j]==mx):
                who_won.append(i)
                break
    #print(who_won)
    lead = [0]*n
    for i in range(1,s-1,2):
        lead[who_won[i]]+=1
    mx=0
    for i in lead:
        if(i>mx):
            mx=i
    for i in range(n):
        if(mx==lead[i]):
            print(i+1)
            break
    
    









