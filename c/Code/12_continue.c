#include <stdio.h>
int main()
{
    int a = 10;
    /* do 循环执行 */
    do
    {
        if (a == 12)
        {
            /* 跳过迭代 */
            a = a + 1;
            continue;
        }
        printf("a 的值： %d\n", a);
        a++;
    } while (a < 15);
    return 0;
}