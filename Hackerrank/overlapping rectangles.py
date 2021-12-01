def mod(n):
    return -1*n if(n<0) else n

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)

def diagram():
    pass
    #    B(X1,Y3)------L3------C(X3,Y3)
    #       |                   |               ABCD for first rectangle R
    #       L2                  L4
    #       |                   |               abcd for second rectangle r
    #   A(X1,Y1)------L1------D(X3,Y1)

def oneintersection(A,B,C,D,a,b,c,d):
    return (A==c or B==d or C==a or D==b)
def twointersections(A,B,C,D,a,b,c,d):
    #check which point of r will be inside 
    pass
    

for _ in range(int(input())):
    X1,Y1,X3,Y3 = [int(i) for i in input().split()]
    x1,y1,x3,y3 = [int(i) for i in input().split()]
    #we will keep R constant and move r to check it position wrt R
    A,B,C,D = (X1,Y1),(X1,Y3),(X3,Y3),(X3,Y1)
    a,b,c,d = (x1,y1),(x1,y3),(x3,y3),(x3,y1)
    L1,L3 = (A,D),(B,C)
    L2,L4 = (A,B),(D,C)
    l1,l3 = (a,d),(b,c)
    l2,l4 = (a,b),(d,c)
    AREA = mod((X3-X1)*(Y3-Y1))
    area = mod((x3-x1)*(y3-y1))
    #check if l1 is intersecting l2 or l4 or both
    temp1 = line_intersection()