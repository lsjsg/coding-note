#include <stdio.h>
int main()
{
    long int m, n;
    int b;
    for(m=2; m<=1000000; m++)
    {
        b=1;
        for(n=2;n<=m/2;n++){
            if( m % n == 0 ){
                b=0;
                break;
                }
            }
        if (b==1){
            printf("%d\n", (int)m);
            }
	}
    return 0;
}
