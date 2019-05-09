/* auto 存储类是所有局部变量默认的存储类。

register 存储类用于定义存储在寄存器中而不是 
    RAM 中的局部变量。这意味着变量的最大尺寸等于寄存器的大小
    （通常是一个词），且不能对它应用一元的 '&' 运算符
    （因为它没有内存位置）。

static 存储类指示编译器在程序的生命周期内保持局部变量的存在，
而不需要在每次它进入和离开作用域时进行创建和销毁。
因此，使用 static 修饰局部变量可以在函数调用之间保持局部变量的值。

static 修饰符也可以应用于全局变量。
当 static 修饰全局变量时，会使变量的作用域限制在声明它的文件内。
全局声明的一个 static 变量或方法可以被任何函数或方法调用，
只要这些方法出现在跟 static 变量或方法同一个文件中。 

extern 当您有多个文件且定义了一个可以在其他文件中使用的全局变量或函数时，
可以在其他文件中使用 extern 来得到已定义的变量或函数的引用。
可以这么理解，extern 是用来在另一个文件中声明一个全局变量或函数。*/

#include <stdio.h>
/* 函数声明 */
void func1(void);
static int count = 10; // 全局变量，static是默认的

int main()
{
    while (count--)
    {
        func1();
    }
    return 0;
}

void func1(void)
{
    /* 'thingy' 是 'func1' 的局部变量 - 只初始化一次
    每次调用函数 'func1' 'thingy' 值不会被重置。*/
    static int thingy = 5;
    thingy++;
    printf("thingy is %d,count is %d\n", thingy, count);
}
