#include <stdio.h>

int main()
{
    int a = 10;
    /* do 循环执行 */
    do
    {
        printf("a 的值： %d\n", a);
        a = a + 1;
    } while (a < 20);
    return 0;
}