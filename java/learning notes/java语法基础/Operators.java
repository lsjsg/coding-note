public class Operators{
    public static void main(String[] args) {
        int a = 10;
        int b = 10;
        int x = 10;
        int y = 10;
        int z = 10;
        System.out.println("add self"+(a++));
        System.out.println("x>y and y>x"+((x>y) && (x<y)));
        System.out.println("self add int the front"+(++b));
        System.out.println("a&x:"+(a&x));
        System.out.println("a|x"+(a|x));
        System.out.println("a^x"+(a^x));
        System.out.println("move left 2"+(a<<2));
        System.out.println("move right 3"+(y>>3));
    }
}