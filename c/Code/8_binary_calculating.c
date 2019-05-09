#include <stdio.h>

int main()
{
    unsigned int a = 60; /* 60 = 0011 1100 */
    unsigned int b = 13; /* 13 = 0000 1101 */
    int c = 0;

    printf("a=%d, b=%d", a, b);

    c = a & b; /* 12 = 0000 1100 */
    printf("按位与操作，按二进制位进行 与 运算\n");
    printf("c = a&b 的值是 %d\n", c);

    c = a | b; /* 61 = 0011 1101 */
    printf("按位或运算符，按二进制位进行 或 运算\n");
    printf("c = a|b 的值是 %d\n", c);

    c = a ^ b; /* 49 = 0011 0001 */
    printf("异或运算符，按二进制位进行 异或 运算\n");
    printf("c = a^b 的值是 %d\n", c);

    c = ~a; /*-61 = 1100 0011 */
    printf("取反运算符，按二进制位进行 取反 运算\n");
    printf("c = ~a 的值是 %d\n", c);

    c = a << 2; /* 240 = 1111 0000 */
    printf("二进制左移运算符。将一个运算对象的各二进制位全部左移若干位左边的二进制位丢弃，右边补0\n");
    printf("Line 5 - c 的值是 %d\n", c);

    c = a >> 2; /* 15 = 0000 1111 */
    printf("二进制右移运算符。将一个数的各二进制位全部右移若干位，正数左补0，负数左补1，右边丢弃。\n");
    printf("Line 6 - c 的值是 %d\n", c);
}