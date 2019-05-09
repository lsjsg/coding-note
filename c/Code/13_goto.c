#include <stdio.h>
int main()
{
    int a = 10;
/* do 循环执行 */
LOOP:
    do
    {
        if (a == 12)
        {
            /* 跳过迭代 */
            a = a + 1;
            goto test;
        }
        printf("a 的值： %d\n", a);
        a++;

    } while (a < 15);
test:
    printf("Excuting this line\n");
    return 0;
}