#include <stdio.h>

/*定义两个全局变量*/
int x = 1;
int y = 2;
int addtwonum();
int main(void)
{
    int result;
    result = addtwonum();
    printf("result 为: %d\n", result);
    return 0;
}

/* 运行时需要使用
gcc 4_define.c 4.0_use_outside file.c -o main 
进行编译
然后使用 ./main运行 */
