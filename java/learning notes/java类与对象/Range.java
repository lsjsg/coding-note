/* 类级变量又称全局级变量或静态变量，需要使用static关键字修饰，你可以与 C/C++ 中的 static 变量对比学习。类级变量在类定义后就已经存在，占用内存空间，可以通过类名来访问，不需要实例化。
对象实例级变量就是成员变量，实例化后才会分配内存空间，才能访问。
方法级变量就是在方法内部定义的变量，就是局部变量。
块级变量就是定义在一个块内部的变量，变量的生存周期就是这个块，出了这个块就消失了，比如 if、for 语句的块。 */

public class Range{
    // 类级别变量
    public static String name = "Demo of range of the variables"; 
    public int i; // 对象实例级别变量
    // 属性块，在类初始化属性时候运行
    {
        int j = 2;// 块级变量
    }
    public void test1(){
        int j = 3;//方法级变量
        if(j==3){
            int k = 5; // 块级变量
        }
        // 这里不能访问块级变量，块级变量只能在块内部访问
        System.out.println("name=" + name + ", i=" + i + ", j=" + j);
    }

    public static void main(String[] args){
        // 不创建对象， 直接通过类名访问类级别变量
        System.out.println(Range.name);
        Range t = new Range();
        t.test1();
    }
}