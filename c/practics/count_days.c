#include <stdio.h>
int main()
{
    int year = 2008;
    int month = 8;
    int day = 8;
    int sum=0;
    for(int i=1;i<month;i++){
        switch (i){
        case 1:
            sum+=31;
            break;
        case 2:
            if(year%4==0){
                sum+=29;
            }
            else{
                sum+=28;
            }
            break;
        case 3:
            sum+=31;
            break;
        case 4:
            sum+=30;
            break;
        case 5:
            sum+=31;
            break;
        case 6:
            sum+=30;
            break;
        case 7:
            sum+=31;
            break;
        case 8:
            sum+=31;
            break;
        case 9:
            sum+=30;
            break;
        case 10:
            sum+=31;
            break;
        case 11:
            sum+=30;
            break;
        case 12:
            sum+=31;
            break;
        }
    }
    sum+=day;
    printf("%d年%d月%d日是该年的第%d天\n",year,month,day,sum);
    return 0;
}
