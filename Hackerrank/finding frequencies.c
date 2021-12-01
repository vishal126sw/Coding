#include <stdio.h>
int main()
{
    int i,j,n,total_queries,count;
    int l[100000],number;
    scanf("%d",&n);
    for(i=0 ; i<n ; i++)
    {
        scanf("%d",&l[i]);
    }
    scanf("%d",&total_queries);
    for(i=0 ; i<total_queries ; i++)
    {
        scanf("%d",&number);
        count = 0;
        for(j=0 ; j<n ; j++)
        {
            if(l[j] == number)
                count ++;
        }
        printf("%d\n",count);
}
    



    return 0;
}