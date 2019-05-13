import javax.swing.text.StyledEditorKit;

/* java的修饰符也叫访问控制符，是指能够控制类，成员变量，方法的使用权限的关键字
在面向对象编程中，访问控制符是一个很重要的概念，可以使用它来保护对类，变量，方法和构造方法的访问
public      共有的，对所有类可见
protected   受保护的，对同一包内的类和所有子类可见
private     私有， 在同一类内可见
默认的       在同一包内可见，默认不使用任何修饰符 */

public class ClassName{
    private String name;
    private int age;

    public String getName(String name){
        this.name = name;
        return name;
    }

    public void setName(){
        System.out.println(this.name);
    }
    public static void main(String[] args) {
        ClassName myclass = new ClassName();
        myclass.getName("test");
        myclass.setName();
        System.out.println(myclass.name);
    }
}

/* 父类中声明为public的方法在子类中也必须为public。
父类中声明为protected的方法在子类中要么声明为protected，要么声明为public。不能声明为private。
父类中默认修饰符声明的方法，能够在子类中声明为private。
父类中声明为private的方法，不能够被继承。 */