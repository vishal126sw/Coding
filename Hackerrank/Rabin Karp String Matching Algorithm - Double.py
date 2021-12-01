for iii in range(int(input())):
    a,b = [i for i in input().split()]
    m,n = len(a),len(b)
    mod = 1000000007
    ha,hb = 0,0 
    HA,HB = 0,0                   
    prime,p = 31,31 
    PRIME,P = 131,131
    count = 0 
    for i in range(m):
        o1 = ord(a[i]) # ASCII of a
        o2 = ord(b[i]) # ASCII of b
        ha = (ha + o1*p)%mod     
        hb = (hb + o2*p)%mod        
        p  = (p*prime)%mod
        HA = (HA + o1*P)%mod     
        HB = (HB + o2*P)%mod        
        P  = (P*PRIME)%mod
    if(ha==hb and HA==HB):
        count += 1
    p1 = prime
    p2 = p 
    P1 = PRIME
    P2 = P
    for i in range(m,n):
        ha = (ha*prime)%mod
        hb = (hb%mod - (ord(b[i-m])*p1)%mod +mod)%mod # remove first
        hb = (hb%mod + (ord( b[i] )*p2)%mod)%mod # add new
        HA = (HA*PRIME)%mod
        HB = (HB%mod - (ord(b[i-m])*P1)%mod +mod)%mod # remove first
        HB = (HB%mod + (ord( b[i] )*P2)%mod)%mod # add new 
        if(ha==hb and HA==HB):
            count += 1
        p1 = (p1*prime)%mod
        p2 = (p2*prime)%mod
        P1 = (P1*PRIME)%mod
        P2 = (P2*PRIME)%mod
    print(count)