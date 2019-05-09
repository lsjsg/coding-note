/* 整数常量可以是十进制、八进制或十六进制的常量。
前缀指定基数：0x 或 0X 表示十六进制，0 表示八进制，
不带前缀则默认表示十进制。
整数常量也可以带一个后缀，后缀是 U 和 L 的组合，
U 表示无符号整数（unsigned），L 表示长整数（long。
后缀可以是大写，也可以是小写，U 和 L 的顺序任意。 */
#include <stdio.h>
#define length 10
#define width 5
#define newline "\n"

int main()
{
    printf("0xFeeL=%d\n", 0xFeeL);
    printf("30ul=%d\n", 30ul);
    printf("314159E-5L=%f\n", 314159E-5L);
    int area;
    area = length * width;
    printf("value of area:%d", area);
    printf("%c", newline);
    return 0;
}