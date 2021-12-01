for iii in range(int(input())):
    a,b = [i for i in input().split()]
    m,n = len(a),len(b)
    mod = 1000000007
    ha,hb = 0,0                    
    prime,p = 31,31        
    count = 0 
    for i in range(m):
        o1 = ord(a[i]) # ASCII of a
        o2 = ord(b[i]) # ASCII of b
        ha = (ha + o1*p)%mod     
        hb = (hb + o2*p)%mod        
        p  = (p*prime)%mod  
    if(ha==hb):
        count += 1
    p1 = prime
    p2 = p 
    for i in range(m,n):
        ha = (ha*prime)%mod
        hb = (hb%mod - (ord(b[i-m])*p1)%mod +mod)%mod # remove first
        hb = (hb%mod + (ord( b[i] )*p2)%mod)%mod # add new 
        if(ha==hb):
            count += 1
        p1 = (p1*prime)%mod
        p2 = (p2*prime)%mod
    print(count)