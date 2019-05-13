// public 是类的修饰符， 表明该类是公共类，可以被其他类访问
public class DefineClass{
    String name;
    int age;
    // 构造方法， 无返回值
    DefineClass(String name1, int age1){
        name = name1;
        age = age1;
        System.out.println("Hello world");
    }
    // 普通方法，必须有返回值
    void say_hi(){
        System.out.println("Hi, my name is"+name);
    }
    void my_age(){
        System.out.println("my age is:"+age);
    }
    public static void main(String[] args) {
        DefineClass myDog = new DefineClass("Dog",3);
        int age = myDog.age;
        String name = myDog.name;
        System.out.println("class name is:"+name+"class attribute age:"+age);
        myDog.say_hi();
        myDog.my_age();
    }
}