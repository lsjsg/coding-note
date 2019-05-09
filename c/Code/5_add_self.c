#include <stdio.h>
int main()
{
    int c;
    int a = 10;
    c = a++;
    printf("先赋值后运算：\n");
    printf("c: c = a++ 的值是 %d\n", c);
    printf("a 的值是 %d\n", a);

    printf("先运算后赋值：\n");
    a = 10;
    c = ++a;
    printf("c: c = ++a 的值是 %d\n", c);
    printf("a 的值是 %d\n", a);
}