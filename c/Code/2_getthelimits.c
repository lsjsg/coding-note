#include <stdio.h>
#include <limits.h>
#include <float.h>
int main()
{
    // %lu 为 32 位无符号整数
    printf("int 字节数是: %lu \n", sizeof(int));
    printf("float 存储最大字节数 : %d \n", sizeof(float));
    // %E 为以指数形式输出单、双精度实数
    printf("float 最小值: %E\n", FLT_MIN);
    printf("float 最大值: %E\n", FLT_MAX);
    printf("精度值: %d\n", FLT_DIG);
    return 0;
}