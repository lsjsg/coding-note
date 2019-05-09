#include <stdio.h>
/* 向函数传递参数的传值调用方法，
把参数的实际值复制给函数的形式参数。
在这种情况下，修改函数内的形式参数不会影响实际参数。
默认情况下，C 语言使用传值调用方法来传递参数。
一般来说，这意味着函数内的代码不会改变用于调用函数的实际参数。*/
/* 函数声明 */
void swap(int x, int y);

int main()
{
    /* 局部变量定义 */
    int a = 100;
    int b = 200;

    printf("交换前，a 的值： %d\n", a);
    printf("交换前，b 的值： %d\n", b);

    /* 调用函数来交换值 */
    swap(a, b);

    printf("交换后，a 的值： %d\n", a);
    printf("交换后，b 的值： %d\n", b);

    return 0;
}
void swap(int x, int y)
{
    int temp;

    temp = x; /* 保存 x 的值 */
    x = y;    /* 把 y 赋值给 x */
    y = temp; /* 把 temp 赋值给 y */

    return;
}