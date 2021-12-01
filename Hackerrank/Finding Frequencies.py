# sol 1 brute force

n=int(input())
l=[int(i) for i in input().split()]
total_queries = int(input())

for i in range(total_queries):
    number = int(input())
    count = 0 
    for j in l:
        if(j == number):
            count += 1
    print(count)