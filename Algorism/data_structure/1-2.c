#include <stdio.h>
int F(int x){
    if (x==0){
        return 0;
    }
    else
    {
        return 2*F(x-1) + x*x;
    }
}
int main(){
    int a = 2;
    printf("the value is:%d\n",F(a));
    return 0;
}